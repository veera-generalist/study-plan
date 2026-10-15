"""Module 05: explicit statuses, denominators, and conservative gates."""
from collections import Counter

outcomes = [
    {"id": "1", "status": "pass"},
    {"id": "2", "status": "pass"},
    {"id": "3", "status": "fail"},
    {"id": "4", "status": "application_error"},
    {"id": "5", "status": "grader_error"},
]
ALLOWED = {"pass", "fail", "application_error", "grader_error"}


def summarize(rows):
    if not rows:
        raise ValueError("No evaluation outcomes")
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("Duplicate case IDs")
    if any(row["status"] not in ALLOWED for row in rows):
        raise ValueError("Unknown outcome status")
    counts = Counter(row["status"] for row in rows)
    judged = counts["pass"] + counts["fail"]
    total = len(rows)
    return {
        "total": total,
        "counts": dict(counts),
        "confirmed_pass_rate": counts["pass"] / total,
        "judged_pass_rate": counts["pass"] / judged if judged else None,
        "measurement_coverage": judged / total,
        "release_gate": counts["grader_error"] == 0
            and counts["application_error"] == 0
            and counts["pass"] == total,
    }


report = summarize(outcomes)
assert report["confirmed_pass_rate"] == 0.4
assert report["measurement_coverage"] == 0.6
assert abs(report["judged_pass_rate"] - 2/3) < 1e-12
assert report["release_gate"] is False
print(report)
