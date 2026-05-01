# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

这是一份给 **OpenAI Codex** 用的科研向 skill 索引。

优先放官方 skill、明确写过支持 Codex 的仓库，以及 Codex 基本可以直接读取的开放 Agent Skills。

每个 skill 只列一次，放在它最常用的场景下面。真正安装或长期使用前，还是先看一眼上游的 `SKILL.md`；这个仓库负责指路，不替代原仓库。

---

## 目录

- [什么是 Codex Skills？](#什么是-codex-skills)
- [收录规则](#收录规则)
- [如何使用这份清单](#如何使用这份清单)
- [Core Picks](#core-picks)
- [Skills 列表](#skills-列表)
- [安装与使用说明](#安装与使用说明)
- [License](#license)
- [参考链接](#参考链接)

---

## 什么是 Codex Skills？

Codex skill 是按文件夹组织的任务说明，用来让 Codex 在某类任务上表现得更稳定。一个典型 skill 包含 `SKILL.md`，也可以带脚本、模板和参考资料。

Codex 会先看到 skill 的名称、简介和路径；只有当任务匹配时，才会读取完整的 `SKILL.md`。这能节省上下文，但也意味着 skill 太多时会挤占提示词空间。OpenAI 官方文档说明，初始 skill 列表会有上下文预算限制，skill 很多时描述会被缩短，极大规模时部分 skill 可能不会出现在初始列表里。

---

## 收录规则

这份清单只保留满足以下条件之一的 skill：

- 官方 OpenAI Codex skills
- 上游仓库明确写明支持 Codex，或明确说明与 Codex 互通
- 基于开放 Agent Skills 格式，且能被 Codex 直接读取或低成本适配

这份清单会主动排除：

- 只服务于其他平台的 skills
- 上游链接失效、目录迁移后找不到明确替代路径的条目
- 与已有条目高度重复、但对科研工作流没有明显新增价值的条目
- Codex 兼容性说不清楚的仓库

---

## 如何使用这份清单

把这个仓库当成科研工作流索引，而不是统一市场。建议先看下面的 Core Picks，再进入具体分类。

按任务类型粗扫：

- 研究编排、项目推进和模型选择：第 1 类。
- 上下文工程、agent 设计和结构化输出：第 2 类。
- 论文写作和正式学术文档：第 3 类。
- 文献阅读、转写和证据整理：第 4 类。
- demo、图表、报告和展示材料：第 5 类。
- 数据、检索、实验追踪和观测：第 6 类。
- 微调、评测、推理服务和 kernel 优化：第 7 类。
- mechanistic interpretability 和模型分析：第 8 类。
- 研究产物、过程记录和可复现性审查：第 9 类。

---

## Core Picks

如果只想快速装一小组，先看这些。它们覆盖面广、来源清楚，也比较不容易造成 skill 列表膨胀。

| Skill | 简介 | 地址 |
|------|------|------|
| `autoresearch` | 编排文献调研、实验迭代、结果综合和论文写作流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `notion-research-documentation` | 在 Notion 中检索资料、整理证据，并生成带引用的简报和报告。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `openai-docs` | 核对最新 OpenAI 产品和 API 文档，并给出有来源依据的建议。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) |
| `huggingface-best` | 基于 Hugging Face 官方 benchmark leaderboard 和元数据筛选、比较候选模型。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-best) |
| `pdf` | 读取、生成并检查 PDF，适合关注版式和渲染的文档工作。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `huggingface-papers` | 查询 Hugging Face 论文页和结构化论文元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `academic-plotting` | 生成论文级图表、消融图和架构图。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `jupyter-notebook` | 创建结构清晰、可复现的 Jupyter Notebook。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `huggingface-datasets` | 通过 Dataset Viewer API 浏览元数据、行数据、搜索、过滤、parquet 链接和统计信息。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-local-models` | 选择 GGUF 模型、量化档位和 llama.cpp 命令，支持本地推理。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-local-models) |
| `huggingface-llm-trainer` | 在 Hugging Face Jobs 上用 TRL 训练或微调语言模型，覆盖 SFT、DPO、GRPO 和 reward model。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `lm-evaluation-harness` | 运行 MMLU、HumanEval、GSM8K、TruthfulQA 等标准 LLM benchmark。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `vllm` | 以高吞吐方式部署大模型，并提供 OpenAI 兼容接口。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `transformer-lens` | 用 HookPoints、activation cache 和 causal tracing 研究 transformer 内部机制。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `ara-compiler` | 把论文、代码仓库、实验日志和笔记编译成带 claims、evidence 和 provenance 的 Agent-Native Research Artifact。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/compiler) |

---

## Skills 列表

### 1. 规划与工作流

| Skill | 简介 | 地址 |
|------|------|------|
| `project-development` | 判断任务是否适合 LLM，并设计研究型 agent 架构。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | 在 Notion 中检索资料、整理证据，并生成带引用的简报和报告。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `notion-knowledge-capture` | 把对话、笔记和决策沉淀为结构化 Notion 页面。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture) |
| `notion-meeting-intelligence` | 结合已有上下文准备会议议程、预读材料和决策文档。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-meeting-intelligence) |
| `autoresearch` | 编排文献调研、实验迭代、结果综合和论文写作流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `brainstorming-research-ideas` | 用结构化框架帮助发现高价值研究方向。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | 使用创造性思维框架生成更有新意的研究想法。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `openai-docs` | 核对最新 OpenAI 产品和 API 文档，并给出有来源依据的建议。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) |
| `huggingface-best` | 基于 Hugging Face 官方 benchmark leaderboard 和元数据筛选、比较候选模型。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-best) |

### 2. 上下文与 Agent 设计

| Skill | 简介 | 地址 |
|------|------|------|
| `context-fundamentals` | 解释 agent 系统里的上下文机制。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | 诊断 lost-in-the-middle 等上下文退化问题。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | 在保留关键状态的前提下压缩长会话。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `context-optimization` | 通过缓存、masking、compaction 和 partitioning 提升有效上下文容量。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) |
| `filesystem-context` | 把文件系统作为上下文溢出层，用于草稿、共享记忆和按需加载。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/filesystem-context) |
| `latent-briefing` | 研究用 KV cache 式 latent handoff 降低 orchestrator-worker 系统的 token 成本。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/latent-briefing) |
| `evaluation` | 为 agent 系统构建 rubric、回归检测和质量门禁。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation) |
| `advanced-evaluation` | 覆盖 LLM-as-a-judge 与偏差控制评测。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |
| `multi-agent-patterns` | 设计 supervisor、swarm 和层级式多 agent 系统。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) |
| `memory-systems` | 设计跨会话持久记忆，并评估长期检索质量。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) |
| `tool-design` | 设计更适合 agent 使用的工具和 MCP 接口，减少歧义。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design) |
| `dspy` | 用声明式提示编程和优化器构建结构化 agent 工作流。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `guidance` | 用正则和语法约束生成，适合结构化输出和多步提示流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/guidance) |
| `instructor` | 用 Pydantic 校验结构化输出，适合信息抽取、标注和自动化。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | 用语法和有限状态机约束生成结构化输出。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |

### 3. 写作与科研表达

| Skill | 简介 | 地址 |
|------|------|------|
| `doc` | 创建和检查 DOCX 文档，并关注渲染结果。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `pdf` | 读取、生成并检查 PDF，适合关注版式和渲染的文档工作。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `huggingface-paper-publisher` | 在 Hugging Face Hub 上发布论文，并管理论文元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | 面向发表场景撰写 ML、AI 和系统论文。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/ml-paper-writing) |
| `systems-paper-writing` | 为 OSDI、SOSP、ASPLOS、NSDI、EuroSys 等系统论文提供段落级结构蓝图。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/systems-paper-writing) |

### 4. 文献阅读与证据综合

| Skill | 简介 | 地址 |
|------|------|------|
| `transcribe` | 转写访谈、会议或录音讲座，并可选做说话人区分。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `whisper` | 用 Whisper 做多语种语音识别与翻译，适合访谈、讲座、播客和音频语料。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/whisper) |
| `huggingface-papers` | 查询 Hugging Face 论文页和结构化论文元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | 搭建研究语料的文档接入与检索管线。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | 为论文库提供高性能向量检索。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | 生成用于文献检索、聚类和召回的语义向量。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. 科研可视化与展示

| Skill | 简介 | 地址 |
|------|------|------|
| `huggingface-gradio` | 用 Python 构建 Gradio Web UI 和交互式研究 demo。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | 用 Hugging Face Trackio 跟踪训练指标、告警和可视化面板。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `academic-plotting` | 生成论文级图表、消融图和架构图。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `presenting-conference-talks` | 把论文整理成 Beamer 或 PPTX 报告，并附 speaker notes 和讲稿。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/presenting-conference-talks) |
| `speech` | 通过 OpenAI Audio API 生成旁白、无障碍朗读和配音音频。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/speech) |
| `imagegen` | 生成或编辑位图视觉素材，适合论文插图、信息图、mockup 和 demo 资产。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/imagegen) |
| `transformers-js` | 在浏览器或 Node.js 中运行 Hugging Face 模型，适合网页 demo 和交互式研究产物。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/transformers-js) |
| `stable-diffusion` | 为多模态研究生成插图、概念图和展示素材。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. 数据、检索与实验追踪

| Skill | 简介 | 地址 |
|------|------|------|
| `jupyter-notebook` | 创建结构清晰、可复现的 Jupyter Notebook。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `hf-cli` | 用 `hf` CLI 管理 Hugging Face 认证、仓库、论文、数据集、bucket、jobs 和 endpoints。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hf-cli) |
| `huggingface-datasets` | 通过 Dataset Viewer API 浏览元数据、行数据、搜索、过滤、parquet 链接和统计信息。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | 把评测结果写入模型卡，并管理 HF Hub 上的自定义评测。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-tool-builder` | 围绕 Hugging Face API 构建可复用脚本，用于元数据采集和自动化。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-tool-builder) |
| `huggingface-local-models` | 选择 GGUF 模型、量化档位和 llama.cpp 命令，支持本地推理。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-local-models) |
| `ray-data` | 把批量推理、预处理和多模态 ETL 从单机扩展到集群。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/ray-data) |
| `nemo-curator` | 通过去重、质量过滤、PII 清洗和多模态清理构建训练语料。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/nemo-curator) |
| `weights-and-biases` | 跟踪实验、超参搜索、产物和模型注册表。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | 处理实验跟踪、模型注册、部署和 autologging 流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `tensorboard` | 可视化标量、嵌入、性能 profile 和训练诊断信息。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `langsmith` | 给 LLM 研究工作流增加 tracing、评估和监控。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | 提供开源 tracing、评测和实验分析能力。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |

### 7. 训练、评测与部署

这一类原本最容易膨胀，所以这里只放和科研训练、评测或部署强相关的代表性条目。

| Skill | 简介 | 地址 |
|------|------|------|
| `huggingface-llm-trainer` | 在 Hugging Face Jobs 上用 TRL 训练或微调语言模型，覆盖 SFT、DPO、GRPO 和 reward model。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | 在本地或 Hugging Face Jobs 上用 Transformers Trainer 训练检测和分类模型。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `axolotl` | 使用 YAML-first 工作流微调模型，覆盖 LoRA、QLoRA、DPO 和多模态训练。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/axolotl) |
| `llama-factory` | 提供 WebUI 和 CLI 的低代码微调流程，支持语言与多模态模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/llama-factory) |
| `unsloth` | 以更低显存和更高速度进行 LoRA/QLoRA 微调，适合本地实验。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/unsloth) |
| `peft` | 覆盖 LoRA、QLoRA、DoRA 等参数高效微调方法。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `trl-fine-tuning` | 用 TRL 完成 SFT、DPO、PPO、GRPO 和 reward model 等后训练流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/trl-fine-tuning) |
| `grpo-rl-training` | 面向推理、可验证任务和自定义奖励函数的 GRPO 后训练。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/grpo-rl-training) |
| `lm-evaluation-harness` | 运行 MMLU、HumanEval、GSM8K、TruthfulQA 等标准 LLM benchmark。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | 用 HumanEval、MBPP、MultiPL-E 和 pass@k 流程评测代码模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `nemo-evaluator` | 通过多后端流程做可复现的 LLM/VLM benchmark。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/nemo-evaluator) |
| `vllm` | 以高吞吐方式部署大模型，并提供 OpenAI 兼容接口。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `sglang` | 用结构化生成和前缀缓存服务 LLM/VLM，适合 JSON 和 tool-calling。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/sglang) |
| `llama-cpp` | 在 CPU、Apple Silicon 和非 CUDA 硬件上运行量化大模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/llama-cpp) |
| `cuda-kernels` | 指导为 Hugging Face diffusers 和 transformers 编写、评测优化 CUDA kernel。 | [huggingface/kernels](https://github.com/huggingface/kernels/tree/main/kernel-builder/skills/cuda-kernels) |

### 8. 可解释性与模型分析

| Skill | 简介 | 地址 |
|------|------|------|
| `transformer-lens` | 用 HookPoints、activation cache 和 causal tracing 研究 transformer 内部机制。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `saelens` | 训练和分析 sparse autoencoders，用于单义特征发现和 superposition 研究。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/saelens) |
| `nnsight` | 在本地或 NDIF 远程环境中做可解释性实验，适合超大 PyTorch 模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/nnsight) |
| `pyvene` | 在 PyTorch 模型上做因果干预、activation patching 和 interchange intervention training。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/pyvene) |

