# Module 04 — Evaluation datasets and test oracles

[Course index](../README.md) · Weeks 7–8 · Prerequisites: Modules 01–03

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
