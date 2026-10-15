# How to work through the course

## Understand the three levels of material

1. **Runnable lesson examples:** twelve small offline programs with controlled synthetic inputs. They teach one concept at a time and verify local behavior. They are not measurements of a real model.
2. **Guided lab assignments:** work you implement using the lessons. Some need a live local or hosted model, suitable hardware or service access, and reviewed labels.
3. **Portfolio projects:** larger deliverables that combine modules. Their code and results must be produced and documented; a project brief is not a finished application.

The [optional live-model bridge](labs/live-model/README.md) gives you an actual request/response adapter after Module 03. Its unit tests use simulated responses. Live execution still needs your chosen local model environment.

## Keep the examples' contracts separate

| Example | Prediction being evaluated | What its score means |
|---|---|---|
| Modules 01–02 | Component or urgent/not-urgent classification | Quality under the example's defined labels |
| Module 03 | Simplified high/low/clarify/review severity decisions | Correctness against that example's impact policy |
| Offline evaluation lab | Stored decision, label, and source-ID contract | Whether all configured exact checks pass |
| Live-model bridge | Component plus evidence explanation | Status ok establishes structure, not semantic correctness |
| Modules 07–08 | Retrieved passages and evidence-based answers | Retrieval and answer measures must be interpreted separately |
| Modules 09–10 | Tool outcomes and sandbox state | Whether actions satisfy required constraints |

These are teaching examples with different schemas, not one interchangeable dataset. In your project, version your own schema and normalize adapters explicitly. Do not feed severity labels to a component grader or compare scores with different definitions.

## Begin with a small reviewed set

Start with 5–10 cases you can inspect completely. Make the pipeline correct, explain each expected result, and preserve raw evidence. Then scale toward the suggested 30/50/60/100-case assignments as time and review capacity allow. These counts are practice targets, not statistically justified minimums or reliability guarantees.

Use development cases for iterative changes. Freeze the chosen candidate before final held-out assessment. If you inspect held-out failures and use them to make changes, document that those cases have entered development and reserve new independent evidence for a later final assessment.

## A workable solo-review path

Two independent competent reviewers provide evidence a solo learner cannot reproduce just by reading the same answer twice. If a second reviewer is unavailable, do a delayed second pass with shuffled cases and predictions hidden where possible. Keep original decisions and disagreement notes.

Call this **solo review**, not independent inter-reviewer agreement. A second model judge is not a replacement for validated human reference labels. Ambiguous or consequential cases can remain unresolved until expert review is available; record that limit in the project report.

## What to produce at each stage

| Stage | Small first artifact | Before claiming the larger milestone |
|---|---|---|
| Modules 01–03 | Offline example plus a reviewed handful of reports | A valid adapter, explicit policy, and a controlled prompt comparison |
| Modules 04–06 | Dataset card, rubric, and reviewed sample | Clean splits, label provenance, judge error analysis |
| Modules 07–08 | Small corpus and inspected retrieval results | Separate retrieval/answer evaluation and a paired experiment |
| Modules 09–10 | Sandbox tools and state assertions | Bounded execution, permission controls, recovery and adversarial cases |
| Modules 11–12 | A trace-backed failure and release report | Measured project outcomes, operational evidence, and independent assessment |

## Prerequisites and pacing

If functions, dictionaries, exceptions, or command-line execution are unfamiliar, spend extra time on Module 01 and its glossary terms. If the code works but you cannot explain its checks, repeat the example with changed inputs before moving on.

The 24-week schedule is an estimate. The suggested weekly allocation totals ten hours; at eight hours, reduce optional reading or extend the calendar. Do not mark a live-model or project milestone complete solely because the offline example passed.

If you lack model access, complete the offline concept path and mark live/project evidence as pending in [PROGRESS.md](PROGRESS.md). There is no need to fabricate measurements to keep pace.

## Out of scope for the core path

This is an introduction to building and evaluating text-based AI applications and agents. It is not a complete deep-learning training program, GPU/inference optimization course, cloud-platform deployment guide, or comprehensive multimodal evaluation course. Fine-tuning, MCP, large model benchmarks, and production framework integrations are study extensions; the course introduces their role without bundling complete production implementations.

For interviews, state which components you actually built and ran. Distinguish controlled fixtures, simulated service tests, and live model measurements in every portfolio result.
