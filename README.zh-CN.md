# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向科研工作流的 **OpenAI Codex** skill 清单。

这份清单会尽量收得保守一些。只有满足以下条件之一的条目，才会被放进来：

- 官方 OpenAI Codex skill
- 上游仓库明确写过支持 Codex 或与 Codex 互通
- 上游仓库采用了 Codex 可读取的开放 Agent Skills 格式

表格里的 skill 名称会尽量贴近上游 skill 名或目录 slug，这样安装路径和提示词里的调用方式更容易和原仓库对上。

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
- 上游仓库明确写明支持 Codex，或明确说明与 Codex 互通
- 基于开放 Agent Skills 格式，且能被 Codex 直接读取或低成本适配

这份清单会主动排除：

- 只服务于其他平台的 skills
- 强依赖平台内建能力、难以迁移成可复用 Codex skill 的工作流
- Codex 兼容性说不清楚的仓库

---

## 如何使用这份清单

把这个仓库当成一个科研工作流索引来用会更合适，而不是把它当成统一市场。表格负责帮你缩小范围，真正的细节还是要回到上游 `SKILL.md` 去看。

如果你第一次看这份清单，按任务类型扫一遍通常就够用了：

- 想看研究编排、项目推进和上下文管理，先看第 1 类和第 2 类。
- 想做论文写作和正式学术文档，先看第 3 类。
- 想做文献阅读和证据整理，先看第 4 类。
- 想做 demo、图表、报告和展示材料，先看第 5 类。
- 想补实验、评测、微调和复现流程，先看第 6 类。
- 想做 mechanistic interpretability 和模型分析，先看第 7 类。

---

## Skills 列表

### 1. 规划与工作流

| Skill | 简介 | 地址 |
|------|------|------|
| `project-development` | 帮助判断任务是否适合 LLM，并设计研究型 agent 架构。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | 在 Notion 中做资料检索、整理，并生成带引用的简报和报告。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `notion-knowledge-capture` | 把对话、笔记和决策沉淀为结构化 Notion 页面，适合知识库、FAQ 和决策记录。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture) |
| `notion-meeting-intelligence` | 结合 Notion 上下文和 Codex 调研，准备会议议程、预读材料和决策文档。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-meeting-intelligence) |
| `autoresearch` | 编排端到端的自主 AI 研究流程，把文献调研、实验迭代、结果综合和论文写作串起来。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `brainstorming-research-ideas` | 用结构化框架帮助发现高价值研究方向。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | 使用创造性思维框架生成更有新意的研究想法。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `dspy` | 用声明式提示编程和优化器构建结构化的研究 agent 工作流。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `guidance` | 用正则和语法约束生成，适合结构化输出、JSON/XML/code 生成和多步提示流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/guidance) |
| `instructor` | 用 Pydantic 校验结构化输出，适合信息抽取、标注和更可靠的研究自动化流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | 用语法和有限状态机约束生成，适合结构化输出和合成数据流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |
| `multi-agent-patterns` | 设计 supervisor、swarm 和层级式多 agent 系统，强调上下文隔离和显式协作。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) |
| `memory-systems` | 设计跨会话持久记忆架构，比较记忆框架并优化长期检索质量。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) |
| `tool-design` | 设计更适合 agent 使用的工具和 MCP 接口，减少歧义并提升选 tool 准确率。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design) |

### 2. 深度思考与研究构思

| Skill | 简介 | 地址 |
|------|------|------|
| `context-fundamentals` | 解释 agent 系统里的上下文机制。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | 诊断 lost-in-the-middle 等上下文退化问题。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | 在保留关键状态的前提下压缩长会话。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `context-optimization` | 通过缓存、masking、compaction 和 partitioning 提升有效上下文容量并降低成本。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) |
| `evaluation` | 为 agent 系统构建评测框架，包括 rubric、回归检测和面向结果的质量门禁。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation) |
| `advanced-evaluation` | 覆盖 LLM-as-a-judge 与偏差控制评测。 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. 写作与科研表达

