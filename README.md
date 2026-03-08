# Codex Academic Skills

[English](README.md) | [简体中文](README.zh-CN.md)

A curated list of research-oriented skills that are usable in **OpenAI Codex**.

The goal is simple: if a skill is listed here, it should either be from the official Codex ecosystem or from a repository that explicitly supports Codex or the open Agent Skills workflow that Codex can use.

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

Codex skills are folder-based instruction bundles that teach Codex how to handle a task more reliably.

A typical skill usually includes:

- a `SKILL.md` file with trigger rules and workflow guidance
- optional scripts, templates, and references
- a stable folder structure that Codex can discover from standard skill locations

In practice, a good skill works like a reusable research playbook: Codex loads it when needed, follows the instructions, and combines that guidance with your local repository context.

---

## Inclusion Rules

This list only keeps skills that satisfy at least one of the following:

- official OpenAI Codex skills
- repositories that explicitly document Codex support
- repositories built around the open Agent Skills format that Codex can consume with minimal adaptation

This list intentionally removes:

- skills that are exclusive to other platforms, for example Claude Code-only skills
- document-oriented workflows that depend on platform-built-in capabilities and do not translate cleanly into reusable Codex skills
- repositories whose Codex compatibility is unclear

---

## How To Use This List

This list works best as a research-workflow index. It helps narrow the search space first, then sends you back to the upstream `SKILL.md` for the actual details.

If you are new to the list, a quick task-based pass is usually enough:

- For research workflow design, task decomposition, and context management, start with sections 1 and 2.
- For paper writing, literature organization, and evidence summaries, start with sections 3 and 4.
- For demos, observability, data work, or experiment pipelines, start with sections 5 and 6.
- If a skill looks promising, open the upstream `SKILL.md` before deciding whether to install or rely on it.

---

## Skill List

### 1. Planning and Workflow

| Skill | What It Does | Link |
|------|--------------|------|
| `project-development` | Helps scope LLM projects, assess task-model fit, and design practical research-agent architectures. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| `notion-research-documentation` | Research across Notion and turn scattered notes into briefs, comparisons, and reports with citations. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `brainstorming-research-ideas` | Guides structured ideation for discovering defensible, high-impact research directions. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas) |
| `creative-thinking-for-research` | Applies cognitive-science creativity frameworks to help generate genuinely novel research ideas. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research) |

### 2. Deep Thinking and Research Framing

| Skill | What It Does | Link |
|------|--------------|------|
| `context-fundamentals` | Explains how context works in agent systems and how to design high-signal task context. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| `context-degradation` | Helps diagnose lost-in-the-middle, distraction, poisoning, and other context failure modes. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| `context-compression` | Teaches how to summarize and compress long-running research or coding sessions without losing critical state. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| `advanced-evaluation` | Covers LLM-as-a-judge workflows, rubric design, and bias-aware automated evaluation. | [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |

### 3. Writing and Scholarly Communication

| Skill | What It Does | Link |
|------|--------------|------|
| `doc` | Codex-oriented DOCX workflow for creating or editing research reports with rendering and layout checks. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/doc) |
| `notion-research-documentation` | Useful for writing research briefs, comparison notes, and structured evidence summaries. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `hugging-face-paper-publisher` | Publishes papers, links them to models or datasets, and generates professional research article pages. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-paper-publisher) |
| `ml-paper-writing` | Writes publication-ready ML/AI/Systems papers with citation verification and venue-aware structure. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing) |

### 4. Literature Reading and Evidence Synthesis

| Skill | What It Does | Link |
|------|--------------|------|
| `notion-research-documentation` | Synthesizes multi-source findings into literature summaries and cited research notes. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) |
| `llamaindex` | Builds document-ingestion and retrieval pipelines for paper corpora, notes, and private research archives. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/14-agents/llamaindex) |
| `faiss` | Provides high-performance dense retrieval for large paper or note embedding collections. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/faiss) |
| `sentence-transformers` | Generates strong semantic embeddings for literature search, clustering, and retrieval. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/15-rag/sentence-transformers) |

### 5. Visualization and Presentation

