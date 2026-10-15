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
