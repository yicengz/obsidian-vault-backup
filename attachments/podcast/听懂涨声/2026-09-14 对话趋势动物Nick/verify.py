#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re
WS = "/Users/bytedance/Library/Application Support/DoubaoWork/Default/.doubaowork/agent_mode/workspace/.sessions/38446039802438402/agents/s_000pKizImfb"

def fmt_ts(ms):
    s = ms // 1000
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"

report = {}
for tag, cfg_file in [("rank4","config_rank4.json"),("rank7","config_rank7.json")]:
    cfg = json.load(open(os.path.join(WS, cfg_file)))
    paras = json.load(open(os.path.join(WS, f"parsed_{tag}.json")))
    md = open(cfg and None or os.path.join(WS,"artifacts",cfg["file_title"]+".md"), encoding="utf-8").read()
    R = {}
    # 1. every original paragraph text appears verbatim
    missing = [i for i,p in enumerate(paras) if p["text"] not in md]
    R["paragraphs_total"] = len(paras)
    R["paragraphs_missing_verbatim"] = missing
    # 2. count ### speaker segments in body
    body = md.split("# 转录正文",1)[1]
    speaker_segs = re.findall(r"^### .+ @ \d", body, re.M)
    R["speaker_segments_in_body"] = len(speaker_segs)
    R["segments_match_paras"] = (len(speaker_segs) == len(paras))
    # 3. chapters: 速览 entries vs body ## headings
    nav = re.findall(r"- \[\[#(.+?)\|", md)
    body_chaps = re.findall(r"^## (\d\d:\d\d.*)$", body, re.M)
    R["nav_entries"] = len(nav)
    R["body_chapters"] = len(body_chaps)
    R["nav_equals_body"] = (len(nav)==len(body_chaps)==cfg and len(cfg["chapters"]))
    R["nav_body_titles_match"] = all(nav[i].strip()==body_chaps[i].strip() for i in range(len(nav)))
    # 4. chapter ts == first paragraph real start ms
    chap_idxs = [i for i,_ in cfg["chapters"]]
    ts_ok = True
    for ci, idx in enumerate(chap_idxs):
        expected = fmt_ts(paras[idx]["ms"])
        if not body_chaps[ci].startswith(expected+" "):
            ts_ok = False
            R.setdefault("ts_mismatch",[]).append((ci, expected, body_chaps[ci]))
    R["chapter_ts_match_real_ms"] = ts_ok
    # 5. density
    R["keywords_count"] = len([k for k in re.split(r"[、,，]", cfg["keywords"]) if k.strip()])
    # speaker summary bullets
    R["n_chapters"] = len(cfg["chapters"])
    # 6. blacklist on self-written: check intro region (before # 转录正文) for banned phrases
    intro = md.split("# 转录正文",1)[0]
    banned = ["不端着","接住"]
    R["blacklist_hits_intro"] = {b: intro.count(b) for b in banned}
    R["blacklist_not_but_pattern_intro"] = len(re.findall(r"不是[^。\n]{1,20}而是", intro))
    report[tag] = R
    print(f"=== {tag} ===")
    for k,v in R.items():
        print(f"  {k}: {v}")

json.dump(report, open(os.path.join(WS,"verify_report.json"),"w"), ensure_ascii=False, indent=1)
