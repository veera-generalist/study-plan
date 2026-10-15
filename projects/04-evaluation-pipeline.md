# Project 04 — Evaluation and release pipeline

## Problem

Changes to prompts, models, retrieval, or tool behavior can regress quality. Build a pipeline that produces inspectable evidence for release decisions.

## Build sequence

1. Package the runner so cases, predictions, graders, and configuration are separate.
2. Preserve raw results and reproducibility metadata.
3. Define fast, scheduled, and release evaluation tiers.
4. Add a comparison report with slice-level wins/losses.
5. Instrument retrieval and tools for diagnosis.
6. Document grading-error and infrastructure-error policies.
7. Produce a release recommendation from a real project run.

## Acceptance evidence

- One-command offline checks and documented live-run setup.
- Versioned datasets, prompts, graders, and configuration.
- Explicit outcomes for invalid data and unavailable graders.
- Latency/error/cost results with clear denominators.
- Held-out evaluation with uncertainty assumptions.
- Links to reviewed critical failures and traces.
- No fabricated performance claims or credentials in artifacts.

## Stretch

Create a deliberate regression and demonstrate that the appropriate tier catches it. Test the failure of the evaluation infrastructure itself so a broken judge cannot silently approve a release.
