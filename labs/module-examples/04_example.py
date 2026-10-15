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
