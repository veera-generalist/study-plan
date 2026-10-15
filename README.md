# Getting started with AI engineering and evaluation

Learn how an AI application works, how to ask it for useful results, and how to check its answers.

All twelve lessons use plain-language explanations, worked examples, guided activities, assignments, and knowledge checks with explained answers. We follow one fictional bookshop, Maple Books, so each new idea builds on something familiar.

## Start here

Open [Lesson 01](modules/01-python-engineering.md). You can complete the written learning path with a notebook or text document. An AI chat tool you already use is optional for trying live responses.

Python remains the implementation language for the coding path. Lesson 05 includes a small optional counting example. The deeper Python programs and application-building work are available separately when you are ready.

## The lessons

| Lesson | What you will make |
|---|---|
| [01 — Getting started with generative AI](modules/01-python-engineering.md) | An assistant idea |
| [02 — Understanding and comparing language models](modules/02-model-foundations.md) | A three-question comparison |
| [03 — Writing useful prompts](modules/03-prompting-and-development.md) | A prompt experiment |
| [04 — Make a small set of questions to learn from](modules/04-datasets-and-oracles.md) | A question collection |
| [05 — Check answers consistently](modules/05-evaluation-harnesses.md) | Review rules and reviewed replies |
| [06 — Get help reviewing answers](modules/06-judges-and-human-review.md) | Reviewer instructions and a comparison |
| [07 — Help an assistant answer from documents](modules/07-rag-engineering.md) | Questions linked to source passages |
| [08 — Compare two versions fairly](modules/08-rag-evaluation-and-statistics.md) | A record of improvements and regressions |
| [09 — Give an assistant a small action](modules/09-tools-and-agents.md) | A pretend tool workflow |
| [10 — Check an assistant when things go wrong](modules/10-agent-evaluation-and-security.md) | Difficult scenarios and expected results |
| [11 — Find where a failure began](modules/11-observability-and-delivery.md) | A step record and change recommendation |
| [12 — Bring it together in a small project](modules/12-optimization-and-career.md) | A project with evidence and limitations |

Read the example, try the activity, and attempt the knowledge check before opening its explanation. The [course guide](COURSE_GUIDE.md) explains how to keep your work. The [roadmap](ROADMAP.md) groups the lessons into manageable stages.

## How these lessons are taught

The organization is inspired by Microsoft's [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners): a scenario, learning objectives, explanations, examples, an assignment, and a knowledge check.

Our writing, bookshop facts, prompts, exercises, and answer explanations are original. The topic sequence is our own. See [attributions](ATTRIBUTIONS.md).

Use the [glossary](GLOSSARY.md) when a word is unfamiliar. You do not need to memorize it before starting.

## From understanding to implementation

The written lessons teach the concepts and decision-making through small examples. A paper simulation is different from running a model or implementing an application.

After you understand the process, use the optional coding path to automate it gradually. Record what you actually built and measured. Completing the introductory lessons is a foundation for further engineering practice, not a claim of professional readiness by itself.

<details>
<summary>Optional technical notes and coding material</summary>

The earlier technical chapters are preserved for all twelve topics in the [technical notes](advanced/README.md). They include Python, mathematical examples, and larger implementation assignments.

- [Python setup](SETUP.md)
- [Small beginner Python example](labs/beginner/README.md)
- [Saved technical examples](labs/module-examples/README.md)
- [Offline evaluation lab](labs/offline-evaluation/README.md)
- [Local-model adapter](labs/live-model/README.md)
- [Larger project briefs](projects/README.md)
- [Reference library](RESOURCES.md)
- [Learning log template](templates/learning-log.md)
- [Progress tracker](PROGRESS.md)

</details>

<details>
<summary>Repository maintenance and verification</summary>

Run `python3 scripts/validate.py` for the offline repository checks. This verifies navigation and code examples; it is not a learner prerequisite or an automated judgment of teaching quality.

- [Validation scope](VALIDATION.md)
- [Earlier technical review](REVIEW.md)
- [Dated reference snapshots](references/README.md)
- [Contribution guidance](CONTRIBUTING.md)

Core sources and the three Microsoft lesson destinations used as teaching-structure references were reviewed on 2026-10-15. External framework examples and real-model inference have not been executed during validation.

</details>
