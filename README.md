# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

A curated list of research-oriented skills that currently work with **OpenAI Codex**.

This list stays deliberately conservative. It favors official sources, repositories that explicitly document Codex interoperability, and open Agent Skills that Codex can read directly.

To keep the list usable, each skill appears only once. If a skill fits several workflows, it is placed under its primary use case. The upstream `SKILL.md` remains the source of truth before installation or serious use.

---

## Table of Contents

- [What Are Codex Skills?](#what-are-codex-skills)
- [Inclusion Rules](#inclusion-rules)
- [How To Use This List](#how-to-use-this-list)
- [Core Picks](#core-picks)
- [Skill List](#skill-list)
- [Installation and Usage](#installation-and-usage)
- [License](#license)
- [References](#references)

---

## What Are Codex Skills?

Codex skills are folder-based instruction bundles that help Codex handle specific tasks more reliably. A typical skill includes a `SKILL.md` file and may also include scripts, templates, or references.

Codex first sees each skill's name, description, and path. It reads the full `SKILL.md` only when the task matches. That keeps context usage under control, but it also means large skill sets have a real cost. OpenAI's docs note that the initial skill list has a context budget; with many installed skills, descriptions may be shortened, and very large sets may omit some skills from the initial list.

---

## Inclusion Rules

This list keeps entries that satisfy at least one of the following:

- official OpenAI Codex skills
- repositories that explicitly document Codex support or interoperability
- open Agent Skills that Codex can read directly or with minimal adaptation

This list intentionally excludes:

- skills that are exclusive to other platforms
- entries whose upstream links disappeared without a clear replacement path
- highly overlapping entries that do not add clear value for research workflows
- repositories whose Codex compatibility is unclear

---

## How To Use This List

Treat this repository as a research-workflow index, not a marketplace. Start with the Core Picks below, then move into the category that matches your bottleneck.

Task-based scan:

- Research orchestration, project planning, and model choice: section 1.
- Context engineering, agent design, and structured outputs: section 2.
- Paper drafting and formal scholarly writing: section 3.
- Literature review, transcription, and evidence synthesis: section 4.
- Demos, figures, talks, and presentation assets: section 5.
- Data, retrieval, experiment tracking, and observability: section 6.
- Fine-tuning, evaluation, serving, and kernel optimization: section 7.
- Mechanistic interpretability and model analysis: section 8.
- Research artifacts, provenance, and reproducibility checks: section 9.

---

## Core Picks

If you only want a small starter set, begin here. These skills cover broad research workflows, have clear upstream sources, and keep the active skill list from getting too crowded.

| Skill | What It Does | Link |
|------|--------------|------|
| `autoresearch` | Orchestrates literature review, experiments, synthesis, and paper-writing workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `notion-research-documentation` | Researches across Notion and synthesizes cited briefs and reports. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `openai-docs` | Looks up current OpenAI product and API documentation with source-grounded guidance. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) |
| `huggingface-best` | Finds and compares candidate models using official Hugging Face benchmark leaderboards and metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-best) |
| `pdf` | Reads, creates, and reviews PDFs when layout and rendering matter. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `huggingface-papers` | Looks up Hugging Face paper pages and structured paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `academic-plotting` | Generates publication-quality charts, ablations, and architecture figures. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `jupyter-notebook` | Creates clean, reproducible Jupyter notebooks for experiments and tutorials. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `huggingface-datasets` | Explores Dataset Viewer API metadata, rows, search, filters, parquet URLs, and statistics. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-local-models` | Selects GGUF models, quantization levels, and llama.cpp commands for local inference. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-local-models) |
| `huggingface-llm-trainer` | Trains or fine-tunes language models with TRL on Hugging Face Jobs, including SFT, DPO, GRPO, and reward models. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `lm-evaluation-harness` | Runs standardized LLM benchmarks such as MMLU, HumanEval, GSM8K, and TruthfulQA. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `vllm` | Serves LLMs with high-throughput inference and OpenAI-compatible endpoints. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `transformer-lens` | Supports mechanistic interpretability with HookPoints, activation caching, and causal tracing. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `ara-compiler` | Compiles papers, repos, logs, and notes into Agent-Native Research Artifacts with claims, evidence, and provenance. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/compiler) |

---

## Skill List

### 1. Planning and Workflow

| Skill | What It Does | Link |
|------|--------------|------|
| `project-development` | Scopes LLM projects and designs practical research-agent architectures. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | Researches across Notion and synthesizes cited briefs and reports. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `notion-knowledge-capture` | Captures conversations, notes, and decisions into structured Notion pages. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture) |
| `notion-meeting-intelligence` | Prepares agendas, pre-reads, and decision docs in Notion. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-meeting-intelligence) |
| `autoresearch` | Orchestrates literature review, experiments, synthesis, and paper-writing workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill) |
| `brainstorming-research-ideas` | Guides structured ideation for high-impact research directions. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | Applies creativity frameworks to generate less obvious research ideas. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `openai-docs` | Looks up current OpenAI product and API documentation with source-grounded guidance. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) |
| `huggingface-best` | Finds and compares candidate models using official Hugging Face benchmark leaderboards and metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-best) |

### 2. Context and Agent Design

| Skill | What It Does | Link |
|------|--------------|------|
| `context-fundamentals` | Explains how context works in agent systems. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | Diagnoses lost-in-the-middle and other context failure modes. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | Compresses long sessions while preserving critical state. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `context-optimization` | Applies caching, masking, compaction, and partitioning to extend effective context capacity. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) |
| `filesystem-context` | Uses files as an overflow layer for scratch pads, shared agent memory, and just-in-time context loading. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/filesystem-context) |
| `latent-briefing` | Studies KV-cache style latent handoff for reducing token cost in orchestrator-worker systems. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/latent-briefing) |
| `evaluation` | Builds evaluation frameworks for agent systems with rubrics, regressions, and quality gates. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation) |
| `advanced-evaluation` | Covers LLM-as-a-judge and bias-aware automated evaluation. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |
| `multi-agent-patterns` | Designs supervisor, swarm, and hierarchical multi-agent systems with clearer coordination. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) |
| `memory-systems` | Designs persistent agent memory and evaluates retrieval quality across sessions. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) |
| `tool-design` | Designs agent-facing tools and MCP interfaces with clearer contracts and less ambiguity. | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design) |
| `dspy` | Uses declarative prompt programming and optimizers for structured agent workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `guidance` | Controls generation with regexes and grammars for structured outputs and multi-step prompting. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/guidance) |
| `instructor` | Produces Pydantic-validated structured outputs for extraction, labeling, and automation. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | Constrains generation with grammars and finite-state machines for structured outputs. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |

### 3. Writing and Scholarly Communication

| Skill | What It Does | Link |
|------|--------------|------|
| `doc` | Creates and reviews DOCX documents with rendering checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `pdf` | Reads, creates, and reviews PDFs when layout and rendering matter. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `huggingface-paper-publisher` | Publishes papers on Hugging Face Hub and manages paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | Writes publication-oriented ML, AI, and systems papers. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/ml-paper-writing) |
| `systems-paper-writing` | Provides paragraph-level blueprints for OSDI, SOSP, ASPLOS, NSDI, and EuroSys papers. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/systems-paper-writing) |

### 4. Literature Reading and Evidence Synthesis

| Skill | What It Does | Link |
|------|--------------|------|
| `transcribe` | Transcribes interviews, meetings, or recorded talks with optional speaker diarization. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `whisper` | Runs multilingual speech recognition and translation for interviews, lectures, podcasts, and audio corpora. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/whisper) |
| `huggingface-papers` | Looks up Hugging Face paper pages and structured paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | Builds document ingestion and retrieval pipelines for research corpora. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | Provides high-performance dense retrieval for paper collections. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | Generates embeddings for literature search, clustering, and retrieval. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. Visualization and Presentation

| Skill | What It Does | Link |
|------|--------------|------|
| `huggingface-gradio` | Builds Gradio web UIs and interactive research demos in Python. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | Tracks training metrics, alerts, and dashboards with Hugging Face Trackio. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `academic-plotting` | Generates publication-quality charts, ablations, and architecture figures. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/academic-plotting) |
| `presenting-conference-talks` | Turns papers into Beamer or PPTX talk decks with speaker notes and scripts. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/presenting-conference-talks) |
| `speech` | Generates narration, accessibility reads, and voiceovers via the OpenAI Audio API. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/speech) |
| `imagegen` | Creates or edits bitmap figures, mockups, infographics, and visual assets. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/imagegen) |
| `transformers-js` | Runs Hugging Face models in JavaScript for browser-side demos and interactive artifacts. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/transformers-js) |
| `stable-diffusion` | Generates figures, concept art, and presentation assets for multimodal research. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. Data, Retrieval, and Experiment Tracking

| Skill | What It Does | Link |
|------|--------------|------|
| `jupyter-notebook` | Creates clean, reproducible Jupyter notebooks for experiments and tutorials. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `hf-cli` | Manages Hugging Face auth, repos, papers, datasets, buckets, jobs, and endpoints from the `hf` CLI. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hf-cli) |
| `huggingface-datasets` | Explores Dataset Viewer API metadata, rows, search, filters, parquet URLs, and statistics. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | Adds and manages evaluation results in model cards and custom HF Hub evaluations. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-tool-builder` | Builds reusable scripts around the Hugging Face API for metadata collection and automation. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-tool-builder) |
| `huggingface-local-models` | Selects GGUF models, quantization levels, and llama.cpp commands for local inference. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-local-models) |
| `ray-data` | Scales batch inference, preprocessing, and multimodal ETL from one machine to clusters. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/ray-data) |
| `nemo-curator` | Curates training corpora with deduplication, quality filtering, PII redaction, and multimodal cleanup. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/05-data-processing/nemo-curator) |
| `weights-and-biases` | Tracks experiments, sweeps, artifacts, and model registries. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | Handles experiment tracking, model registry, deployment, and autologging workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `tensorboard` | Visualizes scalars, embeddings, profiles, and training diagnostics. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `langsmith` | Adds tracing, evaluation, and monitoring to LLM research workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | Provides open-source tracing, evaluation, and experiment analysis. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |

### 7. Training, Evaluation, and Serving

This category can grow quickly, so it keeps representative entries tied closely to research training, evaluation, or serving.

| Skill | What It Does | Link |
|------|--------------|------|
| `huggingface-llm-trainer` | Trains or fine-tunes language models with TRL on Hugging Face Jobs, including SFT, DPO, GRPO, and reward models. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | Trains detection and classification models with Transformers Trainer on Hugging Face Jobs or locally. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `axolotl` | Provides YAML-first fine-tuning workflows for LoRA, QLoRA, DPO, and multimodal training. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/axolotl) |
| `llama-factory` | Provides WebUI and CLI workflows for low-code fine-tuning across language and multimodal models. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/llama-factory) |
| `unsloth` | Accelerates LoRA and QLoRA fine-tuning with lower memory use for local experiments. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/unsloth) |
| `peft` | Covers parameter-efficient fine-tuning with LoRA, QLoRA, DoRA, and adapters. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `trl-fine-tuning` | Uses TRL for post-training workflows such as SFT, DPO, PPO, GRPO, and reward-model training. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/trl-fine-tuning) |
| `grpo-rl-training` | Specializes in GRPO-based post-training for reasoning, verifiable tasks, and custom rewards. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/06-post-training/grpo-rl-training) |
| `lm-evaluation-harness` | Runs standardized LLM benchmarks such as MMLU, HumanEval, GSM8K, and TruthfulQA. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | Benchmarks code models with HumanEval, MBPP, MultiPL-E, and pass@k workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `nemo-evaluator` | Runs reproducible multi-backend benchmarking across LLM and VLM benchmarks. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/nemo-evaluator) |
| `vllm` | Serves LLMs with high-throughput inference and OpenAI-compatible endpoints. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |
| `sglang` | Serves LLMs and VLMs with fast structured generation, prefix caching, and JSON/tool-calling workflows. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/sglang) |
| `llama-cpp` | Runs quantized LLMs on CPUs, Apple Silicon, and non-CUDA hardware. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/llama-cpp) |
| `cuda-kernels` | Guides optimized CUDA kernel writing and benchmarking for Hugging Face diffusers and transformers. | [huggingface/kernels](https://github.com/huggingface/kernels/tree/main/kernel-builder/skills/cuda-kernels) |

### 8. Interpretability and Model Analysis

| Skill | What It Does | Link |
|------|--------------|------|
| `transformer-lens` | Supports mechanistic interpretability with HookPoints, activation caching, and causal tracing. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/transformer-lens) |
| `saelens` | Trains and analyzes sparse autoencoders for monosemantic feature discovery and superposition research. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/saelens) |
| `nnsight` | Runs local or remote interpretability experiments on PyTorch models, including very large models via NDIF. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/nnsight) |
| `pyvene` | Performs causal interventions, activation patching, and interchange intervention training on PyTorch models. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/04-mechanistic-interpretability/pyvene) |

