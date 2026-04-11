# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

A curated list of research-oriented skills that currently work with **OpenAI Codex**.

This list stays intentionally conservative. Every entry is kept only when the upstream source is one of the following:

- an official OpenAI Codex skill
- a repository that explicitly documents Codex interoperability
- a repository that follows the open Agent Skills format Codex can read

Skill names below follow the upstream skill name or folder slug as closely as practical, so install paths and prompt mentions stay close to the source repository.

---

## Table of Contents

- [What Are Codex Skills?](#what-are-codex-skills)
- [Inclusion Rules](#inclusion-rules)
- [How To Use This List](#how-to-use-this-list)
- [Skill List](#skill-list)
- [Installation and Usage](#installation-and-usage)
- [License](#license)
- [References](#references)

---

## What Are Codex Skills?

Codex skills are folder-based instruction bundles that help Codex handle specific tasks more reliably.

A typical skill usually includes:

- a `SKILL.md` file with trigger rules and workflow guidance
- optional scripts, templates, and references
- a stable folder structure that Codex can discover from standard skill locations

In practice, a good skill works like a reusable playbook. Codex loads it when the task matches, follows the instructions, and combines that guidance with the local repository context.

---

## Inclusion Rules

This list keeps entries that satisfy at least one of the following:

- official OpenAI Codex skills
- repositories that explicitly document Codex support or interoperability
- repositories built around the open Agent Skills format that Codex can consume with little or no adaptation

This list intentionally excludes:

- skills that are exclusive to other platforms
- workflows that rely on platform-specific built-ins and do not translate cleanly into reusable Codex skills
- repositories whose Codex compatibility is unclear

---

## How To Use This List

Treat this repository as a research-workflow index, not a marketplace. The tables help narrow the search space; the upstream `SKILL.md` remains the source of truth.

If you are new to the list, a task-based pass is usually enough:

- For workflow design, research orchestration, and context management, start with sections 1 and 2.
- For paper drafting and formal scholarly writing, start with section 3.
- For literature review and evidence synthesis, start with section 4.
- For demos, figures, talks, and polished presentation assets, start with section 5.
- For experiments, evaluation, fine-tuning, and reproducibility work, start with section 6.
- For mechanistic interpretability and model analysis, start with section 7.

---

## Skill List

### 1. Planning and Workflow

| Skill | What It Does | Link |
|------|--------------|------|
| `project-development` | Helps scope LLM projects and design practical research-agent architectures. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | Researches across Notion and synthesizes cited briefs and reports. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `notion-knowledge-capture` | Captures conversations, notes, and decisions into structured Notion pages for wiki, FAQ, or decision-log reuse. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture) |
| `notion-meeting-intelligence` | Prepares agendas, pre-reads, and decision docs in Notion using existing context plus Codex research. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-meeting-intelligence) |
| `autoresearch` | Orchestrates end-to-end autonomous AI research projects, routing literature, experiments, synthesis, and paper-writing workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `brainstorming-research-ideas` | Guides structured ideation for high-impact research directions. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | Applies creativity frameworks to generate novel research ideas. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `dspy` | Uses declarative prompt programming and optimizers to build structured research-agent workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `guidance` | Controls generation with regexes and grammars for structured outputs, JSON/XML/code, and multi-step prompting workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/guidance) |
| `instructor` | Produces Pydantic-validated structured outputs for extraction, labeling, and reliable research automation. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | Constrains generation with grammars and finite-state machines for structured outputs and synthetic data workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |
| `multi-agent-patterns` | Designs supervisor, swarm, and hierarchical multi-agent systems with explicit coordination and context isolation. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) |
| `memory-systems` | Designs persistent agent memory architectures, compares frameworks, and evaluates retrieval quality across sessions. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) |
| `tool-design` | Designs agent-facing tools and MCP interfaces with clearer contracts, naming, and reduced selection ambiguity. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design) |

### 2. Deep Thinking and Research Framing

| Skill | What It Does | Link |
|------|--------------|------|
| `context-fundamentals` | Explains how context works in agent systems. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | Diagnoses lost-in-the-middle and other context failure modes. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | Compresses long sessions while preserving critical state. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `context-optimization` | Applies caching, masking, compaction, and partitioning strategies to extend effective context capacity and reduce cost. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) |
| `evaluation` | Builds evaluation frameworks for agent systems with rubric-based scoring, regressions, and outcome-focused quality gates. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation) |
| `advanced-evaluation` | Covers LLM-as-a-judge and bias-aware automated evaluation. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. Writing and Scholarly Communication