| Skill | 简介 | 地址 |
|------|------|------|
| `doc` | 面向 Codex 的 DOCX 工作流，强调渲染检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | 适合研究简报和结构化证据摘要。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | 读取、生成并检查 PDF，适合需要关注版式和渲染效果的文档工作。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `slides` | 创建和修改可编辑的 `.pptx` 幻灯片，并做版式与溢出检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `huggingface-paper-publisher` | 在 Hugging Face Hub 上发布论文、关联模型或数据集，并管理论文元数据。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | 面向顶会的 ML/AI/Systems 论文写作 skill。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/ml-paper-writing) |
| `systems-paper-writing` | 为 OSDI、SOSP、ASPLOS、NSDI、EuroSys 等系统论文提供段落级结构蓝图和投稿指导。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/systems-paper-writing) |

### 4. 文献阅读与证据综合

| Skill | 简介 | 地址 |
|------|------|------|
| `notion-research-documentation` | 把多来源资料整理为带引用的文献笔记。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | 适合处理论文包、批注文稿和对版式敏感的阅读任务。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `transcribe` | 转写访谈、会议或录音讲座，并可选做说话人区分。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `whisper` | 用 Whisper 做多语种语音识别与翻译，适合访谈、讲座、播客和音频语料。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/whisper) |
| `huggingface-papers` | 查询 Hugging Face 论文页及结构化论文元数据，适合做摘要和论文分析。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | 搭建研究语料的文档接入与检索管线。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | 为论文库提供高性能向量检索。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | 生成用于文献检索、聚类和召回的语义向量。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. 科研可视化与展示美化

| Skill | 简介 | 地址 |
|------|------|------|
| `huggingface-gradio` | 用 Python 构建 Gradio Web UI 和交互式研究 demo。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | 用 Hugging Face Trackio 跟踪训练指标、告警和可视化面板。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `slides` | 制作可编辑的演讲稿、海报和结果汇报幻灯片。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `academic-plotting` | 生成适合 ML 论文的高质量图表、消融图和架构图。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `presenting-conference-talks` | 把论文整理成 Beamer/PPTX 报告，附带 speaker notes 和讲稿。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/presenting-conference-talks) |
| `speech` | 通过 OpenAI Audio API 生成旁白、无障碍朗读和配音音频。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/speech) |
| `imagegen` | 生成或编辑位图视觉素材，适合论文插图、信息图、mockup 和 demo 资产。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/imagegen) |
| `transformers-js` | 在浏览器或 Node.js 中直接运行 Hugging Face 模型，适合网页 demo 和交互式研究产物。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/transformers-js) |
| `langsmith` | 给 LLM 研究工作流增加 tracing、评估和监控。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | 开源的 observability 方案，适合 tracing、评测和实验分析。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `tensorboard` | 可视化标量、嵌入、性能 profile 和训练诊断信息。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `stable-diffusion` | 为多模态研究生成插图、概念图和展示素材。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. 数据与实验

现在的科研流程离不开可复现的数据处理、评测、微调和部署，所以这类 skill 集中放在一起。

