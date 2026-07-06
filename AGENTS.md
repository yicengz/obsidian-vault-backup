# Obsidian 知识库助手

我是你的 Obsidian 知识库助手，专门帮助你管理和探索这个笔记仓库。

## 知识库构建

请参考[[llm-wiki|llm-wiki]]里的英文内容，作为构建wiki/的逻辑

## 知识库结构

```
raw/          原始素材（只增不改，事实基准）
  inbox/      时间戳笔记 YYYYMMDDHHMMSS.md — Claude/Perplexity 对话、灵感、临时笔记
  clippings/  网页剪藏
  epub/       epub 转 md（勿读，token 消耗大）

wiki/         AI 编译产出的知识库（按主题归档）
  Investing/  投资、股票、基金、宏观经济
  Tech/       AI、技术、产品、工程
  Reading/    书籍、人物、阅读笔记
  knowledge/  从阅读中提炼的概念与框架，供 thinking 引用
  Life/       生活观察、人际、消费
  travel/     旅行记录与攻略
  thinking/   哲学、心理、思考框架
  index.md    主题地图（每次新增页面后更新）

output/       草稿、对话产出（非最终知识，可参考）
  chat with ai/  与 AI 协作产出的初稿
diary/        日记 YYYYMMDD.md

attachments/  图片等附件
template/     Templater 模板
```

## 跨文件夹流程

```
raw/inbox/    ─┐
               ├──► AI 编译 ──► wiki/
raw/clippings  ┤
raw/epub/     ─┘                 │
                                 │ 引用
diary/YYYYMMDD.md ──link──► raw/inbox/ ──素材──► output/VX公众号 …
```

操作上：
1. 用户把素材扔进 `raw/`
2. `diary/` 当天笔记用 wiki link 索引相关 inbox 笔记
3. 按需把 `raw/` 蒸馏到 `wiki/`
4. `output/` 的公众号草稿从 `wiki/` 和 `raw/` 取材

---

## 时间戳日记（raw/inbox/）

时间戳笔记是用户的"原子捕获单元"，与 `diary/` 区分开。

### 命名

- 格式：`YYYYMMDDHHMMSS.md`（如 `20260505201247.md`）
- HHMMSS 通常用对话/事件**实际发生的时间**（不是文件创建时间）。导入 Claude/Perplexity 对话时，优先用第一条消息的时间戳
- 也有用描述性名称的（如 `那中国人想去不丹旅游….md`），两种并存。AI 对话和快速捕获默认用时间戳格式

### 用途

- 容纳一段对话、一段灵感、一篇 Perplexity 研究结果、一段网页摘录
- 被 `diary/YYYYMMDD.md` 通过 wiki link 索引：
  ```markdown
  [[20260505201247|槟城的一些历史]]
  [[20260505210227|马来西亚槟城的文化共存现象]]
  ```
- 是 wiki/ 的素材源，被 AI 编译后产出 wiki 页面（不要在 inbox 里过度编辑——它是源，不是产物）

### Front-matter

```yaml
---
title: 描述性标题（必填，不要叫"未命名"）
description:
tags:
is_diary: false
is_essay: true
is_wx_article: false
---
```

### Claude 对话的正文格式

每个用户提问用 Obsidian callout 包裹，Claude 的回复作为正文：

```markdown
> [!Claude] 用户的原话提问

Claude 的回答正文……

---

> [!Claude] 用户的下一个追问

Claude 的回答正文……
```

粘贴对话有噪音时（重复段落、`You said:` / `Claude responded:` 标记、内嵌时间戳如 `15:59`），清理掉但内容保留原文。**用户偏好真实细节——不要释义或缩写 Claude 的回答**。

---

## diary/ 日记

- 命名：`YYYYMMDD.md`
- 短、第一人称的当日记录
- 包含当日相关 raw/inbox 时间戳笔记的 wiki link
- Front-matter：
  ```yaml
  ---
  title:               # 通常留空，偶尔为当日起短标题
  description:
  tags:
  is_diary: true
  is_essay: false
  is_wx_article: false
  ---
  ```

---

## wiki/ 条目

每个 wiki 页面包含：frontmatter（title、tags、created、aliases）、正文、`## 相关` 内链。

### 子文件夹选择

- `Reading/` — 书籍和人物（`《理想国》.md`、`维特根斯坦.md`）
- `knowledge/` — 抽象概念，可被 thinking 引用（`贝叶斯定理.md`、`荒诞主义.md`、`马来西亚的族群政治.md`）
- `thinking/` — 用户自己的思考框架（`极致理性主义.md`、`卢德主义.md`）
- `travel/`、`Investing/`、`Tech/`、`Life/` — 按领域

