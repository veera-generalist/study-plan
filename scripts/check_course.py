"""Check relative Markdown file links and required course sections offline.

This deliberately does not validate external URLs or heading fragments.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("## Outcomes", "## Detailed tutorial:", "## Lab", "## Review and answers",
            "## Exit evidence", "## Supplementary reading and attribution")


def main():
    errors = []
    documents = list(ROOT.rglob("*.md"))
    for path in documents:
        if any(part in {".git", ".venv"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link {target}")
    modules = sorted((ROOT / "modules").glob("*.md"))
    if len(modules) != 12:
        errors.append(f"Expected 12 modules, found {len(modules)}")
    for path in modules:
        content = path.read_text(encoding="utf-8")
        for section in REQUIRED:
            if section not in content:
                errors.append(f"{path.name}: missing {section}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked relative file links and required sections in {len(modules)} modules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
