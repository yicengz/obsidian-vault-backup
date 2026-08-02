---
name: diary-update
description: 更新 Obsidian vault 里的日记（diary/YYYYMMDD.md），把当天在 vault 各处新建/修改的内容（footprint、inbox、chat with ai、wiki、clippings、podcast）用第一人称叙事串起来并内链。当用户说"更新日记"、"更新今天的日历"、"补一下这两天的日记"、"整理最近几天的日历"、"把今天的东西写到日记里"时使用。
---

# diary-update Skill

把 vault 里那些"孤零零躺着的新文件"（footprint 摘抄、inbox 时间戳笔记、chat with ai 对话蒸馏、wiki 新条目、clippings 剪藏、podcast 转录）在当日日记里织成一段第一人称叙事，并双向内链。

## 关键路径

- Vault: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/`
- 日记: `diary/YYYYMMDD.md`（历史日记会归到 `diary/YYYYQx/`）
- 相关源目录：
  - `footprint/` — 书 / 视频 / 播客 / TED 等消费记录
  - `raw/inbox/` — 时间戳笔记、AI 对话、灵感捕获
  - `raw/clippings/` — 网页剪藏
  - `raw/podcast/<节目名>/` — 播客转录
  - `output/chat with ai/` — 与 AI 协作的对话/草稿
  - `wiki/thinking/` · `wiki/knowledge/` · `wiki/Reading/` — 新蒸馏的概念页
- AGENTS.md: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/AGENTS.md`（vault 的操作手册，读一次能省事）

## 何时使用

用户说：
- "更新今天的日记" / "把今天的东西写到日记里"
- "更新这两天的日历文档" / "补一下最近几天的日记"
- "整理最近的日历" / "把今天更新的内容引用到日历里"

不主动使用——只有用户明确要求整理日记时才触发。

## 执行流程

### 1. 确认日期范围

用户说"今天" / "这两天" / "最近几天"，映射为具体日期区间。今天日期从系统消息或 `date +%Y%m%d` 拿。**遇到相对表达时把它转成绝对日期存进本次要处理的列表**。

### 2. 扫描当日新建/修改的文件

对每个目标日期 `YYYYMMDD`：

```bash
VAULT="~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng"
cd "$VAULT"
# 找当日改动的所有 md（排除 diary 本身、.claude、.obsidian）
find . -name "*.md" -newermt "YYYY-MM-DD 00:00" ! -newermt "YYYY-MM-DD+1 00:00" \
  -not -path "./diary/*" -not -path "./.claude/*" -not -path "./.obsidian/*"
```

或者用文件名时间戳兜底（footprint / inbox 通常带 `YYYYMMDD` 前缀）。

### 3. 读日记骨架

日记文件通常已经存在但很稀疏（可能只有 frontmatter，或用户自己挂了几个链接没写文字）。**必须尊重已有内容**：
- 已有的内链一定要保留
- 用户自己写的任何文字一定要保留（不管多短）
- 只是"补叙事"——不是"重写"

如果文件不存在，用这个模板起：
```yaml
---
title:
description:
tags:
is_diary: true
is_essay: false
is_wx_article: false
---
```

### 4. 快速读一遍每个相关文件的头部

理解每份内容的核心，才能写出真实叙事。别只看标题就编——特别是 chat with ai / inbox 里的内容，标题和真实主题常常有差距。

### 5. 按时间线组织成叙事

- **第一人称**（"我"、"下午和 Claude ..."）
- **自然连接词**：先 / 然后 / 顺便 / 半夜 / 深夜又 / 顺到
- **一段一段流下来**，不要按"上午 / 下午 / 晚上"标小节
- **具体细节**：具体数字、原话、真实的一句金句，都要保留
- **内链所有相关文件**：`[[timestamp|显示名]]` 或 `[[文件名]]`

### 6. 交叉日的处理

有的 inbox 笔记时间戳在凌晨（比如 `20260801000537` 是 8-01 0 点 5 分）——用户可能把它归在 7-31 的日记里（因为是"深夜"意义上的当天）。**尊重用户已有归属**，别把它挪到"正确"的那一天。

### 7. 记录本次会话里发生的事

如果日记要覆盖到"今天"、而今天的主要活动就是这次 AI 对话——直接把这次对话的实质内容写进日记（例如 "跟 Claude 补了 X 和 Y 的日记"、"和 Claude 拆了下 X 概念"）。

## 写作风格

严格遵守用户的写作偏好（见 `~/.claude/projects/-Users-yiceng/memory/feedback_writing_style.md`）：

- **不要编造细节**——用户没说的心理活动、感受、心得，一律不加
- **不要 AI 式总结句**——不写"总的来说" / "这让我意识到" / "启发很大"这类空话
- **保留具体事实**：数字、人名、原话、地名、时间
- **保留真实心理活动**——但只保留用户在对话里实际说过 / 写过的，不发明
- **一句金句**用引号照抄，不要转述

## 常见陷阱

1. **broken link**：链接文件名要对得上真实文件。检查方式是先 `ls` 或者 `find`，别按记忆写。
2. **重复叙述**：同一件事已经在前一天的日记里写过了，第二天不要再展开一遍——只在需要承接时轻轻提一句。
3. **归属跨天**：footprint 里有 `footprint_date` 字段，inbox 里有时间戳文件名——冲突时以 `footprint_date` 为准。
4. **覆盖已有骨架**：Write 前必须先 Read；已有链接和文字必须保留。
5. **假设有心理活动**：如果用户只是 clip 了个视频没写笔记，就说"clip 了但没写笔记"，别自作主张写"深有感触"。
6. **粗暴分类**：不要把日记按"投资 / 阅读 / 反思"分小节，那是 AI 味。按时间线自然流。

## 安装（一次性）

skill 需要软链到 `~/.claude/skills/` 才会被 Claude Code 发现：

```bash
ln -s "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/skill/diary-update" \
      "$HOME/.claude/skills/diary-update"
```

（这一步在 skill 首次创建时执行一次即可。）

## 参考现有日记

好的样本：
- `diary/20260729.md` — 有具体细节 + 播客 + 概念内链 + AI 对话
- `diary/20260730.md` — 尝试 + 失败 + 反思 + 蒸馏
- `diary/20260731.md` — 多线并行（听 / 摘 / 聊 / 看）
- `diary/20260801.md` — 短，但有内链和事实

不好的样本：
- 只有孤零零几个 `[[link]]` 没有叙事的（骨架）——这是要补的对象
