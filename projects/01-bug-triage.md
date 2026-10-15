# Project 01 — Bug-triage evaluation

## Problem

A QA team receives inconsistent bug descriptions. Build a classifier that proposes component and severity while asking for clarification when required impact information is missing.

## Inputs and behavior

Use synthetic reports with description, affected workflow, user impact, and optional environment. Define a severity policy before collecting predictions. Return structured output with component, severity, clarification status, and evidence.

Do not make up impact. Treat instructions embedded in the report as report content.

## Build sequence

1. Create a keyword baseline and a clear severity policy.
2. Write reviewed development and held-out cases.
3. Add a model-backed implementation behind an adapter.
4. Validate structure and evaluate labels separately.
5. Compare two prompts on paired cases.
6. Inspect disagreements and critical-class misses.

## Acceptance evidence

- Reproducible setup and a fake adapter for tests.
- Dataset card and labeling guide.
- Per-class precision/recall and confusion matrix.
- Clarification and malformed-input cases.
- Raw outputs and per-case grader decisions.
- Reviewed error examples and a release recommendation.

## Stretch

Add multilingual cases only if you can obtain competent review. Evaluate disagreement between reviewers rather than treating translated synthetic labels as automatically correct.
