"""Module 01: runtime validation and an injectable fake classifier."""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Bug:
    id: str
    description: str


def parse_bug(record: dict) -> Bug:
    if not isinstance(record, dict):
        raise ValueError("Bug record must be an object")
    values = {}
    for name in ("id", "description"):
        value = record.get(name)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be nonempty text")
        values[name] = value.strip()
    return Bug(**values)


def classify(bug: Bug, adapter: Callable[[str], dict]) -> dict:
    try:
        prediction = adapter(bug.description)
    except TimeoutError:
        return {"id": bug.id, "status": "application_error", "label": None}
    label = prediction.get("label") if isinstance(prediction, dict) else None
    if not isinstance(label, str) or label not in {"authentication", "payments", "other"}:
        return {"id": bug.id, "status": "invalid_output", "label": None}
    return {"id": bug.id, "status": "ok", "label": prediction["label"]}


def fake_model(text: str) -> dict:
    return {"label": "authentication" if "login" in text.lower() else "other"}


def unavailable_model(text: str) -> dict:
    raise TimeoutError("simulated provider timeout")


bug = parse_bug({"id": "B-1", "description": "Login is unavailable"})
assert classify(bug, fake_model)["label"] == "authentication"
assert classify(bug, unavailable_model)["status"] == "application_error"
assert classify(bug, lambda text: {"label": "invented"})["status"] == "invalid_output"
assert classify(bug, lambda text: {"label": []})["status"] == "invalid_output"
try:
    parse_bug({"id": "B-2", "description": " "})
except ValueError:
    print("Blank descriptions are rejected before model execution.")
else:
    raise AssertionError("Expected invalid input to be rejected")
print(classify(bug, fake_model))