### 9. Research Artifacts and Reproducibility

| Skill | What It Does | Link |
|------|--------------|------|
| `ara-compiler` | Compiles papers, repos, logs, and notes into Agent-Native Research Artifacts with claims, evidence, and provenance. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/compiler) |
| `ara-research-manager` | Records end-of-session research decisions, experiments, dead ends, and provenance into an ARA directory. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/research-manager) |
| `ara-rigor-reviewer` | Reviews Agent-Native Research Artifacts for evidence relevance, falsifiability, scope, coherence, and rigor. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/22-agent-native-research-artifact/rigor-reviewer) |

---

## Installation and Usage

This repository is a curated list, not a package manager. Current Codex docs describe skills as the authoring format for reusable workflows; for broader distribution, package reusable skills as plugins.

### Install a skill in Codex

Current Codex docs describe these standard skill locations:

- repository scope: `.agents/skills/<skill-name>/`
- user scope: `~/.agents/skills/<skill-name>/`
- admin scope: `/etc/codex/skills/<skill-name>/`

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

Example 3: install the Hugging Face Kernels Codex skill

```bash
kernels skills add --codex --global
```

Example 4: install the Orchestra Research bundle with its upstream installer

```bash
npx @orchestra-research/ai-research-skills
```

### Use a skill in Codex

Once the folder is available in a valid Codex skill location, you can invoke it naturally in your prompt.

Examples:

- `Use autoresearch to set up an experiment loop for this idea.`
- `Use huggingface-best to compare current open models for this benchmark.`
- `Use academic-plotting to turn these ablation results into camera-ready figures.`
- `Use huggingface-local-models to choose a GGUF model for this laptop.`
- `Use ara-compiler to turn this paper and repo into a research artifact.`

### Recommended usage pattern

1. Install a small set of high-frequency skills first, then add project-specific ones as needed.
2. Pick one skill for one clear bottleneck.
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
- [Hugging Face Kernels skills add](https://huggingface.co/docs/kernels/cli-skills)
- [huggingface/kernels](https://github.com/huggingface/kernels)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Agent Skills Open Standard](https://agentskills.io)