| Skill | 简介 | 地址 |
|------|------|------|
| `jupyter-notebook` | 创建结构清晰、可复现的 Jupyter Notebook，适合实验和教程。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `spreadsheet` | 创建、修改并分析电子表格，兼顾公式处理和可视化检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) |
| `hf-cli` | 用 `hf` CLI 管理 Hugging Face 的认证、仓库、论文、数据集、bucket、jobs 和 endpoints。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hf-cli) |
| `huggingface-datasets` | 通过 Dataset Viewer API 浏览 Hugging Face 数据集，覆盖 config、行数据、搜索、过滤和 parquet 访问。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | 把评测结果写入模型卡，导入外部评分，并在 HF Hub 上运行自定义评测。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-tool-builder` | 围绕 Hugging Face API 构建可复用脚本，适合元数据采集、自动化和重复研究流程。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-tool-builder) |
| `huggingface-llm-trainer` | 在 Hugging Face Jobs 上用 TRL 训练或微调语言模型，覆盖 SFT、DPO、GRPO、reward model 和 GGUF 导出。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | 在本地或 Hugging Face Jobs 上训练或微调检测和分类模型，基于 Transformers Trainer。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `huggingface-jobs` | 在 Hugging Face 基础设施上运行 Python 工作负载、定时任务以及 CPU/GPU/TPU 实验。 | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-jobs) |
| `axolotl` | 使用 YAML-first 工作流微调 100+ 模型，覆盖 LoRA、QLoRA、DPO 和多模态训练。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/axolotl) |
| `llama-factory` | 提供 WebUI 和 CLI 的低代码微调流程，支持 100+ 语言与多模态模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/llama-factory) |
| `unsloth` | 以更低显存和更高速度进行 LoRA/QLoRA 微调，适合快速本地实验。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/unsloth) |
| `peft` | 覆盖 LoRA、QLoRA、DoRA 等参数高效微调方法。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `trl-fine-tuning` | 用 TRL 完成 SFT、DPO、PPO、GRPO 和 reward model 等后训练流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/trl-fine-tuning) |
| `grpo-rl-training` | 面向推理、可验证任务、结构化输出和自定义奖励函数的 GRPO 后训练。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/grpo-rl-training) |
| `ray-data` | 把批量推理、数据预处理和多模态 ETL 从单机扩展到集群。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/ray-data) |
| `nemo-curator` | 用 GPU 加速去重、质量过滤、PII 清洗和多模态数据整理，构建训练语料。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/nemo-curator) |
| `weights-and-biases` | 跟踪实验、超参搜索、产物管理和模型注册表。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | 处理实验跟踪、模型注册、部署和 autologging 流程。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `lm-evaluation-harness` | 运行 MMLU、HumanEval、GSM8K、TruthfulQA 等标准 LLM benchmark。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | 用 HumanEval、MBPP、MultiPL-E 和 `pass@k` 流程评测代码模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `nemo-evaluator` | 通过容器化、多后端工作流在 100+ benchmark 上做可复现的 LLM/VLM 评测。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/nemo-evaluator) |
| `vllm` | 以高吞吐方式部署大模型，并提供 OpenAI 兼容接口。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `sglang` | 用前缀缓存和结构化生成能力高效服务 LLM/VLM，适合 JSON 和 tool-calling。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/sglang) |
| `llama-cpp` | 在 CPU、Apple Silicon 和非 CUDA 硬件上运行量化大模型，适合本地或边缘研究部署。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/llama-cpp) |

### 7. 可解释性与模型分析

| Skill | 简介 | 地址 |
|------|------|------|
| `transformer-lens` | 用 HookPoints、activation cache 和 causal tracing 研究 transformer 内部机制。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `saelens` | 训练和分析 sparse autoencoders，用于单义特征发现和 superposition 研究。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/saelens) |
| `nnsight` | 在本地或 NDIF 远程环境中做可解释性实验，适合超大 PyTorch 模型。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/nnsight) |
| `pyvene` | 在 PyTorch 模型上做因果干预、activation patching 和 interchange intervention training。 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/pyvene) |

---

## 安装与使用说明

这个仓库本身是清单，不是包管理器。按照当前 Codex 官方文档，skill 生态可以粗分成两类：

- 用于本地 authoring 和日常使用的本地 skill 文件夹
- 用于分发可复用 skill bundle 的 plugins

实际使用里，大多数条目仍然是把上游 skill 文件夹放进 Codex 的标准 skill 目录来使用。与此同时，一些第三方仓库已经开始自带 installer 或 plugin manifest；如果上游有明确安装方式，建议优先按上游文档来装。

### 在 Codex 中安装 skill

当前 Codex 官方文档给出的标准 skill 目录位置是：

- 仓库级：`.agents/skills/<skill-name>/`
- 用户级：`~/.agents/skills/<skill-name>/`

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

示例 3：使用 Orchestra Research 的上游 installer

```bash
npx @orchestra-research/ai-research-skills
```

示例 4：如果你只想要单个 Orchestra skill，也可以手动复制

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/20-ml-paper-writing/academic-plotting ~/.agents/skills/
```

有些旧文章或旧仓库还会提到 `.codex/skills`，但当前 OpenAI 文档已经把 `.agents/skills` 当成标准本地位置来说明。

### 在 Codex 中使用 skill

只要 skill 文件夹被放进有效的 Codex skill 路径里，就可以在提示词里自然调用。

示例：

- `Use autoresearch to set up an experiment loop for this idea.`
- `Use academic-plotting to turn these ablation results into camera-ready figures.`
- `Use hf-cli to inspect the model, dataset, and paper metadata for this checkpoint.`
- `Use transformer-lens to run activation-patching experiments on this model.`
- `Use huggingface-gradio to build a demo for this paper artifact.`

### 推荐使用方式

1. 每次先拿一个 skill 解决一个明确瓶颈。
2. 先从小任务开始，不要一上来就铺整条长链路。
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
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Agent Skills Open Standard](https://agentskills.io)
