# Optional technical notes

These are the earlier technical chapters, preserved for all twelve topics while the main lessons use a beginner-friendly explanation and practice format.

They contain Python, mathematical examples, formal evaluation terminology, and larger implementation assignments. Use them when you want deeper detail or are ready to program.

| Technical note | Introductory lesson |
|---|---|
| [Python engineering](01-python-engineering.md) | [01 — Getting started with generative AI](../modules/01-python-engineering.md) |
| [Model foundations and metrics](02-model-foundations.md) | [02 — Understanding and comparing language models](../modules/02-model-foundations.md) |
| [Prompting and development](03-prompting-and-development.md) | [03 — Writing useful prompts](../modules/03-prompting-and-development.md) |
| [Datasets and expected behavior](04-datasets-and-oracles.md) | [04 — Make a small set of questions to learn from](../modules/04-datasets-and-oracles.md) |
| [Metrics and evaluation programs](05-evaluation-harnesses.md) | [05 — Check answers consistently](../modules/05-evaluation-harnesses.md) |
| [Model judges and human review](06-judges-and-human-review.md) | [06 — Get help reviewing answers](../modules/06-judges-and-human-review.md) |
| [Retrieval-augmented generation](07-rag-engineering.md) | [07 — Help an assistant answer from documents](../modules/07-rag-engineering.md) |
| [RAG evaluation and statistics](08-rag-evaluation-and-statistics.md) | [08 — Compare two versions fairly](../modules/08-rag-evaluation-and-statistics.md) |
| [Tools, workflows, and agents](09-tools-and-agents.md) | [09 — Give an assistant a small action](../modules/09-tools-and-agents.md) |
| [Agent evaluation and security](10-agent-evaluation-and-security.md) | [10 — Check an assistant when things go wrong](../modules/10-agent-evaluation-and-security.md) |
| [Observability and delivery](11-observability-and-delivery.md) | [11 — Find where a failure began](../modules/11-observability-and-delivery.md) |
| [Optimization and career evidence](12-optimization-and-career.md) | [12 — Bring it together in a small project](../modules/12-optimization-and-career.md) |

The original programs remain in [labs/module-examples](../labs/module-examples/README.md). Repository verification checks their displayed code against those scripts.

Technical notes preserve their earlier examples, terminology, and source credits. The main lessons use the Maple Books scenario and do not assume a particular professional background.

For a first small Python activity, see [the beginner counting example](../labs/beginner/README.md). The full [setup guide](../SETUP.md) is available for later implementation work.

## Before starting the technical notes

The prerequisites at the top of each note refer to other technical notes. They assume more programming practice than the matching written lessons. The earlier week numbers have been removed; use the stages in the [roadmap](../ROADMAP.md) at your own pace.

If Python is new to you, follow the [small coding progression](../labs/beginner/README.md#from-one-program-to-the-technical-notes) before attempting note 01. Reading the introductory AI lessons alone does not teach the programming needed by these notes.

## Example contracts

The technical examples are separate demonstrations, not stages of one compatible application. A contract describes the fields and meanings a particular program expects.

| Material | Task and output | What to keep separate |
|---|---|---|
| Main beginner lessons | Maple Books policy answers and simulated return drafts | These facts and review rules do not define bug classifications. |
| Technical note 01 and local-model lab | Component labels: authentication, payments, other | The adapter status `ok` means structurally valid output, not a verified correct label. |
| Technical note 03 | Simplified impact decisions: high, low, clarify, review | These are severity-policy decisions, separate from component labels. Its earlier richer JSON object is a different project schema. |
| Offline evaluation lab | Stored predictions with decision, label, and source identifiers | Follow that lab's record contract; local-model output cannot be passed in unchanged. |
| Technical note 07 | Authorized lexical search over synthetic release documents | Its source IDs and search units belong to that toy corpus, not Maple Books or a model tokenizer. |
| Technical note 09 | In-memory ticket workflow | This is a separate sandbox, not a working implementation of the beginner return-draft exercise. |

When combining examples in your own project, define one data contract and write an explicit conversion. Preserve execution errors and raw responses. Do not invent missing source evidence or treat severity and component labels as interchangeable.
