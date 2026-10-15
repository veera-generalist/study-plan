"""Module 09: approval bound to content and idempotent sandbox writes."""
import hashlib
import json

STORE = {}


def fingerprint(draft):
    payload = json.dumps(draft, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def save_draft(draft, approval_hash, operation_id):
    if not isinstance(draft, dict) or set(draft) != {"bug_id", "title"}:
        raise ValueError("Invalid draft schema")
    if not all(isinstance(value, str) and value.strip() for value in draft.values()):
        raise ValueError("Draft values must be nonempty text")
    current_hash = fingerprint(draft)
    if approval_hash != current_hash:
        raise PermissionError("Approval does not match this draft")
    if operation_id in STORE:
        saved = STORE[operation_id]
        if saved["hash"] != current_hash:
            raise ValueError("Operation ID reused for different content")
        return saved["ticket_id"]
    ticket_id = f"T-{len(STORE) + 1}"
    STORE[operation_id] = {
        "ticket_id": ticket_id, "hash": current_hash, "draft": dict(draft)
    }
    return ticket_id


draft = {"bug_id": "B-42", "title": "Investigate authentication outage"}
approval = fingerprint(draft)  # Simulates approval from trusted application state.
first = save_draft(draft, approval, "operation-1")
second = save_draft(draft, approval, "operation-1")
assert first == second and len(STORE) == 1
changed = {**draft, "title": "Changed after approval"}
try:
    save_draft(changed, approval, "operation-2")
except PermissionError:
    pass
else:
    raise AssertionError("Changed content must require fresh approval")
assert len(STORE) == 1
print("One approved ticket exists:", first)
print("Retry did not duplicate it; changed content was denied.")
