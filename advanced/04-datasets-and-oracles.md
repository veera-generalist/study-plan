# Module 04 — Evaluation datasets and test oracles

> Optional technical reference. The beginner lesson is [here](../modules/04-datasets-and-oracles.md). Return to this material when you want the deeper implementation detail.

[Course index](../README.md) · Weeks 7–8 · Prerequisites: Modules 01–03

**Terms to know:** [Dataset](../GLOSSARY.md#dataset) · [Oracle](../GLOSSARY.md#oracle) · [Label](../GLOSSARY.md#label) · [Annotation and adjudication](../GLOSSARY.md#annotation-and-adjudication) · [Held-out set](../GLOSSARY.md#held-out-set) · [Provenance and dataset card](../GLOSSARY.md#provenance-and-dataset-card)

## Outcomes

Create an evaluation dataset whose coverage, labels, provenance, and limitations you can defend.

## Lesson 1: Specify behavior rather than a magic sentence

A test oracle is the basis for deciding whether behavior is acceptable. For generated answers it may consist of required facts, forbidden claims, supporting evidence, executable constraints, and a review rubric. One reference answer rarely captures all valid phrasings.

For a question whose answer is absent from the available knowledge base, the expected behavior might be to state the limitation and request the missing document. A confident invented answer should fail even if it sounds helpful.

## Lesson 2: Coverage and provenance

Sample realistic tasks and supplement them with risk-based cases. Include ordinary requests, ambiguity, unavailable evidence, conflicting sources, tool failures, and adversarial inputs. A hand-balanced challenge set is useful for finding defects, but its overall score does not estimate production performance unless its sampling supports that interpretation.

Give each case a stable ID, source, slice, expected behavior, and review status. Keep source document versions. Synthetic cases need human review: generated questions can be unrealistic or leak their answers through wording.

A practical starting record is:

```json
{
  "id": "Q-017",
  "input": "What is the rollback threshold?",
  "expected_behavior": "abstain",
  "required_facts": [],
  "relevant_document_ids": [],
  "slice": "missing_evidence",
  "risk": "high",
  "source": "synthetic-human-reviewed"
}
```

This expectation is conditional on a corpus that contains no threshold. If the corpus changes, review the case rather than blindly preserving its label.

## Lesson 3: Split discipline and labeling

Use development cases for iterative improvements and a separately held-out set for evaluation. Split related documents or near-duplicate questions together when needed to prevent leakage. A random row split can leave nearly identical cases on both sides.

Have reviewers label independently before discussion. Disagreement may expose ambiguity in the policy, missing expertise, or unclear evidence. Preserve original labels and adjudication notes rather than replacing all disagreement with a single unexplained answer.

## Detailed tutorial: construct a dataset you can defend

### 1. Start with the decision the evaluation will support

“Evaluate the assistant” is underspecified. Decide whether the experiment selects a prompt, compares retrieval, checks a release constraint, or investigates failure modes. The evaluation unit might be one question, one conversation, or one complete tool task. Changing that unit changes how you count successes and failures.

For a QA knowledge assistant, define success as answering the question from authorized current documents, including material facts, citing supporting passages, and handling insufficient evidence appropriately. Now a case can encode those requirements rather than merely store a nice-looking answer.

Keep inference input separate from evaluator-only fields. The model gets the question and permitted context. The evaluator gets required facts, reference evidence, expected behavior, and constraints.

### 2. Write an oracle as a set of obligations

Suppose an approved policy says: rollback begins after five consecutive failures and must be approved by the release lead. A reference answer might say “Roll back after five consecutive failures, with release-lead approval.”

A robust oracle can record two required facts, an approved source version, and a prohibition on inventing an exception. “Five failures in a row, approved by the release lead” is an acceptable alternative phrasing. Exact string matching would reject it unnecessarily.

If a policy is absent, the expected outcome changes. Record the corpus version that makes abstention correct. A future corpus update can legitimately invalidate the old label. Dataset maintenance needs domain judgment, just as test maintenance does after a requirements change.

### 3. Sampling: discovery sets and estimation sets

A challenge set deliberately emphasizes edge cases. It is excellent for defect discovery. A representative sample reflects a target workload and supports a different kind of conclusion. Do not average a manually balanced adversarial set and call its score an estimate of everyday user satisfaction.

You can keep both sets and report them separately. Define slices before running when possible: ordinary questions, missing evidence, version conflicts, ambiguous requests, and unauthorized access. Allow overlapping tags when needed; a single case can be both high risk and multilingual. Slice totals then need not add up to the overall case count.

Start small enough to review all labels. More synthetic rows do not compensate for incorrect expected behavior or copied near duplicates.

### 4. Leakage occurs through relationships

Imagine splitting 100 paraphrases of one policy question randomly. Both development and evaluation sets now contain almost the same task. The model or prompt developer can learn the policy-specific pattern from development examples. The evaluation looks more independent than it is.

Group cases by the relationship that could leak: document family, incident, customer, template, or conversation. Keep each group in one split. This does not eliminate all leakage; it makes one important dependency explicit.

### 5. Runnable group-split example

```python
"""Module 04: group related evaluation cases without leakage."""
from hashlib import sha256

cases = [
    {"id": "A-1", "family": "policy-A", "slice": "routine"},
    {"id": "A-2", "family": "policy-A", "slice": "paraphrase"},
    {"id": "B-1", "family": "policy-B", "slice": "missing_evidence"},
    {"id": "C-1", "family": "policy-C", "slice": "routine"},
    {"id": "D-1", "family": "policy-D", "slice": "conflict"},
    {"id": "E-1", "family": "policy-E", "slice": "routine"},
    {"id": "F-1", "family": "policy-F", "slice": "ambiguous"},
]


def split_groups(records):
    groups = sorted(
        {record["family"] for record in records},
        key=lambda value: sha256(("course-split-v1:" + value).encode()).hexdigest(),
    )
    if len(groups) < 2:
        raise ValueError("Need at least two independent groups")
    held_out_groups = set(groups[:max(1, len(groups) // 3)])
    development = [r for r in records if r["family"] not in held_out_groups]
    held_out = [r for r in records if r["family"] in held_out_groups]
    return development, held_out


development, held_out = split_groups(cases)
development_groups = {r["family"] for r in development}
held_out_groups = {r["family"] for r in held_out}
assert not development_groups & held_out_groups
assert len(development) + len(held_out) == len(cases)
assert len({r["id"] for r in cases}) == len(cases)
print("Development IDs:", sorted(r["id"] for r in development))
print("Held-out IDs:", sorted(r["id"] for r in held_out))
print("No document family occurs in both splits.")
```

Run [the saved example](../labs/module-examples/04_example.py). The salted hash gives a reproducible ordering for this fixed set of families. Selecting some complete families prevents the two policy-A paraphrases from being split apart.

The example is a small demonstration. It does not ensure slice balance or representative sampling, and adding new groups can change membership because the selection quota changes. For a real dataset, persist assigned split IDs in a versioned manifest and review changes. Never silently reshuffle a held-out set on each run.

### 6. Build a labeling guide another reviewer can use

A labeling guide should state the evidence hierarchy, labels, decision rules, alternative valid responses, treatment of missing information, and how to flag ambiguity. Include a straightforward pass, a straightforward fail, and a boundary case with a reasoned answer.

Ask two people to label independently before discussion. If one reviewer sees an authoritative source the other did not, the problem may be the review interface. If both see the same evidence but interpret “material claim” differently, improve the rubric. Preserve initial labels, adjudicated labels, and reasons.

Do not resolve an ambiguous case solely because one model judge gives a confident answer. Expert adjudication should connect the expected behavior to requirements and evidence.

### 7. Guided dataset construction

Begin with ten questions you can answer manually from your corpus. For each, record the exact supporting passage and required facts. Add five genuinely unanswerable questions whose absence you verify. Add five questions where the wording leaves the desired version or workflow unclear.

Review the cases before any model run. Then identify groups, assign splits, and document counts. This sequence limits the temptation to relabel inconvenient failures after seeing predictions.

Use the dataset-card template to record intended use, provenance, review status, grouping, limitations, and dates. A public repository should not contain customer incidents merely because they are convenient examples.

### 8. Answer explanation for a disputed label

Question: “When do we roll back?” The corpus contains current policies for two products with different thresholds. A reference answer giving either threshold unconditionally is incomplete. Depending on product context, the desired behavior may be to ask which product or present both with explicit scope. The labeling guide must choose a policy and explain why.

If reviewers cannot agree on intended behavior, mark the case ambiguous rather than scoring the application against an arbitrary hidden rule. An explicit unresolved case is more useful than a fabricated ground truth.

Inspect dataset features in [Phoenix](https://github.com/Arize-ai/phoenix) after designing the underlying data contract. Tools store labels; they do not supply the missing judgment.

## Lab

Create 100 reviewed cases for the QA assistant. Define your own justified allocation across slices; do not claim that 100 cases proves reliability. Write a [dataset card](../templates/dataset-card.md) and [labeling guide](../templates/labeling-guidelines.md). Ask a second reviewer to label a subset, resolve disagreements, and identify near duplicates before splitting.

Keep reference labels out of the model's inference input. They belong to the evaluator.

## Review and answers

- **Is a reference answer always a complete oracle?** No; alternatives may satisfy the same requirements.
- **Can synthetic cases be used directly?** They should be reviewed for realism, correctness, and leakage.
- **What does repeated tuning on the test set do?** It reduces the independence of the performance estimate.
- **What does disagreement tell you?** It can identify policy or task ambiguity, not merely reviewer error.

## Exit evidence

Versioned cases, a split rationale, a dataset card, labeling instructions, and an adjudication example.

## Supplementary reading and attribution

Inspect dataset and test-generation concepts in [Ragas](https://github.com/vibrantlabsai/ragas) and dataset/experiment features in [Phoenix](https://github.com/Arize-ai/phoenix). The records and exercises here are independently written.
