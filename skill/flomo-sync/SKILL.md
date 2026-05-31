---
name: flomo-sync
description: 把 flomo 的 HTML 导出同步到 Obsidian vault。当用户说要同步 flomo / 导入 flomo / 更新 flomo 笔记 / 刚导出了 flomo 包 / 让 Claude 帮忙处理 flomo 时使用。
---

# flomo-sync skill

把 flomo 网页端导出的 HTML 包，转成 markdown 笔记写进用户的 Obsidian vault。

## 关键路径

- 脚本目录: `~/program/flomo-to-obsidian/`
  - `sync.py` — 主转换脚本
  - `sync.sh` — 一行命令的 wrapper（自动找最新导出）
- flomo 导出目录: `~/Documents/flomo/flomo@xxx-YYYYMMDD/`
- Obsidian vault: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/`
- 笔记写到: vault 下的 `raw/inbox/flomo/`，文件名 `YYYYMMDDHHMM.md`
- 附件复制到: vault 下的 `attachments/flomo/`

## 默认使用方式

绝大多数情况下，用户的意图就是"同步最新的 flomo 导出"。直接跑：

```bash
~/program/flomo-to-obsidian/sync.sh
```

wrapper 会自动找 `~/Documents/flomo/` 下最新的 `flomo@xxx-YYYYMMDD/` 目录，
默认只处理 `2026-01-01` 及之后的 memo。脚本是幂等的——已经同步过的 memo 会被跳过。

## 参数化用法

如果用户给了具体日期、或者想换 vault、或者要 dry-run，直接调 `sync.py`：

```bash
python3 ~/program/flomo-to-obsidian/sync.py \
  --export ~/Documents/flomo/<导出目录> \
  --vault  "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng" \
  --since  2026-06-01 \
  [--dry-run]
```

或者用 sh wrapper 改 since：

```bash
~/program/flomo-to-obsidian/sync.sh 2026-06-01
```

## 脚本做了什么

1. 解析 flomo 导出的 HTML（按 `<div class="memo">` 切块）
2. 提取每条 memo 的时间戳（精确到秒）和正文
3. HTML → markdown 转换：
   - `<p>` → 段落（空行分隔）
   - `<ol>` / `<ul>` → 有序/无序列表（前后留空行）
   - `<a>` → `[text](url)`
   - `<strong>`/`<b>` → `**bold**`；`<em>`/`<i>` → `*italic*`
   - `<br/>` → 换行（注意 `<br>` 和 `<b>` 的正则边界）
   - 解码 HTML 实体（`&amp;` → `&` 等）
4. 文件名按 `YYYYMMDDHHMM.md`，同分钟冲突用 `-2`、`-3` 后缀
5. 附件处理：
   - 图片 `<img src="file/X">` → 复制到 `attachments/flomo/X` + `![[...]]` 引用
   - 音频 `<audio src="file/X">` → 复制 + `![[...]]` + flomo 自带的语音转写以 `> [!quote] 语音转写` callout 形式保留
6. 每条笔记末尾自动加 `#来自/flomo` 标签
7. 用 vault 中 `raw/inbox/flomo/*.md` 的文件名前缀做去重，已存在的整条跳过

## 用户的工作流

1. flomo 网页端：设置 → 导出全部 memo（HTML 格式）
2. 解压 zip 到 `~/Documents/flomo/`（保留 `flomo@xxx-YYYYMMDD/` 这个目录结构）
3. 跟 Claude 说一声"同步 flomo"，或者自己跑 `~/program/flomo-to-obsidian/sync.sh`
4. 完事后用户在 Obsidian 里看 `raw/inbox/flomo/`

## 何时不要直接跑

- 用户说"看看上次同步的是哪天"——读 `raw/inbox/flomo/` 里最新文件名的时间戳即可，不用跑脚本
- 用户说"flomo 里我说过 XXX 吗"——直接 `grep -r` vault 里的内容，不要重新同步
- 用户说"我想改 flomo 里的某条"——flomo 是源头，去 flomo 改，下次同步会带过来（注意：脚本现在不更新已存在的笔记，是设计如此，避免覆盖用户在 Obsidian 里的二次编辑）

## 排错

- "找不到 .html 文件"：检查 flomo 导出目录里有没有 `*的笔记.html`
- "缺失附件"：导出 zip 解压时 file/ 目录可能被漏了，检查解压完整性
- 中文显示为 `&amp;` 或乱码：脚本默认用 utf-8 读写，理论上不会发生；如发生，先看导出 HTML 编码
