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
