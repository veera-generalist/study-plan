# Module 01 — Python engineering for AI systems

[Course index](../README.md) · Weeks 1–2 · Prerequisite: basic programming or additional practice time

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
