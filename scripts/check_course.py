"""Check local Markdown file/heading links and required lesson sections.

External URLs are reviewed separately; this is a focused checker for the
inline-link and ATX-heading syntax used by this repository, not a full parser.
"""
import html
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("## Outcomes", "## Detailed tutorial:", "## Lab", "## Review and answers",
            "## Exit evidence", "## Supplementary reading and attribution")
BEGINNER_REQUIRED = ("## Introduction", "## Learning objectives", "## Scenario:",
                     "## Lesson", "## Walkthrough:", "## Try it yourself",
                     "## Assignment", "## Knowledge check", "## What you learned",
                     "## Keep learning")


def outside_fences(text):
    lines = []
    active = None
    for line in text.splitlines():
        match = re.match(r"^\s*(" + chr(96) + r"{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if active is None:
                active = marker
            elif marker[0] == active[0] and len(marker) >= len(active):
                active = None
            continue
        if active is None:
            lines.append(line)
    return "\n".join(lines)


def heading_anchors(text):
    anchors = set()
    counts = Counter()
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", outside_fences(text), re.M):
        title = html.unescape(re.sub(r"<[^>]+>", "", title))
        title = re.sub(r"[*_]", "", title.replace(chr(96), "")).lower()
        slug = re.sub(r"[^\w -]", "", title).replace(" ", "-")
        suffix = counts[slug]
        counts[slug] += 1
        anchors.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return anchors


def local_link_errors(path):
    errors = []
    for target in re.findall(r"\]\(([^)\n]+)\)", outside_fences(path.read_text(encoding="utf-8"))):
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not destination.exists():
            errors.append(f"{path}: missing link {target}")
        elif parsed.fragment and destination.suffix.lower() == ".md":
            anchor = unquote(parsed.fragment)
            if anchor not in heading_anchors(destination.read_text(encoding="utf-8")):
                errors.append(f"{path}: missing heading {target}")
    return errors


def main():
    errors = []
    documents = [
        path for path in ROOT.rglob("*.md")
        if not any(part in {".git", ".venv"} for part in path.relative_to(ROOT).parts)
    ]
    for path in documents:
        errors.extend(local_link_errors(path))
    modules = sorted((ROOT / "modules").glob("*.md"))
    if len(modules) != 12:
        errors.append(f"Expected 12 modules, found {len(modules)}")
    for path in modules:
        content = path.read_text(encoding="utf-8")
        required = BEGINNER_REQUIRED if path.name[:2] in {"01", "02", "03"} else REQUIRED
        for section in required:
            if section not in content:
                errors.append(f"{path.name}: missing {section}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked local file/heading links in {len(documents)} documents and all 12 modules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
