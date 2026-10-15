# Runnable lesson examples

These are optional technical examples. The current beginner Modules 01–03 do not require Python: their earlier code-heavy explanations are preserved in [advanced notes](../../advanced/README.md). Examples 04–12 remain in the later technical draft modules. The matching scripts in this directory use only the Python standard library. They make no network calls, require no credentials, and use original synthetic data.

## Run

From the repository root:

```sh
python3 scripts/run_module_examples.py
```

Or run one script:

```sh
python3 labs/module-examples/07_example.py
```

The runner checks that the displayed Python block in each technical source matches its saved script, then executes the examples with their assertions. Expected behavior:

| Module | Example | What its assertions establish |
|---|---|---|
| 01 | Validation and fake adapter | Blank input is rejected; timeout and invalid output remain distinct |
| 02 | Numeric foundations | Softmax normalization, temperature concentration, cosine and classification counts |
| 03 | Prompt comparison | Candidate wins and losses remain visible alongside aggregate improvement |
| 04 | Dataset grouping | No source family appears in both development and held-out splits |
| 05 | Run statuses | Confirmed-pass rate, judged-pass rate, and coverage use explicit denominators |
| 06 | Judge validation | False passes are identified and pairwise positions map to candidate identities |
| 07 | Retrieval baseline | Scope/version filtering precedes lexical ranking |
| 08 | Statistical comparison | Paired sampling preserves differences; perfect observed performance still has uncertainty |
| 09 | Sandbox writes | Retry is idempotent and modified content requires fresh approval |
| 10 | Agent checks | Actual state can contradict success text; query text cannot change trusted scope |
| 11 | Trace and release gate | Task duration differs from child totals; critical failures block the example gate |
| 12 | Optimization | Mandatory constraints precede quality/cost/latency comparisons |

## What these examples do not establish

They demonstrate engineering and evaluation concepts on controlled data. They do not measure a live LLM, prove resistance to all prompt injection, establish a production quality threshold, or implement a durable concurrent ticket service. Each lesson explains its example's limits and how to extend it.

Use the original module's lab assignment to build the fuller application. Live-model exercises should follow the chosen provider/framework's current documentation and record configuration, usage, and data-handling behavior.
