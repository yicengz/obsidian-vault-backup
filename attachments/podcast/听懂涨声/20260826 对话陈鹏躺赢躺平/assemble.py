#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assemble B套 Obsidian MD for rank2 and rank6 episodes. v2 fixes:
- Host统一为"杨天楠" (metadata + speaker tags), 正文原句"天南"不动
- rank2/rank6 发言总结改为 12-18 条短 bullet
- rank6 章节合并为 26
- rank6 标题使用 manifest 弯引号 U+201C/U+201D
"""
import re, os

WS = "/Users/bytedance/Library/Application Support/DoubaoWork/Default/.doubaowork/agent_mode/workspace/.sessions/38446039802438402/agents/s_000pKizIFWT"
YICENG = "/Users/bytedance/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng"

def parse_transcript(path):
    paras = []
    with open(path) as f:
        lines = f.read().split('\n')
    i = 0
    while i < len(lines) and not lines[i].startswith('Speaker'):
        i += 1
    while i < len(lines):
        line = lines[i].strip()
        m = re.match(r'Speaker\s+(\d+)\s+(\d+):(\d+):(\d+)\.(\d+)', line)
        if m:
            spk = int(m.group(1))
            h, mn, s, ms = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
            start_ms = h*3600000 + mn*60000 + s*1000 + ms
            j = i+1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            text = lines[j].strip() if j < len(lines) else ''
            paras.append({'spk': spk, 'start_ms': start_ms, 'text': text})
            i = j+1
        else:
            i += 1
    return paras

def fmt_ts(ms, force_hour=False):
    s = ms // 1000
    h = s // 3600
    m = (s % 3600) // 60
    sec = s % 60
    if h > 0 or force_hour:
        return f"{h:02d}:{m:02d}:{sec:02d}"
    else:
        return f"{m:02d}:{sec:02d}"

def build_md(cfg):
    paras = cfg['paras']
    name_map = cfg['name_map']
    chapters = cfg['chapters']
    chap_list = []
    for i, (start_idx, title) in enumerate(chapters):
        end_idx = chapters[i+1][0] if i+1 < len(chapters) else len(paras)
        chap_list.append({
            'start_idx': start_idx, 'end_idx': end_idx, 'title': title,
            'start_ms': paras[start_idx]['start_ms'],
        })

    lines = []
    lines.append('---')
    lines.append(f"title: {cfg['title']}")
    lines.append(f"podcast: {cfg['podcast']}")
    lines.append(f"guest: {cfg['guest']}")
    lines.append(f"host: {cfg['host']}")
    lines.append(f"transcribed_at: 2026-10-25")
    lines.append(f"publish_date: {cfg['publish_date']}")
    lines.append(f"duration: {cfg['duration']}")
    lines.append(f"source: {cfg['source']}")
    lines.append('---')
    lines.append('')
    lines.append(f"> 主播：{cfg['host_name']}｜嘉宾：{cfg['guest_names']}")
    lines.append('')
    lines.append('# 导读 · 精华解析')
    lines.append('')
    lines.append('## 关键词')
    lines.append(cfg['keywords'])
    lines.append('')
    lines.append('## 全文摘要')
    lines.append('')
    for para in cfg['summary']:
        lines.append(para)
        lines.append('')
    lines.append('> 导读整理自节目发言；其中经历、数据、预测与投资判断均为发言者观点，未逐项独立核实，不构成收益保证或投资建议。市场有风险，投资需谨慎。')
    lines.append('')
    lines.append('## 发言总结')
    lines.append('')
    for bullet in cfg['speaker_summaries']:
        lines.append(bullet)
    lines.append('')
    lines.append('## 问答回顾')
    lines.append('')
    for qa in cfg['qa_list']:
        lines.append(qa)
        lines.append('')
    lines.append('## 章节速览')
    lines.append('')
    for ch in chap_list:
        ts = fmt_ts(ch['start_ms'], force_hour=(ch['start_ms']>=3600000 or cfg.get('force_hour_ts', False)))
        lines.append(f"- [[#{ts} {ch['title']}|{ts} {ch['title']}]]")
    lines.append('')
    lines.append('# 转录正文')
    lines.append('')
    for ch in chap_list:
        ts = fmt_ts(ch['start_ms'], force_hour=(ch['start_ms']>=3600000 or cfg.get('force_hour_ts', False)))
        lines.append(f"## {ts} {ch['title']}")
        lines.append('')
        lines.append('[[#章节速览|↑ 返回章节速览]]')
        lines.append('')
        for p in paras[ch['start_idx']:ch['end_idx']]:
            spk_name = name_map.get(p['spk'], f"Speaker {p['spk']}")
            pts = fmt_ts(p['start_ms'], force_hour=(p['start_ms']>=3600000 or cfg.get('force_hour_ts', False)))
            lines.append(f"### {spk_name} @ {pts}")
            lines.append(p['text'])
            lines.append('')
    return '\n'.join(lines), chap_list

# ============ rank2 ============
p2 = parse_transcript(os.path.join(WS, 'work/minutes/rank2/artifact-rank2_lo-obcntp3rx9771xs2r96p99o9/transcript.txt'))

rank2_chapters = [
    (0,  "开播最年轻的嘉宾：17岁Warren登场"),
    (6,  "冉总：从建筑师到宏观投研中国负责人"),
    (9,  "父子横穿北美：封闭车厢里的私密对话"),
    (19, "俄勒冈波特兰：加油站和景点串通宰客"),
    (23, "铁锈地带：芝加哥金碧辉煌，小镇屋顶漏雨"),
    (27, "硅谷欣欣向荣，底特律logo字掉了没人修"),
    (32, "学校没教的三件事：讲话、钱、规律"),
    (38, "97年学建筑，98年商品房改革开门"),
    (58, "棚改叫停那年，地产周期见顶"),
    (73, "大一那门证券投资选修课，是白月光"),
    (102, "宏观研究：规律、历史、相关性，最终变条件反射"),
    (117, "魁北克法语区：5岁移民，两三个月法语成母语"),
    (137, "从牛马到有感情的牛马：在加拿大学会享受无聊"),
    (152, "疫情封城的白板：11岁开始听父亲讲市盈率"),
    (156, "四年级买台积电76、英伟达60多：赶上三轮牛熊"),
    (170, "年轻人可以押注，但别把押注变成投资体系"),
    (184, "未来十年中国资本市场，像2002年的房地产"),
    (198, "温哥华富二代说股票会跌，存起来"),
    (229, "在加拿大，敢要敢问就会有人给"),
    (238, "禁忌即诱惑：水壶烫手自己摸一次"),
    (247, "海运200公斤定制：整合中美两边资源"),
    (251, "父母做悬崖下的大气垫：不限制高度，只兜底"),
]

rank2_cfg = {
    'paras': p2,
    'name_map': {1: '杨天楠', 2: 'Warren', 3: '冉总'},
    'chapters': rank2_chapters,
    'title': '中国家庭最缺的一课：一对父子关于钱、认知与风险的坦白局',
    'podcast': '听懂涨声',
    'guest': '冉总、Warren',
    'host': '杨天楠',
    'host_name': '杨天楠',
    'guest_names': '冉总（父）、Warren（子）',
    'publish_date': '2026-10-09',
    'duration': '1:28:31',
    'source': 'https://www.xiaoyuzhoufm.com/episode/6ac77fd3e742e36efcbfdde6',
    'force_hour_ts': True,
    # 20 keywords
    'keywords': '投资启蒙、财商教育、代际对话、价值投资、成长股、北美自驾、东西方教育、复利、原生家庭、温哥华、建筑业周期、宏观投研、地产周期、青春期、社会化实践、领导力、跨文化、底气、放手、认知迭代',
    'summary': [
        '这期是《听懂涨声》开播以来最年轻的嘉宾——17岁的Warren。原本杨天楠只约了Warren的父亲冉总，一位建筑学科班出身、借地产红利把设计公司做到200多人、2018年又转型任北美全球前三宏观研究公司中国负责人的"老爹"。录制开始后看到Warren跃跃欲试，临时拉他一起聊，结果成了一期父子同台的坦白局。两人横穿北美开过5万公里，在网约车上都能为投资策略吵起来；老派的父亲信奉价值投资、过年送儿子长江电力，年轻的儿子却在美股科技股里摸高，11岁起就在疫情封城的白板前听父亲讲市盈率、读财报。',
        '对话从北美自驾的见闻一路谈到东西方教育的底层差异。冉总总结科班教育没教的三件事：怎么讲话（情商）、怎么看待钱、怎么认识规律。Warren则用自己在温哥华的经历对照国内——BC省高中有必修的work experience课，必须去认证企业干满90小时；本地孩子从高中起就在政府听证会、经济竞赛、非营利组织里摸爬滚打，而他回国前在厦门一所私立高中看到新高一学生的"社会实践"只是在学校指指路、摆摆水。',
        '后半程话题落在"钱"本身。冉总直言"现金在所有资产类型里很糟糕"，并把投资逻辑和从小被灌输的普世价值观一一对照：考试要每题都答，投资却要交白卷不碰不懂的；生活要去人多热闹的地方，投资却要避开最热的地方；从小被教育"总要做点什么"，投资却最好买完好资产就躺平。他统计2000年以来中国8到9万家房企，活到现在没踩缝纫机、没被限高的只剩约8000人——1/10，和资本市场"七亏两平一赚"一模一样。',
        '收尾落在亲子关系。冉总说自己和太太是悬崖底下的气垫子：孩子随便爬，不限制高度，但兜底。对非原则性小事，他和两个儿子都背一句"有者想去，没者死去"；原则性的事才详细讲。Warren则总结自己跨文化背景的优势——能整合中美两边资源，海运200多公斤定制物品到北美，成本是当地的五到十倍之差。这场对话没有结论，更像两个男人、两代人、两种投资风格在一张桌子上的同框。',
    ],
    # 16 short bullets
    'speaker_summaries': [
        '- **杨天楠（主播）**：人不折腾不仅会变笨，而且会变得软弱，作为爸爸不能在孩子面前软下来。',
        '- **杨天楠（主播）**：被需要是一种特权，是平台给的；事业型的人离开一线，这种被需要感会被一层层剥掉。',
        '- **杨天楠（主播）**：人和人之间最简单有效的交往方式是朋友——平等、互惠、不计较细碎得失。',
        '- **杨天楠（主播）**：中国家庭过去不需要学理财，是因为闭眼买房摇号就能赚年化27%，这几年逻辑变了。',
        '- **杨天楠（主播）**：美国首富小学送报、中学当球童，中产父母从小让孩子参与社会、理解钱，这是和中国教育很大的差别。',
        '- **Warren**：17岁温哥华高二，BC省注册非营利组织负责人，组织在全加拿大有分支。',
        '- **Warren**：5岁随家移民魁北克法语区，两三个月法语成母语；10岁回中国读公立小学，12岁再回温哥华。',
        '- **Warren**：2020年四年级开始买美股，最早买台积电76、英伟达拆股前60多，2021年中美联储加息前卖出。',
        '- **Warren**：2021年初疫情封城用公司显卡挖以太坊，读白皮书和财报，英语那段时间提升很快。',
        '- **Warren**：自认"不太交易，偏向价值投资者"，但资产涨到疯狂时也会卖。',
        '- **Warren**：在加拿大总结一句话——"敢要敢问，就会有人给"，英语不通也能靠外向积累资源。',
        '- **冉总**：97级建筑学，借98年商品房改革创业，公司最多200多人，夫妻搭档（他1%、太太99%）。',
        '- **冉总**：2018年加盟北美全球前三宏观研究公司，任中国区负责人，2022年底因股份变动离开。',
        '- **冉总**：认知提升本质是"杀死昨天的自己"，是拿绳子勒自己到窒息的过程，不是躺着读书喝茶就能发生。',
        '- **冉总**：未来10-15年中国资本市场类似2002年的房地产——头部真赚钱公司的股票，兑现可能以十年为周期。',
        '- **冉总**：父母要做悬崖下的大气垫，不限制孩子爬多高，但兜底；非原则性小事用"有者想去，没者死去"放手。',
    ],
    # 10 Q&A
    'qa_list': [
        '- **Q：学校里到底缺了什么？** A：冉总总结三件——怎么讲话（情商）、怎么看待钱、怎么认识规律（认识、尊重、顺应）。',
        '- **Q：北美自驾印象最深的事？** A：Warren说在俄勒冈波特兰，景点接连被宰客，加油站的人会和景点的人预谋串通。',
        '- **Q：地产周期你怎么判断的？** A：冉总说本轮地产鼎盛在棚改叫停的2017年结束，全国70个大中城市66%以上房价高点在2017年。',
        '- **Q：为什么40岁还要换赛道？** A：2014年前后投"互联网+"项目血本无归，被真金白银教训后才承认自己认识停留在书本。',
        '- **Q：人到中年为什么不躺平？** A：杨天楠答"人不折腾会变笨变软"；冉总归结为找到"以时间为函数、可积累、自己喜欢"的方向。',
        '- **Q：怎么让孩子早接触钱？** A：冉总给小儿子开5万人民币账户；Warren 11岁起在疫情白板前听父亲讲市盈率、读财报。',
        '- **Q：普世教育和投资逻辑为什么相反？** A：考试每题都要答，投资却要交白卷；生活要去人多的地方，投资却要避开最热的。',
        '- **Q：西方的社会化实践具体是什么？** A：BC省高中work experience是必修课，必须去认证企业干满90小时，不能去自家公司。',
        '- **Q：在北美怎么积累影响力？** A：Warren一句话——"敢要敢问，就会有人给"；冉总补"他知道自己要去哪"。',
        '- **Q：对孩子的期待是什么？** A：冉总说自己和太太是悬崖下的气垫子，不限制高度但兜底；小儿子写作天赋突出，11岁能坐一天写小说。',
    ],
}

md2, cl2 = build_md(rank2_cfg)

# ============ rank6 ============
p6 = parse_transcript(os.path.join(WS, 'work/minutes/rank6/artifact-rank6_lo-obcntpruwglk1xy11vp3p922/transcript.txt'))

# 26 chapters (merged old ch13+ch14 into one)
rank6_chapters = [
    (0,   "开场：30年全球金融经验的陈鹏回国"),
    (6,   "买方投顾为什么80年代中才在美国萌芽"),
    (10,  "70年代大通胀与华尔街之狼"),
    (15,  "美林博士：不收产品方的钱"),
    (16,  "互联网泡沫三年纳指跌85%"),
    (20,  "摩根士丹利痛定思痛：2万投顾超身高盛"),
    (23,  "401K、安然与监管立法"),
    (26,  "“中美不一样”：SBBI中国版的初衷"),
    (33,  "20年维度：股票10%、债券4.5%、现金2.3%"),
    (38,  "东亚家庭50%以上是房地产"),
    (45,  "上海甲级写字楼300万方空置"),
    (50,  "中国基金经理没经历过完整周期"),
    (54,  "情绪对A股驱动是美股2-2.5倍，年化波动率近60%"),
    (62,  "基民情绪损耗：美国10-15%，中国25-30%"),
    (65,  "医生讲手术风险：投资人也要知道亏多少"),
    (69,  "单只股票长期收益只有宽基一半"),
    (76,  "饭桌上听消息：三四只股全跌30-40%"),
    (82,  "食堂打饭：债券先打，股票最后"),
    (87,  "全球40多国：股票风险溢价都是5%"),
    (90,  "真实购买力：通胀下来了利率下来没那么可怕"),
    (95,  "美股百年：分红3-4%、利润6-7%、估值0.2%"),
    (103, "蜂鸟计划：0.16秒的专线"),
    (106, "贝塔便宜，阿尔法贵"),
    (110, "8月回撤25%：景气度是快变量"),
    (118, "4倍杠杆的OpenAI基金经理"),
    (122, "家庭资产配置：房产、现金、金融资产怎么调"),
]

# Curly quotes U+201C/U+201D per manifest
LQ = '\u201c'
RQ = '\u201d'
rank6_title = f'我看了中美几十年的数据，发现投资里{LQ}躺赢{RQ}和{LQ}躺平{RQ}真不是一回事｜对话陈鹏'

rank6_cfg = {
    'paras': p6,
    'name_map': {1: '杨天楠', 2: '陈鹏'},
    'chapters': rank6_chapters,
    'title': rank6_title,
    'podcast': '听懂涨声',
    'guest': '陈鹏',
    'host': '杨天楠',
    'host_name': '杨天楠',
    'guest_names': '陈鹏（博士）',
    'publish_date': '2026-08-26',
    'duration': '0:55:59',
    'source': 'https://www.xiaoyuzhoufm.com/episode/6a8e6921ef65145dfcc58800',
    'force_hour_ts': False,
    # 19 keywords
    'keywords': '大类资产、风险溢价、买方投顾、SBBI、资产配置、波动率、基民收益、贝塔阿尔法、房地产、401K、互联网泡沫、摩根士丹利、长期收益、分红、估值、杠杆、FOMO、家庭资产负债表、有知有行',
    'summary': [
        '这期是杨天楠与拥有30年全球金融经验的陈鹏博士对谈。陈鹏大部分时间在美国研究大类资产风险收益与配置，回国后听到最多的一句话是"你美国那套东西在这里行不通"。于是他和有知有行合作推出了《SBBI大类资产年报》中国版，用客观历史数据验证：在中美两个大国，资产定价、风险来源、居民行为到底有多少共通之处。',
        '前半程复盘美国买方投顾的四十年演进——70-80年代大通胀加《华尔街之狼》式卖方销售损害投资者利益，催生了不收产品方钱、用机构方法投资的早期投顾；90年代末互联网泡沫纳斯达克三年跌85%、2008年金融危机又一次教育市场，才把大机构推上转型路。摩根士丹利2008年后痛定思痛加码财富投顾，如今全美2万多线下投顾，市值和市盈率都已超过高盛。401K也不是一开始就完美——早期允许员工重仓本公司股票，安然、世通事件后才立法限制。',
        '落到中国数据：20年维度股票长期年化约10%、债券约4.5%、现金约2.3%（刚好抵通胀）。陈鹏本人在对话中给出的判断包括——过去二十几年A股年化波动率接近60%、美股约20%（他预计未来A股波动率是美股两倍左右）；情绪对市场的驱动作用是美股的2-2.5倍；中国基民因高买低卖每年损失约25%-30%，美国约10%-15%。这些数字是陈鹏在对话中的口述观点，不是外部权威定论。',
        '后半程拆解长期收益来源：美股百年维度，分红3%-4%、企业利润增长6%-7%、估值变动仅0.2%-0.3%；A股长期收益10%里分红只占15%、利润增长占85%、估值变动约-0.5%。陈鹏用食堂打饭比喻资本偿付优先级——债券投资人先打、股票排在最后。他提醒普通投资者：单只A股长期平均收益只有宽基指数的一半；贝塔便宜（ETF费率低），阿尔法昂贵且稀缺；追热点、上杠杆、听饭局消息是亏得最快的方式。收尾给家庭资产配置三条优化方向：非自住房产重新评估持有性价比、长期闲钱别只放储蓄、逐步增配金融资产并适度分散海外。',
    ],
    # 14 short bullets
    'speaker_summaries': [
        '- **杨天楠（主播）**：补充上海甲级写字楼三年新增300多万方、商场400万方，而社零从2023年6月至今下降21.6%。',
        '- **杨天楠（主播）**：8月1-30日中国科技股单月回撤约25%，比2016年1月熔断平均跌幅还大。',
        '- **杨天楠（主播）**：自己2015年A股大牛市、2022年房地产顶部都跑脱了一轮，但今年7月科技股暴跌时一犹豫没跑掉。',
        '- **杨天楠（主播）**：理性是有边界的，只能赚合乎情理的钱；没有单股仓位上限的围栏，长期风险很大。',
        '- **杨天楠（主播）**：贝塔本身已经不错，而且ETF费率降下来很便宜；阿尔法贵，还常被包装成贝塔高价卖给你。',
        '- **杨天楠（主播）**：金融机构过去很难抑制动量销售——卖得好因为涨得多，AUM、销售、高波动产品三者一结合压力就大。',
        '- **陈鹏**：30年全球金融经验，美国长期做大类资产配置与风险研究，《中国大类资产投资年报》（SBBI中国版）作者。',
        '- **陈鹏**：买方投顾兴起跟投资者体验关系最大——70-80年代大通胀加《华尔街之狼》式卖方把散户伤到极致，才有人站出来做不收产品方钱的模式。',
        '- **陈鹏**：长期收益与风险手拉手，没有免费午餐；股票比债券风险大，是由公司资本构成优先级决定的。',
        '- **陈鹏**：股票长期收益拆成三块——分红、利润增长、估值变动；美股百年估值变动仅0.2%-0.3%，A股约-0.5%。',
        '- **陈鹏**：单只A股长期平均收益只有宽基指数一半；要买单只，至少要确认它能比指数多赚一倍。',
        '- **陈鹏**：投资要像看病一样交给信得过的专业人士，把时间花在自己的行业创造超额收益更划算。',
        '- **陈鹏**：贝塔宽基ETF便宜且市场提供；阿尔法是博弈，散户面对的可能是机构——《蜂鸟计划》里机构为0.16秒挖专线、融16亿美元。',
        '- **陈鹏**：家庭配置三条——非自住房产重新评估持有性价比、长期闲钱别只放储蓄、逐步增配金融资产并适度分散海外。',
    ],
    # 11 Q&A
    'qa_list': [
        '- **Q：美国买方投顾为什么80年代中才萌芽？** A：陈鹏说跟投资者体验关系最大，70-80年代大通胀加卖方销售把散户伤到极致才有人站出来。',
        '- **Q：大机构什么时候才转型？** A：90年代末互联网泡沫纳指跌85%、2008年金融危机；摩根士丹利2008年后重点压财富投顾，如今市值和市盈率都超过高盛。',
        '- **Q：401K是怎么一步一步变合理的？** A：早期允许投个股、鼓励买本公司股票；安然、世通倒闭后养老金归零，监管才立法限制。',
        '- **Q：为什么要做SBBI中国版？** A：陈鹏回国总被说"中美不一样"，他就想用客观数据把中国大类资产的长期收益、风险、底层逻辑呈现出来。',
        '- **Q：20年维度中国大类资产收益是多少？** A：陈鹏本人给出——股票约10%、债券约4.5%、现金约2.3%（刚抵通胀）。',
        '- **Q：A股波动率到底多高？** A：陈鹏在对话中说过去二十几年A股年化波动率接近60%、美股约20%，他预计未来A股是美股两倍左右。',
        '- **Q：基民为什么不赚钱？** A：陈鹏算过美国基金投资者年损失约10%-15%，中国和印度等新兴市场约25%-30%。',
        '- **Q：普通投资者第一步该怎么做？** A：像医生讲手术风险一样先搞清楚股票的收益风险特征、短期赔钱概率、最差情况赔多少。',
        '- **Q：股票收益长期从哪来？** A：美股百年分红3%-4%、利润增长6%-7%、估值0.2%-0.3%；A股分红占15%、利润增长85%、估值约-0.5%。',
        '- **Q：贝塔和阿尔法怎么选？** A：陈鹏说贝塔宽基ETF便宜、市场提供；阿尔法是博弈，散户面对的可能是机构。',
        '- **Q：2026年当下家庭怎么配？** A：自住房先排除；投资性房产重新评估性价比；长期闲钱可增配收益更高资产；金融资产占比应提升并适度分散海外。',
    ],
}

md6, cl6 = build_md(rank6_cfg)

# ============ Write outputs ============
out_dir = os.path.join(WS, 'artifacts')
os.makedirs(out_dir, exist_ok=True)

# Remove old rank6 file with straight quotes (if exists)
old_r6_name = '我看了中美几十年的数据，发现投资里"躺赢"和"躺平"真不是一回事｜对话陈鹏.md'
for d in [out_dir, os.path.join(YICENG, 'raw/podcast/听懂涨声')]:
    old = os.path.join(d, old_r6_name)
    if os.path.exists(old):
        os.remove(old)
        print(f"REMOVED old: {old}")

rank2_fn = rank2_cfg['title'] + '.md'
rank6_fn = rank6_cfg['title'] + '.md'

with open(os.path.join(out_dir, rank2_fn), 'w') as f:
    f.write(md2)
with open(os.path.join(out_dir, rank6_fn), 'w') as f:
    f.write(md6)

yiceng_dir = os.path.join(YICENG, 'raw/podcast/听懂涨声')
os.makedirs(yiceng_dir, exist_ok=True)
with open(os.path.join(yiceng_dir, rank2_fn), 'w') as f:
    f.write(md2)
with open(os.path.join(yiceng_dir, rank6_fn), 'w') as f:
    f.write(md6)

# Stats
def count_section(md, heading):
    # count bullets under a section
    start = md.find(heading)
    if start < 0: return 0
    nxt = md.find('\n## ', start+1)
    if nxt < 0: nxt = md.find('\n# ', start+1)
    section = md[start:nxt] if nxt > 0 else md[start:]
    return len(re.findall(r'^- ', section, re.M))

print(f"\n=== rank2 ===")
print(f"bytes: {len(md2.encode('utf-8'))}")
print(f"chapters: {len(cl2)}")
print(f"paragraphs (### count): {md2.count(chr(10)+'### ')}")
print(f"summary paragraphs: {len(rank2_cfg['summary'])}")
print(f"keyword count (顿号分隔): {len(rank2_cfg['keywords'].split('、'))}")
print(f"speaker_summaries bullets: {len(rank2_cfg['speaker_summaries'])}")
print(f"qa bullets: {len(rank2_cfg['qa_list'])}")

print(f"\n=== rank6 ===")
print(f"bytes: {len(md6.encode('utf-8'))}")
print(f"chapters: {len(cl6)}")
print(f"paragraphs (### count): {md6.count(chr(10)+'### ')}")
print(f"summary paragraphs: {len(rank6_cfg['summary'])}")
print(f"keyword count (顿号分隔): {len(rank6_cfg['keywords'].split('、'))}")
print(f"speaker_summaries bullets: {len(rank6_cfg['speaker_summaries'])}")
print(f"qa bullets: {len(rank6_cfg['qa_list'])}")
print(f"rank6 title: {rank6_cfg['title']!r}")

print(f"\nWROTE:")
print(f"  artifacts/{rank2_fn}")
print(f"  artifacts/{rank6_fn}")
print(f"  yiceng/raw/podcast/听懂涨声/{rank2_fn}")
print(f"  yiceng/raw/podcast/听懂涨声/{rank6_fn}")
