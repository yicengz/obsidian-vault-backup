#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merge_podcast.py — 把「无人知晓」某一期的 _原文.md(逐字稿)与 _导读.md 合并成
单一的 Obsidian 友好 _原文.md,结构见同目录 SKILL.md。

用法:
    python3 merge_podcast.py "<原文.md 路径>" "<导读.md 路径>" [输出路径]
    # 输出路径省略时,原地覆盖「原文.md」,并生成 .bak 备份

    # 也可只给一个「集号目录」,自动在该目录里按 E{n} 配对:
    python3 merge_podcast.py --dir "<podcast 目录>" --ep E07

这个脚本只做「确定性的结构变换」。真人名替换 / 转录纠错 属于需要理解语义的步骤,
请先按 SKILL.md 的约定处理好 _原文.md 里的说话人与错字,再跑本脚本。
"""
import sys, os, re, shutil, glob

# ---------- 工具 ----------
def ts_to_sec(ts):
    parts = [int(x) for x in ts.split(":")]
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0, parts[0], parts[1]
    else:
        return 0
    return h * 3600 + m * 60 + s

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

# ---------- 解析 原文(逐字稿) ----------
TURN_RE = re.compile(r"^\*\*【(.+?) @ ([0-9:]+)】\*\*\s*(.*)$")

def parse_yuanwen(text):
    lines = text.split("\n")
    # frontmatter
    fm = []
    body_start = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm = lines[: i + 1]
                body_start = i + 1
                break
    # header: 主播/嘉宾 引用行
    host_lines = [l for l in lines[body_start:] if l.startswith(">")]
    # turns
    turns = []  # (speaker, ts, sec, text)
    for l in lines[body_start:]:
        m = TURN_RE.match(l.strip())
        if m:
            spk, ts, txt = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            turns.append((spk, ts, ts_to_sec(ts), txt))
    return fm, host_lines, turns

# ---------- 解析 导读 ----------
def split_sections(text):
    """把 markdown 按 '## 标题' 切成 {标题: [内容行...]}(有序)。"""
    lines = text.split("\n")
    secs = []
    cur = None
    for l in lines:
        m = re.match(r"^##\s+(.+?)\s*$", l)
        if m:
            cur = (m.group(1).strip(), [])
            secs.append(cur)
        elif cur is not None:
            cur[1].append(l)
    return secs

def parse_chapters(sec_lines):
    """从『章节速览』section 解析出 [(ts, title, [summary_lines])]。"""
    chapters = []
    i = 0
    head_re = re.compile(r"^-\s+\*\*(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+?)\*\*\s*$")
    while i < len(sec_lines):
        m = head_re.match(sec_lines[i].strip())
        if m:
            ts, title = m.group(1), m.group(2).strip()
            i += 1
            summ = []
            while i < len(sec_lines) and not head_re.match(sec_lines[i].strip()):
                summ.append(sec_lines[i])
                i += 1
            # 清理:去首尾空行、去缩进
            cleaned = [s.strip() for s in summ if s.strip()]
            chapters.append((ts, title, ts_to_sec(ts), " ".join(cleaned)))
        else:
            i += 1
    return chapters

def strip_edges(lines):
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines

# ---------- 组装 ----------
def build(fm, host_lines, turns, dao_secs):
    dao = {name: strip_edges(body[:]) for name, body in dao_secs}
    chapters = parse_chapters(dao.get("章节速览", []))

    out = []
    out.extend(fm)
    out.append("")
    out.extend(host_lines)
    out.append("")
    out.append("---")
    out.append("")

    # ===== 导读 · 精华解析 =====
    out.append("# 导读 · 精华解析")
    out.append("")

    def emit_section(title):
        if title in dao and dao[title]:
            out.append(f"## {title}")
            out.append("")
            out.extend(dao[title])
            out.append("")

    # 顺序:关键词 → 全文摘要 → 发言总结 → 章节速览 → 问答回顾
    emit_section("关键词")
    emit_section("全文摘要")
    emit_section("发言总结")

    # 章节速览(目录,带跳转链接)
    out.append("## 章节速览")
    out.append("")
    for ts, title, _sec, _summ in chapters:
        anchor = f"{ts} {title}"
        out.append(f"- [[#{anchor}|{anchor}]]")
    out.append("")

    emit_section("问答回顾")

    # ===== 转录正文 =====
    out.append("# 转录正文")
    out.append("")

    ch_idx = 0
    n_ch = len(chapters)
    for spk, ts, sec, txt in turns:
        # 在这条发言前,把所有「起始时间 <= 当前发言时间」的章节插进来
        while ch_idx < n_ch and chapters[ch_idx][2] <= sec:
            cts, ctitle, _cs, csumm = chapters[ch_idx]
            out.append(f"## {cts} {ctitle}")
            out.append("")
            out.append("[[#章节速览|↑ 返回章节速览]]")
            out.append("")
            if csumm:
                out.append("> [!QUOTE] 章节概要")
                out.append("> " + csumm)
                out.append("")
            ch_idx += 1
        out.append(f"### {spk} @ {ts}")
        out.append("")
        out.append(txt)
        out.append("")

    # 剩余未插入的章节(极少见)追加到末尾
    while ch_idx < n_ch:
        cts, ctitle, _cs, csumm = chapters[ch_idx]
        out.append(f"## {cts} {ctitle}")
        out.append("")
        out.append("[[#章节速览|↑ 返回章节速览]]")
        out.append("")
        if csumm:
            out.append("> [!QUOTE] 章节概要")
            out.append("> " + csumm)
            out.append("")
        ch_idx += 1

    # 收敛多余空行
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text, len(chapters), len(turns)

# ---------- 入口 ----------
def resolve_pair(directory, ep):
    yw = glob.glob(os.path.join(directory, f"*{ep} *_原文.md"))
    dd = glob.glob(os.path.join(directory, f"*{ep} *_导读.md"))
    if not yw or not dd:
        sys.exit(f"未找到 {ep} 的 原文/导读 配对:原文={yw} 导读={dd}")
    return yw[0], dd[0]

def main():
    args = sys.argv[1:]
    out_path = None
    if args and args[0] == "--dir":
        directory = args[1]
        ep = None
        if "--ep" in args:
            ep = args[args.index("--ep") + 1]
        if not ep:
            sys.exit("--dir 模式需要 --ep E07")
        yw_path, dd_path = resolve_pair(directory, ep)
    else:
        if len(args) < 2:
            sys.exit(__doc__)
        yw_path, dd_path = args[0], args[1]
        if len(args) >= 3:
            out_path = args[2]

    if out_path is None:
        out_path = yw_path  # 原地覆盖

    fm, host_lines, turns = parse_yuanwen(read(yw_path))
    dao_secs = split_sections(read(dd_path))
    result, n_ch, n_turn = build(fm, host_lines, turns, dao_secs)

    if os.path.exists(out_path):
        shutil.copy(out_path, out_path + ".bak")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✅ 合并完成 → {out_path}")
    print(f"   章节 {n_ch} 个,发言 {n_turn} 段")
    print(f"   备份 → {out_path}.bak" if os.path.exists(out_path + '.bak') else "")

if __name__ == "__main__":
    main()
