# Module 10 — Agent evaluation and security

[Course index](../README.md) · Weeks 19–20 · Prerequisite: Module 09

## Outcomes

Evaluate task outcomes and execution constraints, and investigate adversarial failures in your own sandbox application.

## Lesson 1: Outcome and trajectory

The final answer is only one observable. Inspect selected tools, validated arguments, intermediate states, side effects, and final sandbox state. An agent may say “created one ticket” after creating two, or claim success after a failed write.

Outcome checks ask whether the task succeeded. Trajectory checks ask whether execution satisfied required constraints. Avoid prescribing one exact sequence unless the process itself is a requirement; different paths can be valid.

Reset sandbox state between cases. Ensure graders do not accidentally mutate it. Save initial and final snapshots so comparisons are auditable.

## Lesson 2: Repeated success

For a task evaluated across k attempts:

- pass@k asks whether at least one attempt succeeds.
- pass^k asks whether all k attempts succeed.

If independent attempts have success probability p, these probabilities are 1 − (1 − p)^k and p^k respectively. Independence is an assumption, often imperfect in real systems. Report empirical trial details and any estimator used. A workflow with human retries may value one measure differently from an unattended one-shot operation.

## Lesson 3: Security as application behavior

Direct injection comes from the request; indirect injection arrives through external content such as documents or tool output. Other important tests include unauthorized document access, data leakage, malformed arguments, approval bypass, duplicate writes, excessive resource use, and over-refusal of legitimate tasks.

Separate an observed vulnerability from an automated detector's suspicion. A scanner finding needs reproduction and interpretation. Security controls should be enforced by application/tool boundaries, supported by prompts and monitoring.

## Lab

In your own synthetic sandbox, create a document that instructs the assistant to reveal a fake secret and a tool response that requests an unauthorized action. Add cases for cross-user access, denied approval, repeated save requests, and valid benign requests.

Evaluate final state, access logs, task completion, and whether the model complied with malicious instructions. Review tool findings manually. Implement a control, add a regression case, and repeat the same assessment.

Do not run scans against systems outside your authorized project scope.

## Review and answers

- **Can a correct final message hide a defect?** Yes; actual state or actions may disagree.
- **Should all successful paths be identical?** No; require exact sequences only when necessary.
- **Does passing a scanner establish security?** No; coverage and detectors are limited.
- **Why test benign requests alongside attacks?** Controls can prevent valid tasks or cause excessive refusal.

## Exit evidence

A test matrix, state assertions, repeated-trial summary, one reproduced finding, and a verified remediation.

## Supplementary reading and attribution

Use [garak](https://github.com/NVIDIA/garak), [Promptfoo](https://github.com/promptfoo/promptfoo), and [Anthropic's agent evaluation article](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). The sandbox scenarios are original; no attack corpus is bundled.
