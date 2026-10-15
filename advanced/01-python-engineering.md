# Module 01 — Python engineering for AI systems

> Optional technical reference. The current beginner lesson is [here](../modules/01-python-engineering.md). All twelve beginner lessons have a written path; use this note when you are ready for implementation.

[Course home](../README.md) · [Technical-note index](README.md) · Prerequisite: basic programming or additional practice time

**Terms to know:** [API](../GLOSSARY.md#api) · [Adapter](../GLOSSARY.md#adapter) · [Schema](../GLOSSARY.md#schema) · [Type hint](../GLOSSARY.md#type-hint) · [Runtime validation](../GLOSSARY.md#runtime-validation) · [JSONL](../GLOSSARY.md#jsonl) · [Exception](../GLOSSARY.md#exception)

## Outcomes

Build a small data-processing application with clear interfaces, explicit validation, useful errors, and meaningful tests. Transfer your automation experience into reusable application code.

## Lesson 1: Boundaries make systems testable

Separate four responsibilities: loading input, validating records, invoking a model adapter, and recording results. If all four live in one function, a provider timeout becomes difficult to distinguish from malformed data. A model adapter lets your tests supply stored responses without network access.

Define your first boundary as a Python function accepting a list of messages and returning a typed result. Keep provider-specific response parsing inside the adapter. Your application should not depend on a vendor's full response object.

Use type hints to describe intent, then validate external data at runtime: type hints alone do not reject a string where an integer was expected. JSON parsing only establishes syntactic validity. It does not establish that required fields exist.

## Lesson 2: Data and error handling

JSONL stores one JSON object per line. It is convenient for datasets because one record can be appended or inspected independently. Give each case a stable ID; line numbers change when cases are reordered.

Distinguish invalid input, application errors, and infrastructure errors. A retry may help a temporary timeout, but repeating a permanently invalid request wastes time. Set timeouts, bound retry counts, and record the original failure. In asynchronous code, bound concurrency to avoid resource exhaustion or rate-limit storms.

Do not silently skip a bad record. Either reject the run or emit an explicit invalid-record result. Your report's denominator must remain understandable.

## Worked example

A record contains `{"id": "B-1", "description": ""}`. Parsing succeeds, but the empty description violates your input contract. Reject it before inference. A record with a real description followed by a model timeout is valid input with an execution error. Those events should have different statuses.

## Detailed tutorial: Python from an automation engineer's perspective

### 1. Trace the data, then choose the abstraction

Imagine an automation suite that receives a bug report, submits it to an AI classifier, and records a component label. There are three different contracts: the report must be usable, the classifier must return a valid result, and the returned label must be correct. The first two can be checked using code. The third needs a reference policy or reviewed label.

Use a dictionary at the JSON boundary because JSON naturally represents named fields. Convert validated input into a small data object so the rest of the program can rely on established invariants. A list preserves a sequence of records. A dictionary indexed by stable ID supports comparing two runs. A set is useful for allowed enum values or duplicate detection.

In Python, assignment binds a name to an object; it does not copy the object. If two variables refer to one list and you append through either variable, both observe the change. This matters when a grader mutates a shared prediction and a later grader sees modified input. Prefer treating case records as immutable during a run. A frozen dataclass prevents assigning its fields; nested mutable objects still require care.

### 2. Functions, classes, and interfaces

A function should expose an intention such as parse_bug or classify rather than perform unrelated work hidden behind a generic name. Return a result when the caller needs to make a decision; printing alone makes the result awkward to test or aggregate. Use exceptions for failures that the caller must handle explicitly.

A dataclass generates boilerplate initialization and representation for a record. It does not validate arbitrary values automatically. A type hint such as description: str helps people and static tools; passing an integer can still succeed unless runtime code checks it.

The adapter in the example below is a callable: a function-like object that receives text and returns a prediction dictionary. Passing it as an argument is dependency injection. A test supplies a fake adapter; a later application supplies a hosted-model adapter. You do not need an inheritance hierarchy to gain that separation.

### 3. A complete runnable example

Save and run the linked script, or copy this complete block into a Python file. It uses no third-party packages. The fake classifier is a keyword baseline, not an LLM.

```python
"""Module 01: runtime validation and an injectable fake classifier."""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Bug:
    id: str
    description: str


def parse_bug(record: dict) -> Bug:
    if not isinstance(record, dict):
        raise ValueError("Bug record must be an object")
    values = {}
    for name in ("id", "description"):
        value = record.get(name)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be nonempty text")
        values[name] = value.strip()
    return Bug(**values)


def classify(bug: Bug, adapter: Callable[[str], dict]) -> dict:
    try:
        prediction = adapter(bug.description)
    except TimeoutError:
        return {"id": bug.id, "status": "application_error", "label": None}
    label = prediction.get("label") if isinstance(prediction, dict) else None
    if not isinstance(label, str) or label not in {"authentication", "payments", "other"}:
        return {"id": bug.id, "status": "invalid_output", "label": None}
    return {"id": bug.id, "status": "ok", "label": prediction["label"]}


def fake_model(text: str) -> dict:
    return {"label": "authentication" if "login" in text.lower() else "other"}


def unavailable_model(text: str) -> dict:
    raise TimeoutError("simulated provider timeout")


bug = parse_bug({"id": "B-1", "description": "Login is unavailable"})
assert classify(bug, fake_model)["label"] == "authentication"
assert classify(bug, unavailable_model)["status"] == "application_error"
assert classify(bug, lambda text: {"label": "invented"})["status"] == "invalid_output"
assert classify(bug, lambda text: {"label": []})["status"] == "invalid_output"
try:
    parse_bug({"id": "B-2", "description": " "})
except ValueError:
    print("Blank descriptions are rejected before model execution.")
else:
    raise AssertionError("Expected invalid input to be rejected")
print(classify(bug, fake_model))
```

Expected behavior: the program first reports that blank descriptions were rejected, then prints a successful authentication classification. Its assertions also check timeout handling and unsupported labels. Run [the saved example](../labs/module-examples/01_example.py) with:

~~~sh
python3 labs/module-examples/01_example.py
~~~

The parse function strips surrounding whitespace before creating Bug. classify calls an injected dependency and translates a known timeout into a recorded status. It does not catch every Exception; an unexpected programming error should remain visible rather than becoming a misleading normal result. Schema failure is recorded separately from execution failure.

### 4. Read JSONL without losing evidence

Use a context manager when opening a file so it closes even when processing raises an exception. Specify UTF-8. Enumerate lines starting at one to include useful locations in validation errors. Parse each line, validate it, and check IDs before invoking the model.

Decide whether blank lines are allowed and document the choice. Do not use an unrestricted “except: continue”; it changes the denominator by dropping difficult records. For a batch run, either fail before execution when the dataset is invalid, or include explicit invalid-input records in a separately reported count.

Write reports to a different path from the inputs. Recording input hashes helps establish which bytes produced a report. It does not establish that the labels were correct.

### 5. Timeouts, retries, and concurrency

A timeout limits how long one operation can occupy resources. A retry repeats selected failures. A total deadline limits the whole task, including retries. Without a total deadline, three individually reasonable timeouts can create an unacceptable user wait.

Only retry when repetition is appropriate. A malformed request usually needs correction. A timed-out read may be retried within a budget. A timed-out write may already have succeeded; it needs idempotency or state inspection before repetition. We build that control in Module 09.

Concurrency improves throughput when many requests wait on external work, but unrestricted concurrency can exceed service limits. A semaphore can bound outstanding requests. Asynchronous Python does not make CPU-heavy processing automatically parallel. Learn concurrency after the sequential pipeline is correct so timing does not hide basic failures.

### 6. Guided modification and solution reasoning

Change the fake adapter to return a list instead of a dictionary. The program should produce invalid_output. If it crashes while calling .get, the type check was removed or placed too late. Change the input description to an integer; parse_bug should reject it before the adapter is called.

Next, create an adapter that always returns authentication. The interface tests will pass on authentication input, but classification quality will fail on payments reports. This shows why contract tests and behavioral evaluation must remain separate.

Add a test asserting that the original report dictionary stays unchanged. Then add a duplicate ID to a JSONL file and explain whether rejection happens before any model requests. Your evidence should establish the actual boundary, not just that some exception occurred.

### 7. Common debugging patterns

| Symptom | Likely issue | First check |
|---|---|---|
| Works manually but fails in a suite | Shared mutable state or configuration | Compare inputs before/after each call |
| Every error becomes “other” | Overly broad exception handling | Preserve execution and validation statuses |
| Type hint exists but bad data passes | No runtime validation | Exercise external input boundaries |
| Intermittent duplicate records | Retries or repeated writes | Inspect operation IDs and stored state |

For Python-specific details, read the official [Python tutorial](https://docs.python.org/3/tutorial/), especially data structures, exceptions, classes, and modules. This lesson's code and examples are independently written.

## Lab

1. Run the [offline lab](../labs/offline-evaluation/README.md) and read its loader.
2. Build a separate bug-report loader accepting ID, description, and component.
3. Reject duplicate IDs, blank descriptions, and unsupported components.
4. Add a fake classifier with success, timeout, and malformed-output modes.
5. Write results without overwriting the source data.
6. Add tests for the meaningful boundary conditions above.
7. Document how to reproduce the run from a clean checkout.

Stretch: replace hand-written validation with a schema library, keeping the observable behavior unchanged.

## Review and answers

- **Why inject a model adapter?** To test application behavior independently of network access and provider implementations.
- **Does a type hint validate JSON?** No. Validate untrusted input at runtime.
- **Should every failure be retried?** No. Retry selected transient errors with limits; surface permanent errors.
- **Why stable IDs?** To compare results across ordering changes and preserve provenance.

## Exit evidence

Submit the loader, tests, a sample result file, and a short explanation of one failure you reproduced. You should be able to explain every assertion.

## Supplementary reading and attribution

The [Microsoft course](https://github.com/microsoft/generative-ai-for-beginners) provides application examples. Use its setup and text-application material after practicing the independent boundaries above. See [source register](../ATTRIBUTIONS.md).
