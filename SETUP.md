# Setup

## Offline starting point

Install Git and a supported Python 3 release (3.11 or newer is suitable for the included lab). No API key is required.

```sh
git clone https://github.com/veera-generalist/study-plan.git
cd study-plan
python3 --version
python3 labs/offline-evaluation/evaluate.py
python3 -m unittest discover -s labs/offline-evaluation -p 'test_*.py' -v
python3 scripts/check_course.py
```

The evaluator writes a report under the lab's ignored reports directory. Its default run uses stored synthetic predictions, so it makes no network requests.

## Environment for later exercises

Create an isolated environment before adding optional packages:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Choose dependencies from the current instructions of the framework being studied; record installed versions in your project. The main course does not impose one combined environment across all frameworks.

## Model access

Hosted model calls and model-based grading may incur charges. Start with a small, explicit run budget, a few cases, bounded concurrency, and recorded usage. Local models avoid hosted inference charges but have hardware and runtime requirements. Choose based on your available machine rather than assuming a GPU.

Keep credentials in environment variables or an ignored local configuration file. Use public or synthetic data for your public portfolio. Understand any selected tool's tracing, telemetry, and hosted-storage behavior before sending data.

## Reproducibility record

For every external lab, record Python and package versions, application commit, dataset version, prompt version, model identifier, supported generation settings, grader version, execution time, and run budget. Hosted model identifiers may not guarantee permanent behavior.

## If an example fails

Check the exact error, the upstream README, release notes, and your installed versions. Avoid copying obsolete SDK calls from old notebooks. Record the fix and its cause in your learning log. Distinguish environment failures from application failures.
