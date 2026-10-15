# Pre-push course review

Reviewed: **2026-10-15**. Scope: all twelve lesson/example pairs, glossary navigation, setup, roadmap, project briefs, templates, attribution records, executable checks, and primary reference destinations.

This review produced local fixes. It did not publish or push changes.

## Findings and resolutions

| Finding | Why it mattered | Resolution and evidence |
|---|---|---|
| Missing expected_label on an abstention case caused an uncaught KeyError | Contradicted the documented invalid-data exit behavior | Required fields validated before grading; CLI regression test checks exit 2 with no traceback |
| Direct evaluator calls could crash on non-object records | Validation behavior differed by entry point | Non-object records now receive an explicit ValueError; regression coverage added |
| Malformed JSON diagnostics omitted the dataset's actual line context | A beginner could investigate the wrong line | Loader adds source filename and JSONL line number; regression test added |
| Module 08 suggested inspecting held-out failures before selecting the candidate | Conflicted with the course's split discipline | Candidate selection now uses development data; final held-out assessment follows freezing |
| Severity example left known intermediate impacts outside its decision rules | A real model could be asked to choose from an incomplete policy | Added explicit review behavior; rich-schema example now includes evidence about workaround/core workflow |
| A repair instruction used stored_b[D] as though D were a variable | Copying it into Python would raise a NameError | Corrected to the quoted dictionary key stored_b["D"] |
| Beginner setup included an intentionally failing command in its main sequence | Could be mistaken for a failed installation or stop a script | Main sequence uses the fixture's 0.75 demonstration threshold; strict failing gate is explained separately |
| Link checking skipped heading fragments | Glossary links could silently break | Local fragment checks added with fenced-code and duplicate-heading tests |
| Example verification could run with assertions disabled | Could report success without executing its correctness assertions | Optimized Python execution is rejected; a regression test verifies this |
| Reference citations used generic license fragments and no captured revisions | Source review and later reuse were harder to audit | Thirteen repository snapshots and file-specific license links recorded |
| Archived/legacy setup paths needed clearer treatment | Learners could mistake old examples for current setup | Resource notes distinguish Anthropic archive, Ragas legacy APIs, Microsoft's retirement notice, and current docs |
| Offline examples had no concrete first live-inference adapter | The transition from fixtures to real responses was underspecified | Optional local Ollama adapter and guided lab added, with seven simulated-response tests |
| Solo review and independent reviewer agreement were blurred | A learner could overstate reference-label evidence | Course guide and Module 06 distinguish solo practice from independent review |
| Different mini-examples use different prediction schemas | Component, severity, and evidence checks could be combined incorrectly | Course guide maps contracts; live/offline labs explain normalization boundaries |
| Search-token splitting could be confused with model tokenization | Incorrect context/billing estimates could follow | Module 07 explicitly distinguishes its lexical search units from model tokens |
| Suggested hours and dataset sizes needed a beginner path | Could encourage rushing or claiming arbitrary sample counts prove reliability | Guide starts with 5–10 reviewed cases, explains scaling targets, and reconciles the ten-hour allocation |

## Source freshness

Fifteen existing repository metadata destinations were checked. Thirteen core repositories have captured revision/license paths in [references/repositories.json](references/repositories.json). Primary documentation destinations, including the optional lab's Ollama references, were retrievable during review.

The [reference notes](references/README.md) explain archive status, current versus legacy APIs, and source-specific licensing. Generic repository visibility is not used as a license conclusion. External docs can change after this date.

## Verification result

- All twelve displayed examples match their scripts and execute successfully.
- **28 unit tests passed:** evaluator 15, navigation/verification 6, local adapter 7.
- Local file links, glossary heading targets, and required lesson sections passed.
- Python compilation passed.
- The eight-case fixture still produces six passes and two deliberate failures.
- Both educational gate outcomes were checked through the offline validator.
- Whitespace/error checks on the Git diff passed.

Reproduce using `python3 scripts/validate.py`; see [VALIDATION.md](VALIDATION.md).

## Remaining limits and owner decisions

- No real model or upstream framework integration was executed. The optional adapter is unit-tested with simulated responses; a live smoke run and model-quality assessment remain learner work.
- The larger project briefs are assignments, not completed portfolio applications. Offline example success does not establish those milestones.
- Python 3.14.8 was exercised; the full range of suggested compatible interpreters was not tested.
- This repository still has no selected repository-wide redistribution license. Attributions document sources but do not choose terms for the owner's original material.
- The course is an applied text/agent engineering introduction. Deep model training, GPU serving, comprehensive multimodal evaluation, and full cloud deployment remain outside its core scope.

These limits are explicit in the setup, course guide, or attribution material. They do not invalidate the checked offline study path, but they constrain what can be claimed about the course and its examples.
