# -*- coding: utf-8 -*-
"""整理支付宝+微信账单 -> 对齐飞书多维表格登记格式"""
import openpyxl, json, re
from datetime import datetime

BASE = '/Users/yiceng/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/output/账单整理-20260701-20261005'

# ---------- 读取支付宝 ----------
with open(f'{BASE}/alipay_record_20261006_1258.txt', encoding='gbk', errors='replace') as f:
    lines = f.read().splitlines()
header = [h.strip() for h in lines[4].split(',')]
ali = []
for l in lines[5:]:
    if l.startswith('---') or not l.strip():
        break
    parts = [p.strip() for p in l.split(',')]
    d = dict(zip(header, parts))
    d['来源'] = '支付宝'
    ali.append(d)

# ---------- 读取微信 ----------
wb = openpyxl.load_workbook(f'{BASE}/微信支付账单流水文件(20260701-20261005)_20261006125240.xlsx')
ws = wb.active
wx = []
for row in ws.iter_rows(min_row=19, values_only=True):
    if not row[0]:
        continue
    d = dict(zip(['交易时间','交易类型','交易对方','商品','收/支','金额(元)','支付方式','当前状态','交易单号','商户单号','备注'], row))
    d['来源'] = '微信'
    wx.append(d)

# ---------- 已在飞书表中登记的记录（去重依据）: (日期, 时间, 金额) ----------
existing = {
    ('2026-07-02','16:25',19.00), ('2026-07-02','14:29',0.90), ('2026-07-02','18:55',13.90),
    ('2026-07-02','23:07',54.70), ('2026-07-02','21:55',42.00),
    ('2026-07-03','13:32',36.00), ('2026-07-03','13:58',0.60), ('2026-07-03','15:43',0.90),
    ('2026-07-03','18:18',35.00), ('2026-07-03','20:34',273.00),
}

