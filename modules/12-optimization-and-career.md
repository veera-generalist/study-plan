# Module 12 — Optimization, capstone, and career evidence

[Course index](../README.md) · Weeks 23–24 · Prerequisites: Modules 01–11

**Terms to know:** [Baseline](../GLOSSARY.md#baseline) · [Overfitting](../GLOSSARY.md#overfitting) · [Tradeoff frontier](../GLOSSARY.md#tradeoff-frontier) · [Fine-tuning](../GLOSSARY.md#fine-tuning) · [Practical significance](../GLOSSARY.md#practical-significance) · [Cost per successful task](../GLOSSARY.md#cost-per-successful-task)

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

## Detailed tutorial: optimize with evidence and present your judgment

### 1. Diagnose before choosing a technique

A wrong answer can result from unavailable evidence, failed parsing, poor retrieval, unclear instructions, model limitations, tool errors, or a faulty grader. Each calls for a different intervention.

If the authoritative document was never ingested, fine-tuning is not the first fix. If retrieval consistently misses exact error codes, lexical or hybrid search may help. If the model has evidence but omits required facts, improve instructions, examples, or model choice and measure the result. If the judge is wrong, fix the measurement before optimizing the application against it.

Write a hypothesis linking the intervention to an observed failure. “Add a reranker because relevant passages are present in the candidate set but ranked too low” is testable. “Use the latest framework” does not identify a cause.

### 2. Control the experiment

Preserve the baseline configuration. State the one major change, development dataset, metrics, critical constraints, operational budget, and expected practical benefit. Use development data for iteration and reserve independent evidence for the chosen candidate.

If a change combines a new prompt and new model, you can evaluate the whole package, but attributing improvement to one component requires additional comparisons. Make that limitation clear.

Record unsuccessful experiments too. They explain what did not help and reduce repeated work. A portfolio containing only wins can conceal weak experimental discipline.

### 3. Optimization techniques and prerequisites

Prompt optimization searches instructions or examples against a metric. It requires a meaningful metric and protected evaluation data. Retrieval tuning changes parsing, chunking, ranking, filtering, or reranking. It requires relevance evidence and component diagnostics.

Fine-tuning updates parameters. It needs suitable, permitted training data, an independently evaluated baseline, and a plan for overfitting and deployment. It may help stable task behavior, but it does not turn model memory into an always-current authorized database.

Caching and batching improve operating efficiency under the right conditions. A cache must respect content version, prompt/model configuration, user scope, and task-specific validity. An invalid cache can be fast and inexpensive while returning the wrong or unauthorized answer.

### 4. Multi-objective decisions

Quality, cost, and latency are often in tension. One configuration dominates another when it is no worse in all considered objectives and strictly better in at least one. Non-dominated candidates form a tradeoff frontier.

First apply mandatory constraints such as no known approval bypasses. Then compare eligible candidates. A frontier does not select the deployment automatically; operating requirements and uncertainty still matter.

### 5. Runnable tradeoff example

```python
"""Module 12: choose among synthetic measured tradeoffs without one magic score."""
candidates = [
    {"name": "baseline", "quality": 0.90, "cost": 0.02, "latency_ms": 600,
     "critical_failures": 0},
    {"name": "larger-model", "quality": 0.95, "cost": 0.08, "latency_ms": 1000,
     "critical_failures": 0},
    {"name": "retrieval-fix", "quality": 0.93, "cost": 0.02, "latency_ms": 650,
     "critical_failures": 0},
    {"name": "bad-cache", "quality": 0.94, "cost": 0.01, "latency_ms": 200,
     "critical_failures": 1},
    {"name": "slower-copy", "quality": 0.90, "cost": 0.03, "latency_ms": 800,
     "critical_failures": 0},
]


def dominates(left, right):
    no_worse = (
        left["quality"] >= right["quality"]
        and left["cost"] <= right["cost"]
        and left["latency_ms"] <= right["latency_ms"]
    )
    strictly_better = (
        left["quality"] > right["quality"]
        or left["cost"] < right["cost"]
        or left["latency_ms"] < right["latency_ms"]
    )
    return no_worse and strictly_better


eligible = [row for row in candidates if row["critical_failures"] == 0]
frontier = [
    row for row in eligible
    if not any(dominates(other, row) for other in eligible)
]
names = {row["name"] for row in frontier}
assert names == {"baseline", "larger-model", "retrieval-fix"}
assert "bad-cache" not in names
print("Eligible tradeoff frontier:", sorted(names))
print("Choose from it using operating requirements and independent evidence.")
```

Run [the saved example](../labs/module-examples/12_example.py). The unsafe cache is excluded by a critical constraint. The slower copy is dominated. Baseline, larger model, and retrieval fix remain because each has some tradeoff.

All numbers are synthetic demonstration inputs. The code does not estimate uncertainty, validate grader quality, or prove practical significance. In a real experiment, close quality differences may not justify treating one point as clearly superior.

### 6. Resist metric gaming

If a grader rewards citations without checking support, optimization may teach the system to add irrelevant citations. If it rewards answer length, outputs can become verbose. If it ignores abstention, a system can appear accurate by refusing difficult tasks.

Add counterexamples and independent review where proxy weaknesses matter. Track coverage, critical failures, and user-task completion. Do not keep adding ad hoc rules solely to preserve a flattering score; revise the evaluation design when it no longer matches the intended behavior.

Automated optimization with a framework such as DSPy increases the value of clean splits. Repeated search can discover ways to score well on development data that do not generalize.

### 7. Build the capstone as an evidence narrative

Your capstone should answer five questions: What problem mattered? What did the baseline do? Which failures did you find? What change addressed a cause? What evidence supports the final recommendation?

A useful demonstration walks through one successful case and one informative failure. Show the source passage, model output, tool state, and grader result. Explain what is known and what remains uncertain. Avoid claiming production readiness because a small synthetic set passes.

Use the release-report template, dataset card, labeling guide, experiment record, and trace evidence. Reproducibility means another person can follow the setup and understand the artifacts, even if an external model later changes.

### 8. Position your experience honestly

Your existing seniority in QA gives you practice in risk, architecture review, triage, test strategy, and stakeholder decisions. Add concrete AI evidence rather than presenting yourself as a beginner in all engineering.

A factual project statement might say: “Implemented a synthetic release-policy assistant, separated retrieval and generation metrics, identified a version-filtering defect, and compared a fix on held-out questions.” Add counts and improvements only from stored runs.

Distinguish course projects from production deployment experience. For engineering roles, emphasize the application and controls you built. For evaluation roles, emphasize dataset design, grader validation, failure taxonomy, uncertainty, and decision quality.

### 9. Guided presentation and answer reasoning

Prepare a five-minute demo and a ten-minute design review. Expect questions about why you chose a dataset, how you validated a judge, what could invalidate the score, and how you would monitor the system after release.

If asked why a candidate with the highest score was rejected, show the critical constraint or the cost/latency requirement. If asked whether the model is reliable, answer within the measured task, dataset, and operating conditions rather than making a general claim.

Finish by naming the next experiment you would run and why. That demonstrates an evidence-based development process, not merely completion of a tutorial.

Study [DSPy](https://github.com/stanfordnlp/dspy) for optimization and [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) for a distinct model-benchmarking route. This tradeoff example is original.

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
