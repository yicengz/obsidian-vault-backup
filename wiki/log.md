---
title: Wiki Log
description: 按时间倒序的 wiki 演进记录
---

# Wiki Log

按时间倒序的 wiki 演进记录。每条以 `## [YYYY-MM-DD] action | title` 起头，方便用
`grep "^## \[" log.md | tail -N` 解析最近 N 条。

action 可能值：`ingest`、`batch-ingest`、`lint`、`refactor`、`query-archive`。

---

## [2026-06-16] batch-ingest | 帕慕克 + 通讯隔离

蒸馏来源（2 份高价值素材）：

- 2026-06-09 与 AI 的「自我洁净」对谈（[[20260610230455]]）— 起点是读《伊斯坦布尔》遇到帕慕克那段话，串起公婆吃饭的矛盾感、阶级特权、生育率塌方、社保 vs 8 小时工时、数据 vs 道德
- 2026-06-15 自己的公众号 [[VX公众号 数仓连续出差3周|【数仓工作分享】❓]] — "飞机作为通讯隔离带"那一段

新建 wiki 条目（3 个）：

- [[自我洁净]] · thinking
- [[帕慕克]] · Reading（人物页）
- [[通讯隔离]] · knowledge

更新文件：

- [[index|Wiki Index]] — 加入 3 个新条目，移除上一轮 🆕 标记，更新 Last compiled
- [[log|Wiki Log]] — 本文件追加

本轮跳过的源（含理由）：

- `raw/clippings/《以爱为家》……` — 有完整内容但用户暂未要求处理
- `raw/clippings/高中老师就业率造假.md` + `raw/clippings/保护电脑手机U盘.md` — B 站视频 clipping，无 transcript
- `raw/inbox/20260615003643.md`（统计局数仓建设可行性分析）— 用户暂未要求处理；下次可考虑落到 Tech/
- `raw/inbox/[20260608.md` — 空文件
- `output/VX公众号 主键重复了.md` — 用户的工程笔记，本身是产出，不反向蒸馏；可考虑做 Tech/冷热分治 概念页
- `output/chat with ai/数仓 & 出差 & 劳累.md` — 协作草稿（v1/v2/v3），是 raw 性质
- `diary/*` — 个人随笔，按规矩不蒸馏

待办（lint）：

- [[帕慕克]] 提到的 hüzün 值得单独成页（土耳其"接受失落"的状态）
- [[自我洁净]] 触及的"数据 vs 道德"、"信息开放 ≠ 行动平等"、"社保 vs 8 小时工时（float vs 零 float）"几条值得拆条
- 旧 wiki 条目的一行摘要仍待补

---

## [2026-06-10] batch-ingest | 6 月初一轮

蒸馏来源（4 份高价值素材）：

- 看理想《不止减压的正念艺术》关怀篇第 3 集 — 杨光，"做一个普通人"
- 看理想《自我、爱与理想：给青年的哲学启蒙课》第三讲第 16 集 — 蔡文菁/刘擎团队，"如何认识死亡"
- 金鱼脑《清迈数字游牧》YouTube 视频
- 有知有行 × 陈鹏《SBBI 2025 中国大类资产年报》

新建 wiki 条目（8 个）：

- [[《不止减压的正念艺术》]] · Reading
- [[《自我、爱与理想：给青年的哲学启蒙课》]] · Reading
- [[刘擎]] · Reading（人物页）
- [[自我关怀]] · knowledge
- [[渗透性自我]] · knowledge
- [[死亡观]] · thinking
- [[清迈]] · travel
- [[中国大类资产长期回报-SBBI2025|中国大类资产长期回报 (SBBI 2025)]] · Investing

更新文件：

- [[index|Wiki Index]] — 重写为带每页一行摘要的目录，并加 🆕 标记
- [[log|Wiki Log]] — 本文件新建

本轮跳过的源（含理由）：

- B 站两篇 clipping（刘擎×白彤东 AI 教育 / 影视飓风 AI 内容识别）— 只有标题+描述+弹幕，**无 transcript**。先在 [[刘擎]] 页面里作为"已剪藏的内容"挂着，等补笔记后再蒸馏概念页
- `output/book/` × 7 + `output/movie/` × 1 — 是 frontmatter-only 的 milestone book/movie cards（仅书名/作者/一句 comment），**没有可蒸馏的正文**。维持原状
- `raw/inbox/20260605220949.md` — 空文件
- `raw/inbox/20260531154147.md` — 用户随笔《坐在电脑前，我不知道该做什么》，是 essay 不是概念源
- `raw/inbox/flomo/*` — 存量 flomo 笔记（5 月中旬内容），本轮未处理

待办（lint）：

- 旧 wiki 条目的一行摘要待补
- [[渗透性自我]] 提到的「共具身性」（Anna Ciaunica）值得单独成页
- 刘擎×白彤东对谈如有补笔记，蒸馏 `Tech/AI与教育` 概念页
- B 站影视飓风《你被 AI 内容骗过吗》如有补笔记，蒸馏 `Tech/AI生成内容识别` 概念页
