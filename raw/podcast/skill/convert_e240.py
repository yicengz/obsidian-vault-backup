#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 知行小酒馆 E240 的 _原文.md / _导读.md / _思维导图.md 合并成一个
Obsidian 友好的 _原文.md。结构遵循 podcast/skill/docx转md.md 规范。

用法: python3 convert_e240.py <原文.md> <导读.md> <思维导图.md> <输出.md>
"""
import sys, re

# ---- 说话人映射 ----
# 发言人1 = 主播 雨白;发言人2 = 嘉宾 李井奎
SPK = {
    "发言人1": "雨白",
    "发言人2": "李井奎",
}
HOST = "雨白"
GUEST = "李井奎"
PODCAST = "知行小酒馆"
TITLE = "E240 和李井奎聊聊：那些大家都知道的事，怎么一说出口就变了？"
TRANSCRIBED_AT = "2026-07-06"

# ---- 高置信度转录纠错(保守;仅改明确同音错字)----
def fix(t):
    # 嘉宾姓名:标题/文件名权威写法「李井奎」;逐字稿/导读 ASR 误作「李景奎」
    t = t.replace("李景奎", "李井奎")
    # 主播名:开场白 ASR 若误作「俞白」,权威写法「雨白」
    t = t.replace("我是俞白", "我是雨白")
    return t

def repl_speakers(t):
    for k in sorted(SPK, key=len, reverse=True):
        t = t.replace(k, SPK[k])
    return t

def ts_to_sec(ts):
    p = [int(x) for x in ts.split(":")]
    if len(p) == 3: return p[0]*3600 + p[1]*60 + p[2]
    if len(p) == 2: return p[0]*60 + p[1]
    return 0

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

# ---------- 解析原文逐字稿 ----------
SPK_LINE = re.compile(r"^(发言人\d+)\s+(\d{1,2}:\d{2}(?::\d{2})?)\s*$")

def parse_transcript(text):
    lines = text.split("\n")
    turns = []
    cur_name = cur_ts = None
    buf = []
    def flush():
        nonlocal buf, cur_name, cur_ts
        if cur_name and buf:
            txt = fix(" ".join(x.strip() for x in buf if x.strip()))
            if txt:
                turns.append((cur_name, cur_ts, ts_to_sec(cur_ts), txt))
        buf = []
    for l in lines:
        s = l.strip()
        m = SPK_LINE.match(s)
        if m:
            flush()
            cur_name = SPK.get(m.group(1), m.group(1))
            cur_ts = m.group(2)
        elif re.match(r"^\d{4}年\d{2}月\d{2}日", s):
            continue
        elif s and cur_name:
            buf.append(s)
        elif s and cur_name is None:
            continue
    flush()
    return turns

# ---------- 解析导读 ----------
def split_h2(text):
    secs, cur = [], None
    for l in text.split("\n"):
        m = re.match(r"^##\s+(?!#)(.+?)\s*$", l)
        if m:
            cur = (m.group(1).strip(), [])
            secs.append(cur)
        elif cur is not None:
            cur[1].append(l)
    return secs

def parse_chapters(lines):
    head = re.compile(r"^#{3,6}\s+(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+?)\s*$")
    chapters, i = [], 0
    while i < len(lines):
        m = head.match(lines[i].strip())
        if m:
            ts, title = m.group(1), m.group(2).strip()
            i += 1
            summ = []
            while i < len(lines) and not head.match(lines[i].strip()):
                summ.append(lines[i])
                i += 1
            summary = fix(" ".join(x.strip() for x in summ if x.strip()))
            chapters.append((ts, title, ts_to_sec(ts), summary))
        else:
            i += 1
    return chapters

def clean_block(lines):
    while lines and not lines[0].strip(): lines.pop(0)
    while lines and not lines[-1].strip(): lines.pop()
    return lines

def main():
    yw, dd, mm, out = sys.argv[1:5]
    yw_text = read(yw)
    turns = parse_transcript(yw_text)
    secs = dict((n, clean_block(b[:])) for n, b in split_h2(read(dd)))
    chapters = parse_chapters(secs.get("章节速览", []))

    o = []
    o += ["---", f"title: {TITLE}", f"podcast: {PODCAST}",
          f"transcribed_at: {TRANSCRIBED_AT}", "---", ""]
    o += [f"> 主播:{HOST}", f"> 嘉宾:{GUEST}", "", "---", ""]

    o += ["# 导读 · 精华解析", ""]

    def emit(title, transform=None):
        body = secs.get(title)
        if not body: return
        o.append(f"## {title}")
        o.append("")
        for l in body:
            o.append(transform(l) if transform else l)
        o.append("")

    emit("关键词")
    emit("全文摘要")

    mind = read(mm).split("\n")
    o.append("## 思维导图")
    o.append("")
    for l in secs.get("思维导图", []):
        if l.strip().startswith("!["):
            o.append(l.rstrip())
            o.append("")
            break
    for l in mind:
        if re.match(r"^###\s", l):
            continue
        o.append(l.rstrip())
    o.append("")

    if secs.get("发言总结"):
        o.append("## 发言总结")
        o.append("")
        for l in secs["发言总结"]:
            m = re.match(r"^#{3,6}\s+(发言人\d+)\s*$", l.strip())
            if m:
                o.append(f"### {SPK.get(m.group(1), m.group(1))}")
            else:
                o.append(repl_speakers(fix(l)))
        o.append("")

    o += ["## 章节速览", ""]
    for ts, title, _s, _sm in chapters:
        anchor = f"{ts} {title}"
        o.append(f"- [[#{anchor}|{anchor}]]")
    o.append("")

    if secs.get("问答回顾"):
        o.append("## 问答回顾")
        o.append("")
        for l in secs["问答回顾"]:
            s = repl_speakers(fix(l))
            s = re.sub(r"^(.+?)\s*(问|答)[：:]\s*", r"**\1 \2:** ", s)
            o.append(s)
        o.append("")

    o += ["# 转录正文", ""]
    ci, n = 0, len(chapters)
    for spk, ts, sec, txt in turns:
        while ci < n and chapters[ci][2] <= sec:
            cts, ctitle, _cs, csumm = chapters[ci]
            o += [f"## {cts} {ctitle}", "", "[[#章节速览|↑ 返回章节速览]]", ""]
            if csumm:
                o += ["> [!QUOTE] 章节概要", "> " + csumm, ""]
            ci += 1
        o += [f"### {spk} @ {ts}", "", txt, ""]
    while ci < n:
        cts, ctitle, _cs, csumm = chapters[ci]
        o += [f"## {cts} {ctitle}", "", "[[#章节速览|↑ 返回章节速览]]", ""]
        if csumm:
            o += ["> [!QUOTE] 章节概要", "> " + csumm, ""]
        ci += 1

    text = re.sub(r"\n{3,}", "\n\n", "\n".join(o))
    if not text.endswith("\n"): text += "\n"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"OK chapters={len(chapters)} turns={len(turns)}")

if __name__ == "__main__":
    main()
