# Offline evaluation lab

A small, original, standard-library lab for understanding deterministic grading, complete coverage, explicit errors, and slice reports. It uses eight synthetic cases and stored predictions. It makes no model calls and is not a RAG/LLM quality benchmark.

## Run

From the repository root:

```sh
python3 labs/offline-evaluation/evaluate.py
python3 -m unittest discover -s labs/offline-evaluation -p 'test_*.py' -v
```

The default evaluation intentionally includes two failed cases and exits **1**. This is the expected demonstration, not a broken installation. Inspect `labs/offline-evaluation/reports/report.json`.

To exercise successful run behavior using a threshold of 0.75:

```sh
python3 labs/offline-evaluation/evaluate.py --min-pass-rate 0.75
```

The threshold is an educational CLI option, not a recommended production release criterion. Invalid datasets, missing/extra predictions, or invalid configuration exit **2**. File/JSON errors also exit 2 with an explanation.

## Data contract

Cases require id, expected_decision (answer or abstain), expected_label (text or explicit null), allowed_source_ids, citation_required, and slice. Even an abstention case must include expected_label: null; omitting the field is invalid data. Predictions specify the case ID, decision, label, and source IDs.

A case passes only when all of its checks pass. IDs and schemas are checked before grading. The report includes all cases, failed check names, slice rates, input-file hashes, and the runner version.

## Deliberate failures

- C-04: the expected action is abstention, but the prediction answers.
- C-07: the prediction cites a source outside the allowed set.

There are six passes and two failures: 0.75 overall. These numbers describe fixed fixtures only. They are not evidence of a real model's performance.

## What this lab cannot measure

It cannot determine whether a source actually supports prose, evaluate answer helpfulness, or estimate live model variability. A known source ID is not proof of groundedness. Expected labels are used by the evaluator, never as an input to a model.

## Exercises

1. Trace C-04 through validation, grading, and reporting.
2. Add one valid case and its prediction; inspect the new denominator.
3. Introduce a duplicate ID and confirm exit 2.
4. Remove a prediction and confirm complete-coverage validation.
5. Add a separate semantic criterion in a new project and document how its grader is validated.
6. Compare two prediction files by case ID and explain wins/losses.

All files in this lab are original examples. Source reading and reuse guidance are in [ATTRIBUTIONS.md](../../ATTRIBUTIONS.md).
