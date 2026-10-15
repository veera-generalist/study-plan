# From Senior QA to AI Engineering and Evaluation

A practical, evaluation-first course for a QA engineer with 15+ years of experience transitioning into applied AI engineering and AI evaluation engineering.

**Course format:** 12 modules across approximately 24 weeks at 8–10 hours per week. This is a learning estimate, not a job-placement promise. Each module includes a detailed tutorial, a complete runnable Python example, expected behavior, guided practice with answer reasoning, and a larger lab assignment. External repositories provide supplementary reading and implementation examples.

## Start here

1. Read the [roadmap](ROADMAP.md) and [setup guide](SETUP.md).
2. Complete [Module 01](modules/01-python-engineering.md).
3. Run the [module examples](labs/module-examples/README.md), then the [offline evaluation lab](labs/offline-evaluation/README.md).
4. Update your [progress tracker](PROGRESS.md) with evidence after each module.
5. Keep a [learning log](templates/learning-log.md).

## Course contents

| Module | Weeks | Topic | Evidence you produce |
|---|---|---|---|
| [01](modules/01-python-engineering.md) | 1–2 | Python engineering | Validated data pipeline and tests |
| [02](modules/02-model-foundations.md) | 3–4 | Models, tokens, embeddings, ML basics | Classification baseline and error analysis |
| [03](modules/03-prompting-and-development.md) | 5–6 | Prompting, structured output, AI-assisted coding | Controlled prompt comparison |
| [04](modules/04-datasets-and-oracles.md) | 7–8 | Evaluation datasets and labeling | Dataset card and labeling guidelines |
| [05](modules/05-evaluation-harnesses.md) | 9–10 | Metrics, graders, evaluation runners | Reproducible evaluation report |
| [06](modules/06-judges-and-human-review.md) | 11–12 | LLM judges and human review | Judge validation report |
| [07](modules/07-rag-engineering.md) | 13–14 | Retrieval-augmented generation | QA knowledge assistant |
| [08](modules/08-rag-evaluation-and-statistics.md) | 15–16 | RAG metrics and statistical comparisons | Paired experiment with uncertainty |
| [09](modules/09-tools-and-agents.md) | 17–18 | Tools, workflows, agents | Bounded sandbox workflow |
| [10](modules/10-agent-evaluation-and-security.md) | 19–20 | Agent evaluation and adversarial testing | State-based checks and security findings |
| [11](modules/11-observability-and-delivery.md) | 21–22 | Traces, CI, production feedback | Release evaluation pipeline |
| [12](modules/12-optimization-and-career.md) | 23–24 | Optimization and career evidence | Capstone report and portfolio |

## Supporting material

- [Twelve runnable lesson examples and verification command](labs/module-examples/README.md)
- [Annotated GitHub reading library](RESOURCES.md)
- [Attributions and reuse policy](ATTRIBUTIONS.md)
- [Glossary](GLOSSARY.md)
- [Portfolio project briefs](projects/README.md)
- [Evaluation report template](templates/evaluation-report.md)
- [Dataset card template](templates/dataset-card.md)
- [Labeling guidelines template](templates/labeling-guidelines.md)
- [Experiment record template](templates/experiment-record.md)
- [Contribution guidance](CONTRIBUTING.md)

## Learning principles

Build a small system, state what good behavior means, collect representative cases, evaluate it, inspect failures, and improve one thing at a time. Use deterministic checks for exact requirements and calibrated human/model judgments for semantic requirements. Preserve the evidence behind every quality claim.

Your QA expertise transfers directly to failure analysis, test design, automation, and release decisions. Add Python, model behavior, data discipline, and statistical reasoning. Practice building the systems you evaluate.

## Scope and provenance

This is an independently written study course assembled with AI assistance for this repository. It is not an official course from any referenced organization, and no endorsement is implied. Upstream courses, source code, notebooks, and figures are linked rather than mirrored. Read [ATTRIBUTIONS.md](ATTRIBUTIONS.md) before importing outside material.

Research links were checked on 2026-10-15. External APIs, model availability, and repository locations can change. All included Python examples and the offline lab are independent of provider APIs; follow each upstream project's current setup instructions for external exercises. The examples use controlled synthetic data and do not constitute measured live-model performance.
