# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

A curated list of research-oriented skills that work with **OpenAI Codex**.

This list is intentionally conservative. Each entry is included only when the upstream source is one of the following:

- an official OpenAI Codex skill
- a repository that explicitly documents Codex support
- a repository that follows the open Agent Skills format Codex can read

Skill names below follow the upstream `SKILL.md` name or folder slug whenever possible, so install paths and prompt mentions stay close to the source repository.

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

Codex skills are folder-based instruction bundles that help Codex handle a task more reliably.

A typical skill usually includes:

- a `SKILL.md` file with trigger rules and workflow guidance
- optional scripts, templates, and references
- a stable folder structure that Codex can discover from standard skill locations

In practice, a good skill works like a reusable playbook. Codex loads it when the task matches, follows the instructions, and combines that guidance with the local repository context.

---

## Inclusion Rules

This list keeps entries that satisfy at least one of the following:

- official OpenAI Codex skills
- repositories that explicitly document Codex support
- repositories built around the open Agent Skills format that Codex can consume with little or no adaptation

This list intentionally excludes:

- skills that are exclusive to other platforms, such as Claude Code-only skills
- document workflows that depend on platform-specific built-ins and do not translate cleanly into reusable Codex skills
- repositories whose Codex compatibility is unclear

---

## How To Use This List

Treat this repository as a research-workflow index, not a marketplace. The tables help narrow the search space; the upstream `SKILL.md` is still the source of truth.

If you are new to the list, a task-based pass is usually enough:

- For workflow design, task decomposition, and context management, start with sections 1 and 2.
- For paper writing, presentation work, and formal deliverables, start with sections 3 and 5.
- For literature review and evidence synthesis, start with section 4.
- For experiments, evaluation, fine-tuning, and reproducibility work, start with section 6.

---

## Skill List

### 1. Planning and Workflow

| Skill | What It Does | Link |
|------|--------------|------|
| `project-development` | Helps scope LLM projects and design practical research-agent architectures. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | Researches across Notion and synthesizes cited briefs and reports. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `brainstorming-research-ideas` | Guides structured ideation for high-impact research directions. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | Applies creativity frameworks to generate novel research ideas. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |
| `dspy` | Uses declarative prompt programming and optimizers to build structured research-agent workflows. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/dspy) |
| `instructor` | Produces Pydantic-validated structured outputs for extraction, labeling, and reliable research automation. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/instructor) |
| `outlines` | Constrains generation with grammars and finite-state machines for structured outputs and synthetic data workflows. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/16-prompt-engineering/outlines) |

### 2. Deep Thinking and Research Framing

| Skill | What It Does | Link |
|------|--------------|------|
| `context-fundamentals` | Explains how context works in agent systems. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | Diagnoses lost-in-the-middle and other context failure modes. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | Compresses long sessions while preserving critical state. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `advanced-evaluation` | Covers LLM-as-a-judge and bias-aware automated evaluation. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. Writing and Scholarly Communication

| Skill | What It Does | Link |
|------|--------------|------|
| `doc` | Codex-oriented DOCX workflow with rendering checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | Useful for research briefs and structured evidence summaries. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | Reads, creates, and reviews PDFs when layout and rendering matter. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `slides` | Creates and edits `.pptx` slide decks with editable output and layout validation. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `huggingface-paper-publisher` | Publishes papers on Hugging Face Hub, links them to models or datasets, and manages paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) |
| `ml-paper-writing` | Writes publication-ready ML/AI/Systems papers. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing) |

### 4. Literature Reading and Evidence Synthesis

| Skill | What It Does | Link |
|------|--------------|------|
| `notion-research-documentation` | Turns multi-source findings into cited literature notes. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `pdf` | Useful for paper packets, annotated drafts, and layout-sensitive reading workflows. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| `transcribe` | Transcribes interviews, meetings, or recorded talks with optional speaker diarization. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) |
| `huggingface-papers` | Looks up Hugging Face paper pages and structured paper metadata for summaries or analysis. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) |
| `llamaindex` | Builds document-ingestion and retrieval pipelines for research corpora. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | Provides high-performance dense retrieval for paper collections. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | Generates embeddings for literature search, clustering, and retrieval. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. Visualization and Presentation

