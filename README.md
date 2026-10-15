# Getting started with AI engineering and evaluation

Learn how an AI application works, how to ask it for useful results, and how to check its answers.

**Our current focus is the first three lessons.** They are written for someone new to AI, with explanations, worked examples, guided practice, and assignments. Python remains the language for later implementation work; you do not need it to begin these lessons.

## Start here

| Lesson | What you will learn | What you will make |
|---|---|---|
| [01 — Getting started with generative AI](modules/01-python-engineering.md) | What a model does, what an application adds, and why answers need checking | A small assistant idea |
| [02 — Understanding and comparing language models](modules/02-model-foundations.md) | Why responses differ and how to compare them for a task | A three-question comparison |
| [03 — Writing useful prompts](modules/03-prompting-and-development.md) | How to give clear instructions, relevant facts, and a useful answer format | A prompt and one documented improvement |

Start with Lesson 01. Read the example, try the activity, and answer the knowledge check before opening its explanations. You can work entirely from the supplied examples or optionally try an AI chat tool you already have.

## How these lessons are taught

We use one fictional bookshop across the three lessons. Each lesson introduces the ideas it needs in everyday language before asking you to use them.

The organization is inspired by Microsoft's [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners): a scenario, learning objectives, explanations, examples, an assignment, and a knowledge check. The writing, bookshop scenario, exercises, and answer explanations in this repository are original. See [attributions](ATTRIBUTIONS.md).

Read the [short course guide](COURSE_GUIDE.md) if you want help getting started. Look up a word in the [glossary](GLOSSARY.md) when you need it; you do not need to study the glossary first.

## What to do after Lesson 03

Pause and review your assistant idea, comparison sheet, and prompt experiment. These show whether the basic ideas are becoming clear.

The remaining Modules 04–12 retain their earlier technical draft. They have not yet been rewritten in this beginner format. The [roadmap](ROADMAP.md) records the wider direction, but those chapters are not a prerequisite for finishing the current three lessons.

<details>
<summary>Optional technical notes and coding material</summary>

The earlier first-three chapters are preserved for later use:

- [Python engineering](advanced/01-python-engineering.md)
- [Model mathematics and classification](advanced/02-model-foundations.md)
- [Prompt comparisons in Python](advanced/03-prompting-and-development.md)

Other optional material:

- [Python setup and later exercises](SETUP.md)
- [Saved technical examples](labs/module-examples/README.md)
- [Offline evaluation lab](labs/offline-evaluation/README.md)
- [Local-model adapter](labs/live-model/README.md)
- [Project briefs](projects/README.md)
- [Reference library](RESOURCES.md)
- [Learning log template](templates/learning-log.md)
- [Progress tracker](PROGRESS.md)

These programs and project assignments go beyond the current introductory lessons. You can return to them after the concepts feel familiar.

</details>

<details>
<summary>Repository maintenance and verification</summary>

Run `python3 scripts/validate.py` for the offline repository checks. This is for verifying the material and examples; it is not a learner prerequisite.

- [Validation scope](VALIDATION.md)
- [Earlier technical review](REVIEW.md)
- [Dated reference snapshots](references/README.md)
- [Contribution guidance](CONTRIBUTING.md)

Core sources were reviewed on 2026-10-15. The three Microsoft lesson destinations used for this rewrite were also reviewed on that date. External examples and real-model inference have not been executed during validation.

</details>
