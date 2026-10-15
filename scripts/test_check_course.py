"""Regression checks for documentation navigation."""
import tempfile
import subprocess
import sys
import unittest
from pathlib import Path

from check_course import heading_anchors, local_link_errors


class LinkTests(unittest.TestCase):
    def test_example_runner_rejects_disabled_assertions(self):
        runner = Path(__file__).resolve().parent / "run_module_examples.py"
        result = subprocess.run([sys.executable, "-O", str(runner)],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("without Python optimization", result.stdout)

    def test_code_fences_do_not_create_heading_targets(self):
        fence = chr(96) * 3
        text = f"# Real\n{fence}python\n# Not a heading\n{fence}\n"
        self.assertEqual(heading_anchors(text), {"real"})

    def test_duplicate_headings_get_distinct_anchors(self):
        self.assertEqual(heading_anchors("# Topic\n# Topic\n"), {"topic", "topic-1"})

    def test_local_and_cross_file_fragments_are_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            other = root / "other.md"
            other.write_text("# Valid heading\n", encoding="utf-8")
            page = root / "page.md"
            page.write_text("# Page\n[ok](other.md#valid-heading)\n[bad](other.md#missing)\n",
                            encoding="utf-8")
            errors = local_link_errors(page)
            self.assertEqual(len(errors), 1)
            self.assertIn("missing heading", errors[0])

    def test_missing_file_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "page.md"
            page.write_text("[bad](absent.md)\n", encoding="utf-8")
            self.assertIn("missing link", local_link_errors(page)[0])

    def test_external_links_are_not_claimed_as_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "page.md"
            page.write_text("[source](https://example.com/page#section)\n", encoding="utf-8")
            self.assertEqual(local_link_errors(page), [])


if __name__ == "__main__":
    unittest.main()
