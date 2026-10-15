# Project 02 — QA knowledge assistant

## Problem

Engineers need answers about synthetic release policies, rollback procedures, and test strategy. Build a retrieval-based assistant with source references.

## Corpus

Write 15–25 original documents. Include versioned policies, a marked draft, an outdated procedure, one conflict, and a topic with no documented answer. Preserve IDs, versions, and authority metadata.

## Build sequence

1. Parse and index documents with metadata.
2. Implement keyword retrieval and log top results.
3. Add answer generation with citations and abstention.
4. Create relevance labels and answer requirements.
5. Compare one retrieval or chunking change.
6. Review source-version errors and missing-evidence cases.

## Acceptance evidence

- Source provenance and ingestion/retrieval code.
- Document-level retrieval metrics with explicit definitions.
- Separate answer correctness, support, and citation checks.
- Version-selection and access-control cases.
- Paired baseline/candidate report with slice counts.
- Clear limitations of generated and human-reviewed grades.

## Stretch

Add embeddings, hybrid retrieval, or reranking one at a time. Demonstrate a practical improvement relative to the simple baseline before accepting extra complexity.