| Skill | What It Does | Link |
|------|--------------|------|
| `doc` | Codex-oriented DOCX workflow with rendering checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | Useful for research briefs and structured evidence summaries. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | Reads, creates, and reviews PDFs when layout and rendering matter. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `slides` | Creates and edits `.pptx` slide decks with editable output and layout validation. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `huggingface-paper-publisher` | Publishes papers on Hugging Face Hub, links them to models or datasets, and manages paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | Writes publication-ready ML/AI/Systems papers. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/ml-paper-writing) |
| `systems-paper-writing` | Provides paragraph-level blueprints and venue-specific guidance for OSDI, SOSP, ASPLOS, NSDI, and EuroSys papers. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/systems-paper-writing) |

### 4. Literature Reading and Evidence Synthesis

| Skill | What It Does | Link |
|------|--------------|------|
| `notion-research-documentation` | Turns multi-source findings into cited literature notes. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | Useful for paper packets, annotated drafts, and layout-sensitive reading workflows. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `transcribe` | Transcribes interviews, meetings, or recorded talks with optional speaker diarization. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `whisper` | Runs robust multilingual speech recognition and translation for interviews, lectures, podcasts, and audio corpora. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/whisper) |
| `huggingface-papers` | Looks up Hugging Face paper pages and structured paper metadata for summaries or analysis. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | Builds document ingestion and retrieval pipelines for research corpora. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | Provides high-performance dense retrieval for paper collections. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | Generates embeddings for literature search, clustering, and retrieval. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. Visualization and Presentation

| Skill | What It Does | Link |
|------|--------------|------|
| `huggingface-gradio` | Builds Gradio web UIs and interactive research demos in Python. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | Tracks training metrics, alerts, and dashboards with Hugging Face Trackio. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `slides` | Builds editable slide decks for talks, posters, and result reviews. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `academic-plotting` | Generates publication-quality charts, ablations, and architecture figures for ML papers. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `presenting-conference-talks` | Turns papers into Beamer/PPTX talk decks with speaker notes and talk scripts. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/presenting-conference-talks) |
| `speech` | Generates narration, accessibility reads, and voiceovers via the OpenAI Audio API. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/speech) |
| `imagegen` | Creates or edits bitmap figures, mockups, infographics, and other visual assets for papers or demos. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/imagegen) |
| `transformers-js` | Runs Hugging Face models directly in JavaScript for browser-side demos and interactive research artifacts. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/transformers-js) |
| `langsmith` | Adds tracing, evaluation, and monitoring to LLM research workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | Open-source observability for tracing, evaluation, and experiment analysis. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `tensorboard` | Visualizes scalars, embeddings, profiles, and training diagnostics. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `stable-diffusion` | Generates figures, concept art, and presentation assets for multimodal research. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. Data and Experimentation

Research workflows now depend on reproducible data handling, evaluation, fine-tuning, and deployment. This section keeps those skills together.

