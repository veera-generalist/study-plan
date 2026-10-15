"""Module 12: choose among synthetic measured tradeoffs without one magic score."""
candidates = [
    {"name": "baseline", "quality": 0.90, "cost": 0.02, "latency_ms": 600,
     "critical_failures": 0},
    {"name": "larger-model", "quality": 0.95, "cost": 0.08, "latency_ms": 1000,
     "critical_failures": 0},
    {"name": "retrieval-fix", "quality": 0.93, "cost": 0.02, "latency_ms": 650,
     "critical_failures": 0},
    {"name": "bad-cache", "quality": 0.94, "cost": 0.01, "latency_ms": 200,
     "critical_failures": 1},
    {"name": "slower-copy", "quality": 0.90, "cost": 0.03, "latency_ms": 800,
     "critical_failures": 0},
]


def dominates(left, right):
    no_worse = (
        left["quality"] >= right["quality"]
        and left["cost"] <= right["cost"]
        and left["latency_ms"] <= right["latency_ms"]
    )
    strictly_better = (
        left["quality"] > right["quality"]
        or left["cost"] < right["cost"]
        or left["latency_ms"] < right["latency_ms"]
    )
    return no_worse and strictly_better


eligible = [row for row in candidates if row["critical_failures"] == 0]
frontier = [
    row for row in eligible
    if not any(dominates(other, row) for other in eligible)
]
names = {row["name"] for row in frontier}
assert names == {"baseline", "larger-model", "retrieval-fix"}
assert "bad-cache" not in names
print("Eligible tradeoff frontier:", sorted(names))
print("Choose from it using operating requirements and independent evidence.")