| Skill | What It Does | Link |
|------|--------------|------|
| `gradio` | Builds interactive demos and polished research interfaces for models, ablations, and prototypes. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/huggingface-gradio) |
| `hugging-face-trackio` | Tracks and visualizes training metrics with real-time dashboards. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-trackio) |
| `langsmith-observability` | Adds tracing, evaluation, and monitoring for LLM apps and experiment pipelines. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/langsmith) |
| `phoenix-observability` | Open-source observability for tracing, experiments, and real-time analysis of AI systems. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/17-observability/phoenix) |
| `stable-diffusion-image-generation` | Useful for generating figures, visual concepts, teaser graphics, or multimodal assets for presentations. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/18-multimodal/stable-diffusion) |

### 6. Data and Experimentation

This is an extra category I recommend keeping because modern research workflows depend on it heavily.

| Skill | What It Does | Link |
|------|--------------|------|
| `hugging-face-datasets` | Creates, manages, queries, and transforms datasets on Hugging Face Hub. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-datasets) |
| `hugging-face-evaluation` | Adds and manages structured evaluation results for models and benchmarks. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-evaluation) |
| `hugging-face-model-trainer` | Trains or fine-tunes LLMs with TRL on Hugging Face Jobs. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-model-trainer) |
| `hugging-face-jobs` | Runs compute jobs on Hugging Face infrastructure for evaluation, generation, or training workflows. | [huggingface/skills](https://github.com/huggingface/skills/tree/main/skills/hugging-face-jobs) |
| `evaluating-llms-harness` | Runs standardized academic benchmarks such as MMLU, HumanEval, GSM8K, and TruthfulQA. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/11-evaluation/lm-evaluation-harness) |
| `serving-llms-vllm` | Serves LLMs with high-throughput inference and OpenAI-compatible endpoints. | [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/12-inference-serving/vllm) |

---

## Installation and Usage

This repository is a curated list, not a unified marketplace. You usually install a skill from its original source repository into a Codex skill directory.

### Install a skill in Codex

Common Codex skill locations include:

- repository scope: `.codex/skills/<skill-name>/`
- user scope: `~/.codex/skills/<skill-name>/`

Example 1: install an official Codex-oriented skill from `openai/skills`

```bash
mkdir -p ~/.codex/skills
cd /tmp
git clone --depth 1 https://github.com/openai/skills.git
cp -R skills/skills/.curated/notion-research-documentation ~/.codex/skills/
```

Example 2: install a research skill from `AI-Research-SKILLs`

```bash
mkdir -p ~/.codex/skills
cd /tmp
git clone --depth 1 https://github.com/Orchestra-Research/AI-Research-SKILLs.git
cp -R AI-Research-SKILLs/20-ml-paper-writing ~/.codex/skills/ml-paper-writing
```

### Use a skill in Codex

Once the folder is in a valid Codex skill location, you can invoke it naturally in your prompt.

Examples:

- `Use the ml-paper-writing skill to turn this repo into a NeurIPS-style draft.`
- `Use brainstorming-research-ideas to generate three defensible project directions.`
- `Use notion-research-documentation to turn these source notes into a cited literature brief.`
- `Use evaluating-llms-harness to benchmark this checkpoint on MMLU and GSM8K.`
- `Use gradio to build a polished demo for this paper artifact.`

### Recommended usage pattern

1. Pick one skill for one clear bottleneck.
2. Start with a narrow task, not a giant workflow.
3. Read the upstream `SKILL.md` before relying on output.
4. For academic work, it is worth manually checking citations, claims, equations, dataset handling, and benchmark settings, especially when copyright, privacy, attribution, or research-integrity requirements matter.

---

## License

The content of this repository is released under the [MIT License](LICENSE).

Third-party skills linked from this list keep their own licenses. Always check the original repository before installing or redistributing anything.

If you notice a dead link, a compatibility change, or a clearly better entry for the list, a short issue or PR is enough.

---

## References

- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [openai/skills](https://github.com/openai/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [huggingface/skills](https://github.com/huggingface/skills)
- [awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)
- [Agent Skills Open Standard](https://agentskills.io)
