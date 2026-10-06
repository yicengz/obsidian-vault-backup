# -*- coding: utf-8 -*-
"""生成账单整理 HTML"""
import json, html
from collections import Counter

BASE = '/Users/yiceng/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/output/账单整理-20260701-20261005'
d = json.load(open(f'{BASE}/processed.json'))
main, excluded, income = d['main'], d['excluded'], d['income']

def esc(s):
    return html.escape(str(s))

# 主表行
rows_html = []
for i, r in enumerate(main):
    flag_badge = '<span class="flag">待确认</span>' if r['flag'] else ''
    refund = f"{r['refund']:.2f}" if r['refund'] else ''
    cls = ' class="uncertain"' if r['flag'] else ''
    rows_html.append(
        f"<tr{cls}><td>{i+1}</td><td class='name'>{esc(r['name'])}</td><td>{r['time']}</td>"
        f"<td class='num'>{r['amount']:.2f}</td><td></td><td class='num'>{refund}</td>"
        f"<td>{esc(r['member'])}</td><td>{esc(r['payer'])}</td>"
        f"<td>{esc(r['d1'])}</td><td>{esc(r['d2'])}</td><td>{esc(r['d3'])}</td>"
        f"<td>{esc(r['proj'])}</td><td>{esc(r['rigid'])}</td>"
        f"<td><span class='src src-{r['src']}'>{r['src']}</span></td>"
        f"<td class='raw' title='{esc(r['raw'])}'>{flag_badge}{esc(r['raw'][:38])}</td></tr>")

# TSV 数据（粘贴用）
def tsv_seg(rows, cols):
    out = []
    for r in rows:
        vals = []
        for c in cols:
            v = r.get(c, '')
            if c == 'refund':
                v = f"{r['refund']:.2f}" if r['refund'] else ''
            if c == 'amount':
                v = f"{r['amount']:.2f}"
            vals.append(str(v))
        out.append('\t'.join(vals))
    return '\n'.join(out)

segA = tsv_seg(main, ['name', 'time', 'amount', 'deduct', 'refund'])
segB = tsv_seg(main, ['member', 'payer', 'd1', 'd2', 'd3', 'proj', 'rigid'])

# 排除明细按原因分组
exc_groups = Counter(x[5] for x in excluded)
exc_summary = ''.join(f"<span class='tag'>{esc(k)} × {v}</span>" for k, v in exc_groups.most_common())
exc_rows = ''.join(
    f"<tr><td>{x[0]}</td><td><span class='src src-{x[1]}'>{x[1]}</span></td><td>{esc(x[2])}</td>"
    f"<td>{esc(x[3][:40])}</td><td class='num'>{x[4]:.2f}</td><td>{esc(x[5])}</td></tr>"
    for x in excluded)

# 收入明细
inc_rows = ''.join(
    f"<tr><td>{x[0]}</td><td>{esc(x[1])}</td><td>{esc(x[4])}</td><td class='num'>{x[3]:.2f}</td></tr>"
    for x in income)

total = sum(r['amount'] - r['refund'] for r in main)
uncertain_n = sum(1 for r in main if r['flag'])

