"""Run all offline course checks without downloading models or calling services."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    if sys.flags.optimize:
        print("Run validation without -O/PYTHONOPTIMIZE so lesson assertions execute.")
        return 1
    commands = [
        ["scripts/check_course.py"],
        ["scripts/run_module_examples.py"],
        ["-m", "unittest", "discover", "-s", "scripts", "-p", "test_*.py", "-v"],
        ["-m", "unittest", "discover", "-s", "labs/offline-evaluation",
         "-p", "test_*.py", "-v"],
        ["-m", "unittest", "discover", "-s", "labs/live-model",
         "-p", "test_*.py", "-v"],
        ["-m", "compileall", "-q", "scripts", "labs"],
    ]
    for arguments in commands:
        result = subprocess.run([sys.executable, *arguments], cwd=ROOT, check=False)
        if result.returncode:
            print(f"FAILED: {' '.join(arguments)}", flush=True)
            return 1
    with tempfile.TemporaryDirectory() as directory:
        report = Path(directory) / "report.json"
        for threshold, expected_exit in (("1.0", 1), ("0.75", 0)):
            result = subprocess.run(
                [sys.executable, "labs/offline-evaluation/evaluate.py",
                 "--min-pass-rate", threshold, "--report", str(report)],
                cwd=ROOT, check=False,
            )
            if result.returncode != expected_exit:
                print("Unexpected fixture gate exit status")
                return 1
            data = json.loads(report.read_text(encoding="utf-8"))
            if (data["total"], data["passed"], data["failed"]) != (8, 6, 2):
                print("Unexpected fixture results")
                return 1
    print("All offline checks passed; strict fixture gate failed exactly as expected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
