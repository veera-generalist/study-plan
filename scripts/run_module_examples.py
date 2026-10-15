"""Verify displayed lesson code matches saved examples and execute assertions."""
import re
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    if sys.flags.optimize:
        print("Run without Python optimization (-O/PYTHONOPTIMIZE); examples use assertions.")
        return 1
    failures = []
    modules = sorted((ROOT / "modules").glob("*.md"))
    if len(modules) != 12:
        print(f"Expected 12 modules, found {len(modules)}")
        return 1
    fence = chr(96) * 3
    for module in modules:
        prefix = module.name[:2]
        example = ROOT / "labs/module-examples" / f"{prefix}_example.py"
        blocks = re.findall(
            "^" + fence + r"python\n(.*?)^" + fence + r"\s*$",
            module.read_text(encoding="utf-8"), flags=re.MULTILINE | re.DOTALL,
        )
        if not example.exists() or len(blocks) != 1:
            failures.append(f"{module.name}: expected one saved/displayed example")
            continue
        if blocks[0].strip() != example.read_text(encoding="utf-8").strip():
            failures.append(f"{module.name}: displayed code differs from saved script")
            continue
        try:
            completed = subprocess.run(
                [sys.executable, str(example)], cwd=ROOT,
                env={key: value for key, value in os.environ.items()
                     if key != "PYTHONOPTIMIZE"},
                text=True, capture_output=True, timeout=10, check=False,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{example.name}: exceeded 10 seconds")
            continue
        if completed.returncode != 0:
            failures.append(f"{example.name}: {completed.stdout}\n{completed.stderr}")
        else:
            print(f"PASS {module.name}")
    if failures:
        print("\n".join(failures))
        return 1
    print("All 12 displayed examples match their scripts and execute successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
