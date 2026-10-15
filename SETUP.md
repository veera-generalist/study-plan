# Setup

## For the first three lessons

No installation is required. Start with [Lesson 01](modules/01-python-engineering.md) and use a notebook or text document for the activities. An AI chat tool you already use is optional. The written examples let you begin without one.

The setup below is for later coding exercises and repository maintenance. You can skip it while working through the current three lessons.

<details>
<summary>Optional Python setup and later coding exercises</summary>

## Offline starting point

Install Git and a supported Python 3 release (3.11 or newer is suitable for the included lab). No API key is required.

Validation was performed on Python 3.14.8. Earlier compatible releases are a compatibility target, not a tested version matrix. On systems where the interpreter is named `python` or `py` instead of `python3`, use that command consistently and confirm its version. Python's `/3/` documentation follows its current release; select your interpreter's documentation version when needed.

```sh
git clone https://github.com/veera-generalist/study-plan.git
cd study-plan
python3 --version
python3 scripts/run_module_examples.py
python3 labs/offline-evaluation/evaluate.py --min-pass-rate 0.75
python3 -m unittest discover -s labs/offline-evaluation -p 'test_*.py' -v
python3 scripts/check_course.py
```

The module-example runner verifies the saved technical examples and their displayed code. Examples 01–03 are now in the optional advanced notes; examples 04–12 remain in the later draft modules. It should report twelve passing examples. The evaluator writes a report under the lab's ignored reports directory; the command above deliberately uses the fixture's 0.75 pass rate so setup exits successfully. That educational threshold is not a production quality recommendation. Neither command makes network requests.

After setup, run the strict gate separately:

```sh
python3 labs/offline-evaluation/evaluate.py
```

This command intentionally exits 1 because the stored fixtures contain two failures. That is expected; see the lab README. Run lesson verification without `-O` or `PYTHONOPTIMIZE`, because it executes assertion-based examples.

## Environment for later exercises

For the complete offline pre-push check, run `python3 scripts/validate.py`. It also runs the optional adapter's simulated tests without making model calls.

Create an isolated environment before adding optional packages:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Choose dependencies from the current instructions of the framework being studied; record installed versions in your project. The main course does not impose one combined environment across all frameworks.

## Model access

When you choose to begin coding, follow the [optional local-model lab](labs/live-model/README.md). Its unit tests work offline; actual inference requires a separately prepared model service.

Hosted model calls and model-based grading may incur charges. Start with a small, explicit run budget, a few cases, bounded concurrency, and recorded usage. Local models avoid hosted inference charges but have hardware and runtime requirements. Choose based on your available machine rather than assuming a GPU.

Keep credentials in environment variables or an ignored local configuration file. Use public or synthetic data for your public portfolio. Understand any selected tool's tracing, telemetry, and hosted-storage behavior before sending data.

## Reproducibility record

For every external lab, record Python and package versions, application commit, dataset version, prompt version, model identifier, supported generation settings, grader version, execution time, and run budget. Hosted model identifiers may not guarantee permanent behavior.

## If an example fails

Check the exact error, the upstream README, release notes, and your installed versions. Avoid copying obsolete SDK calls from old notebooks. Record the fix and its cause in your learning log. Distinguish environment failures from application failures.

</details>
