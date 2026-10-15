# Module 08 — RAG evaluation and statistical reasoning

[Course index](../README.md) · Weeks 15–16 · Prerequisites: Modules 04–07

**Terms to know:** [Recall at k](../GLOSSARY.md#recall-at-k) · [MRR](../GLOSSARY.md#mrr) · [Paired comparison](../GLOSSARY.md#paired-comparison) · [Bootstrap](../GLOSSARY.md#bootstrap) · [Confidence interval](../GLOSSARY.md#confidence-interval)

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

## Detailed tutorial: from scores to defensible conclusions

### 1. Work a retrieval example by hand

Suppose the relevant documents are D2 and D4. A retriever returns D1, D2, D3 in its first three results. Recall@3 is 1/2: one of two relevant documents was found. Precision@3 is 1/3: one of the three returned documents is relevant. The first relevant document is at rank two, so reciprocal rank is 1/2.

If a second query's first relevant document appears at rank one, the MRR across these two queries is (0.5 + 1)/2 = 0.75. Document what happens when no relevant document is retrieved: reciprocal rank is zero.

If labels omit another genuinely relevant passage, your metric can unfairly penalize retrieval. Relevance judgments and their completeness are part of the measurement, not a neutral background detail.

### 2. Grade claims rather than citation decoration

An answer says, “Roll back after five consecutive failures, and notify Finance within two hours.” The retrieved policy supports the threshold but says nothing about Finance. Split the response into material claims. One is supported, one is not.

A claim-support proportion would be one supported claim out of two under this simplified decomposition. A strict groundedness gate might fail the entire answer because any unsupported material claim is unacceptable. These are different aggregation rules over similar evidence.

A model-based faithfulness metric also depends on how it extracts claims and judges support. It can make mistakes at either step. Read the exact [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) before comparing its scores with another implementation.

### 3. Understand what your sample represents

An observed pass rate is a statistic over evaluated units. To infer future performance, you need assumptions about how those units relate to the target workload. A confidence interval over hand-picked examples does not make them representative.

Repeated executions of one question explore execution variation. Different questions explore task variation. Ten runs of one easy question are not equivalent to ten independent user tasks. If your data contains related questions from the same document or customer, consider grouping that dependence in sampling and analysis.

### 4. Paired comparisons preserve information

If A and B answer the same questions, examine case-level differences. A candidate can gain two tasks and lose one, giving a net gain of one. Knowing the lost task's risk can change the decision.

The paired bootstrap samples task differences with replacement. Each sampled difference retains the A/B pairing. Sampling A and B separately discards that relationship and estimates a different uncertainty structure.

A percentile interval is a useful teaching tool, not a guarantee that all small-sample statistical issues disappear. Small or dependent datasets can make intervals unstable. State the method, seed, repetition count, and sampling unit.

### 5. Runnable statistical example

```python
"""Module 08: paired bootstrap and a Wilson interval on synthetic outcomes."""
import random
from math import sqrt
from statistics import mean

# Same eight tasks, evaluated under two configurations.
baseline = [1, 1, 1, 1, 0, 0, 0, 0]
candidate = [1, 1, 1, 0, 1, 1, 0, 0]


def paired_bootstrap(a, b, repetitions=2000, seed=7):
    if len(a) != len(b) or not a:
        raise ValueError("Need nonempty paired samples")
    rng = random.Random(seed)
    differences = [right - left for left, right in zip(a, b)]
    estimates = sorted(
        mean(rng.choice(differences) for _ in differences)
        for _ in range(repetitions)
    )
    return mean(differences), (
        estimates[int(0.025 * repetitions)],
        estimates[int(0.975 * repetitions) - 1],
    )


def wilson(successes, total, z=1.96):
    if total <= 0 or not 0 <= successes <= total:
        raise ValueError("Invalid binomial counts")
    p = successes / total
    denominator = 1 + z*z / total
    center = (p + z*z / (2*total)) / denominator
    half = z * sqrt(p*(1-p)/total + z*z/(4*total*total)) / denominator
    return center - half, center + half


difference, interval = paired_bootstrap(baseline, candidate)
assert difference == 0.125
assert interval[0] <= difference <= interval[1]
assert interval[0] <= 0 <= interval[1]
lower, upper = wilson(8, 8)
assert lower < 1.0 and abs(upper - 1.0) < 1e-12
print("Observed candidate-minus-baseline:", difference)
print("Illustrative paired percentile interval:", interval)
print("Wilson interval for 8/8 passes:", (round(lower, 3), round(upper, 3)))
```

Run [the saved example](../labs/module-examples/08_example.py). The candidate improves from four to five passes among eight tasks: an observed increase of 0.125. The interval includes zero, illustrating substantial uncertainty in this tiny synthetic sample.

The Wilson interval for eight passes out of eight has a lower bound below one. Observing no failures does not establish perfect reliability. This interval assumes an appropriate binomial sampling interpretation; it does not validate your dataset or judge.

The random seed makes the analysis repeatable. It does not make model generation deterministic.

### 6. Practical significance and release decisions

A statistically clear small gain can be operationally irrelevant. A modest overall gain can also conceal a severe regression in an important slice. Decide in advance what improvement would matter and which constraints cannot be traded away.

For example, you might accept a slower response if it substantially improves critical correctness, or reject a cheaper model because it fails approval checks. These decisions require task-specific requirements, not a universal numeric threshold.

When many candidate prompts are compared and only the best is reported, selection can overfit the dataset. Use development data for repeated search, then independent held-out evidence for the final candidate. Record how many alternatives were considered.

### 7. Latency and cost measurement

Report the measurement boundary: full user task, model call, retrieval operation, or grading step. p95 latency describes a percentile, but estimates from a handful of tasks are noisy. Keep errors and timeouts visible; dropping them makes latency look better.

Calculate cost per successful task as total application execution cost divided by completed successful tasks, under your stated definition. If no tasks succeed, the ratio is undefined; report that directly. Keep evaluation-model costs separate from production application cost.

### 8. Guided exercise and answer reasoning

Swap one candidate success for a failure on a critical case while fixing an easy case. The total score stays unchanged. The release decision can still change because the failure consequences differ. Explain that explicitly rather than trying to force all risk into one average.

Next, repeat each row ten times and compute an interval as though all rows were independent. It may become narrower, but you have not collected new independent task information. Describe why clustered or task-level treatment is more appropriate.

For an answer-quality report, include raw counts, slice definitions, grader limitations, a paired result table, and a recommendation. The reader should see what was observed separately from what you infer.

Python's [statistics documentation](https://docs.python.org/3/library/statistics.html) is a reference for the standard-library functions used here; the interval implementation and exercise are original.

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
