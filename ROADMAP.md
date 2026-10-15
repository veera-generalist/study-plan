# 24-week roadmap

## Role definitions

For this course, an **AI Native / Applied AI Engineer** builds software around model capabilities: retrieval, structured generation, tools, agents, and operational controls. The term “AI native” varies by employer; inspect actual responsibilities.

An **AI Evaluation Engineer** designs datasets, graders, experiments, failure analysis, and quality gates. This course focuses on engineering evaluations of applications and agents, with an optional route into model benchmarking.

Start with evaluation as your specialization while building enough application engineering depth to diagnose failures across the system.

## Weekly schedule

Use roughly two hours for reading, five for implementation, two for evaluation, and one for recording findings. Reduce scope before abandoning the feedback loop. If Python is new, spend extra weeks on Module 01; if you are already a Python SDET, demonstrate its exit criteria and move forward.

| Weeks | First week | Second week |
|---|---|---|
| 1–2 | Python, JSONL, types, Git | Validation, exceptions, tests |
| 3–4 | Tokens, inference, embeddings | ML metrics and classification errors |
| 5–6 | Prompt contracts and schemas | Prompt comparison and code review |
| 7–8 | Dataset design and provenance | Labeling, disagreement, held-out split |
| 9–10 | Deterministic graders and harness | Slice reports and failure handling |
| 11–12 | Rubric design and annotation | Judge validation and calibration |
| 13–14 | Parsing, chunking, retrieval | Grounded answers and citations |
| 15–16 | Retrieval and answer metrics | Paired experiments and uncertainty |
| 17–18 | Tool contracts and state | Workflow recovery and bounded agents |
| 19–20 | Outcome and trace evaluation | Injection, leakage, authorization tests |
| 21–22 | Instrumentation and replay | CI tiers and release decisions |
| 23–24 | Controlled optimization | Capstone, presentation, interview practice |

## Milestones

- After week 4: explain basic model behavior and analyze a classification baseline.
- After week 8: defend your dataset composition and expected behaviors.
- After week 12: reproduce an evaluation and explain grader limitations.
- After week 16: diagnose retrieval versus generation failures.
- After week 20: evaluate tool outcomes and application permissions.
- After week 24: present an evidence-backed release recommendation.

## Minimum learning stack

Use Python, Git, standard-library JSON/CSV tooling, and a test runner. The included lab uses Python's unittest. Add pytest and schema validation as exercises. Later choose one model provider or local model, one retrieval implementation, one evaluation framework, and one tracing tool.

Start with DeepEval or Promptfoo rather than adopting several frameworks at once. Add Ragas when studying RAG metrics and Phoenix when studying traces. These are learning choices, not mandatory dependencies.

## Definition of completion

A module is complete when its exercise works, you have inspected failures, its review questions make sense to you, and you link evidence in PROGRESS.md. Reading alone is insufficient. No scores, elapsed hours, or certifications substitute for explaining your decisions.
