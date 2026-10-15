# Contributing to this study plan

Write for people learning AI for the first time. For Modules 01–03, use an introduction, learning objectives, a scenario, explained concepts, a worked example, guided practice, an assignment, a knowledge check with answer explanations, and further reading. Define unfamiliar words where they appear. Use examples that suit the idea; do not force comparisons to the learner's profession. Python code is optional at this introductory stage. Modules 04–12 retain their earlier technical structure until a later rewrite.

For an edit:

Explain new technical words when first introduced and add a plain-language glossary entry with a QA example. Keep each module's **Terms to know** links useful for someone new to AI.

1. Explain the learning problem or factual correction.
2. Update the lesson, example, and answer guidance together.
3. Run `python3 scripts/validate.py` for the full offline verification, including local file/heading links, examples, evaluator tests, and optional-adapter simulated tests.
4. Keep upstream source review separate: the offline validation does not check external URL availability or run an actual model.
5. Record new sources and any imported material in ATTRIBUTIONS.md.
6. Preserve honest limitations; do not invent experiment results or completion evidence.

Do not paste entire upstream courses into this repository. A link and attribution do not automatically permit redistribution. Follow the source-specific process in ATTRIBUTIONS.md.

Use synthetic or publicly reusable data. Include reproducible instructions for runnable examples. Keep credentials and generated reports out of commits.
