# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向科研工作流的 **OpenAI Codex** skill 清单。

这份清单会尽量收得保守一些。只有满足以下条件之一的条目，才会被放进来：

- 官方 OpenAI Codex skill
- 上游仓库明确写过支持 Codex
- 上游仓库采用了 Codex 可读取的开放 Agent Skills 格式

表格里的 skill 名称会尽量跟随上游 `SKILL.md` 的名字或目录 slug，这样安装路径和提示词里的调用方式更容易和原仓库对上。

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

Codex skill 本质上是一组按文件夹组织的任务说明，用来让 Codex 在某类任务上表现得更稳定。

一个典型的 skill 通常包括：

- 一个 `SKILL.md`，说明触发条件和工作流程
- 可选的脚本、模板和参考资料
- 一套能被 Codex 从标准目录里发现的文件结构

实际使用时，一个好的 skill 更像一份可复用的工作手册。任务匹配时，Codex 会读取它，再把这些说明和当前仓库上下文结合起来执行。

---

## 收录规则

这份清单只保留满足以下条件之一的 skill：

- 官方 OpenAI Codex skills
- 上游仓库明确写明支持 Codex
- 基于开放 Agent Skills 格式，且能被 Codex 直接读取或低成本适配

这份清单会主动排除：

- 只服务于其他平台的 skills，例如 Claude Code 专属技能
- 强依赖平台内建能力、难以迁移成可复用 Codex skill 的文档工作流
- Codex 兼容性说不清楚的仓库

---

## 如何使用这份清单

把这个仓库当成一个科研工作流索引来用会更合适，而不是把它当成统一市场。表格负责帮你缩小范围，真正的细节还是要回到上游 `SKILL.md` 去看。

如果你第一次看这份清单，按任务类型扫一遍通常就够用了：

- 想找流程设计、任务拆解和上下文管理，先看第 1 类和第 2 类。
- 想做论文写作、答辩汇报和正式交付物，先看第 3 类和第 5 类。
- 想做文献阅读和证据整理，先看第 4 类。
- 想补实验、评测、微调和复现流程，先看第 6 类。

---

## Skills 列表

### 1. 规划与工作流

| Skill | 简介 | 地址 |
|------|------|------|
| `project-development` | 帮你判断任务是否适合 LLM，并设计研究型 agent 架构。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | 在 Notion 中做资料检索、整理，并生成带引用的简报和报告。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `brainstorming-research-ideas` | 用结构化框架帮助发现高价值研究方向。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | 使用创造性思维框架生成更有新意的研究想法。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `dspy` | 用声明式提示编程和优化器构建结构化的研究 agent 工作流。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `instructor` | 用 Pydantic 校验结构化输出，适合信息抽取、标注和更可靠的研究自动化流程。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | 用语法和有限状态机约束生成，适合结构化输出和合成数据流程。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |

### 2. 深度思考与研究构思

| Skill | 简介 | 地址 |
|------|------|------|
| `context-fundamentals` | 解释 agent 系统里的上下文机制。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | 诊断 lost-in-the-middle 等上下文退化问题。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | 在保留关键状态的前提下压缩长会话。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `advanced-evaluation` | 覆盖 LLM-as-a-judge 与偏差控制评测。 | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. 写作与科研表达

| Skill | 简介 | 地址 |
|------|------|------|
| `doc` | 面向 Codex 的 DOCX 工作流，强调渲染检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | 适合研究简报和结构化证据摘要。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | 读取、生成并检查 PDF，适合需要关注版式和渲染效果的文档工作。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `slides` | 创建和修改可编辑的 `.pptx` 幻灯片，并做版式与溢出检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `huggingface-paper-publisher` | 在 Hugging Face Hub 上发布论文、关联模型或数据集，并管理论文元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | 面向顶会的 ML/AI/Systems 论文写作 skill。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing) |

### 4. 文献阅读与证据综合

| Skill | 简介 | 地址 |
|------|------|------|
| `notion-research-documentation` | 把多来源资料整理为带引用的文献笔记。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | 适合处理论文包、批注文稿和对版式敏感的阅读任务。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `transcribe` | 转写访谈、会议或录音讲座，并可选做说话人区分。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `huggingface-papers` | 查询 Hugging Face 论文页及结构化论文元数据，适合做摘要和论文分析。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | 搭建研究语料的文档接入与检索管线。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | 为论文库提供高性能向量检索。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | 生成用于文献检索、聚类和召回的语义向量。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. 科研可视化与展示美化

