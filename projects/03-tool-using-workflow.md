# Project 03 — Tool-using QA workflow

## Problem

An assistant gathers bug information, finds relevant guidance, drafts a ticket, and saves it after explicit approval in a synthetic local environment.

## Tools and controls

Provide search_documents, get_bug, and save_draft interfaces. Define schemas, permissions, side effects, failure conditions, and operation IDs. Enforce authorization outside the model. Approval must correspond to the actual draft being saved.

## Build sequence

1. Implement an explicit workflow baseline.
2. Add schema checks and sandbox storage.
3. Enforce approval, step limits, and idempotency.
4. Inject tool timeouts and interrupted execution.
5. Optionally allow model-driven selection of read tools.
6. Compare task outcomes and operating cost.

## Acceptance evidence

- State diagram and tool contracts.
- Initial/final sandbox snapshots per case.
- Assertions for content, duplicate records, and unauthorized effects.
- Denied approval, changed-after-approval, timeout, and retry cases.
- Repeated-trial results with clear success definitions.
- At least one reviewed adversarial-content case.
- Outcome checks that do not rely solely on the final message.

## Stretch

Add persisted recovery. Simulate a completed write whose response was lost and prove that recovery avoids a second write.