| Skill | What It Does | Link |
|------|--------------|------|
| `gradio` | Builds Gradio demos and interactive research interfaces in Python. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `huggingface-trackio` | Tracks training metrics, alerts, and dashboards with Hugging Face Trackio. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) |
| `slides` | Builds editable slide decks for talks, posters, and result reviews. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/slides) |
| `langsmith` | Adds tracing, evaluation, and monitoring to LLM research workflows. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix` | Open-source observability for tracing, evaluation, and experiment analysis. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `tensorboard` | Visualizes scalars, embeddings, profiles, and training diagnostics. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/tensorboard) |
| `stable-diffusion` | Generates figures, concept art, and presentation assets for multimodal research. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. Data and Experimentation

Research workflows now depend on reproducible data handling, evaluation, and experiment tracking, so this category keeps those skills together.

| Skill | What It Does | Link |
|------|--------------|------|
| `jupyter-notebook` | Creates clean, reproducible Jupyter notebooks for experiments and tutorials. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) |
| `spreadsheet` | Creates, edits, and analyzes spreadsheets with formula-aware workflows and visual checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) |
| `huggingface-datasets` | Explores Hugging Face datasets through the Dataset Viewer API, including splits, search, filters, and parquet export. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) |
| `huggingface-community-evals` | Runs local evaluations for Hugging Face Hub models with `inspect-ai` or `lighteval`, with sensible backend selection. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) |
| `huggingface-llm-trainer` | Trains or fine-tunes language models with TRL on Hugging Face Jobs, including SFT, DPO, GRPO, and reward models. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) |
| `huggingface-vision-trainer` | Trains or fine-tunes vision models for detection, classification, and segmentation on Hugging Face Jobs. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer) |
| `huggingface-jobs` | Runs data processing, inference, experiments, or training jobs on Hugging Face infrastructure. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-jobs) |
| `peft` | Covers parameter-efficient fine-tuning with LoRA, QLoRA, DoRA, and related adapter methods. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/03-fine-tuning/peft) |
| `weights-and-biases` | Tracks experiments, sweeps, artifacts, and model registries. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/weights-and-biases) |
| `mlflow` | Handles experiment tracking, model registry, deployment, and autologging workflows. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/13-mlops/mlflow) |
| `lm-evaluation-harness` | Runs standardized LLM benchmarks such as MMLU, HumanEval, GSM8K, and TruthfulQA. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `bigcode-evaluation-harness` | Benchmarks code models with HumanEval, MBPP, MultiPL-E, and `pass@k` workflows. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/bigcode-evaluation-harness) |
| `vllm` | Serves LLMs with high-throughput inference and OpenAI-compatible endpoints. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |

---

## Installation and Usage

This repository is a curated list, not a unified marketplace. In most cases, you install a skill from its upstream repository and place it in a Codex skill directory.

### Install a skill in Codex

Current Codex docs describe these standard skill locations:

- repository scope: `.agents/skills/<skill-name>/`
- user scope: `~/.agents/skills/<skill-name>/`

For official OpenAI skills, the simplest path is usually `$skill-installer`.

Example 1: install an official curated skill from `openai/skills`

```bash
$skill-installer pdf
```

Example 2: install a third-party skill manually

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/huggingface/skills.git
cp -R skills/skills/huggingface-papers ~/.agents/skills/
```

Example 3: install a research skill from `AI-Research-SKILLs`

```bash
mkdir -p ~/.agents/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/03-fine-tuning/peft ~/.agents/skills/
```

Some older guides and repos still mention `.codex/skills`, but the current OpenAI documentation uses `.agents/skills` as the standard location.

### Use a skill in Codex

Once the folder is available in a valid Codex skill location, you can invoke it naturally in your prompt.

Examples:

- `Use the ml-paper-writing skill to turn this repo into a NeurIPS-style draft.`
- `Use dspy to prototype an optimizer-backed prompt pipeline for this ablation.`
- `Use huggingface-community-evals to smoke-test this checkpoint on MMLU and GSM8K.`
- `Use pdf to review these camera-ready pages for layout issues.`
- `Use gradio to build a demo for this paper artifact.`

### Recommended usage pattern

1. Pick one skill for one clear bottleneck.
2. Start with a narrow task instead of a full workflow.
3. Read the upstream `SKILL.md` before relying on the result.
4. For academic work, manually check citations, claims, equations, data handling, and benchmark settings.
5. If a skill touches remote services or external datasets, verify authentication, quotas, privacy, and licensing before running it at scale.

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
