# Module 06 — LLM judges and human evaluation

[Course index](../README.md) · Weeks 11–12 · Prerequisites: Modules 04–05

## Outcomes

Design anchored rubrics and validate automated grading against independently reviewed examples.

## Lesson 1: Turn vague quality into observable criteria

“Good answer: 1–5” leaves too much interpretation. Start with distinct criteria such as factual support, completeness, and correct handling of missing evidence. Define the evidence needed to pass and representative failures.

An original groundedness rubric:

- Pass: every material factual claim is supported by the supplied evidence.
- Fail: at least one material claim is contradicted or unsupported.
- Unscorable: required evidence is unavailable to the grader.

Completeness is a separate criterion. An answer can be fully supported but omit half the request. Decide how to handle trivial versus material claims before labeling.

## Lesson 2: Judge inputs and vulnerabilities

A pointwise judge scores one output; a pairwise judge compares two. Pairwise evaluation can be easier for nuanced preferences but may suffer from order effects. Randomize or swap positions and inspect inconsistent decisions.

A judge can favor verbosity, familiar phrasing, or outputs resembling its own style. Evaluated text may contain instructions trying to influence its grade. Treat that text as untrusted data and test this boundary.

Require structured decisions and short evidence references. Explanations help audit decisions but do not prove the judge reasoned correctly. Never treat a model's self-reported confidence as validated calibration.

## Lesson 3: Validate the measurement

Have two reviewers independently label a sample, then adjudicate differences. Preserve their initial decisions. Use these examples to improve a rubric, then test the revised judge on a separate set.

If “fail” is the positive class, a false negative is a genuine defect that the judge passes. For release protection this may be more costly than a false alarm. Report failure-detection precision and recall, raw counts, and performance on important slices. Agreement statistics can be useful, but no single number resolves a bad rubric.

Calibration concerns whether predicted probabilities correspond to empirical frequencies. A binary judge without probability estimates can still be validated for accuracy and failure detection; do not call that probability calibration automatically.

## Lab

Collect 60 outputs with mixed quality. Independently label a subset twice, adjudicate, and record examples of disagreement. Run one judge and produce its confusion matrix against the reviewed labels. Inspect every false pass. Revise the rubric using development examples and measure on fresh reviewed outputs.

If you do not have model access, practice with a second person's judgments and analyze the same measurement problems.

## Review and answers

- **Does a detailed judge explanation establish correctness?** No; compare decisions with evidence and reviewed labels.
- **Why separate groundedness and completeness?** They describe different properties.
- **What does a false pass mean?** The grader accepted a genuine failure under the reference labeling.
- **Can you tune and validate on the same labels?** You can develop there, but need separate evidence to estimate generalization.

## Exit evidence

A versioned rubric, annotation history, judge comparison, examples of judge errors, and a decision about where human review remains necessary.

## Supplementary reading and attribution

Inspect evaluation recipes in [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) and the grader categories in [Anthropic's agent evaluation article](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). These exercises are original.
