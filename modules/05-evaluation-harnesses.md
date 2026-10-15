# Module 05 — Metrics, graders, and evaluation harnesses

[Course index](../README.md) · Weeks 9–10 · Prerequisite: Module 04

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

## Lab

Run the [offline evaluator](../labs/offline-evaluation/README.md), read every case result, and compare it with the stored predictions. It deliberately contains failures and therefore exits with a nonzero status by default. Its report is an educational contract check, not a semantic LLM benchmark.

Extend it with a new slice or a numeric constraint. Then build a separate live-model adapter in your project. Ensure an API error cannot be turned into a pass. Use the [report template](../templates/evaluation-report.md).

## Review and answers

- **Why store raw outputs?** To audit scores and regrade without another model call.
- **Why report grader errors separately?** Missing measurement is different from known application behavior.
- **Should all criteria be averaged?** No; mandatory safety or correctness requirements can require individual gates.
- **Is repeated grading of stored output a live-model stability test?** No; it evaluates the grader or harness, not repeated generation.

## Exit evidence

A reproducible run, per-case and slice results, explicit error policy, and an explained failing case.

## Supplementary reading and attribution

Study [DeepEval](https://github.com/confident-ai/deepeval) for Python evaluation workflows and [Promptfoo](https://github.com/promptfoo/promptfoo) for configured comparisons. No framework source is copied into the included lab.