html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>账单整理 2026-07-01 ~ 2026-10-05</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, "PingFang SC", sans-serif; background: #f5f6f8; color: #1f2329; padding: 24px; }}
  .container {{ max-width: 1500px; margin: 0 auto; }}
  h1 {{ font-size: 22px; margin-bottom: 4px; }}
  .sub {{ color: #646a73; font-size: 13px; margin-bottom: 20px; }}
  .cards {{ display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; }}
  .card {{ background: #fff; border-radius: 10px; padding: 14px 20px; box-shadow: 0 1px 2px rgba(0,0,0,.06); }}
  .card .v {{ font-size: 24px; font-weight: 600; }}
  .card .k {{ font-size: 12px; color: #646a73; margin-top: 2px; }}
  .card.warn .v {{ color: #d88000; }}
  .paste-box {{ background: #fff; border: 1px solid #dee0e3; border-radius: 10px; padding: 16px 20px; margin-bottom: 20px; }}
  .paste-box h2 {{ font-size: 15px; margin-bottom: 8px; }}
  .paste-box ol {{ font-size: 13px; color: #444; padding-left: 20px; line-height: 1.9; }}
  .btns {{ margin-top: 10px; display: flex; gap: 10px; }}
  button {{ background: #3370ff; color: #fff; border: none; border-radius: 6px; padding: 8px 18px; font-size: 13px; cursor: pointer; }}
  button:hover {{ background: #245bdb; }}
  button.ghost {{ background: #eff0f1; color: #1f2329; }}
  .section {{ background: #fff; border-radius: 10px; box-shadow: 0 1px 2px rgba(0,0,0,.06); margin-bottom: 20px; overflow: hidden; }}
  .section > h2 {{ font-size: 15px; padding: 14px 20px; border-bottom: 1px solid #f0f0f0; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 12.5px; }}
  thead th {{ position: sticky; top: 0; background: #f7f8fa; padding: 8px 10px; text-align: left; font-weight: 500; color: #646a73; white-space: nowrap; z-index: 2; }}
  tbody td {{ padding: 7px 10px; border-top: 1px solid #f5f5f5; white-space: nowrap; }}
  tbody tr:hover {{ background: #f5f9ff; }}
  tr.uncertain {{ background: #fff7e6; }}
  tr.uncertain:hover {{ background: #ffefc2; }}
  .num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .name {{ font-weight: 500; }}
  .src {{ font-size: 11px; padding: 1px 7px; border-radius: 8px; }}
  .src-支付宝 {{ background: #e6f4ff; color: #1677ff; }}
  .src-微信 {{ background: #f6ffed; color: #52c41a; }}
  .flag {{ font-size: 11px; background: #d88000; color: #fff; border-radius: 4px; padding: 1px 6px; margin-right: 6px; }}
  .raw {{ color: #8f959e; max-width: 280px; overflow: hidden; text-overflow: ellipsis; }}
  .tag {{ display: inline-block; background: #eff0f1; border-radius: 6px; padding: 3px 10px; font-size: 12px; margin: 3px 6px 3px 0; }}
  details {{ padding: 0 20px 16px; }}
  summary {{ cursor: pointer; font-size: 13px; color: #3370ff; padding: 10px 0; }}
  .paste-hint {{ background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; padding: 10px 14px; font-size: 12.5px; margin: 0 20px 16px; line-height: 1.8; }}
  .scroll {{ overflow-x: auto; }}
</style>
</head>
<body>
<div class="container">
  <h1>账单整理 · 2026-07-01 至 2026-10-05</h1>
  <div class="sub">支付宝 + 微信支付，已按「BJXZ 记账」多维表格的字段与分类规范整理，按时间倒序</div>

  <div class="cards">
    <div class="card"><div class="v">{len(main)}</div><div class="k">待录入支出</div></div>
    <div class="card"><div class="v">¥{total:,.2f}</div><div class="k">待录入合计（已扣退款）</div></div>
    <div class="card warn"><div class="v">{uncertain_n}</div><div class="k">待确认（黄色行）</div></div>
    <div class="card"><div class="v">{len(excluded)}</div><div class="k">已排除流水</div></div>
    <div class="card"><div class="v">{len(income)}</div><div class="k">收入（单独列出）</div></div>
  </div>

  <div class="paste-box">
    <h2>📋 粘贴到多维表格的方法</h2>
    <ol>
      <li>先在下方检查黄色「待确认」行，修正分类或删除不需要的行（可直接在表格里点单元格改，改完再复制）。</li>
      <li>到多维表格「支出-小庄庄」视图，点 <b>+ 添加记录</b> 旁空白处，选中第一条空行的「收支说明」单元格。</li>
      <li>点【复制第①段】后粘贴 → 会依次填入 收支说明 / 收支时间 / 收支金额 / 抵扣金额 / 退款金额（消费金额是公式列，自动跳过不贴）。</li>
      <li>再选中第一行的「成员」单元格，点【复制第②段】粘贴 → 依次填入 成员 / 收付款人 / 大类 / 小类 / 细分类 / 项目 / 刚性收支。</li>
    </ol>
    <div class="btns">
      <button onclick="copySeg('segA', this)">复制第①段（说明~退款金额）</button>
      <button onclick="copySeg('segB', this)">复制第②段（成员~刚性收支）</button>
    </div>
  </div>

  <div class="section">
    <h2>待录入明细（{len(main)} 条，倒序）</h2>
    <div class="paste-hint">💡 黄色行为拿不准的分类/大额转账/旅游消费，建议逐条确认后再复制。单元格可点击直接编辑（仅影响本页复制结果）。</div>
    <div class="scroll">
    <table id="mainTable">
      <thead><tr>
        <th>#</th><th>收支说明</th><th>收支时间</th><th>收支金额</th><th>抵扣金额</th><th>退款金额</th>
        <th>成员</th><th>收付款人</th><th>大类</th><th>小类</th><th>细分类</th><th>项目</th><th>刚性收支</th>
        <th>来源</th><th>备注 / 原始商户</th>
      </tr></thead>
      <tbody>{''.join(rows_html)}</tbody>
    </table>
    </div>
  </div>

  <div class="section">
    <h2>收入明细（{len(income)} 条 · 未纳入上方，是否登记由你决定）</h2>
    <div class="scroll">
    <table>
      <thead><tr><th>时间</th><th>对方</th><th>类型</th><th>金额</th></tr></thead>
      <tbody>{inc_rows}</tbody>
    </table>
    </div>
  </div>

  <div class="section">
    <h2>已排除流水（{len(excluded)} 条）</h2>
    <div style="padding: 12px 20px 0;">{exc_summary}</div>
    <details>
      <summary>展开查看全部排除明细</summary>
      <div class="scroll">
      <table>
        <thead><tr><th>时间</th><th>来源</th><th>对方</th><th>商品</th><th>金额</th><th>排除原因</th></tr></thead>
        <tbody>{exc_rows}</tbody>
      </table>
      </div>
    </details>
  </div>
</div>

<textarea id="segA" style="position:fixed;left:-9999px">{esc(segA)}</textarea>
<textarea id="segB" style="position:fixed;left:-9999px">{esc(segB)}</textarea>
<script>
// 表格单元格可编辑（除序号/来源/备注）
document.querySelectorAll('#mainTable tbody td').forEach((td, i) => {{
  const col = i % 15;
  if (col >= 1 && col <= 12) td.contentEditable = true;
}});

function currentRows() {{
  // 读取（可能被编辑过/剔除过）的表格内容
  return [...document.querySelectorAll('#mainTable tbody tr')]
    .filter(tr => !tr.classList.contains('removed'))
    .map(tr => [...tr.cells].slice(1, 13).map(td => td.innerText.trim()));
}}

// 点序号剔除/恢复某行
document.querySelectorAll('#mainTable tbody tr').forEach(tr => {{
  tr.cells[0].style.cursor = 'pointer';
  tr.cells[0].title = '点击剔除/恢复此行';
  tr.cells[0].addEventListener('click', () => {{
    tr.classList.toggle('removed');
    tr.style.opacity = tr.classList.contains('removed') ? '0.35' : '';
    tr.style.textDecoration = tr.classList.contains('removed') ? 'line-through' : '';
  }});
}});

function copySeg(which, btn) {{
  const rows = currentRows();
  const data = rows.map(cols =>
    which === 'segA' ? cols.slice(0, 5).join('\\t') : cols.slice(5, 12).join('\\t')
  ).join('\\n');
  navigator.clipboard.writeText(data).then(() => {{
    const old = btn.innerText;
    btn.innerText = '✅ 已复制 ' + rows.length + ' 行';
    setTimeout(() => btn.innerText = old, 2000);
  }});
}}
</script>
</body>
</html>"""

with open(f'{BASE}/账单整理-20260701-20261005.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)
print('HTML written,', len(html_doc), 'bytes')
