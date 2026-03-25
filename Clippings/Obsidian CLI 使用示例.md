# Obsidian CLI 使用示例

## 场景1：搜索特定主题的笔记

### 以前的方式 (高 token 消耗)
```
AI: 让我搜索你的 Obsidian 中关于 "AI" 的笔记...
[扫描所有文件]
[读取每个文件内容]
[匹配关键词]
```

### 使用 CLI 的方式 (低 token 消耗)
```bash
obsidian search "AI"
# 或
obsidian search-content "人工智能"
```

## 场景2：读取特定笔记

### 以前的方式
```
AI: 让我读取那篇关于 AlphaGo 的文章...
[扫描目录找到文件]
[读取整个文件]
```

### 使用 CLI 的方式
```bash
obsidian print "AlphaGo - The Movie"
# 或使用 REST API
curl http://127.0.0.1:27124/vault/Clippings/AlphaGo%20-%20The%20Movie.md
```

## 场景3：创建新笔记

### 以前的方式
```
AI: 让我为你创建一个新笔记...
[使用 WriteFile 工具]
```

### 使用 CLI 的方式
```bash
obsidian create "Clippings/新文章.md" --content "# 标题\n\n内容..."
# 或 REST API
curl -X POST http://127.0.0.1:27124/vault/Clippings/新文章.md \
  -H "Content-Type: text/markdown" \
  -d "# 标题\n\n内容"
```

## 场景4：追加内容到每日笔记

```bash
obsidian append "今天学到了..."
# 或使用 daily 命令打开今日笔记
obsidian daily
```

## Token 节省估算

| 操作 | 文件扫描方式 | CLI 方式 | 节省 |
|------|------------|---------|------|
| 搜索笔记 | ~5000 tokens (扫描) | ~100 tokens (命令) | 98% |
| 读取笔记 | ~3000 tokens (全文) | ~500 tokens (结果) | 83% |
| 列出文件 | ~2000 tokens | ~50 tokens | 97% |

---

*配置完成后，我会优先使用这些命令来操作你的 Obsidian，而不是直接读取文件。喵～*
