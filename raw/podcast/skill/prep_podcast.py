#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prep_podcast.py — 步骤A:把「无人知晓」某一期的 _原文.docx / _导读.docx
转成 merge_podcast.py 需要的中间 md(真名标注 + 转录纠错 + 结构化)。

用法:
    python3 prep_podcast.py "<原文.docx>" "<导读.docx>" <out_dir> <ep>
每期的说话人映射写在 EP_MAP 里。
输出:<out_dir>/<原文stem>.md 和 <out_dir>/<导读stem>.md
"""
import sys, os, re, docx

# 主播固定为 孟岩。发言人N -> 真名。solo 只有 发言人1。
EP_MAP = {
    # 标准双人 (发言人1=孟岩, 发言人2=嘉宾)
    "E02": {"发言人1": "孟岩", "发言人2": "陈嘉禾"},
    "E03": {"发言人1": "孟岩", "发言人2": "张奔斗"},
    "E05": {"发言人1": "孟岩", "发言人2": "简七"},
    "E06": {"发言人1": "孟岩", "发言人2": "曹名长"},
    "E07": {"发言人1": "孟岩", "发言人2": "吴海燕"},
    "E08": {"发言人1": "孟岩", "发言人2": "方三文"},
    "E12": {"发言人1": "孟岩", "发言人2": "池建强"},
    "E14": {"发言人1": "孟岩", "发言人2": "爱哲"},
    "E16": {"发言人1": "孟岩", "发言人2": "少楠"},
    "E17": {"发言人1": "孟岩", "发言人2": "张寒"},
    "E18": {"发言人1": "孟岩", "发言人2": "陈鹏"},
    "E22": {"发言人1": "孟岩", "发言人2": "老六"},
    "E24": {"发言人1": "孟岩", "发言人2": "孙方"},
    "E25": {"发言人1": "孟岩", "发言人2": "季凯帆"},
    "E26": {"发言人1": "孟岩", "发言人2": "吴鲁加"},
    "E32": {"发言人1": "孟岩", "发言人2": "成庆"},
    "E34": {"发言人1": "孟岩", "发言人2": "顾中一"},
    "E36": {"发言人1": "孟岩", "发言人2": "周奇墨"},
    "E38": {"发言人1": "孟岩", "发言人2": "陈行甲"},
    "E39": {"发言人1": "孟岩", "发言人2": "重轻"},
    "E41": {"发言人1": "孟岩", "发言人2": "阿娇"},
    # solo (仅孟岩)
    "E10": {"发言人1": "孟岩"},
    "E15": {"发言人1": "孟岩"},
    "E19": {"发言人1": "孟岩"},
    "E20": {"发言人1": "孟岩"},
    "E21": {"发言人1": "孟岩"},
    "E23": {"发言人1": "孟岩"},
    "E30": {"发言人1": "孟岩"},
    "E31": {"发言人1": "孟岩"},
    "E33": {"发言人1": "孟岩"},
    "E35": {"发言人1": "孟岩"},
    "E37": {"发言人1": "孟岩"},
    "E40": {"发言人1": "孟岩"},
    # 非标准 (主播不是发言人1)
    "E04": {"发言人1": "张潇雨", "发言人2": "孟岩"},
    "E09": {"发言人1": "黄海", "发言人2": "孟岩"},
    "E11": {"发言人1": "孟岩", "发言人2": "刘飞"},
    "E13": {"发言人1": "孟岩", "发言人2": "Zara"},
    "E27": {"发言人1": "厚望", "发言人2": "孟岩"},
    "E28": {"发言人1": "Steve", "发言人2": "孟岩"},
}

# 嘉宾列表(用于 header;主播固定孟岩)
GUESTS = {
    "E02":"陈嘉禾","E03":"张奔斗","E05":"简七","E06":"曹名长","E07":"吴海燕",
    "E08":"方三文","E12":"池建强","E14":"爱哲","E16":"少楠","E17":"张寒",
    "E18":"陈鹏","E22":"老六(读库)","E24":"孙方","E25":"季凯帆","E26":"吴鲁加",
    "E32":"成庆","E34":"顾中一","E36":"周奇墨","E38":"陈行甲","E39":"重轻","E41":"阿娇",
    "E04":"张潇雨","E09":"黄海","E11":"刘飞(三五环)","E13":"Zara","E27":"厚望(面基)","E28":"Steve",
}

# 全局转录纠错:主播名各种音转文误写 -> 孟岩
HOST_FIX = ["梦言","梦妍","梦魇","孟妍","莫言","孟艳","梦岩","孟颜"]

# 每期特定嘉宾纠错
EP_FIX = {
    "E12": {"迟建强":"池建强"},
    "E24": {"孙芳":"孙方"},
    "E26": {"吴璐佳":"吴鲁加","吴路加":"吴鲁加"},
    "E38": {"陈星甲":"陈行甲"},
}

DATE_RE = re.compile(r"^\d{4}年\d{2}月\d{2}日")
SPK_RE  = re.compile(r"^(发言人\d+)\s+(\d{1,2}:\d{2}(?::\d{2})?)\s*$")

def fix_text(t, ep):
    for w in HOST_FIX:
        t = t.replace(w, "孟岩")
    for k, v in EP_FIX.get(ep, {}).items():
        t = t.replace(k, v)
    return t

def clean_title(s):
    return re.sub(r"_(原文|导读)$", "", s).strip()

def parse_yuanwen(path, ep, mapping):
    d = docx.Document(path)
    big = ""
    turns = []  # (name, ts, text)
    cur_name, cur_ts, buf = None, None, []
    def flush():
        nonlocal buf, cur_name, cur_ts
        if cur_name and buf:
            txt = fix_text(" ".join(x.strip() for x in buf if x.strip()), ep)
            if txt:
                turns.append((cur_name, cur_ts, txt))
        buf = []
    for p in d.paragraphs:
        t = p.text.strip()
        if p.style.name == "大标题" and not big:
            big = clean_title(t); continue
        if not t: continue
        if DATE_RE.match(t): continue
        m = SPK_RE.match(t)
        if m:
            flush()
            spk = m.group(1)
            cur_name = mapping.get(spk, spk)
            cur_ts = m.group(2)
        else:
            buf.append(t)
    flush()
    return big, turns

def write_yuanwen_md(out_path, title, ep, turns):
    guest = GUESTS.get(ep)
    lines = []
    lines.append("---")
    lines.append(f"title: {title}")
    lines.append("podcast: 无人知晓")
    lines.append("transcribed_at: 2026-07-12")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    if guest:
        lines.append("> 主播:孟岩")
        lines.append(f"> 嘉宾:{guest}")
    else:
        lines.append("> 主播:孟岩")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 转录正文")
    lines.append("")
    for name, ts, txt in turns:
        lines.append(f"**【{name} @ {ts}】** {txt}")
        lines.append("")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")

def parse_daodu(path, ep, mapping):
    d = docx.Document(path)
    big = ""
    out = []
    cur_section = None       # 当前一级标题名
    for p in d.paragraphs:
        style = p.style.name
        t = p.text.rstrip()
        ts = t.strip()
        if style == "大标题" and not big:
            big = clean_title(ts); continue
        if not ts and cur_section is None:
            continue
        if DATE_RE.match(ts):
            continue
        if style == "一级标题":
            cur_section = ts
            out.append(("H2", ts))
            continue
        if style == "二级正文":
            out.append(("SUB", cur_section, ts))
            continue
        # Normal
        out.append(("P", cur_section, ts))
    return big, out

def render_daodu_md(out_path, title, ep, items, mapping):
    lines = []
    lines.append("---")
    lines.append(f"title: {title} · 导读")
    lines.append("podcast: 无人知晓")
    lines.append("generated_at: 2026-07-12")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title} · 导读")
    lines.append("")
    lines.append("---")
    lines.append("")
    # reverse-map 发言人N -> 真名 用于 发言总结/问答回顾
    def repl_speaker(s):
        for spk, name in mapping.items():
            s = s.replace(spk, name)
        return fix_text(s, ep)

    for it in items:
        kind = it[0]
        if kind == "H2":
            lines.append("")
            lines.append(f"## {it[1]}")
            lines.append("")
        elif kind == "SUB":
            sec, txt = it[1], it[2]
            txt = fix_text(txt, ep)
            if sec == "章节速览":
                lines.append(f"- **{txt}**")
                lines.append("")
            elif sec == "发言总结":
                lines.append(f"### {repl_speaker(txt)}")
                lines.append("")
            elif sec == "问答回顾":
                # 形如「发言人1 问:...」
                s = repl_speaker(txt)
                s = re.sub(r"^(.+?)\s*(问|答)[:：]\s*", r"**\1 \2:** ", s)
                lines.append(s)
                lines.append("")
            else:
                lines.append(f"### {repl_speaker(txt)}")
                lines.append("")
        else:  # P (Normal)
            sec, txt = it[1], it[2]
            if not txt.strip():
                continue
            txt = fix_text(txt, ep)
            if sec == "章节速览":
                lines.append(f"  {txt}")
                lines.append("")
            elif sec == "问答回顾":
                s = repl_speaker(txt)
                s = re.sub(r"^(.+?)\s*(问|答)[:：]\s*", r"**\1 \2:** ", s)
                lines.append(s)
                lines.append("")
            else:
                lines.append(repl_speaker(txt))
                lines.append("")
    # collapse blanks
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")

def main():
    yw_docx, dd_docx, out_dir, ep = sys.argv[1:5]
    mapping = EP_MAP[ep]
    title, turns = parse_yuanwen(yw_docx, ep, mapping)
    yw_stem = clean_title(os.path.splitext(os.path.basename(yw_docx))[0]) + "_原文"
    dd_stem = clean_title(os.path.splitext(os.path.basename(dd_docx))[0]) + "_导读"
    write_yuanwen_md(os.path.join(out_dir, yw_stem + ".md"), title, ep, turns)
    dtitle, items = parse_daodu(dd_docx, ep, mapping)
    render_daodu_md(os.path.join(out_dir, dd_stem + ".md"), title, ep, items, mapping)
    print(f"{ep}: turns={len(turns)} title={title}")

if __name__ == "__main__":
    main()
