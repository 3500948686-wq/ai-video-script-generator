# 🎬 AI 视频脚本自动生成工具

> 输入一个主题，3 秒内生成结构化的短视频脚本 —— 基于 Python + 大模型 API 的自动化创作工具。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

## 📌 项目简介

本项目是一个**轻量级、可演示的 AI 辅助创作原型工具**，旨在验证大语言模型在内容生产流程中的落地可行性。

通过预先设计的 **System Prompt 约束**，工具能够将任意主题转化为包含 **钩子-干货-引导** 三段式结构的短视频脚本，并自动提取素材关键词、保存为 Markdown 文档，实现**从灵感到初稿的自动化串联**。

该项目体现了以下能力：
- ✅ 大模型 API 集成与 Prompt Engineering
- ✅ 自动化工作流设计（主题输入 → 生成 → 结构化输出）
- ✅ Vibe Coding 实践（AI 辅助编码 + 人工调试优化）
- ✅ 工程化意识（密钥管理、异常降级、文档沉淀）

---

## 🚀 功能亮点

| 模块 | 说明 |
|:---|:---|
| **智能脚本生成** | 调用 Kimi 大模型 API，根据结构化 Prompt 生成包含标题、关键词、三段式正文的完整脚本。 |
| **自动化流程串联** | 输入主题后自动完成生成、关键词提取、时间戳添加、Markdown 文件保存的全流程。 |
| **优雅降级机制** | 当 API 不可用时，自动切换为本地预设模板，保证演示流程不中断。 |
| **密钥安全隔离** | 通过 `config.py` 管理敏感信息，配合 `.gitignore` 确保 API Key 不会泄露到公开仓库。 |

---

## 📸 运行示例

在终端输入主题后，工具自动生成结构化的 Markdown 脚本文件：

![运行截图](screenshot.png)

*（上图展示了从输入主题到生成脚本文件的完整终端交互过程）*

生成的脚本示例预览：

```markdown
## 🎯 视频标题：面试中如何展示项目经验 | 3步让面试官追着你问

### 🔑 核心关键词
`STAR法则` `数据量化` `埋钩子技巧` `Vibe Coding`

### 0-5秒 钩子开头
> 面试官让你“介绍一下这个项目”，千万别从盘古开天辟地开始讲...

### 6-30秒 干货核心
> 第一步：用STAR原则重构经历。第二步：把“效果很好”改成“效率提升40%”...

### 31-45秒 结尾引导
> 这套方法论来自我实际项目的复盘。想看完整 Prompt 模板？评论区见...
```

---

## 🛠️ 技术栈

- **语言**：Python 3.8+
- **大模型接口**：Moonshot AI (Kimi) API
- **依赖库**：`requests` (HTTP 请求)
- **开发范式**：Vibe Coding (AI 辅助生成核心框架 + 人工优化 Prompt 与流程逻辑)

---

## ⚙️ 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/ai-video-script-generator.git
cd ai-video-script-generator
```

### 2. 安装依赖

```bash
pip install requests
```

### 3. 配置 API Key

```bash
# 复制配置模板
cp config.example.py config.py

# 用文本编辑器打开 config.py，填入你的 Kimi API Key
# API_KEY = "sk-你的真实密钥"
```

> 📌 没有 Kimi API Key？可以去 [Moonshot AI 开放平台](https://platform.moonshot.cn/) 免费注册获取。

### 4. 运行工具

```bash
python video_script_generator.py
```

根据提示输入视频主题（或直接修改代码中的默认主题），即可在目录下获得一个以 `.md` 结尾的脚本文件。

---

## 📁 项目结构

```
.
├── video_script_generator.py   # 主程序入口
├── config.example.py           # 配置文件模板（可公开）
├── config.py                   # 本地配置文件（已被 .gitignore 忽略）
├── .gitignore                  # Git 忽略规则
├── README.md                   # 项目说明文档
└── screenshot.png              # 运行效果截图
```

---

## 🔭 后续优化方向

- [ ] 接入剪映/必剪 API，实现脚本到字幕的自动导入
- [ ] 引入向量检索，根据关键词推荐免版权素材
- [ ] 使用 LangChain 封装多轮对话式脚本优化功能
- [ ] 提供 Web 界面（Gradio/Streamlit），降低使用门槛

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源，欢迎 Star ⭐ 和 PR。

---

## 👤 作者

- **GitHub**: [@ffffflash](https://github.com/ffffflash)
- **项目背景**: 源于个人对“AI + 内容创作”效率工具的探索，验证大模型在结构化生成任务中的实用性。

---

*如果这个项目对你有帮助，请给一个 ⭐ Star 支持一下！*
```

现在刷新 GitHub 页面，你会看到一个非常专业的项目首页，发给 HR 绝对加分。
