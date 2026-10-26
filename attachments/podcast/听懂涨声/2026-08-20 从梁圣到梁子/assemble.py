#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
from intro_content import (R4_SUMMARY, R4_SPEAKER_SUMMARY, R4_QA,
                           R7_SUMMARY, R7_SPEAKER_SUMMARY, R7_QA, DISCLAIMER)

WS = "/Users/bytedance/Library/Application Support/DoubaoWork/Default/.doubaowork/agent_mode/workspace/.sessions/38446039802438402/agents/s_000pKizImfb"
PROJ = "/Users/bytedance/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng"

def fmt_ts(ms):
    s = ms // 1000
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"

def assemble(tag, config, summary, speaker_sum, qa):
    paras = json.load(open(os.path.join(WS, f"parsed_{tag}.json")))
    name_map = config["name_map"]
    chapters = config["chapters"]  # list of (para_idx, title)

    out = []
    # frontmatter
    out.append("---")
    out.append(f'title: {config["file_title"]}')
    out.append(f'podcast: {config["podcast"]}')
    out.append(f'guest: {config["guest"]}')
    out.append(f'host: {config["host"]}')
    out.append(f'transcribed_at: 2026-10-25')
    out.append(f'publish_date: {config["publish_date"]}')
    out.append(f'duration: {config["duration"]}')
    out.append(f'source: {config["source"]}')
    out.append(f'minutes: {config["minute_url"]}')
    out.append("---")
    out.append("")
    # quote line + disclaimer
    out.append(f'> 主播：{config["host"]}｜嘉宾：{config["guest"]}')
    out.append("")
    out.append(f"> {DISCLAIMER}")
    out.append("")
    # 导读
    out.append("# 导读 · 精华解析")
    out.append("")
    out.append("## 关键词")
    out.append(config["keywords"])
    out.append("")
    out.append("## 全文摘要")
    out.append("")
    for p in summary:
        out.append(p)
        out.append("")
    out.append("## 发言总结")
    out.append("")
    for b in speaker_sum:
        out.append(f"- {b}")
    out.append("")
    out.append("## 问答回顾（主播 × 嘉宾）")
    out.append("")
    for q, a in qa:
        out.append(f"- **Q：{q}** A：{a}")
    out.append("")
    out.append("## 章节速览")
    out.append("")
    # chapter timestamps from real paragraph start ms
    chap_ts = []
    for idx, title in chapters:
        ts = fmt_ts(paras[idx]["ms"])
        chap_ts.append((ts, title))
        out.append(f"- [[#{ts} {title}|{ts} {title}]]")
    out.append("")
    out.append("# 转录正文")
    out.append("")
    # body
    n_chaps = len(chapters)
    for ci, (idx, title) in enumerate(chapters):
        end_idx = chapters[ci+1][0] if ci+1 < n_chaps else len(paras)
        ts = fmt_ts(paras[idx]["ms"])
        out.append(f"## {ts} {title}")
        out.append("[[#章节速览|↑ 返回章节速览]]")
        out.append("")
        for j in range(idx, end_idx):
            p = paras[j]
            spk = name_map.get(p["speaker"], p["speaker"])
            pts = fmt_ts(p["ms"])
            out.append(f"### {spk} @ {pts}")
            out.append(p["text"])
            out.append("")
    text = "\n".join(out)
    return text, len(paras), n_chaps

results = {}
for tag, cfg_file, summ, spsum, qa, proj_subdir in [
    ("rank4", "config_rank4.json", R4_SUMMARY, R4_SPEAKER_SUMMARY, R4_QA, "2026-09-14 对话趋势动物Nick"),
    ("rank7", "config_rank7.json", R7_SUMMARY, R7_SPEAKER_SUMMARY, R7_QA, "2026-08-20 从梁圣到梁子"),
]:
    config = json.load(open(os.path.join(WS, cfg_file)))
    text, nparas, nchaps = assemble(tag, config, summ, spsum, qa)
    # save to workspace artifacts
    art_dir = os.path.join(WS, "artifacts")
    out_path = os.path.join(art_dir, config["file_title"] + ".md")
    open(out_path, "w", encoding="utf-8").write(text)
    # project raw path
    proj_dir = os.path.join(PROJ, "raw/podcast/听懂涨声")
    proj_path = os.path.join(proj_dir, config["file_title"] + ".md")
    open(proj_path, "w", encoding="utf-8").write(text)
    # attachments materials copy
    att_dir = os.path.join(PROJ, "attachments/podcast/听懂涨声", proj_subdir)
    att_path = os.path.join(att_dir, config["file_title"] + ".md")
    open(att_path, "w", encoding="utf-8").write(text)
    results[tag] = {
        "title": config["file_title"], "n_paras": nparas, "n_chaps": nchaps,
        "artifacts_path": out_path, "project_path": proj_path, "attachments_path": att_path,
        "bytes": os.path.getsize(proj_path),
    }
    print(tag, "paras", nparas, "chaps", nchaps, "bytes", os.path.getsize(proj_path))

json.dump(results, open(os.path.join(WS, "build_results.json"), "w"), ensure_ascii=False, indent=1)