# ---------- 分类规则 ----------
def classify(cp, item, amount, hour):
    """返回 (收支说明, 大类, 小类, 细分类, 成员, 刚性, flag)  flag='' 或 '待确认'"""
    t = cp + ' ' + item
    # 交通
    if '高德打车' in t: return ('高德打车','基本交通','通勤','打车','小庄庄','','')
    if '滴滴打车' in t or ('滴滴出行' in t and '单车' not in t): return ('滴滴打车','基本交通','通勤','打车','小庄庄','','')
    if '哈啰' in t or '单车' in t: return ('共享单车','基本交通','通勤','单车','小庄庄','','')
    if '轨道交通' in t or '地铁' in t: return ('地铁','基本交通','通勤','地铁','小庄庄','','')
    if '12306' in t or '铁路' in t: return ('火车票','基本交通','通勤','高铁','小庄庄','','')
    if '华铁旅客' in t: return ('火车站内消费','基本交通','通勤','高铁','小庄庄','','待确认')
    if '漕河泾物业' in t or '临港漕河泾' in t: return ('漕河泾停车','基本交通','停车','临时停车','小庄庄','','')
    if '停简单' in t: return ('停车费','基本交通','停车','临时停车','小庄庄','','')
    if '瑞虹天地' in t: return ('瑞虹天地停车','基本交通','停车','临时停车','小庄庄','','')
    if '苏河湾万象天地' in t: return ('苏河湾停车','基本交通','停车','临时停车','小庄庄','','')
    if '八号桥' in t: return ('八号桥停车','基本交通','停车','临时停车','小庄庄','','待确认')
    if '蔚来' in t and '维修' in t: return ('蔚来汽车维修','','','','双人行','','待确认')
    if '南孚' in t: return ('蔚来车钥匙电池','购物消费','家居','零散','双人行','','待确认')
    # 生活缴费
    if '电力' in t: return ('电费','基本生活','物业','电费','双人行','✅','')
    if '水务' in t: return ('水费','基本生活','物业','水费','双人行','✅','')
    if '燃气' in t: return ('燃气费','基本生活','物业','燃气费','双人行','✅','')
    if '绿城物业' in t and '美丽苑' in t: return ('美丽苑物业费','基本生活','物业','物业费','双人行','','待确认')
    if '中国移动' in t or '中国电信' in t: return ('话费充值','基本生活','通讯','话费','小庄庄','✅','')
    # 饮品零食
    if '魔盒' in t or '友宝' in t or '百纶集' in t: return ('公司饮料柜','基本饮食','零嘴','饮品','小庄庄','','')
    if 'Manner' in t: return ('Manner咖啡','基本饮食','补充','咖啡','小庄庄','','')
    if '星巴克' in t: return ('星巴克','基本饮食','补充','咖啡','小庄庄','','')
    if 'luckin' in t or '瑞幸' in t: return ('瑞幸咖啡','基本饮食','补充','咖啡','小庄庄','','')
    if 'Grid Coffee' in t: return ('Grid Coffee','基本饮食','补充','咖啡','小庄庄','','')
    if '喜茶' in t or '1点点' in t or '太犇牛' in t: return (cp.split('（')[0].split('(')[0],'基本饮食','零嘴','饮品','小庄庄','','')
    if '旺旺牛奶' in t: return ('旺旺牛奶','基本饮食','补充','牛奶','小庄庄','','')
    if '逸刻' in t:
        if any(k in t for k in ['七星','万宝路','利群','芙蓉王','钻石','苏烟','直冲']):
            return ('买烟','基本饮食','零嘴','烟酒','小庄庄','','')
        return ('逸刻便利店','基本饮食','零嘴','零食','小庄庄','','')
    if '全家' in t or 'FamilyMart' in t or '华丽便利店' in t or '芙蓉兴盛' in t or '京东便利店' in t:
        return ('便利店','基本饮食','零嘴','零食','小庄庄','','')
    if '名杰烟酒' in t or '启泰超市烟酒' in t: return ('烟酒超市','基本饮食','零嘴','烟酒','小庄庄','','')
    if 'FASCINO' in t or '朴下隆九' in t: return (('FASCINO面包' if 'FASCINO' in t else '朴下隆九'),'基本饮食','零嘴','零食','小庄庄','','')
    if '鲜芋仙' in t or '汕心' in t: return (cp.replace('淘宝闪购','').strip() or item.split('(')[0],'基本饮食','零嘴','零食','小庄庄','','')
    # 超市
    if '奥乐齐' in t: return ('奥乐齐超市','购物消费','超市','','双人行','','')
    if '元华超市' in t: return ('元华超市','购物消费','超市','','双人行','','')
    if '名创优品' in t: return ('名创优品','购物消费','家居','零散','小庄庄','','')
    if '屈臣氏' in t: return ('屈臣氏','购物消费','美妆','护肤品','小庄庄','','待确认')
    # 医疗
    if '医院' in t: return ('闸北中心医院','医疗药品','就诊','','小庄庄','','')
    # 数码软件
    if 'Kimi' in t or '月之暗面' in t: return ('Kimi会员','购物消费','数码','软件','小庄庄','','')
    if '腾讯视频' in t: return ('腾讯视频会员','购物消费','休闲','会员','小庄庄','','')
    if '哔哩哔哩' in t: return ('B站充电','购物消费','休闲','会员','小庄庄','','')
    if 'Hbomax' in t.lower() or 'hbomax' in t: return ('HBO Max订阅','购物消费','休闲','会员','小庄庄','','')
    if '罗技' in t: return ('罗技鼠标','购物消费','数码','电子产品','小庄庄','','')
    if '陀螺' in t: return ('指尖陀螺','购物消费','家居','零散','小庄庄','','')
    # 学习
    if '当当' in t or '乐开书店' in t or '多抓鱼' in t or '悉达多' in t: return ('买书','自我提升','学习','书籍','小庄庄','','')
    if '活动行' in t: return ('有知有行活动报名','自我提升','学习','课程','小庄庄','','待确认')
    # 服饰
    if 'T 恤' in t or 'T恤' in t: return ('有知有行T恤','购物消费','服饰','日常','小庄庄','','')
    # 按摩
    if '怡萱企管' in t or '情雨科技' in t or '樱奈' in t: return ('按摩','购物消费','休闲','按摩','小庄庄','','待确认')
    # 旅游
    if 'Airbnb' in t or '爱彼迎' in t: return ('Airbnb住宿','','','','双人行','','待确认')
    if '赫程国际' in t or '城市古利' in t: return ('城市古利','','','','双人行','','待确认')
    # 鲜花/人情
    if '鲜花' in t or '囍花狸' in t: return ('鲜花','人情往来','送礼','','双人行','','待确认')
    if '红包' in t: return ('微信红包','人情往来','红包','','小庄庄','','待确认')
    if '群收款' in t: return ('群收款','人情往来','请客','','小庄庄','','待确认')
    if '转账' in t: return ('转账-' + cp.split('(')[0].strip(),'','','','','','待确认')
    if '账户通' in t: return ('账户通付款','','','','','','待确认')
    if '代金券' in t: return ('抖音代金券','基本饮食','三餐','','小庄庄','','待确认')
    if '宠悦' in t or 'KK-Store' in t: return ('KK-Store','','','','','','待确认')
    # 餐饮（最后兜底）
    food_kw = ['烧烤','外卖','米粉','盖码饭','喜家德','肥汁米蘭','老碗会','点都德','野炉子','椒锅锅','野人先生',
               '新发现','真食净香居','寿司','蚝大胆','黄焖鸡','半步颠','大排档','威皇','优布劳','首尔朴宝',
               '谷沙','隆汕','麦当劳','肯德基','华莱士','鸡腿堡','汉堡','面铺','鲜包','餐饮','美团','大众点评','团购']
    if any(k in t for k in food_kw):
        if cp in ('淘宝闪购', '美团', '美团平台商户', '抖音生活服务商家'):
            # 从商品名提取真实商户名
            name = re.sub(r'(外卖订单|美团收银\d*|团购-.*|点餐订单.*|可选.*)', '', item)
            name = re.sub(r'[（(].*?[)）]', '', name).strip(' ·-')
            if '·' in name:
                name = name.split('·')[0]
            name = name or cp
        else:
            name = cp
            name = re.sub(r'[（(].*?[)）]', '', name)
            for junk in ['上海漕之应餐饮有限公司', '上海喜河餐饮合伙企业', '上海朴下隆九品牌管理有限公司']:
                if junk in name and len(name) > len(junk) + 2:
                    name = name.replace(junk, '')
            name = name.strip(' ·-') or cp[:12]
        if '新发现' in t: name = '新发现'
        if amount >= 150:
            return (name,'购物消费','大餐','','双人行','','')
        if hour >= 21:
            return (name,'基本饮食','零嘴','夜宵','小庄庄','','')
        if hour < 10:
            return (name,'基本饮食','三餐','早餐','小庄庄','','')
        if hour < 15:
            return (name,'基本饮食','三餐','午餐','小庄庄','','')
        return (name,'基本饮食','三餐','晚餐','小庄庄','','')
    return (cp[:15],'','','','','','待确认')

