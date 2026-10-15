# Course validation

Validation date: **2026-10-15**. Runtime actually exercised: **Python 3.14.8** on the local macOS environment. Compatibility with earlier supported releases is a target, not a tested version matrix.

## One-command offline verification

From the repository root:

```sh
python3 scripts/validate.py
```

This command downloads nothing and makes no model/service calls. It checks:

- Local Markdown file links and heading fragments, including glossary navigation.
- Beginner lesson sections in Modules 01–03 and the existing technical sections in Modules 04–12.
- Agreement between saved technical scripts and their displayed code: examples 01–03 now live in the optional advanced notes; 04–12 remain in the later draft modules.
- Execution of all twelve examples with assertions enabled.
- **28 unit tests:** 15 evaluator tests, 6 navigation/verification tests, and 7 optional-adapter simulated-response tests.
- Python syntax compilation.
- Expected evaluator outcomes: 6/8 stored predictions pass; the strict threshold returns 1 and the 0.75 demonstration threshold returns 0.

The validator itself returns 0 only when those expected outcomes are satisfied. Running the strict evaluator alone still returns 1 by design.

## Individual checks

```sh
python3 scripts/check_course.py
python3 scripts/run_module_examples.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 -m unittest discover -s labs/offline-evaluation -p 'test_*.py' -v
python3 -m unittest discover -s labs/live-model -p 'test_*.py' -v
python3 -m compileall -q scripts labs
```

Do not run lesson verification with Python optimization enabled; the verification runner rejects disabled assertions.

## Reference checks

The [reference snapshot register](references/README.md) records thirteen core repository revisions and direct license-file paths. Repository metadata also confirmed the historical Anthropic courses archive and Hugging Face Evaluate's current status; its README points readers toward LightEval for newer LLM evaluations.

Primary documentation destinations were retrieved during review as described in that register. This manual source review is separate from the offline validator.

## Scope and limitations

The first three lessons have been rewritten for beginners. Their written assignments and knowledge checks do not require Python. Verification of the optional code is repository maintenance, not a prerequisite for a learner. The earlier technical review predates this teaching rewrite; later Modules 04–12 have not been rewritten.

The Markdown checker supports the inline-link and ATX-heading syntax used in this repository. It is not a complete Markdown parser and does not check external website fragments.

Upstream examples, framework installations, a real Ollama model, paid inference, and full portfolio implementations were **not** executed. The live adapter's tests simulate HTTP responses; they establish request/parsing/error behavior, not model accuracy. The fixture scores are controlled examples, not production quality estimates.

Detailed findings and resolutions are in [REVIEW.md](REVIEW.md).
