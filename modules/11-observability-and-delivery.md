# Module 11 — Observability, CI, and production feedback

[Course index](../README.md) · Weeks 21–22 · Prerequisites: Modules 05–10

## Outcomes

Diagnose a failure from traces, create evaluation tiers, and write an evidence-backed release recommendation.

## Lesson 1: Observe enough to explain a result

A trace records an execution, and spans describe component operations such as retrieval, model inference, or tool execution. Capture IDs, relationships, versions, timings, errors, and enough input/output evidence to debug within your data-handling requirements.

At minimum, link a result to application commit, case ID, dataset version, prompt version, model identifier, supported generation settings, retrieved document versions, tool calls, and grader versions. Observability makes behavior visible; evaluation interprets it against requirements.

Replay can mean regrading stored outputs or executing the application again. Name which operation you performed. Re-execution can encounter changed external services or model behavior.

## Lesson 2: Layer your checks

| Tier | Typical content | Decision |
|---|---|---|
| Pull request | Unit/contract checks and a small critical behavior set | Whether the change is ready for broader evaluation |
| Scheduled | Larger slices, repeated trials, comparative experiments | Whether drift or regressions need investigation |
| Release | Held-out evidence, state checks, security review, operational results | Whether to deploy, canary, revise, or hold |

Choose thresholds from risk, product needs, baseline behavior, and measurement reliability. Illustrative educational thresholds are not universal industry standards.

A grading-service outage should not generate a false green release. Decide when to fail closed, rerun, or request manual review; report the reason explicitly.

## Lesson 3: Operational metrics and feedback

Measure p50/p95 latency, timeouts, error rates, resource use, and cost per successful task. Define what “successful” means. A cheap failed response is not an economical completed task. Add evaluation expenses separately from application inference cost.

Production feedback is noisy. Users may not report defects, and feedback may contain sensitive information. Review and sanitize sampled failures before adding them to a versioned dataset. Monitor input distribution changes as well as scores.

Deploy changes gradually when appropriate and define rollback signals in advance.

## Lab

Instrument your QA assistant with a tracing tool. Introduce a retrieval defect and a tool timeout, then diagnose each from evidence. Configure a fast check and a broader scheduled evaluation in your project. Store reports without credentials or private data.

Write a release report using [the template](../templates/evaluation-report.md). Include one blocked measurement or unresolved risk rather than inventing complete certainty.

## Review and answers

- **Is a trace itself a quality score?** No; it records behavior.
- **Why version graders?** A grading change can shift scores without application changes.
- **Should an unavailable judge pass the build?** Follow an explicit policy; never silently report missing measurement as success.
- **Why cost per successful task?** It reflects useful outcomes rather than calls alone.

## Exit evidence

A trace-backed diagnosis, documented CI tiers, reproducibility metadata, and a concrete release recommendation.

## Supplementary reading and attribution

Use [Phoenix](https://github.com/Arize-ai/phoenix) for tracing and experiments, and [Made With ML](https://github.com/GokuMohandas/Made-With-ML) for broader production practices.
