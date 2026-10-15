"""Original offline contract-evaluation example; no model or network access."""
import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

VERSION = "1.0"
DECISIONS = {"answer", "abstain"}


def read_jsonl(path):
    records = []
    seen = set()
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number}: expected an object")
            record_id = record.get("id")
            if not isinstance(record_id, str) or not record_id.strip():
                raise ValueError(f"{path}:{line_number}: missing or invalid ID")
            if record_id in seen:
                raise ValueError(f"{path}:{line_number}: duplicate ID {record_id}")
            seen.add(record_id)
            records.append(record)
    if not records:
        raise ValueError(f"{path}: no records")
    return records


def string_list(value):
    return isinstance(value, list) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )


def validate_case(case):
    expected = case.get("expected_decision")
    label = case.get("expected_label")
    if not isinstance(expected, str) or expected not in DECISIONS:
        raise ValueError(f"{case['id']}: invalid expected decision")
    if not isinstance(case.get("slice"), str) or not case["slice"].strip():
        raise ValueError(f"{case['id']}: invalid slice")
    if not string_list(case.get("allowed_source_ids")):
        raise ValueError(f"{case['id']}: invalid allowed sources")
    if type(case.get("citation_required")) is not bool:
        raise ValueError(f"{case['id']}: citation_required must be boolean")
    if expected == "answer" and (not isinstance(label, str) or not label.strip()):
        raise ValueError(f"{case['id']}: answer case needs an expected label")
    if expected == "abstain" and label is not None:
        raise ValueError(f"{case['id']}: abstention label must be null")
    if case["citation_required"] and not case["allowed_source_ids"]:
        raise ValueError(f"{case['id']}: required citation has no allowed source")


def grade(case, prediction):
    decision = prediction.get("decision")
    label = prediction.get("label")
    sources = prediction.get("source_ids")
    schema_valid = (
        isinstance(decision, str)
        and decision in DECISIONS
        and "label" in prediction
        and (label is None or isinstance(label, str))
        and string_list(sources)
    )
    if not schema_valid:
        return {"schema_valid": False}
    return {
        "schema_valid": True,
        "decision_correct": decision == case["expected_decision"],
        "label_correct": label == case["expected_label"],
        "sources_allowed": all(
            source in case["allowed_source_ids"] for source in sources
        ),
        "citation_present": not case["citation_required"] or bool(sources),
    }


def evaluate(cases, predictions):
    if not cases or not predictions:
        raise ValueError("Cases and predictions must be nonempty")
    for records, name in ((cases, "cases"), (predictions, "predictions")):
        ids = [record.get("id") for record in records]
        if any(not isinstance(item, str) or not item.strip() for item in ids):
            raise ValueError(f"Invalid ID in {name}")
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplicate IDs in {name}")
    for case in cases:
        validate_case(case)
    by_id = {prediction["id"]: prediction for prediction in predictions}
    case_ids = {case["id"] for case in cases}
    if case_ids != set(by_id):
        missing = sorted(case_ids - set(by_id))
        extra = sorted(set(by_id) - case_ids)
        raise ValueError(f"Coverage mismatch: missing={missing}, extra={extra}")
    results = []
    slices = defaultdict(lambda: {"total": 0, "passed": 0})
    for case in cases:
        checks = grade(case, by_id[case["id"]])
        passed = all(checks.values())
        results.append({
            "id": case["id"],
            "slice": case["slice"],
            "passed": passed,
            "checks": checks,
            "failed_checks": [name for name, value in checks.items() if not value],
        })
        slices[case["slice"]]["total"] += 1
        slices[case["slice"]]["passed"] += int(passed)
    for summary in slices.values():
        summary["pass_rate"] = summary["passed"] / summary["total"]
    passed_count = sum(result["passed"] for result in results)
    return {
        "runner_version": VERSION,
        "total": len(cases),
        "passed": passed_count,
        "failed": len(cases) - passed_count,
        "pass_rate": passed_count / len(cases),
        "slices": dict(sorted(slices.items())),
        "results": results,
    }


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(cases_path, predictions_path, report_path, threshold):
    if not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("Threshold must be a finite number between 0 and 1")
    resolved_inputs = {Path(cases_path).resolve(), Path(predictions_path).resolve()}
    if Path(report_path).resolve() in resolved_inputs:
        raise ValueError("Report must not overwrite an input file")
    report = evaluate(read_jsonl(cases_path), read_jsonl(predictions_path))
    report["input_hashes"] = {
        "cases_sha256": file_hash(cases_path),
        "predictions_sha256": file_hash(predictions_path),
    }
    report["threshold"] = threshold
    report["gate_passed"] = report["pass_rate"] >= threshold
    destination = Path(report_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Passed {report['passed']}/{report['total']} ({report['pass_rate']:.0%})")
    print(f"Report: {destination}")
    return 0 if report["gate_passed"] else 1


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=root / "cases.jsonl")
    parser.add_argument("--predictions", type=Path, default=root / "predictions.jsonl")
    parser.add_argument("--report", type=Path, default=root / "reports/report.json")
    parser.add_argument("--min-pass-rate", type=float, default=1.0)
    args = parser.parse_args()
    try:
        return run(args.cases, args.predictions, args.report, args.min_pass_rate)
    except (ValueError, OSError) as error:
        parser.exit(2, f"Evaluation input/configuration error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