| Skill | 简介 | 地址 |
|------|------|------|
| `gradio` | 用 Python 搭建 Gradio demo 和交互式研究界面。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | 用 Hugging Face Trackio 跟踪训练指标、告警和可视化面板。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `slides` | 制作可编辑的演讲稿、海报和结果汇报幻灯片。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `langsmith` | 给 LLM 研究工作流增加 tracing、评估和监控。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | 开源的 observability 方案，适合 tracing、评测和实验分析。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `tensorboard` | 可视化标量、嵌入、性能 profile 和训练诊断信息。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `stable-diffusion` | 为多模态研究生成插图、概念图和展示素材。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. 数据与实验

现在的科研流程离不开可复现的数据处理、评测和实验跟踪，所以这类 skill 也集中放在一起。

| Skill | 简介 | 地址 |
|------|------|------|
| `jupyter-notebook` | 创建结构清晰、可复现的 Jupyter Notebook，适合实验和教程。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `spreadsheet` | 创建、修改并分析电子表格，兼顾公式处理和可视化检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) |
| `huggingface-datasets` | 通过 Dataset Viewer API 浏览 Hugging Face 数据集，覆盖 split、搜索、过滤和 parquet 导出。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | 用 `inspect-ai` 或 `lighteval` 在本地评测 Hugging Face Hub 模型，并帮助选择合适后端。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-llm-trainer` | 使用 Hugging Face Jobs 和 TRL 训练或微调语言模型，覆盖 SFT、DPO、GRPO 和 reward model。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | 在 Hugging Face Jobs 上训练或微调视觉模型，覆盖检测、分类和分割任务。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `huggingface-jobs` | 在 Hugging Face 基础设施上运行数据处理、推理、实验或训练任务。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-jobs) |
| `peft` | 覆盖 LoRA、QLoRA、DoRA 等参数高效微调方法。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `weights-and-biases` | 跟踪实验、超参搜索、产物管理和模型注册表。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | 处理实验跟踪、模型注册、部署和 autologging 流程。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `lm-evaluation-harness` | 运行 MMLU、HumanEval、GSM8K、TruthfulQA 等标准 LLM benchmark。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | 用 HumanEval、MBPP、MultiPL-E 和 `pass@k` 流程评测代码模型。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `vllm` | 以高吞吐方式部署大模型，并提供 OpenAI 兼容接口。 | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |

---

## 安装与使用说明

这个仓库本身是清单，不是统一市场。大多数情况下，你还是需要从上游仓库安装 skill，然后放进 Codex 的 skill 目录。

### 在 Codex 中安装 skill

按照当前 Codex 官方文档，常见的 skill 目录位置是：

- 仓库级：`.agents/skills/<skill-name>/`
- 用户级：`~/.agents/skills/<skill-name>/`

如果是官方 `openai/skills`，最省事的方式通常是直接用 `$skill-installer`。

示例 1：安装一个官方 curated skill

```bash
$skill-installer pdf
```

示例 2：手动安装第三方 skill

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/huggingface/skills.git
cp -R skills/skills/huggingface-papers ~/.agents/skills/
```

示例 3：安装一个 AI-Research-SKILLs 里的科研 skill

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/03-fine-tuning/peft ~/.agents/skills/
```

有些旧文章或旧仓库还会提到 `.codex/skills`，但当前 OpenAI 文档已经把 `.agents/skills` 当成标准位置来说明。

### 在 Codex 中使用 skill

只要 skill 文件夹被放进有效的 Codex skill 路径里，就可以在提示词里自然调用。

示例：

- `Use the ml-paper-writing skill to turn this repo into a NeurIPS-style draft.`
- `Use dspy to prototype an optimizer-backed prompt pipeline for this ablation.`
- `Use huggingface-community-evals to smoke-test this checkpoint on MMLU and GSM8K.`
- `Use pdf to review these camera-ready pages for layout issues.`
- `Use gradio to build a demo for this paper artifact.`

### 推荐使用方式

1. 每次先拿一个 skill 解决一个明确瓶颈。
2. 先从小任务开始，不要一上来就铺整条长链路。
3. 真正依赖输出前，先读一遍上游仓库的 `SKILL.md`。
4. 科研场景里，引用、结论、公式、数据处理和 benchmark 设置都建议人工复核。
5. 如果 skill 会接触远程服务或外部数据集，先确认鉴权、配额、隐私和许可证边界。

---

## License

本仓库内容以 [MIT License](LICENSE) 发布。

本清单中链接到的第三方 skill 仍然遵循各自原始仓库的 License。安装、复制或二次分发前，请先检查原始仓库声明。

如果你发现失效链接、命名变化，或者有明显更合适的条目，开个 issue 或 PR 简单说明就行。

---

## 参考链接

- [Agent Skills – Codex](https://developers.openai.com/codex/skills)
- [openai/skills](https://github.com/openai/skills)
- [huggingface/skills](https://github.com/huggingface/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Agent Skills Open Standard](https://agentskills.io)