### 9. 研究产物与可复现性

| Skill | 简介 | 地址 |
|------|------|------|
| `ara-compiler` | 把论文、代码仓库、实验日志和笔记编译成带 claims、evidence 和 provenance 的 Agent-Native Research Artifact。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/compiler) |
| `ara-research-manager` | 在会话结束时把研究决策、实验、失败路径和来源记录进 ARA 目录。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/research-manager) |
| `ara-rigor-reviewer` | 从证据相关性、可证伪性、范围、论证连贯性和方法严谨性审查 ARA。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/rigor-reviewer) |

---

## 安装与使用说明

这个仓库本身是清单，不是包管理器。按照当前 Codex 官方文档，skill 是可复用工作流的 authoring format；如果要把 skill 分发给更多人，推荐用 plugin 来打包。

### 在 Codex 中安装 skill

当前 Codex 官方文档给出的标准 skill 目录包括：

- 仓库级：`.agents/skills/<skill-name>/`
- 用户级：`~/.agents/skills/<skill-name>/`
- 管理员级：`/etc/codex/skills/<skill-name>/`

示例 1：安装一个 `openai/skills` 官方 curated skill

```bash
$skill-installer pdf
```

示例 2：手动安装一个 Hugging Face skill

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/huggingface/skills.git
cp -R skills/skills/huggingface-papers ~/.agents/skills/
```

示例 3：安装 Hugging Face Kernels 的 Codex skill

```bash
kernels skills add --codex --global
```

示例 4：使用 Orchestra Research 的上游 installer

```bash
npx @orchestra-research/ai-research-skills
```

### 在 Codex 中使用 skill

只要 skill 文件夹被放进有效的 Codex skill 路径里，就可以在提示词里自然调用。

示例：

- `Use autoresearch to set up an experiment loop for this idea.`
- `Use huggingface-best to compare current open models for this benchmark.`
- `Use academic-plotting to turn these ablation results into camera-ready figures.`
- `Use huggingface-local-models to choose a GGUF model for this laptop.`
- `Use ara-compiler to turn this paper and repo into a research artifact.`

### 推荐使用方式

1. 先装少量高频 skill，再按项目需要增加。
2. 每次先拿一个 skill 解决一个明确瓶颈。
3. 真正依赖输出前，先读一遍上游仓库的 `SKILL.md`。
4. 如果上游仓库自带 installer、plugin manifest 或 fallback `AGENTS.md`，先看上游安装文档，再决定是否混用安装方式。
5. 科研场景里，引用、结论、公式、数据处理和 benchmark 设置都建议人工复核。
6. 如果 skill 会接触远程服务或外部数据集，先确认鉴权、配额、隐私和许可证边界。

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
- [Hugging Face Kernels skills add](https://huggingface.co/docs/kernels/cli-skills)
- [huggingface/kernels](https://github.com/huggingface/kernels)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Agent Skills Open Standard](https://agentskills.io)
