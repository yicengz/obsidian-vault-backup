# Obsidian CLI 配置指南

## 版本信息
- Obsidian 版本: 1.12.4 ✅ (支持 CLI)

## 启用官方 CLI

### 步骤 1: 在 Obsidian 应用中开启 CLI

1. 打开 Obsidian 应用
2. 进入 **Settings (设置)** → **General (通用)** → **Advanced (高级)**
3. 找到 **Command line interface (命令行界面)**
4. 开启开关

开启后，Obsidian 会自动将 `obsidian` 命令添加到 PATH。

### 步骤 2: 验证安装

开启后，在终端运行:
```bash
which obsidian
obsidian --help
```

## 可选: 安装 Obsidian CLI REST API 插件 (推荐)

这个插件提供 HTTP API 接口，更适合 AI 工具调用。

### 安装步骤

1. 在 Obsidian 中打开 **Settings** → **Community plugins (社区插件)**
2. 关闭 **Safe mode (安全模式)**
3. 点击 **Browse (浏览)**，搜索 **"Obsidian CLI REST"**
4. 安装并启用插件
5. 插件会自动在 `http://127.0.0.1:27124` 启动服务器

### 验证 REST API

```bash
# 测试服务器是否运行
curl http://127.0.0.1:27124/

# 搜索笔记
curl "http://127.0.0.1:27124/search?q=关键词"

# 获取笔记内容
curl "http://127.0.0.1:27124/vault/笔记名.md"
```

## 常用命令

### 官方 CLI 命令
```bash
# 打开指定笔记
obsidian open "笔记名"

# 搜索笔记
obsidian search "关键词"

# 打开今日日记
obsidian daily

# 追加内容到今日日记
obsidian append "要添加的内容"

# 创建新笔记
obsidian create "新笔记.md" --content "内容"
```

### REST API 端点
```bash
# 列出所有笔记
curl http://127.0.0.1:27124/vault/

# 获取笔记内容
curl http://127.0.0.1:27124/vault/笔记路径.md

# 搜索内容
curl "http://127.0.0.1:27124/search?q=关键词"

# 创建/更新笔记
curl -X POST http://127.0.0.1:27124/vault/新笔记.md \
  -H "Content-Type: text/markdown" \
  -d "# 标题\n\n内容"
```

## 与 Kimi CLI 集成

配置完成后，更新 `AGENTS.md` 让 Kimi 知道如何使用 Obsidian CLI：

```markdown
## Obsidian CLI 工具

当需要操作 Obsidian 笔记时，优先使用以下命令：

1. **搜索笔记**: `obsidian search "关键词"`
2. **读取笔记**: `obsidian print "笔记名"` 或 REST API
3. **创建笔记**: `obsidian create "路径.md" --content "内容"`
4. **追加到日记**: `obsidian append "内容"`

这样可以避免直接读取大量文件，节省 token。
```

## 故障排查

### 官方 CLI 无法连接
- 确保 Obsidian 应用正在运行
- 检查 Settings → General → Advanced → Command line interface 是否开启
- 重启 Obsidian 应用

### REST API 无法访问
- 确保插件已正确安装和启用
- 检查端口 27124 是否被占用: `lsof -i :27124`
- 重启 Obsidian 应用

## 参考链接

- [Obsidian CLI 官方文档](https://help.obsidian.md/Advanced+topics/Command+line+interface)
- [Obsidian CLI REST 插件](https://github.com/dsebastien/obsidian-cli-rest)
