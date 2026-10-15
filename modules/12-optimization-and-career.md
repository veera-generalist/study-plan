# Module 12 — Optimization, capstone, and career evidence

[Course index](../README.md) · Weeks 23–24 · Prerequisites: Modules 01–11

## Outcomes

Improve one component with controlled evidence and present your engineering judgment clearly.

## Lesson 1: Optimize against trustworthy measurements

Build a baseline before optimizing. Candidate changes include a different prompt, model, retrieval strategy, reranker, cache, or workflow. Changing all of them at once makes causal interpretation difficult.

Optimize on development data. Keep held-out evidence independent of repeated selection. A larger model may improve difficult answers while increasing cost and latency; a smaller model may be sufficient for extraction. Compare task-specific outcomes rather than selecting by general reputation.

Fine-tuning changes weights and needs suitable examples, consent/provenance, and independent evaluation. Retrieval tuning is appropriate when evidence is missed. Prompt optimization is appropriate when instructions or examples are inadequate. Fix the diagnosed cause.

## Lesson 2: Avoid optimizing the proxy at the user's expense

A metric is a proxy for desired behavior. If it rewards length, the system can become verbose. If it rewards any citation, it can cite irrelevant sources. Add counterexamples and human review where these incentives matter.

Track quality, critical failures, latency, and cost together. Preserve configurations on the useful tradeoff frontier rather than declaring one winner without operating requirements.

Inspect [DSPy](https://github.com/stanfordnlp/dspy) after you can explain your metric and dataset. Automated optimization increases the importance of independent evaluation; it does not replace it.

## Lesson 3: Present a senior engineer's evidence

Your portfolio should show architectural reasoning, coverage choices, measurement limits, diagnosis, and release judgment. Keep claims factual. Say what the project demonstrates, how it was measured, and what remains unresolved.

An honest project description might be: “Built a synthetic QA-document assistant; evaluated retrieval and answer quality separately; found a version-selection failure; compared a metadata filter with the baseline on held-out questions.” Add numbers only from recorded runs.

Do not imply professional AI deployment experience solely from a course project. Combine your existing QA leadership experience with new, inspectable AI engineering artifacts.

## Lab — capstone

Choose one [project brief](../projects/README.md) or combine them. Freeze a baseline and evaluation plan. Improve one component, measure the result, inspect regressions, and write a release recommendation. Prepare a five-minute demonstration and a ten-minute technical walkthrough.

## Review and answers — interview practice

- **How do you test a nondeterministic system?** Separate deterministic software checks from repeated behavioral evaluation, define datasets and rubrics, and report uncertainty.
- **How do you diagnose a RAG failure?** Inspect source availability, parsing, retrieval, evidence selection, generation, and grading in order.
- **When do you trust a judge?** After validating it on independently reviewed examples for the intended criteria and slices, with known limits.
- **How do you choose a release gate?** Connect risk and product requirements to reliable measurements, critical constraints, and an explicit error policy.
- **What failed in your project?** Show a real case, its root cause, the attempted fix, and measured consequences.

## Exit evidence

A reproducible repository, dataset card, evaluated baseline, controlled experiment, reviewed failures, release report, and clear demonstration.

## Supplementary reading and attribution

For deeper model benchmarking, inspect [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). Model benchmark scores do not automatically establish quality for your application. For production context, revisit [Made With ML](https://github.com/GokuMohandas/Made-With-ML).
