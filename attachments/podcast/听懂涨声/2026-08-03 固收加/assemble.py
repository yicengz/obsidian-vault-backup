import re, sys, json

def parse(path):
    blocks = []
    cur = None
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    pat = re.compile(r'^Speaker (\d) (\d+):(\d+):(\d+)\.(\d+)\s*$')
    for ln in lines:
        m = pat.match(ln)
        if m:
            if cur: blocks.append(cur)
            h, mi, s, ms = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
            start_ms = ((h*3600)+mi*60+s)*1000+ms
            cur = {'spk': m.group(1), 'start_ms': start_ms, 'text': ''}
        else:
            if cur is not None:
                cur['text'] += ln
    if cur: blocks.append(cur)
    for b in blocks:
        b['text'] = b['text'].strip()
    return blocks

def fmt_ts(ms):
    total_s = int(ms//1000)
    h = total_s//3600
    mi = (total_s%3600)//60
    s = total_s%60
    if h>0:
        return f"{h:02d}:{mi:02d}:{s:02d}"
    return f"{mi:02d}:{s:02d}"

def main(cfg_path):
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    blocks = parse(cfg['transcript'])
    name_map = cfg['name_map']
    chapters = cfg['chapters']  # list of {start_ms, title}

    # assign blocks to chapters
    ch_of_block = []
    ci = 0
    for b in blocks:
        # find last chapter whose start_ms <= block start_ms
        while ci+1 < len(chapters) and chapters[ci+1]['start_ms'] <= b['start_ms']:
            ci += 1
        # if block before first chapter, assign 0
        idx = 0
        for i,c in enumerate(chapters):
            if c['start_ms'] <= b['start_ms']:
                idx = i
        ch_of_block.append(idx)

    out = []
    # frontmatter
    fm = cfg['frontmatter']
    out.append('---')
    out.append(f"title: {fm['title']}")
    out.append(f"podcast: {fm['podcast']}")
    out.append(f"guest: {fm['guest']}")
    out.append(f"host: {fm['host']}")
    out.append(f"transcribed_at: {fm['transcribed_at']}")
    out.append(f"publish_date: {fm['publish_date']}")
    out.append(f"duration: {fm['duration']}")
    out.append(f"source: {fm['source']}")
    if fm.get('minute_url'):
        out.append(f"minute_url: {fm['minute_url']}")
    out.append('---')
    out.append('')
    # quote line
    out.append(f"> {cfg['quote_line']}")
    out.append('')
    out.append(f"> [!NOTE] 导读整理自节目发言；其中经历、数据、预测与投资判断均为发言者观点，未逐项独立核实，不构成收益保证或投资建议。")
    out.append('')
    # intro
    out.append('# 导读 · 精华解析')
    out.append('## 关键词')
    out.append(cfg['keywords'])
    out.append('')
    out.append('## 全文摘要')
    out.append('')
    for p in cfg['summary_paragraphs']:
        out.append(p)
        out.append('')
    out.append('## 发言总结')
    for sp in cfg['speak_points']:
        out.append(f"- **{sp[0]}**：{sp[1]}")
    out.append('')
    out.append(cfg['qa_heading'])
    for q in cfg['qa']:
        out.append(f"- **{q[0]}** {q[1]}")
    out.append('')
    out.append('## 章节速览')
    for c in chapters:
        ts = fmt_ts(c['start_ms'])
        out.append(f"- [[#{ts} {c['title']}|{ts} {c['title']}]]")
    out.append('')
    out.append('# 转录正文')
    out.append('')

    # body
    for i,c in enumerate(chapters):
        ts = fmt_ts(c['start_ms'])
        out.append(f"## {ts} {c['title']}")
        out.append('[[#章节速览|↑ 返回章节速览]]')
        out.append('')
        for bi,b in enumerate(blocks):
            if ch_of_block[bi] != i: continue
            name = name_map.get(b['spk'], b['spk'])
            bts = fmt_ts(b['start_ms'])
            out.append(f"### {name} @ {bts}")
            out.append(b['text'])
            out.append('')
    text = '\n'.join(out)
    open(cfg['out'], 'w', encoding='utf-8').write(text)
    print(f"WROTE {cfg['out']}")
    print(f"chapters={len(chapters)} blocks={len(blocks)}")
    # verify chapter block counts
    from collections import Counter
    cnt = Counter(ch_of_block)
    for i,c in enumerate(chapters):
        print(f"  ch{i} {fmt_ts(c['start_ms'])} blocks={cnt.get(i,0)}")

if __name__=='__main__':
    main(sys.argv[1])
