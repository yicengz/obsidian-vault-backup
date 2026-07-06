---
title: Wiki Log
description: 按时间倒序的 wiki 演进记录
---

# Wiki Log

按时间倒序的 wiki 演进记录。每条以 `## [YYYY-MM-DD] action | title` 起头，方便用
`grep "^## \[" log.md | tail -N` 解析最近 N 条。

action 可能值：`ingest`、`batch-ingest`、`lint`、`refactor`、`query-archive`。

---

## [2026-07-06] batch-ingest | 共同知识 + SBBI E241 补充

蒸馏来源（2 份高价值素材，均为 2026-07-06 播出的《知行小酒馆》最新两期）：

- 《知行小酒馆》E240 和李井奎聊聊：那些大家都知道的事，怎么一说出口就变了？（原文/导读/思维导图存于 `raw/podcast/`，索引摘要在 [[202607061112 知行小酒馆 E240 共同知识|和李井奎聊聊：那些大家都知道的事，怎么一说出口就变了？]]）
- 《知行小酒馆》E241 这次真的不一样吗？在市场喧嚣里，找到不变的参照系｜SBBI China 2025 上线（同上，索引摘要在 [[202607061113 知行小酒馆 E241 SBBI China 2025|这次真的不一样吗？在市场喧嚣里，找到不变的参照系｜SBBI China 2025 上线]]）

新建 wiki 条目（3 个）：

- [[共同知识]] · knowledge — 博弈论意义上的 common knowledge，与"共识"的关键区分
- [[《共同知识》]] · Reading（书页）— 平克原著
- [[李井奎]] · Reading（人物页）— 译者，浙大经济学者，凯恩斯文集独立翻译者

更新文件：

- [[中国大类资产长期回报-SBBI2025|中国大类资产长期回报 (SBBI 2025)]] · Investing — 追加 "E241 补充"章节：A 股长期收益三分解（分红 20% / 利润增长 8% / 估值 -0.5%）、指数 vs 个股体验的巨大 gap、AI 泡沫的历史类比、每周记账 & 一年一次再平衡的实操建议
- [[index|Wiki Index]] — 加入 3 个新条目 + 1 个 🔄 更新标记，移除上一轮 🆕，更新 Last compiled
- [[log|Wiki Log]] — 本文件追加

本轮跳过的源（含理由）：

- E240/E241 各自的 mp3 音频 — 用户明确只处理 md，音频留在 `~/Downloads/`
- 后半段李井奎讲凯恩斯的具体思想（自由社会理念、和哈耶克通信）— 值得单独一个"凯恩斯"人物页，但本期讨论重心在"共同知识"，把凯恩斯的碎片先放在 [[李井奎]] 里，等有第二个源再拆条

待办（lint）：

- 凯恩斯值得独立人物页（本轮已在 [[李井奎]] 里埋伏了核心判断："世人对凯恩斯最大的误解……"）
- E241 里"AI 与历史泡沫"的历史类比框架（蒸汽机 / 电力 / 互联网泡沫）值得抽出成 knowledge 概念页，暂时先塞在 SBBI 页里
- 上一轮遗留：[[中道]] 提到的高德威/《长期主义》独立 Reading 页；[[有限与无限的游戏]] 补页；旧条目一行摘要补齐；hüzün / 共具身性 拆条

---

## [2026-07-01] batch-ingest | 中道 + 创作者 + 鲎式生存

蒸馏来源（4 份高价值素材）：

- 《无人知晓》E31 中（孟岩，2026-06-29 转录）— 整期讲"中道"，串了一连串看似矛盾的金句（专注森林/细节决定成败、小步快跑/两年磨一剑、心理安全感/硬核文化、自我表达/忘记自我、风险与收益、成功/失败是成功之母…）
- 《无人知晓》E39（孟岩 × 重轻，2026-06-23 转录）— 谈 Rick Rubin《The Creative Act》、创作者状态、不打稿、城市发展门槛、苏格拉底 "not wanting something is as good as having something"
- 人物公众号《周末了，活得别太挑剔》（2026-05-24，2026-06-28 剪藏）— 鲎和蟑螂的生存策略
- Seeking Alpha *Nvidia Stock: The Next Dividend Aristocrat?*（Steven Cress，2026-06-26，2026-06-28 剪藏）

新建 wiki 条目（7 个）：

- [[中道]] · thinking
- [[班尼斯特效应]] · knowledge
- [[心理安全感与硬核文化]] · knowledge
- [[重轻]] · Reading（人物页）
- [[《创造力法则》]] · Reading（书页，Rick Rubin *The Creative Act*）
- [[不挑剔的生存策略]] · thinking
- [[股息贵族]] · Investing

更新文件：

- [[index|Wiki Index]] — 加入 7 个新条目，移除上一轮 🆕，更新 Last compiled
- [[log|Wiki Log]] — 本文件追加

本轮跳过的源（含理由）：

- `footprint/千岛湖.md`、`footprint/上海大学溜达一圈.md` — 只有 frontmatter / 空文件
- `raw/inbox/Trump calls Iran deal 'unconditional surrender'…` — 空文件
- `output/book/《黄仁勋与英伟达之芯》.md` — 空文件（仅 milestone card）
- `output/VX公众号 初心.md` + `output/chat with ai/VX公众号 初心.md` — 用户自己的公众号草稿，是产出不反向蒸馏
- `diary/20260619-20260628` — 个人随笔，按规矩不蒸馏

待办（lint）：

- [[中道]] 提到的「同时追求两件矛盾的事」（高德威/《长期主义》）值得有独立 Reading 页
- [[《创造力法则》]] 提到的 [[有限与无限的游戏]] 是 dangling link，需要补
- 旧 wiki 条目的一行摘要仍待补
- 帕慕克的 hüzün（上一轮遗留）、渗透性自我里的「共具身性」（上一轮遗留）仍未拆条

---

## [2026-06-16] batch-ingest | 帕慕克 + 通讯隔离

蒸馏来源（2 份高价值素材）：

- 2026-06-09 与 AI 的「自我洁净」对谈（[[20260610230455]]）— 起点是读《伊斯坦布尔》遇到帕慕克那段话，串起公婆吃饭的矛盾感、阶级特权、生育率塌方、社保 vs 8 小时工时、数据 vs 道德
- 2026-06-15 自己的公众号 [[VX公众号 自费头等舱的通讯隔离 & 落地后的忙碌|【数仓工作分享】❓]] — "飞机作为通讯隔离带"那一段

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
