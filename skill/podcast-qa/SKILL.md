---
name: podcast-qa
description: 把关于播客逐字稿的 AI 问答保存到 Obsidian vault。当用户说"保存播客问答"、"把这期播客问答存起来"、"记录这次播客问答"、"存到 obsidian"，且对话上下文涉及某期播客时使用。
---

# podcast-qa Skill

把当前会话中关于某期播客的 Q&A，写入 vault 的 `raw/inbox/YYYYMMDDHHMMSS.md`，并链接回源播客逐字稿。

## 关键路径

- Skill 目录（源）：`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/skill/podcast-qa/`
- Skill 目录（发现）：`~/.claude/skills/podcast-qa`（symlink 到 vault 内目录）
- 脚本：`scripts/save_qa.py`
- 播客逐字稿建议位置：`raw/podcasts/<节目名>/<期数> <标题>.md`
- Q&A 输出位置：`raw/inbox/YYYYMMDDHHMMSS.md`
- 今日日记：`diary/YYYYMMDD.md`

## 何时使用

当用户听完/聊完一期播客后，明确说：
- "保存播客问答"
- "把这期播客问答存起来"
- "记录这次播客问答"
- "存到 obsidian"

且当前对话上下文能识别出具体是哪期播客。

## 执行流程

1. **确认源播客**
   - 从当前对话上下文中找出播客节目名、期数、标题。
   - 在 `raw/podcasts/` 下寻找对应的逐字稿文件（按 `raw/podcasts/<节目名>/` 递归搜索）。
   - 如果找不到，询问用户逐字稿位置，或先用当前会话中的引用信息继续。

2. **准备 Q&A 内容**
   - 提取用户关于播客的问题和 AI 的回答。
   - 保留用户原话，不要缩写或释义 AI 的回答。
   - 多个问答轮次用 `---` 分隔。
   - 每个问答块使用 `[!warning] <AI 名称>` callout：
     - `[!warning]` 提供暖色（琥珀/橙色）底色。
     - 标题写当前 AI 名称：`Kimi Code`、`Claude Code` 或 `其他`。
     - 如果同一轮对话里换了 agent，每个 callout 标题都要对应更新。

3. **调用脚本写入**
   推荐先把 Q&A 内容写到一个临时文件，再用 `--content-file` 传入：
   ```bash
   python3 "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/skill/podcast-qa/scripts/save_qa.py" \
     --vault "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng" \
     --show "无人知晓" \
     --episode "E43" \
     --title "没有更好的生活" \
     --agent "Kimi Code" \
     --transcript "raw/podcasts/无人知晓/E43 张潇雨、孟岩对话许哲：没有更好的生活.md" \
     --content-file "/tmp/qa_content.md" \
     --link-diary
   ```

4. **汇报结果**
   - 告诉用户写入的文件名和路径。
   - 如果日记链接成功，也提一下。

## 输出文件格式

文件名：`raw/inbox/YYYYMMDDHHMMSS.md`（使用对话开始时间或当前时间）。

Frontmatter：
```yaml
---
title: 无人知晓 E43 问答：没有更好的生活
description: 基于《没有更好的生活》逐字稿的 AI 问答
tags:
  - podcast/无人知晓
  - podcast-qa
source: "[[E43 张潇雨、孟岩对话许哲：没有更好的生活|没有更好的生活]]"
agent: Kimi Code
is_diary: false
is_essay: true
is_wx_article: false
---
```

正文（暖色高亮块 + AI 来源标识）：
```markdown
> [!warning] Kimi Code
> 用户的问题原文
>
> AI 的回答正文……

---

> [!warning] Kimi Code
> 用户的追问原文
>
> AI 的回答正文……
```

## 播客逐字稿存放建议

建议用户把未来导入的逐字稿放在：
```
raw/podcasts/<节目名>/<期数> <标题>.md
```
例如：
```
raw/podcasts/无人知晓/E43 张潇雨、孟岩对话许哲：没有更好的生活.md
raw/podcasts/知行小酒馆/E221 对话张潇雨：生活太重要，以至于不能太认真.md
```

## 何时不要直接写

- 用户只是问"这期播客讲了什么"——正常回答即可，等用户说保存再调用 skill。
- 用户没有明确说保存，但想继续追问——先继续对话，最后再保存。
- 找不到对应逐字稿且用户也未提供——不要猜测，先问清楚。

## 排错

- "找不到播客文件"：检查 `raw/podcasts/<节目名>/` 下是否有对应 md 文件。
- "日记链接失败"：通常是因为 `diary/YYYYMMDD.md` 不存在；脚本会尝试创建。
- 中文路径问题：脚本使用 UTF-8，路径含空格时记得加引号。
