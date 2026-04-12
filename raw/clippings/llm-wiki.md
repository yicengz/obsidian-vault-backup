---
title: "llm-wiki"
link: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author:
  - "karpathy"
publish_date:
clip_date: 2026-04-12
description: "llm-wiki. GitHub Gist: instantly share code, notes, and snippets."
tags:
  - "clippings"
---
## LLM Wiki

A pattern for building personal knowledge bases using LLMs.

用 LLM 构建个人知识库的一种模式。

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

这是一份想法文件，设计用来直接粘贴给你自己的 LLM Agent（比如 OpenAI Codex、Claude Code、OpenCode / Pi 等）。它的目标是传达高层次的思路，具体细节由你和 Agent 协作完成。

## The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

大多数人用 LLM 处理文档的方式都是 RAG：上传一堆文件，LLM 在提问时检索相关片段，生成答案。这能用，但每次提问 LLM 都要从头重新"发现"知识，没有任何积累。如果你问一个需要综合五篇文档的微妙问题，LLM 每次都得重新找、重新拼。什么都没有沉淀下来。NotebookLM、ChatGPT 文件上传、以及大多数 RAG 系统都是这个逻辑。

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then *kept current*, not re-derived on every query.

这里的思路不同。LLM 不只是在提问时从原始文档检索，而是**增量地构建并维护一个持久化的 wiki**——一组结构化、相互链接的 markdown 文件，夹在你和原始资料之间。每当你加入一个新来源，LLM 不只是把它索引起来等以后检索，而是读它、提取关键信息、整合进现有 wiki——更新实体页、修订主题摘要、标记新数据与旧结论的矛盾、强化或挑战已有的综合判断。知识只编译一次，之后持续保持更新，而不是每次查询都重新推导。

This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

这就是核心差异：**wiki 是一个持久存在、不断复利的产物。** 交叉引用已经在那里了，矛盾已经被标注了，综合分析已经反映了你读过的一切。每加入一个来源、每问一个问题，wiki 都会变得更丰富。

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

你从来不需要（或很少需要）自己写 wiki——LLM 负责写和维护所有内容。你负责选材、探索、问出好问题。LLM 做所有体力活——摘要、交叉引用、归档、记账，这些让知识库随着时间真正变得有用的工作。实际操作中，我一边开着 LLM Agent，一边开着 Obsidian。LLM 根据我们的对话做编辑，我实时浏览结果——点链接、看图谱视图、读更新后的页面。Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。

This can apply to a lot of different contexts. A few examples:

这套方法可以用在很多场景，举几个例子：

- **Personal**: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
- **个人**：追踪自己的目标、健康、心理、自我提升——把日记、文章、播客笔记归档，逐渐建立起一幅关于自己的结构化图景。

- **Research**: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
- **研究**：花几周或几个月深入某个主题——读论文、文章、报告，逐步建立一个带有演进论点的完整 wiki。

- **Reading a book**: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
- **读书**：边读边归档每一章，为人物、主题、情节线索建页，记录它们之间的联系。读完后你就有了一本丰富的伴读 wiki。想想像 [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) 这样的粉丝 wiki——数千个相互链接的页面，涵盖人物、地点、事件、语言，由志愿者社区历经多年建成。你可以在阅读过程中个人建出类似的东西，由 LLM 做所有交叉引用和维护。

- **Business/team**: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
- **企业/团队**：由 LLM 维护的内部 wiki，输入来自 Slack 对话、会议记录、项目文档、客户通话。可以有人工审核环节。wiki 能保持更新，因为 LLM 做了团队里没人想做的维护工作。

- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where you're accumulating knowledge over time and want it organized rather than scattered.
- **竞品分析、尽职调查、旅行规划、课程笔记、爱好深潜**——任何你在随时间积累知识、希望它有条理而非四散的场景。

## Architecture

There are three layers:

分三层：

**Raw sources** — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

**原始来源**——你精心挑选的原始文档集合。文章、论文、图片、数据文件。这些是不可变的——LLM 只读不改。这是你的事实基准。

**The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**Wiki**——一个由 LLM 生成的 markdown 文件目录。包含摘要、实体页、概念页、比较页、总览、综合分析。这一层完全由 LLM 掌管：它创建页面，在新来源加入时更新页面，维护交叉引用，保持一致性。你负责读，LLM 负责写。

**The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

**Schema（规范文档）**——一份告诉 LLM wiki 如何结构化、遵循什么约定、在摄入来源/回答问题/维护 wiki 时走什么流程的文档（比如 Claude Code 用 CLAUDE.md，Codex 用 AGENTS.md）。这是核心配置文件——正是它让 LLM 成为一个守纪律的 wiki 维护者，而不是普通聊天机器人。你和 LLM 会随着时间共同演化这份文档，摸索出什么方式适合你的领域。

## Operations

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

**摄入（Ingest）。** 你把新来源放入原始集合，告诉 LLM 去处理它。示例流程：LLM 读取来源，与你讨论核心要点，在 wiki 里写一页摘要，更新索引，更新 wiki 中相关的实体页和概念页，在日志里追加一条记录。一个来源可能会涉及 10-15 个 wiki 页面。我个人偏好一次摄入一个来源、全程参与——读摘要、检查更新、引导 LLM 重点强调什么。但你也可以一次批量摄入多个来源，减少监督。开发适合自己风格的工作流，并记录在 schema 里供以后的会话使用，这件事取决于你。

**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

**查询（Query）。** 你向 wiki 提问。LLM 搜索相关页面，读取，综合出带引用的答案。答案可以有不同形式——markdown 页面、比较表格、幻灯片（Marp）、图表（matplotlib）、画布。重要的洞察：**好的答案可以作为新页面归档回 wiki。** 你让 LLM 做的比较、分析、你发现的联系——这些都很有价值，不应该消失在聊天记录里。这样你的探索就像摄入的来源一样，在知识库里不断复利。