# ---------- 处理 ----------
main_rows = []      # 待录入
excluded = []       # 已排除
income_rows = []    # 收入（待用户决定）

# 支付宝退款映射: key=(交易对方, 商品去掉'退款-') -> 金额
ali_refunds = {}
for r in ali:
    if r['收/支'] == '不计收支' and '亲情卡' not in r['商品名称']:
        key = (r['交易对方'], r['商品名称'].replace('退款-',''))
        ali_refunds[key] = float(r['金额（元）'])

for r in ali:
    cp, item = r['交易对方'], r['商品名称']
    amt = float(r['金额（元）'] or 0)
    dt = r['交易创建时间'][:16]
    if '亲情卡' in item:
        excluded.append((dt, '支付宝', cp, item, amt, '亲情卡流水'))
        continue
    if r['收/支'] == '不计收支':
        excluded.append((dt, '支付宝', cp, item, amt, '退款（已合并到原消费行）'))
        continue
    if r['交易状态'] != '交易成功':
        excluded.append((dt, '支付宝', cp, item, amt, '交易状态:' + r['交易状态']))
        continue
    if '绿城物业' in cp and abs(amt - 3350.39) < 1:
        excluded.append((dt, '支付宝', cp, item, amt, '季度物业费，表中已按月登记'))
        continue
    hour = int(dt[11:13])
    name, d1, d2, d3, member, rigid, flag = classify(cp, item, amt, hour)
    refund = ali_refunds.get((cp, item), 0)
    row = {'time': dt, 'name': name, 'amount': amt, 'refund': refund, 'member': member,
           'payer': '小庄庄', 'd1': d1, 'd2': d2, 'd3': d3, 'proj': '日常生活' if d1 else '',
           'rigid': rigid, 'flag': flag, 'src': '支付宝', 'raw': cp + '|' + item}
    key = (dt[:10], dt[11:16], amt)
    if key in existing:
        excluded.append((dt, '支付宝', cp, item, amt, '已在多维表格中登记'))
        continue
    main_rows.append(row)

