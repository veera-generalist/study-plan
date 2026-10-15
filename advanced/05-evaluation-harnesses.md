# Module 05 — Metrics, graders, and evaluation harnesses

> Optional technical reference. The beginner lesson is [here](../modules/05-evaluation-harnesses.md). Return to this material when you want the deeper implementation detail.

[Course index](../README.md) · Weeks 9–10 · Prerequisite: Module 04

**Terms to know:** [Evaluation harness](../GLOSSARY.md#evaluation-harness) · [Grader](../GLOSSARY.md#grader) · [Deterministic grader](../GLOSSARY.md#deterministic-grader) · [Semantic grader](../GLOSSARY.md#semantic-grader) · [Coverage](../GLOSSARY.md#coverage) · [Metric](../GLOSSARY.md#metric)

## Outcomes

Run reproducible evaluations that preserve raw evidence and distinguish model failures from invalid measurements.

## Lesson 1: Choose a grader for each requirement

A deterministic grader checks a precisely defined condition: schema validity, an exact label, a numeric tolerance, a known identifier, or a database state. A semantic grader assesses meaning: whether evidence supports a claim or whether a response addresses the question.

Use each where appropriate. Substring checks are cheap but fragile: “the threshold is not five” contains “five.” Embedding similarity can reward a topically related contradiction. A model judge can interpret meaning but adds its own errors, cost, and variation.

Define whether each criterion is mandatory or advisory. A weighted average can hide a critical permission violation behind good formatting and helpful tone.

## Lesson 2: Execution and measurement are separate

A harness loads cases, invokes the application, records outputs, runs graders, and aggregates results. It also needs case IDs, versioned configuration, explicit error states, and an understandable denominator.

Keep at least these concepts distinct:

- Application returned an unacceptable answer.
- Application failed to execute.
- Grader could not produce a valid measurement.
- Dataset case is invalid.

Report unknown measurements explicitly. For example, 80 passes, 15 failures, and 5 grading errors is not an 80/95 success claim without qualification. You might report 80/100 confirmed passes and a separate 5% grading-error rate.

## Lesson 3: Reports should support decisions

Report by slice as well as overall. Save raw outputs and per-criterion results so a reviewer can challenge a score. Include application commit, prompt version, model settings, dataset hash, and grader version.

Repeat executions when variability matters. Identical stored responses are useful for testing the harness; they do not measure live model variability.

## Worked example

Two versions both pass 90% overall. Version B improves easy formatting cases but loses two high-risk abstention cases. Aggregate equality does not establish equivalent quality. Review the loss severity and intended operating context.

## Detailed tutorial: build a trustworthy measurement pipeline

### 1. Separate the system under test from the evaluator

An application receives a task and produces an output or side effect. The harness controls execution and records what happened. Graders interpret the evidence. Aggregation summarizes judgments. A defect in any layer can create a misleading quality claim.

Use a stored-output mode to debug graders without paying for another generation run. Use a live-execution mode to evaluate the application. Give each its own run metadata. Regrading a stored answer under a new rubric is not a new application trial.

For a model integration, save the actual normalized response and relevant provider metadata before grading. If your grader unexpectedly fails, the raw answer remains available for investigation.

### 2. Map every requirement to a measurement

A requirement like “return one of three severity labels” maps to a set-membership check. “Never create a ticket without approval” maps to approval/state evidence. “Answer using only supplied sources” maps to claim-support evaluation, not merely checking for bracketed numbers.

Write down each grader's input, output range, invalid-input behavior, and known blind spots. A substring check can pass “not five failures.” A similarity check can reward a contradiction. A model judge can miss an unsupported statement. There is no universal grader; combine suitable evidence.

Treat critical constraints as separate gates. A weighted average of helpfulness, formatting, and authorization could let perfect style compensate for an unauthorized write. That is the wrong aggregation for a mandatory constraint.

### 3. Design statuses before calculating averages

Choose explicit statuses such as pass, fail, application_error, grader_error, and invalid_case. The last often belongs in dataset validation before execution. An application timeout is evidence of task noncompletion. A grader timeout means the application result was not measured by that grader.

Different reports can present different useful denominators. The important part is to name them:

- Confirmed passes divided by all scheduled valid cases.
- Passes divided by successfully judged cases.
- Successfully judged cases divided by all scheduled valid cases.
- Application and grading error rates.

Do not call all of these “accuracy.” A candidate can appear better if a grader fails disproportionately on its hardest outputs.

### 4. Runnable reporting example

```python
"""Module 05: explicit statuses, denominators, and conservative gates."""
from collections import Counter

outcomes = [
    {"id": "1", "status": "pass"},
    {"id": "2", "status": "pass"},
    {"id": "3", "status": "fail"},
    {"id": "4", "status": "application_error"},
    {"id": "5", "status": "grader_error"},
]
ALLOWED = {"pass", "fail", "application_error", "grader_error"}


def summarize(rows):
    if not rows:
        raise ValueError("No evaluation outcomes")
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("Duplicate case IDs")
    if any(row["status"] not in ALLOWED for row in rows):
        raise ValueError("Unknown outcome status")
    counts = Counter(row["status"] for row in rows)
    judged = counts["pass"] + counts["fail"]
    total = len(rows)
    return {
        "total": total,
        "counts": dict(counts),
        "confirmed_pass_rate": counts["pass"] / total,
        "judged_pass_rate": counts["pass"] / judged if judged else None,
        "measurement_coverage": judged / total,
        "release_gate": counts["grader_error"] == 0
            and counts["application_error"] == 0
            and counts["pass"] == total,
    }


report = summarize(outcomes)
assert report["confirmed_pass_rate"] == 0.4
assert report["measurement_coverage"] == 0.6
assert abs(report["judged_pass_rate"] - 2/3) < 1e-12
assert report["release_gate"] is False
print(report)
```

Run [the saved example](../labs/module-examples/05_example.py). It reports two confirmed passes among five cases: 40%. Among the three cases that received pass/fail judgments, two passed: about 66.7%. Measurement coverage is 60%. Neither rate alone describes the full run.

The demonstration uses a deliberately strict gate requiring all cases to pass and no errors. This is an educational policy, not a universal release standard. Your production gate must reflect risk, task criticality, and measurement reliability.

### 5. Understand aggregation from first principles

Suppose slice A has 90 cases and slice B has 10. Averaging their two pass rates gives them equal weight. Pooling all cases gives A nine times the influence. Either can be appropriate for a declared purpose, but they answer different questions.

Keep both overall counts and slice counts. For overlapping tags, a case may contribute to several slice summaries. Do not add those summaries to reconstruct total cases.

For multi-criterion results, decide whether passing requires all mandatory criteria, an allowed score range, or reviewed exceptions. Record criterion-level scores so a reviewer can see why a case failed.

### 6. Walk through the included evaluator

Open the existing offline evaluator and follow this path: read_jsonl, validate_case, evaluate, grade, summarize slices, then write the report. Notice that duplicate IDs and coverage mismatches are rejected before aggregation. A prediction cannot disappear silently.

The fixture's source check only establishes that IDs are allowed. It does not determine whether a document supports prose. Preserve that limitation when describing the lab in a portfolio. An impressive-looking number measured against a weak contract remains weak evidence.

### 7. Guided experiment and solution reasoning

Make the grader unavailable for a known failing case. A naive script that drops grading errors may improve its reported judged-case pass rate. The correct interpretation is reduced measurement coverage, not improved application behavior.

Next, add a new perfectly passing routine case. The overall rate increases, but the missing-evidence slice does not improve. This demonstrates why dataset composition changes must be recorded when comparing runs.

Finally, store a per-case criterion dictionary and write a table of failed criterion names. A useful error report should let you jump directly to the evidence, not only display a single red percentage.

### 8. Framework adoption after the contract is clear

When you adopt DeepEval or Promptfoo, map your concepts into the framework: test cases, metrics/assertions, configuration, runs, and reports. Do not assume a built-in metric shares your business definition because its name sounds right. Read its required inputs and implementation or documentation.

Keep deterministic unit tests for the harness itself. An evaluation system can regress: a denominator bug, ID join error, or unhandled judge result can approve a broken application.

Use the current [DeepEval repository](https://github.com/confident-ai/deepeval) and [Promptfoo repository](https://github.com/promptfoo/promptfoo) for integration study. The report logic above is original and independent of those frameworks.

## Lab

Run the [offline evaluator](../labs/offline-evaluation/README.md), read every case result, and compare it with the stored predictions. It deliberately contains failures and therefore exits with a nonzero status by default. Its report is an educational contract check, not a semantic LLM benchmark.

Extend it with a new slice or a numeric constraint. Then use the [optional local-model adapter](../labs/live-model/README.md) as a starting point for a separate live adapter in your project. Its component-label schema differs from the stored evaluator fixture; normalize records explicitly rather than treating them as interchangeable. Ensure an API error cannot be turned into a pass. Use the [report template](../templates/evaluation-report.md).

## Review and answers

- **Why store raw outputs?** To audit scores and regrade without another model call.
- **Why report grader errors separately?** Missing measurement is different from known application behavior.
- **Should all criteria be averaged?** No; mandatory safety or correctness requirements can require individual gates.
- **Is repeated grading of stored output a live-model stability test?** No; it evaluates the grader or harness, not repeated generation.

## Exit evidence

A reproducible run, per-case and slice results, explicit error policy, and an explained failing case.

## Supplementary reading and attribution

Study [DeepEval](https://github.com/confident-ai/deepeval) for Python evaluation workflows and [Promptfoo](https://github.com/promptfoo/promptfoo) for configured comparisons. No framework source is copied into the included lab.
