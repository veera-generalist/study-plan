# Initial edition validation

Validation date: 2026-10-15.

## Checks performed

- Python syntax compilation for the included scripts.
- Eleven unit tests for the offline evaluator: known outcomes, malformed output, missing/extra predictions, duplicate IDs, empty input, inconsistent cases, gate/report behavior, invalid thresholds, and protection against overwriting inputs.
- Relative Markdown file-link checks and required sections across all twelve modules.
- Default offline evaluation: six of eight stored predictions pass (75%); the strict default threshold intentionally returns exit 1.
- Threshold demonstration at 0.75: returns exit 0.

## Reproduce

```sh
python3 scripts/check_course.py
python3 -m unittest discover -s labs/offline-evaluation -p 'test_*.py' -v
python3 -m compileall -q scripts labs/offline-evaluation
python3 labs/offline-evaluation/evaluate.py
python3 labs/offline-evaluation/evaluate.py --min-pass-rate 0.75
```

The fourth command is deliberately a failing quality gate; see the lab README.

## Limits

The link checker validates relative file targets, not external URL availability or heading anchors. External sources were reviewed during research, but upstream examples and paid/live model calls were not executed. The lab evaluates stored synthetic contracts and does not establish real-model or production quality. Learner project implementations remain assignments.
