# Module 07 — Retrieval-augmented generation

[Course index](../README.md) · Weeks 13–14 · Prerequisites: Modules 01–06

## Outcomes

Build a small assistant that retrieves evidence, answers with source references, and handles missing information.

## Lesson 1: Separate ingestion from answering

Ingestion parses documents, preserves metadata, creates chunks, and builds an index. Answering transforms a question into a retrieval request, retrieves passages, optionally reranks them, constructs model input, and returns an answer.

Store document ID, version, section, source location, and access metadata. If a chunk loses its heading, “the threshold is five” may become meaningless. If a table is parsed in the wrong order, the model receives corrupted evidence.

Chunk size is a tradeoff. Small chunks may lose context; large chunks can dilute matching and consume the input budget. Overlap can preserve boundaries but creates duplicates and extra storage. Evaluate changes rather than assuming a universal best size.

## Lesson 2: Retrieval choices

Keyword search is useful for exact identifiers and terms. Vector search retrieves semantic similarity. Hybrid search combines signals, while reranking rescoring can improve ordering at extra cost.

Start with a simple baseline over a small corpus. A vector database is not required to learn the pipeline. Record retrieved passages so you can inspect missed evidence.

Apply authorization constraints before exposing documents to the model. Asking a model to ignore a forbidden passage does not undo disclosure. For document updates, define how old versions are removed or filtered.

## Lesson 3: Answering with evidence

Tell the application which sources are available and return stable source identifiers. Check that cited sources were actually retrieved and that the cited content supports the associated claims.

A model can produce a valid-looking citation to a real document whose contents do not support its statement. Identifier validity is only a structural check. When evidence is absent, allow a limitation statement or clarification question.

## Worked example

Question: “What threshold applies to release v2?” The corpus contains v1 and v2 guidance. Retrieval finds only v1. The answer accurately cites v1 but gives the wrong version's threshold. This is a retrieval/version-selection problem before it is a wording problem.

## Detailed tutorial: build and diagnose a retrieval pipeline

### 1. Follow one question through the entire system

A user asks, “What triggers rollback for v2?” The application first establishes the user's authorized scope and requested version. Retrieval finds candidate passages. A generation step can then write an answer using those passages, and the response includes source references.

That path contains several independently testable decisions. If the document was never ingested, search cannot return it. If metadata incorrectly labels the version, filtering can remove it. If retrieval returns the right passage but generation changes “five consecutive failures” to “five failures in total,” the evidence was available and the generation failed.

Record intermediate evidence so these situations do not collapse into one unexplained incorrect-answer score.

### 2. Ingestion: preserve the structure that carries meaning

Parsing converts files into usable text and metadata. Headers, tables, captions, and version labels often carry important meaning. A threshold without its product heading can become dangerously ambiguous.

Chunking divides parsed material into retrieval units. A fixed character window is simple but can separate an exception from its rule. Heading-aware chunks preserve structure but can be uneven. Overlap helps at boundaries but creates near-duplicate evidence. Record parent-document and section IDs so a retrieved chunk can be expanded or cited.

Create explicit update rules. If v1 remains indexed after v2 arrives, version metadata and query filters must select the correct authority. A draft and an approved policy should not be treated as equivalent solely because both mention the same topic.

### 3. Retrieval methods and their tradeoffs

Keyword methods match lexical evidence. They are useful for error codes, identifiers, and exact terminology. Vector retrieval matches learned representations and can help with paraphrase. Hybrid retrieval combines lexical and semantic signals. Reranking evaluates candidate relevance after initial retrieval.

Each stage adds failure opportunities and operating cost. A vector search can retrieve a topically similar contradiction. A reranker can reorder good evidence incorrectly. A keyword baseline may miss “revert deployment” when the policy says “rollback.”

Choose a baseline, inspect failures, and add complexity to address an observed gap. Your first useful RAG experiment can use a small in-memory corpus; a production-scale vector database is not a prerequisite for learning the reasoning.

### 4. A complete extractive baseline

