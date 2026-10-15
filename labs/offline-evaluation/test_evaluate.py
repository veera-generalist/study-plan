"""Tests for meaningful grading and reporting boundary conditions."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from evaluate import evaluate, read_jsonl, run

ROOT = Path(__file__).resolve().parent


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases = read_jsonl(ROOT / "cases.jsonl")
        self.predictions = read_jsonl(ROOT / "predictions.jsonl")

    def test_known_fixture_results_and_slices(self):
        report = evaluate(self.cases, self.predictions)
        self.assertEqual((report["total"], report["passed"], report["failed"]), (8, 6, 2))
        self.assertEqual(report["slices"]["missing_evidence"]["pass_rate"], 0.5)
        self.assertEqual(
            [row["id"] for row in report["results"] if not row["passed"]],
            ["C-04", "C-07"],
        )

    def test_schema_error_is_a_failed_case(self):
        predictions = copy.deepcopy(self.predictions)
        predictions[0]["source_ids"] = "D-1"
        report = evaluate(self.cases, predictions)
        self.assertEqual(report["total"], 8)
        self.assertEqual(report["results"][0]["failed_checks"], ["schema_valid"])

    def test_missing_and_extra_predictions_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Coverage mismatch"):
            evaluate(self.cases, self.predictions[:-1])
        predictions = self.predictions + [{
            "id": "EXTRA", "decision": "abstain", "label": None, "source_ids": []
        }]
        with self.assertRaisesRegex(ValueError, "Coverage mismatch"):
            evaluate(self.cases, predictions)

    def test_missing_null_reference_field_is_invalid_data(self):
        cases = copy.deepcopy(self.cases)
        del cases[2]["expected_label"]
        with self.assertRaisesRegex(ValueError, "missing fields.*expected_label"):
            evaluate(cases, self.predictions)

    def test_nonobject_records_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "must be an object"):
            evaluate([None], self.predictions)

    def test_json_error_reports_source_line(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.jsonl"
            path.write_text('{"id":"A"}\nnot-json\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid.jsonl:2: invalid JSON"):
                read_jsonl(path)

    def test_cli_invalid_case_exits_two_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            cases = copy.deepcopy(self.cases)
            del cases[2]["expected_label"]
            path = Path(directory) / "cases.jsonl"
            path.write_text("\n".join(json.dumps(case) for case in cases), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "evaluate.py"), "--cases", str(path),
                 "--report", str(Path(directory) / "report.json")],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("expected_label", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_duplicate_case_and_prediction_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            evaluate(self.cases + [self.cases[0]], self.predictions)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            evaluate(self.cases, self.predictions + [self.predictions[0]])

    def test_duplicate_jsonl_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.jsonl"
            path.write_text('{"id":"A"}\n{"id":"A"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate ID"):
                read_jsonl(path)

    def test_empty_dataset_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([], [])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.jsonl"
            path.write_text("", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "no records"):
                read_jsonl(path)

    def test_inconsistent_case_is_rejected(self):
        cases = copy.deepcopy(self.cases)
        cases[0]["allowed_source_ids"] = []
        with self.assertRaisesRegex(ValueError, "no allowed source"):
            evaluate(cases, self.predictions)

    def test_invalid_prediction_decision_does_not_crash_grading(self):
        predictions = copy.deepcopy(self.predictions)
        predictions[0]["decision"] = []
        report = evaluate(self.cases, predictions)
        self.assertFalse(report["results"][0]["passed"])

    def test_run_exit_gate_report_and_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            arguments = (ROOT / "cases.jsonl", ROOT / "predictions.jsonl", path)
            self.assertEqual(run(*arguments, 1.0), 1)
            self.assertEqual(run(*arguments, 0.75), 0)
            report = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(report["gate_passed"])
            self.assertEqual(len(report["input_hashes"]["cases_sha256"]), 64)

    def test_nonfinite_or_out_of_range_threshold_is_rejected(self):
        for threshold in (float("nan"), float("inf"), -0.1, 1.1):
            with self.subTest(threshold=threshold):
                with self.assertRaisesRegex(ValueError, "Threshold"):
                    run(ROOT / "cases.jsonl", ROOT / "predictions.jsonl",
                        ROOT / "unused.json", threshold)

    def test_inputs_cannot_be_overwritten_by_report(self):
        with self.assertRaisesRegex(ValueError, "overwrite"):
            run(ROOT / "cases.jsonl", ROOT / "predictions.jsonl",
                ROOT / "cases.jsonl", 1.0)


if __name__ == "__main__":
    unittest.main()
