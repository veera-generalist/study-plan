# Optional bridge: call a real local model

Use this optional coding lab when you understand the introductory lessons and are ready to work with Python and a local model service. It demonstrates constructing a request, validating the actual response, and preserving the evidence. The earlier stored-output Python comparison is now an [optional technical note](../../advanced/03-prompting-and-development.md); the main Lesson 03 does not require this setup.

## What is and is not verified

The Python adapter and seven simulated-response tests are included. A real model was **not** downloaded or run during course validation. Model quality, runtime, hardware suitability, and structured-output support must be checked on your chosen setup. Passing the tests validates adapter behavior, not model accuracy.

## 1. Prepare one local model

Follow the official [Ollama quickstart](https://docs.ollama.com/quickstart). Choose an actually downloaded local model suitable for your hardware; do not select a cloud-routed model for this local exercise. Model tags change, so this course does not hard-code one.

Use `ollama list` to find your installed model name. If none is installed, follow the current quickstart's download instructions. Start the local Ollama application/service. This course does not install or start it automatically.

The adapter calls `http://127.0.0.1:11434/api/chat`. It uses a non-streaming request and a JSON schema, as described by the [official chat API](https://docs.ollama.com/api/chat). If you use a different provider, implement its own adapter rather than changing only the URL.

## 2. Check the adapter without a model

From the repository root:

```sh
python3 -m unittest discover -s labs/live-model -p 'test_*.py' -v
```

These tests simulate the HTTP service. They make no network requests.

## 3. Make one real request

Replace YOUR_INSTALLED_LOCAL_MODEL with the exact name from `ollama list`:

```sh
python3 labs/live-model/classify.py --model YOUR_INSTALLED_LOCAL_MODEL --text "Users cannot sign in after the deployment."
```

The command makes one request, with a 60-second socket timeout and a requested generation limit. The timeout is not a strict total deadline over all socket activity; the model may also stop before producing valid output. No retry is hidden in this adapter.

Results are written to the ignored `labs/live-model/reports/response.json`. Use only synthetic/public input. The report includes the raw response, requested/returned model identifiers where available, prompt version, status, prediction when valid, and elapsed time. Rename reports or pass a new `--report` path when comparing runs.

## 4. Interpret the result

| Status | Meaning | Next action |
|---|---|---|
| ok | The response completed and satisfied the local output contract | Review whether the label and explanation are actually correct |
| invalid_output | The service replied but its response/prediction did not satisfy the contract | Inspect raw_response; investigate truncation, model support, or format |
| application_error | The request could not complete successfully | Check service availability, model installation, or timeout |

Exit 0 means a structurally valid prediction, **not** proven correctness. Exit 1 means an application/output failure. Exit 2 means invalid local input/configuration or a report-write failure.

The label vocabulary is component classification: authentication, payments, or other. It is separate from [technical note 03's severity-decision example](../../advanced/03-prompting-and-development.md).

## 5. Turn inference into evaluation

Write ten reviewed reports with component reference labels before running inference. Keep those labels outside the request. Run each case once with a unique report path, join predictions by a stable case ID in your own runner, and distinguish invalid outputs from wrong-but-valid labels. Then compute per-class precision/recall and inspect every error.

Compare a second prompt only on development cases. Freeze the chosen candidate before assessing held-out cases. Record Ollama version, model identity/digest from your local tooling, prompt version, case IDs, raw responses, and run settings. The adapter's returned model name alone is not a complete reproducibility record.

## Attribution

This adapter and its fixtures are original code. The linked Ollama documentation is the API reference; no upstream example source is bundled. See [ATTRIBUTIONS.md](../../ATTRIBUTIONS.md).