for r in wx:
    cp, item = str(r['交易对方']), str(r['商品'])
    amt = float(r['金额(元)'])
    dt = str(r['交易时间'])[:16]
    typ, status = r['交易类型'], str(r['当前状态'])
    if '亲属卡' in typ:
        excluded.append((dt, '微信', cp, item, amt, '亲属卡流水'))
        continue
    if r['收/支'] == '收入':
        if '退款' in typ:
            excluded.append((dt, '微信', cp, item, amt, '红包退款（对应红包支出已剔除）'))
        else:
            income_rows.append((dt, cp, item, amt, typ))
        continue
    # 支出
    if status == '已全额退款':
        excluded.append((dt, '微信', cp, item, amt, '已全额退款'))
        continue
    refund = 0
    m = re.search(r'已退款[¥(]*([\d.]+)', status)
    if m:
        refund = float(m.group(1))
    if '绿城物业' in cp and abs(amt - 3350.49) < 1:
        excluded.append((dt, '微信', cp, item, amt, '季度物业费，表中已按月登记'))
        continue
    hour = int(dt[11:13])
    name, d1, d2, d3, member, rigid, flag = classify(cp, item if item != '/' else typ, amt, hour)
    if '红包' in typ:
        who = cp.replace('发给', '')
        name = '红包-' + who
        d1, d2, d3, member = '人情往来', '红包', '', '小庄庄'
        flag = '待确认'
    row = {'time': dt, 'name': name, 'amount': amt, 'refund': refund, 'member': member,
           'payer': '小庄庄', 'd1': d1, 'd2': d2, 'd3': d3, 'proj': '日常生活' if d1 else '',
           'rigid': rigid, 'flag': flag, 'src': '微信', 'raw': cp + '|' + item}
    key = (dt[:10], dt[11:16], amt)
    if key in existing:
        excluded.append((dt, '微信', cp, item, amt, '已在多维表格中登记'))
        continue
    main_rows.append(row)

main_rows.sort(key=lambda x: x['time'], reverse=True)
excluded.sort(key=lambda x: x[0], reverse=True)
income_rows.sort(key=lambda x: x[0], reverse=True)

uncertain = [r for r in main_rows if r['flag']]
print(f"待录入: {len(main_rows)} 条（其中待确认 {len(uncertain)} 条）")
print(f"已排除: {len(excluded)} 条")
print(f"收入(单独列出): {len(income_rows)} 条")
print(f"待录入合计支出: {sum(r['amount']-r['refund'] for r in main_rows):.2f} 元")
print("\n待确认明细:")
for r in uncertain:
    print(' ', r['time'], r['name'], r['amount'], r['raw'][:50])

with open(f'{BASE}/processed.json', 'w', encoding='utf-8') as f:
    json.dump({'main': main_rows, 'excluded': excluded, 'income': income_rows}, f, ensure_ascii=False, indent=1)
print("\nsaved processed.json")