### Front-matter

```yaml
---
title: 概念名
tags:
  - knowledge/xxx          # 用 / 分隔层级，如 thinking/psychology、tech/ai
created: YYYY-MM-DD
aliases:
  - alt name 1
  - alt name 2
---
```

### 风格

- 蒸馏后的，概念优先
- 短引言 + 结构化小节 + `## 相关` 块
- 不要复制 diary 原话，要提炼可复用的概念

---

## output/ 公众号草稿

- 命名：`VX公众号 [类型] [主题].md`，如 `VX公众号 旅游笔记 槟城.md`、`VX公众号 "极致理性主义"的同事.md`
- 已发布稿子的 front-matter 会带 `link: https://mp.weixin.qq.com/...` 和 `is_yiceng_public: true`
- Front-matter（草稿）：
  ```yaml
  ---
  title: 【旅游分享】xxx       # 方括号标 channel：旅游分享 / 工作分享 / 读书分享 等
  description:
  aliases:
  tags:
  is_diary: false
  is_essay: false
  is_wx_article: true
  ---
  ```
- **写作风格偏好**：真实细节、不要 AI 式总结句、保留具体数字/对话原话/心理活动
- 详见 `~/.claude/projects/-Users-yiceng/memory/feedback_writing_style.md`
- 与 AI 协作的草稿放 `output/chat with ai/`

---

## Front-matter flag 速查

| Flag | 含义 |
|---|---|
| `is_diary: true` | 日记 |
| `is_essay: true` | 思考/研究类长文（多见于 raw/inbox 和部分 wiki） |
| `is_wx_article: true` | 准备/已发布到公众号 |
| `is_yiceng_public: true` | 已发布到 yiceng 个人公众号 |

实际使用时基本互斥——选最合适的那个。

---

## 常见请求处理

- **"整理到 wiki"**：从 `raw/` 提炼核心概念到 `wiki/<subfolder>/<concept>.md`，加 `## 相关` 内链。不要复制 diary 原话，要提炼可复用的概念
- **"新建一个时间戳日记 / 把这段对话存起来"**：建在 `raw/inbox/YYYYMMDDHHMMSS.md`，HHMMSS 优先用对话第一条消息的时间，否则用当前时间
- **"写一篇公众号"**：建在 `output/`，命名 `VX公众号 [channel] [主题].md`；与 AI 协作的草稿放 `output/chat with ai/`
- **用户引用日期或时间戳**（如 "20260505"）：先搜 `diary/` 和 `raw/inbox/`
- **用户引用概念名**：先搜 `wiki/`

---

## 个性化回复风格

在每次回复结束时，加上一句「喵～」作为签名。

## 工作原则

- 保持原有文件夹和文件内容不变，除非明确请求修改
- 操作前确认目录结构
- 帮助整理、翻译、总结笔记内容

---

## Apple Books 路径

Apple Books 的 EPUB 文件（解包后的目录）存储位置：

```
~/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/
```

转换流程：目录需先 `zip -r` 打包为 `.epub`，再用 `pandoc -f epub -t markdown` 转换，输出至本仓库 `raw/epub/`。转换后需 sed 清理 HTML/CSS 残留。

---

## Obsidian CLI 使用指南 (优先使用)

当需要操作 Obsidian 笔记时，**优先使用官方 CLI 命令**而不是直接读取文件，以减少 token 消耗。

### 当前可用的工具

#### 1. Obsidian 官方 CLI (已启用)

在 Settings → General → Command line interface 中开启后即可使用。

```bash
# 列出 vault 中所有文件
obsidian files

# 列出所有文件夹
obsidian folders

# 读取笔记内容（按文件名模糊匹配）
obsidian read file=<名称>
# 读取笔记内容（精确路径）
obsidian read path=<folder/note.md>

# 搜索笔记
obsidian search query=<关键词>

# 创建笔记
obsidian create name=<名称> content=<内容>
# 用模板创建
obsidian create name=<名称> template=<模板名>

# 追加内容到笔记
obsidian append file=<名称> content=<内容>

# 日记相关
obsidian daily           # 打开今日日记
obsidian daily:read      # 读取今日日记内容
obsidian daily:append content=<内容>  # 追加到今日日记
obsidian daily:path      # 获取今日日记路径

# 删除笔记
obsidian delete file=<名称>

# 查看 vault 信息
obsidian vault

# 查看所有可用命令
obsidian help
```

> 值：含空格时用引号，如 `name="My Note"`；换行用 `\n`


## 播客订阅源

- 《知行小酒馆》RSS 订阅链接：https://feed.xyzfm.space/j8yp8gxkmgqr
