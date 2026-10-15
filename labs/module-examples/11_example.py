"""Module 11: inspect a trace and apply a declared release policy."""
trace = [
    {"trace_id": "T1", "span_id": "S1", "parent_id": None,
     "name": "task", "start_ms": 0, "end_ms": 140, "status": "ok"},
    {"trace_id": "T1", "span_id": "S2", "parent_id": "S1",
     "name": "retrieve", "start_ms": 5, "end_ms": 25, "status": "ok"},
    {"trace_id": "T1", "span_id": "S3", "parent_id": "S1",
     "name": "generate", "start_ms": 30, "end_ms": 135, "status": "ok"},
]
root = next(span for span in trace if span["parent_id"] is None)
task_latency = root["end_ms"] - root["start_ms"]
child_duration_sum = sum(
    span["end_ms"] - span["start_ms"]
    for span in trace if span["parent_id"] is not None
)
assert task_latency == 140
assert child_duration_sum == 125  # Child spans do not cover all task overhead.

baseline = {"quality": 0.90, "critical_failures": 0,
            "grader_errors": 0, "p95_ms": 1000}
candidate = {"quality": 0.93, "critical_failures": 1,
             "grader_errors": 0, "p95_ms": 950}


def release_gate(reference, proposed):
    # Illustrative declared policy, not a universal threshold.
    return (
        proposed["quality"] >= reference["quality"]
        and proposed["critical_failures"] == 0
        and proposed["grader_errors"] == 0
        and proposed["p95_ms"] <= 1200
    )


assert not release_gate(baseline, candidate)
print("Task latency:", task_latency, "sum of child spans:", child_duration_sum)
print("Release gate:", release_gate(baseline, candidate))
