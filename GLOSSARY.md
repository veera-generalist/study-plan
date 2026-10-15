# Working glossary

| Term | Meaning in this course |
|---|---|
| Abstention | Declining to provide an unsupported answer, often with a limitation or clarification |
| Agent | A system that delegates some action selection or execution planning to a model |
| Application evaluation | Measuring the complete task-specific system, including retrieval and tools |
| Baseline | A preserved reference implementation/configuration for comparison |
| Calibration | Agreement between probability estimates and empirical outcome frequencies |
| Chunk | A document segment used in indexing and retrieval |
| Context window | Model/interface limit on supplied and generated token content |
| Dataset card | Description of dataset provenance, composition, labeling, use, and limitations |
| Deterministic grader | Code that evaluates a precise condition without model judgment |
| Embedding | Numeric representation used for similarity and other tasks |
| Evaluation slice | A subset defined by intent, risk, language, difficulty, or another property |
| Faithfulness | Support of answer claims by supplied context under a stated definition |
| Fine-tuning | Updating model parameters using training examples |
| Ground truth | Reference labels or outcomes; their provenance and uncertainty still matter |
| Hallucination | Generated content that is unsupported or incorrect under the task's requirements |
| Held-out set | Cases reserved from iterative development for independent evaluation |
| Idempotency | Repeating an operation does not create additional unintended effects |
| Inference | Running a trained model to produce outputs |
| Judge | A human or model applying evaluation criteria |
| Leakage | Information improperly crosses a boundary, such as test labels entering development |
| MRR | Mean reciprocal rank of the first relevant retrieval result |
| Oracle | The basis for determining expected behavior |
| Paired comparison | Comparing versions on the same tasks while preserving case-level relationships |
| pass@k | Success in at least one of k attempts; specify the estimator and setup |
| pass^k | Success in all k attempts under the defined trial setup |
| Prompt injection | Untrusted content attempts to redirect system behavior |
| RAG | Retrieval-augmented generation: retrieving evidence for generation |
| Recall@k | Fraction of labeled relevant items retrieved in the evaluated top-k results |
| Rubric | Explicit criteria and decision anchors used for grading |
| Semantic grader | A grader assessing meaning rather than only structure/exact matching |
| Slice regression | Deterioration in a particular subset, even if the overall score improves |
| Span | One operation represented within a trace |
| Structured output | Output conforming to specified fields, types, or schema |
| Token | A model-specific unit of represented content |
| Trace | Linked observations of operations within an execution |
| Workflow | A system with application-prescribed control flow |