| Skill | What It Does | Link |
|------|--------------|------|
| `jupyter-notebook` | Creates clean, reproducible Jupyter notebooks for experiments and tutorials. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `spreadsheet` | Creates, edits, and analyzes spreadsheets with formula-aware workflows and visual checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) |
| `hf-cli` | Manages Hugging Face auth, repos, papers, datasets, buckets, jobs, and endpoints from the `hf` CLI. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hf-cli) |
| `huggingface-datasets` | Explores Hugging Face datasets via the Dataset Viewer API, including configs, rows, search, filters, and parquet access. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | Adds and manages evaluation results in model cards, imports external scores, and runs custom HF Hub evaluations. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-tool-builder` | Builds reusable scripts around the Hugging Face API for metadata collection, automation, and repeatable research workflows. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-tool-builder) |
| `huggingface-llm-trainer` | Trains or fine-tunes language models with TRL on Hugging Face Jobs, including SFT, DPO, GRPO, reward models, and GGUF export. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | Trains or fine-tunes detection and classification models with Transformers Trainer on Hugging Face Jobs or locally. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `huggingface-jobs` | Runs Python workloads, scheduled jobs, and CPU/GPU/TPU experiments on Hugging Face infrastructure. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-jobs) |
| `axolotl` | Provides YAML-first fine-tuning workflows for 100+ models, including LoRA, QLoRA, DPO, and multimodal training. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/axolotl) |
| `llama-factory` | Provides WebUI and CLI workflows for no-code or low-code fine-tuning across 100+ language and multimodal models. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/llama-factory) |
| `unsloth` | Accelerates LoRA/QLoRA fine-tuning with lower memory use for rapid local experimentation. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/unsloth) |
| `peft` | Covers parameter-efficient fine-tuning with LoRA, QLoRA, DoRA, and related adapter methods. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `trl-fine-tuning` | Uses TRL for post-training workflows such as SFT, DPO, PPO, GRPO, and reward-model training. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/trl-fine-tuning) |
| `grpo-rl-training` | Specializes in GRPO-based post-training for reasoning, verifiable tasks, structured outputs, and custom reward functions. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/grpo-rl-training) |
| `ray-data` | Scales batch inference, preprocessing, and multi-modal ETL from a single machine to clusters. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/ray-data) |
| `nemo-curator` | Curates training corpora with GPU-accelerated deduplication, quality filtering, PII redaction, and multimodal cleanup. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/nemo-curator) |
| `weights-and-biases` | Tracks experiments, sweeps, artifacts, and model registries. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | Handles experiment tracking, model registry, deployment, and autologging workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `lm-evaluation-harness` | Runs standardized LLM benchmarks such as MMLU, HumanEval, GSM8K, and TruthfulQA. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | Benchmarks code models with HumanEval, MBPP, MultiPL-E, and `pass@k` workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `nemo-evaluator` | Runs reproducible multi-backend benchmarking across 100+ LLM/VLM benchmarks with containerized workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/nemo-evaluator) |
| `vllm` | Serves LLMs with high-throughput inference and OpenAI-compatible endpoints. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `sglang` | Serves LLMs and VLMs with fast structured generation, prefix caching, and strong JSON/tool-calling workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/sglang) |
| `llama-cpp` | Runs quantized LLMs on CPUs, Apple Silicon, and non-CUDA hardware for local or edge research deployments. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/llama-cpp) |

### 7. Interpretability and Model Analysis

| Skill | What It Does | Link |
|------|--------------|------|
| `transformer-lens` | Supports mechanistic interpretability research with HookPoints, activation caching, and causal tracing on transformer internals. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `saelens` | Trains and analyzes sparse autoencoders for monosemantic feature discovery and superposition research. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/saelens) |
| `nnsight` | Runs local or remote interpretability experiments on PyTorch models, including very large models via NDIF. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/nnsight) |
| `pyvene` | Performs causal interventions, activation patching, and interchange intervention training on PyTorch models. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/pyvene) |

---

## Installation and Usage

This repository is a curated list, not a package manager. Current Codex docs distinguish between:

- local skill folders for authoring and day-to-day use
- plugins for distributing reusable skill bundles more broadly

In practice, most entries here are still used by placing an upstream skill folder in a standard Codex skill directory. Some third-party repositories also ship their own installers or plugin manifests; when they do, prefer the upstream installation path they document.

### Install a skill in Codex

Current Codex docs describe these standard skill locations:

- repository scope: `.agents/skills/<skill-name>/`
- user scope: `~/.agents/skills/<skill-name>/`

Example 1: install an official curated skill from `openai/skills`

```bash
$skill-installer pdf
```

Example 2: install a Hugging Face skill manually

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/huggingface/skills.git
cp -R skills/skills/huggingface-papers ~/.agents/skills/
```

Example 3: install the Orchestra Research bundle with its upstream installer

```bash
npx @orchestra-research/ai-research-skills
```

Example 4: manually copy a single Orchestra skill if you only want one

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/20-ml-paper-writing/academic-plotting ~/.agents/skills/
```

Some older guides and repos still mention `.codex/skills`, but the current OpenAI documentation uses `.agents/skills` as the standard local location.

### Use a skill in Codex

Once the folder is available in a valid Codex skill location, you can invoke it naturally in your prompt.

Examples:

- `Use autoresearch to set up an experiment loop for this idea.`
- `Use academic-plotting to turn these ablation results into camera-ready figures.`
- `Use hf-cli to inspect the model, dataset, and paper metadata for this checkpoint.`
- `Use transformer-lens to run activation-patching experiments on this model.`
- `Use huggingface-gradio to build a demo for this paper artifact.`

### Recommended usage pattern

1. Pick one skill for one clear bottleneck.
2. Start with a narrow task instead of a full workflow.
3. Read the upstream `SKILL.md` before relying on the result.
4. If the source repository ships its own installer, plugin manifest, or fallback `AGENTS.md`, read its install docs before mixing methods.
5. For academic work, manually check citations, claims, equations, data handling, and benchmark settings.
6. If a skill touches remote services or external datasets, verify authentication, quotas, privacy, and licensing before running it at scale.

---

## License

The content of this repository is released under the [MIT License](LICENSE).

Third-party skills linked from this list keep their own licenses. Always check the original repository before installing or redistributing anything.

If you notice a dead link, a naming change, or a clearly better entry for the list, a short issue or PR is enough.

---

## References

- [Agent Skills – Codex](https://developers.openai.com/codex/skills)
- [openai/skills](https://github.com/openai/skills)
- [huggingface/skills](https://github.com/huggingface/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Agent Skills Open Standard](https://agentskills.io)