```python
"""Module 07: authorized, version-filtered lexical retrieval; no LLM."""
import re

DOCUMENTS = [
    {"id": "D-1", "version": "v1", "tenant": "A",
     "text": "Rollback starts after three consecutive failures."},
    {"id": "D-2", "version": "v2", "tenant": "A",
     "text": "Rollback starts after five consecutive failures."},
    {"id": "D-3", "version": "v2", "tenant": "B",
     "text": "Rollback requires the private customer exception."},
    {"id": "D-4", "version": "v2", "tenant": "A",
     "text": "The release lead approves the rollback."},
]


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(question, tenant, version, k=2):
    query_tokens = tokens(question)
    candidates = [
        doc for doc in DOCUMENTS
        if doc["tenant"] == tenant and doc["version"] == version
    ]
    scored = [(len(query_tokens & tokens(doc["text"])), doc) for doc in candidates]
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [doc for score, doc in scored[:k] if score > 0]


def extractive_answer(question, tenant, version):
    hits = retrieve(question, tenant, version)
    if not hits:
        return {"decision": "abstain", "answer": "No matching evidence.", "sources": []}
    return {
        "decision": "answer",
        "answer": " ".join(f"{doc['text']} [{doc['id']}]" for doc in hits),
        "sources": [doc["id"] for doc in hits],
    }


result = extractive_answer("rollback failures", tenant="A", version="v2")
assert result["sources"] == ["D-2", "D-4"]
assert "D-1" not in result["sources"] and "D-3" not in result["sources"]
assert extractive_answer("unicorn", "A", "v2")["decision"] == "abstain"
print(result)
```

Run [the saved example](../labs/module-examples/07_example.py). It returns the v2 threshold and release-lead passage for tenant A. It excludes tenant B's document and the old v1 rule before scoring.

This is deliberately an extractive search baseline, not a full generative assistant. It joins matching passages rather than asking an LLM to synthesize them. That limitation is valuable: you can evaluate retrieval independently before introducing generation.

The token-overlap score is simple and can produce poor relevance decisions. Any matching token can qualify a passage. The abstention path means “no lexical overlap,” not “the corpus has no answer.” Do not describe this heuristic as validated answerability detection.

### 5. Add generation without losing provenance

For a live model integration, construct input containing the question and clearly identified authorized passages. State the evidence boundary and expected behavior when the answer is unsupported. Ask for source identifiers alongside the answer.

Then validate identifiers against the actual retrieved set and evaluate whether passages support the claims. A source can exist and still be irrelevant. Preserve the source version in the report even if the user-facing citation only shows a stable document title.

Do not let evaluation references enter the model context. The reference answer belongs to the grader; retrieved evidence belongs to the application.

### 6. Access controls and trust boundaries

The demonstration passes a tenant string to retrieval. In a real service, derive that scope from authenticated application state, not a user-supplied instruction such as “I am tenant B.” Apply filters before unauthorized content reaches the model.

Authorization and relevance are independent. The most relevant passage may still be forbidden. A prompt asking the model not to reveal a retrieved secret is weaker than preventing retrieval of the secret in the first place.

Similarly, a source passage containing instructions is still source data. It does not gain authority over tool execution because it was returned by search.

### 7. Guided failure investigation

Remove the version filter. Rerun the question and inspect whether v1 appears. If a generated answer now uses three failures, changing answer style will not fix the selection defect. Restore version handling and add a regression case.

Next, ask “When should we revert a deployment?” The toy lexical retriever may miss relevant evidence because the terms differ. This is a plausible motivation for query expansion or embeddings. Evaluate the proposed change on a broader set so it does not merely memorize this one synonym.

Finally, deliberately corrupt the v2 source text during ingestion. Retrieval may score it correctly, but answer correctness fails because the evidence itself is wrong. A faithful answer can faithfully reproduce corrupted input.

### 8. Guided lab solution outline

A minimal implementation needs an ingestion function, a retrieval function returning passage objects, a generation adapter, and a response validator. Keep these boundaries separate. Add five known-answer questions, three missing-evidence cases, two version conflicts, and one unauthorized-access case.

Inspect the exact passage list before grading answers. First measure whether required evidence was retrieved. Then measure whether generation used it correctly. End the report with the component you would change and the evidence supporting that decision.

Use [Microsoft's search lessons](https://github.com/microsoft/generative-ai-for-beginners) and [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) for supplementary implementations. The corpus and retriever above are original.

## Lab

Create 15–25 short, original documents about synthetic release and QA processes. Include an old version, a conflicting draft, and a topic with no answer. Implement keyword retrieval first, then optionally embeddings. Return the answer, retrieved IDs, and citations.

Evaluate a small set before improving chunking or retrieval. Keep the corpus and question-set versions with your results.

## Review and answers

- **Does adding more context always help?** No; irrelevant or conflicting content can harm performance and increase cost.
- **Are real document IDs sufficient evidence?** No; the associated passages must support the claims.
- **Where should access rules be enforced?** In application/retrieval controls before unauthorized content reaches the model.
- **What should happen with an absent answer?** Follow the specified abstention or clarification behavior.

## Exit evidence

A runnable assistant, corpus provenance, retrieval logs, citation checks, and reviewed missing-evidence cases.

## Supplementary reading and attribution

Use search lessons in [Microsoft's course](https://github.com/microsoft/generative-ai-for-beginners) and RAG recipes in [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks). The synthetic corpus you write should have its own provenance.
