# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

一个只收录 **OpenAI Codex 可用 skill** 的科研向清单仓库。

目标很直接：只要出现在这里，要么它来自官方 Codex 生态，要么上游仓库已经明确支持 Codex，或者采用了 Codex 可直接消费的 Agent Skills 开放格式。

---

## 目录

- [什么是 Codex Skills？](#什么是-codex-skills)
- [收录规则](#收录规则)
- [如何使用这份清单](#如何使用这份清单)
- [Skills 列表](#skills-列表)
- [安装与使用说明](#安装与使用说明)
- [License](#license)
- [参考链接](#参考链接)

---

## 什么是 Codex Skills？

Codex skill 本质上是一组按文件夹组织的任务说明，它可以让 Codex 在特定场景下更稳定地完成工作。

一个典型的 skill 往往包含：

- 一个 `SKILL.md`，说明触发条件与工作流
- 可选的脚本、模板和参考资料
- 一套可被 Codex 自动发现的目录结构

实际使用中，一个好的 skill 很像一份可复用的科研工作手册：当任务匹配时，Codex 会加载它、阅读它，并结合当前仓库上下文执行。

---

## 收录规则

这份清单只保留满足以下条件之一的 skill：

- 官方 OpenAI Codex skills
- 上游仓库明确写明支持 Codex
- 基于开放 Agent Skills 格式，且能被 Codex 低成本使用

这份清单会主动移除：

- 其他平台专属 skills（如 Claude Code 专属）
- 依赖平台内建能力、难以作为可复用 Codex skill 使用的文档类工作流
- Codex 兼容性不明确的仓库

---

## 如何使用这份清单

这份清单更像一个面向科研工作流的索引页。它适合帮你先缩小范围，再回到上游 skill 的 `SKILL.md` 看细节，而不是替代原始文档。

如果你是第一次来到这里，可以按任务先粗看一遍：

- 想找研究流程设计、任务拆解和上下文管理，可以先看第 1 类和第 2 类。
- 想做论文写作、文献整理或证据摘要，可以先看第 3 类和第 4 类。
- 想补 demo、观测、数据处理或实验流程，可以先看第 5 类和第 6 类。
- 看到合适的条目后，建议继续打开上游 skill 的 `SKILL.md`，再决定是否安装或纳入自己的工作流。

---

## Skills 列表

### 1. 规划与工作流

| Skill | 简介 | 地址 |
|------|------|------|
| `project-development` | 帮你判断任务是否适合 LLM，如何设计研究型 agent 项目和整体架构。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | 在 Notion 中做资料检索、整理和结构化写作，适合生成带引用的简报、对比文档和研究报告。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `brainstorming-research-ideas` | 用结构化框架帮助研究者发现更可辩护、更有潜力的研究方向。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | 用认知科学中的创造性思维框架，帮助生成更有新意的研究想法。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |

### 2. 深度思考与研究构思

| Skill | 简介 | 地址 |
|------|------|------|
| `context-fundamentals` | 解释 agent 系统里的上下文机制，以及如何设计高信号任务上下文。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | 帮你识别 lost-in-the-middle、分心、污染等上下文退化问题。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | 教你如何压缩长会话或长研究流程，同时尽量不丢失关键状态。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `advanced-evaluation` | 覆盖 LLM-as-a-judge、rubric 设计和评测偏差控制等高级评测方法。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. 写作与科研表达

| Skill | 简介 | 地址 |
|------|------|------|
| `doc` | 更偏 Codex 工作流的 DOCX 处理 skill，适合研究报告和正式文档的版式检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | 适合把研究记录写成简报、比较表和结构化证据摘要。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `hugging-face-paper-publisher` | 发表和管理论文，关联模型/数据集，并生成较专业的 paper 页面。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-paper-publisher) |
| `ml-paper-writing` | 面向 NeurIPS、ICML、ICLR、ACL 等会议的论文写作 skill，覆盖结构、引用核查和成稿流程。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing) |

### 4. 文献阅读与证据综合

| Skill | 简介 | 地址 |
|------|------|------|
| `notion-research-documentation` | 把多来源资料整理为文献综述、证据笔记和带引用的研究摘要。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `llamaindex` | 适合搭建论文库、笔记库和私有研究资料的文档接入与检索管线。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | 适合在大规模论文向量库和笔记向量库上做高性能相似检索。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | 用于生成高质量语义向量，适合做文献检索、聚类和相似度分析。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. 科研可视化与展示美化

| Skill | 简介 | 地址 |
|------|------|------|
| `gradio` | 快速搭建交互式 demo、研究原型和展示页面。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `hugging-face-trackio` | 跟踪并可视化训练过程指标，支持实时 dashboard。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-trackio) |
| `langsmith-observability` | 给 LLM 应用和实验流程增加 tracing、监控和系统化评估。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix-observability` | 开源的 AI observability 方案，适合 tracing、实验对比和实时分析。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `stable-diffusion-image-generation` | 适合生成展示图、视觉概念图、海报元素或多模态展示素材。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. 数据与实验（推荐补充类别）

这一类我建议保留，因为现代科研工作流几乎离不开它。

| Skill | 简介 | 地址 |
|------|------|------|
| `hugging-face-datasets` | 在 Hugging Face Hub 上创建、管理、查询和变换数据集。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-datasets) |
| `hugging-face-evaluation` | 管理 benchmark 结果、模型评测结果和结构化评测元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-evaluation) |
| `hugging-face-model-trainer` | 使用 Hugging Face Jobs 和 TRL 进行大模型训练或微调。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-model-trainer) |
| `hugging-face-jobs` | 在 Hugging Face 基础设施上运行训练、评测或生成任务。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-jobs) |
| `evaluating-llms-harness` | 运行 MMLU、HumanEval、GSM8K、TruthfulQA 等标准学术 benchmark。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `serving-llms-vllm` | 用高吞吐推理方式部署模型，并提供 OpenAI 兼容接口。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |

---

## 安装与使用说明

这个仓库本身是清单，不是统一的技能市场。通常你需要去 skill 的原始仓库安装它，然后放进 Codex 的 skill 目录。

### 在 Codex 中安装 skill

Codex 常见的 skill 目录位置包括：

- 仓库级：`.codex/skills/<skill-name>/`
- 用户级：`~/.codex/skills/<skill-name>/`

示例 1：安装官方 Codex 风格 skill

```bash
mkdir -p ~/.codex/skills
cd /tmp
git clone --depth 1 https://github.com/openai/skills.git
cp -R skills/skills/.curated/notion-research-documentation ~/.codex/skills/
```

示例 2：安装科研 skill

```bash
mkdir -p ~/.codex/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/20-ml-paper-writing ~/.codex/skills/ml-paper-writing
```

### 在 Codex 中使用 skill

只要 skill 文件夹被放进有效的 Codex skill 路径里，就可以在提示词里自然调用。

示例：

- `Use the ml-paper-writing skill to turn this repo into a NeurIPS-style draft.`
- `Use brainstorming-research-ideas to generate three defensible project directions.`
- `Use notion-research-documentation to turn these source notes into a cited literature brief.`
- `Use evaluating-llms-harness to benchmark this checkpoint on MMLU and GSM8K.`
- `Use gradio to build a polished demo for this paper artifact.`

### 推荐使用方式

1. 每次只针对一个明确瓶颈选一个 skill。
2. 先从小任务开始，不要一上来就跑超长链路。
3. 真正依赖输出前，先读一遍上游仓库的 `SKILL.md`。
4. 在科研场景里，引用、结论、公式、数据处理和 benchmark 设置都建议人工复核；涉及版权、隐私、署名或科研诚信的内容，也最好先对照上游仓库和本地流程确认。

---

## License

本仓库内容以 [MIT License](LICENSE) 发布。

本清单中链接到的第三方 skill 仍然遵循各自原始仓库的 License。安装、复制或二次分发前，请先检查原始仓库声明。

如果你发现失效链接、兼容性变化，或有明显更合适的条目，欢迎直接开 issue 或 PR 简单说明。

---

## 参考链接

- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [openai/skills](https://github.com/openai/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [huggingface/skills](https://github.com/huggingface/skills)
- [awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)
- [Agent Skills Open Standard](https://agentskills.io)
