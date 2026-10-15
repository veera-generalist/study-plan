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

## Detailed tutorial: connect experiments to operations

### 1. A useful trace answers a concrete question

When a user reports a wrong rollback threshold, you need to reconstruct what the application knew and did. Which corpus version was searched? Which passages were returned? What input was sent to the model? Did a tool timeout? Which grader scored the response?

A trace links operations within one execution. Spans represent individual operations and can have parent/child relationships. Use a common trace ID to correlate retrieval, model calls, and tools. Add stable task/run IDs so traces connect to evaluation cases and reports.

Instrumentation should be useful without unnecessarily exposing data. Record identifiers and redacted or access-controlled payloads according to the system's needs. Do not automatically export private source text to a hosted tracing service.

### 2. Durations and the critical path

Full task latency is measured at the task boundary. Adding child-span durations does not always reproduce it. There may be application overhead, gaps, retries, or parallel work. Parallel operations can have overlapping durations whose sum exceeds wall-clock task time.

Report p50 and p95 over the intended unit: complete tasks, individual model calls, or tool requests. Mixing units produces confusing dashboards. Timeouts belong in operational reports even when a percentile calculation excludes incomplete durations by policy; explain that exclusion.

### 3. Runnable trace and gate example

```python
"""Module 11: inspect a trace and apply a declared release policy."""
trace = [
    {"trace_id": "T1", "span_id": "S1", "parent_id": None,
     "name": "task", "start_ms": 0, "end_ms": 140, "status": "ok"},
    {"trace_id": "T1", "span_id": "S2", "parent_id": "S1",
     "name": "retrieve", "start_ms": 5, "end_ms": 25, "status": "ok"},
    {"trace_id": "T1", "span_id": "S3", "parent_id": "S1",
     "name": "generate", "start_ms": 30, "end_ms": 135, "status": "ok"},
]
root = next(span for span in trace if span["parent_id"] is None)
task_latency = root["end_ms"] - root["start_ms"]
child_duration_sum = sum(
    span["end_ms"] - span["start_ms"]
    for span in trace if span["parent_id"] is not None
)
assert task_latency == 140
assert child_duration_sum == 125  # Child spans do not cover all task overhead.

baseline = {"quality": 0.90, "critical_failures": 0,
            "grader_errors": 0, "p95_ms": 1000}
candidate = {"quality": 0.93, "critical_failures": 1,
             "grader_errors": 0, "p95_ms": 950}


def release_gate(reference, proposed):
    # Illustrative declared policy, not a universal threshold.
    return (
        proposed["quality"] >= reference["quality"]
        and proposed["critical_failures"] == 0
        and proposed["grader_errors"] == 0
        and proposed["p95_ms"] <= 1200
    )


assert not release_gate(baseline, candidate)
print("Task latency:", task_latency, "sum of child spans:", child_duration_sum)
print("Release gate:", release_gate(baseline, candidate))
```

Run [the saved example](../labs/module-examples/11_example.py). The task takes 140 ms, while its child operations total 125 ms. The missing 15 ms represents overhead/gaps in this synthetic timeline.

The candidate improves quality from 0.90 to 0.93 and has lower p95 latency, but it fails the declared release gate because one critical failure occurred. These fixture numbers are illustrative, not measured application results. The example shows how a mandatory constraint differs from an averaged quality score.

The simplified dictionaries omit sample sizes and uncertainty. A real release report must include those; the gate alone is not the complete decision record.

### 4. Design evaluation tiers for feedback time

Pull-request checks should give fast, actionable feedback. Run unit and contract tests plus a small set of important behavioral cases. Keep their cost and variability understood so developers investigate meaningful failures rather than ignore noise.

Scheduled evaluations can run larger datasets, more slices, repeated trials, and broader security cases. Release evaluations add held-out evidence, critical state checks, expert review, operational metrics, and a deployment recommendation.

Do not place every expensive model-based evaluation on every tiny edit. Conversely, do not call a small smoke set comprehensive release evidence. State the purpose and limitations of each tier.

### 5. Failures of the evaluation service need a policy

Suppose the judge API is unavailable during a release. The application may be healthy, but the required quality evidence is missing. Your pipeline should say “measurement unavailable” rather than green.

For a consequential release, the policy may hold until a rerun or approved manual review. For an exploratory experiment, it may save outputs and postpone grading. The right policy depends on the decision. In all cases, preserve the reason and avoid silently changing denominators.

Test the pipeline's own failure paths: missing files, duplicate IDs, malformed judge output, partial provider failures, and upload failures. The system making the release recommendation is also software.

### 6. Cost and quality in production

Track inference requests, retrieval/reranking resources, tool usage, and failed/retried work. Compare cost per successful task under an explicit success definition. A low-cost response that leaves the task incomplete may be more expensive after retries and human correction.

Keep evaluation expenses separate. A complex judge can cost more than generating the candidate answer, which may affect how often you run it. Sampling and targeted grading can help, but record what coverage you give up.

Cache carefully. If your cache key omits prompt, model, document version, or access scope, it can return stale or unauthorized content. Correct cache boundaries are part of AI application testing.

### 7. Production feedback does not label itself

Thumbs-up/down feedback is useful but incomplete. Some users do not respond, some reward persuasive wrong answers, and some failures occur without visible feedback. Reviewed incident samples, task outcomes, and targeted human annotation can add evidence.

Before adding production records to a public or shared evaluation set, review permissions, sensitive content, and representativeness. Preserve a provenance note and label revision history. A production failure becomes a regression case only after intended behavior is established.

Monitor workload changes as well as score changes. A new product version or user population can shift input distribution beyond what your old dataset represents.

### 8. Guided release exercise

Introduce a retrieval metadata bug and trace one failed case. Identify whether parsing, filtering, ranking, or generation first diverged from the requirement. Record the evidence supporting that diagnosis.

Then create a release report with a candidate that improves average correctness but breaks denied-approval behavior. The reasoned answer is to hold or revise under a policy making approval mandatory. Include the actual failing case rather than only stating “security risk.”

Define canary monitoring and rollback signals before deployment. A canary reduces exposure while collecting new evidence; it does not excuse missing critical pre-release controls.

Read [OpenTelemetry's trace concepts](https://opentelemetry.io/docs/concepts/signals/traces/) and [Phoenix](https://github.com/Arize-ai/phoenix) for supplementary material. The timeline and gate implementation above are original.

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