**Lint.** Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

**整理（Lint）。** 定期让 LLM 对 wiki 做健康检查。检查项：页面间的矛盾，被新来源取代的过时结论，没有入链的孤岛页面，被提及但缺少独立页面的重要概念，缺失的交叉引用，可以通过网络搜索填补的数据空白。LLM 很擅长建议新的待探索问题和新的值得寻找的来源。这让 wiki 在成长过程中保持健康。

## Indexing and logging

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

两个特殊文件帮助 LLM（和你）在 wiki 成长时导航，它们的用途不同：

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

**index.md** 以内容为导向。它是 wiki 里所有内容的目录——每个页面都附有链接、一行摘要，以及可选的元数据（如日期或来源数量）。按类别组织（实体、概念、来源等）。LLM 在每次摄入时更新它。回答查询时，LLM 先读索引找到相关页面，再深入阅读。这在中等规模下效果出奇地好（约 100 个来源、数百个页面），且不需要基于嵌入的 RAG 基础设施。

**log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

**log.md** 以时间为顺序。它是一份只追加的记录，记录发生了什么、何时发生——摄入、查询、整理通过。一个实用技巧：如果每条记录以统一前缀开头（例如 `## [2026-04-02] ingest | Article Title`），日志就可以用简单的 unix 工具解析——`grep "^## \[" log.md | tail -5` 可以给出最近 5 条记录。日志为你提供 wiki 演进的时间线，帮助 LLM 了解最近做了什么。

## Optional: CLI tools

At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. [qmd](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

在某个时间点，你可能想构建一些小工具来帮助 LLM 更高效地操作 wiki。最显而易见的是 wiki 页面的搜索引擎——在小规模下索引文件就够了，但随着 wiki 增长，你需要真正的搜索。[qmd](https://github.com/tobi/qmd) 是个不错的选择：它是一个针对 markdown 文件的本地搜索引擎，支持 BM25/向量混合搜索和 LLM 重排，全部在设备上运行。它既有 CLI（LLM 可以 shell 调用），也有 MCP 服务器（LLM 可以作为原生工具使用）。你也可以自己构建更简单的东西——当需求出现时，让 LLM 帮你 vibe code 一个简单的搜索脚本。

## Tips and tricks

- **Obsidian Web Clipper** is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.
- **Obsidian Web Clipper** 是一个将网页文章转为 markdown 的浏览器插件，对于快速把来源导入原始集合非常有用。

- **Download images locally.** In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. `raw/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.
- **把图片下载到本地。** 在 Obsidian 设置 → 文件与链接中，将"附件文件夹路径"设为固定目录（如 `raw/assets/`）。然后在设置 → 快捷键中搜索"Download"，找到"下载当前文件的附件"并绑定快捷键（如 Ctrl+Shift+D）。抓取文章后按快捷键，所有图片就下载到本地了。这是可选的，但很有用——它让 LLM 能直接查看和引用图片，而不依赖可能失效的 URL。注意 LLM 无法在一次处理中原生读取带内联图片的 markdown——解决办法是让 LLM 先读文字，再单独查看部分或全部引用图片以获取额外上下文。有点笨拙，但够用。

- **Obsidian's graph view** is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.
- **Obsidian 的图谱视图**是查看 wiki 形态的最佳方式——什么和什么相连，哪些页面是枢纽，哪些是孤岛。

- **Marp** is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.
- **Marp** 是一种基于 markdown 的幻灯片格式，Obsidian 有对应插件，可以直接从 wiki 内容生成演示文稿。

- **Dataview** is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.
- **Dataview** 是一个 Obsidian 插件，可以对页面 frontmatter 运行查询。如果 LLM 给 wiki 页面加了 YAML frontmatter（标签、日期、来源数量），Dataview 可以生成动态表格和列表。

- The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.
- Wiki 本质上就是一个 markdown 文件的 git 仓库，版本历史、分支、协作都是免费赠送的。

## Why this works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

维护知识库的繁琐之处不在于阅读或思考，而在于记账：更新交叉引用，保持摘要最新，标注新数据与旧结论的矛盾，维护数十个页面的一致性。人类会放弃 wiki，因为维护负担的增长速度超过价值的积累。LLM 不会厌倦，不会忘记更新交叉引用，可以在一次处理中涉及 15 个文件。wiki 能持续得到维护，因为维护成本接近于零。

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

人类的工作是筛选来源、引导分析、问出好问题、思考这一切意味着什么。LLM 的工作是其他所有事情。

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

这个想法在精神上与 Vannevar Bush 的 Memex（1945）相通——一个带有文档间联想路径的个人精选知识库。Bush 的愿景比互联网后来的样子更接近这里描述的东西：私人的、主动策划的，文档之间的连接与文档本身同样有价值。他没能解决的问题是谁来做维护。LLM 解决了这个问题。

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.

这份文档有意保持抽象。它描述的是想法，而不是具体实现。确切的目录结构、schema 约定、页面格式、工具选择——所有这些都取决于你的领域、你的偏好和你选择的 LLM。上面提到的一切都是可选且模块化的——拿有用的，忽略没用的。比如：你的来源可能纯文本，根本不需要图片处理；你的 wiki 可能足够小，只需要索引文件，不需要搜索引擎；你可能不在乎幻灯片，只想要 markdown 页面；你可能想要一套完全不同的输出格式。正确的使用方式是把这份文档分享给你的 LLM Agent，一起实例化一个适合你需求的版本。这份文档唯一的任务是传达这个模式，其余的 LLM 都能搞定。
