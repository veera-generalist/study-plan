# Module 08 — RAG evaluation and statistical reasoning

[Course index](../README.md) · Weeks 15–16 · Prerequisites: Modules 04–07

## Outcomes

Separate retrieval from answer quality and compare configurations without overstating a small score difference.

## Lesson 1: Define the measurement unit

For document-level judgments, Recall@k is the fraction of known relevant documents retrieved among the first k results. Precision@k is the fraction of the evaluated top-k results judged relevant; specify treatment when fewer than k results are returned. Reciprocal rank is 1/rank of the first relevant result, or zero if none is found; MRR averages this across queries.

These metrics depend on relevance labels. Incomplete labels can penalize genuinely useful results. Claim-based, LLM-scored context recall is a different operational definition from document Recall@k; name exactly which you use.

Answer faithfulness assesses support from retrieved context. Correctness assesses the task's requirements and reference evidence. A faithful answer can repeat an outdated document. A correct guess can lack supporting evidence. Citation validity and citation support are also distinct.

## Lesson 2: Compare the same cases

Run A and B on identical cases and preserve case-level differences. In a 100-case experiment, A passes 82 and B passes 85. B might fix eight cases and break five, including a critical one. The aggregate difference is insufficient for a release decision.

Use a paired bootstrap to estimate uncertainty in a mean difference: sample case IDs with replacement, keep each sampled case's A/B outcomes paired, compute the difference, and repeat. State the sampling unit and interval method. If many questions come from one document, a document-level or clustered analysis may better reflect dependence.

Repeated trials on the same question are not independent new questions. Separate task variation from execution variation. A fixed seed makes an analysis reproducible, not a model perfectly deterministic.

## Lesson 3: Interpret the result honestly

Confidence intervals express uncertainty under assumptions about sampling and measurement. They do not correct mislabeled cases, judge bias, or unrepresentative datasets. Define practical significance and risk thresholds before comparing many versions. Repeatedly selecting the best result from numerous experiments can overfit the evaluation.

Report sample sizes for slices. Zero observed critical failures is useful evidence but does not prove a zero underlying failure rate.

## Lab

Compare two retrieval strategies on your held-out questions. Report document recall, answer correctness, abstention behavior, latency, and per-case wins/losses. Implement a paired bootstrap with a recorded seed. Inspect failures before selecting a configuration.

Write one paragraph distinguishing observed improvement from what you can infer about future production traffic.

## Review and answers

- **Is a three-point gain automatically reliable?** No; inspect uncertainty, sampling, measurement, and practical impact.
- **Does faithfulness establish current factual correctness?** No; the retrieved evidence may be outdated or wrong.
- **Why pair cases in a bootstrap?** To preserve the relationship between A and B on the same task.
- **Can bootstrap fix biased labels?** No; measurement quality must be addressed separately.

## Exit evidence

A paired report with definitions, counts, uncertainty assumptions, critical regressions, and a justified decision.

## Supplementary reading and attribution

See Ragas documentation for [context recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) and [faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/). Framework metric names are not interchangeable definitions.
