"""Deterministic contract tests for the offline dual-mode renderer."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_preview import CSS, render_html, render_markdown, validate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets" / "example-answer.json"
RENDERER = ROOT / "scripts" / "render_preview.py"


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = validate(json.loads(EXAMPLE.read_text(encoding="utf-8")))

    def test_both_modes_preserve_decision_and_slots(self):
        webpage = render_html(self.doc)
        markdown = render_markdown(self.doc)
        for phrase in ("只留下三个信息槽", "scientists", "2015 年的发现之后", "只记住一个任务标签"):
            self.assertIn(phrase, webpage)
            self.assertIn(phrase, markdown)

    def test_rich_preview_contains_real_radio_and_feedback_logic(self):
        webpage = render_html(self.doc)
        self.assertIn('class="card"', webpage)
        self.assertEqual(webpage.count('<input type="radio"'), 3)
        self.assertIn('type="submit" disabled', webpage)
        self.assertNotIn('type="radio" checked', webpage)
        self.assertIn('aria-live="polite"', webpage)
        self.assertIn("feedback.textContent=checked.dataset.feedback", webpage)
        self.assertIn("@media(max-width:540px)", webpage)
        self.assertIn("form.addEventListener('change'", webpage)
        self.assertIn("form.addEventListener('submit'", webpage)

    def test_screenshot_grounded_visual_tokens(self):
        self.assertIn("--content-width:720px", CSS)
        self.assertIn("--surface:#f6f6f6", CSS)
        self.assertIn("--r-card:14px", CSS)
        self.assertIn("line-height:1.75", CSS)
        self.assertIn("min-height:44px", CSS)
        self.assertIn("prefers-reduced-motion", CSS)
        self.assertNotIn("font-size:clamp(25px,4vw,34px)", CSS)

    def test_semantic_steps_and_progressive_details(self):
        webpage = render_html(self.doc)
        markdown = render_markdown(self.doc)
        self.assertIn('<ol class="steps">', webpage)
        self.assertEqual(webpage.count('<li class="step">'), 5)
        self.assertIn('<details class="details">', webpage)
        self.assertIn("展开第一性原理解释", markdown)
        self.assertIn('class="callout"', webpage)

    def test_inline_mark_and_bold_render_safely_and_degrade_in_markdown(self):
        webpage = render_html(self.doc)
        markdown = render_markdown(self.doc)
        self.assertIn('<mark>只记住一个任务标签</mark>', webpage)
        self.assertIn('<strong>慢思考</strong>', webpage)
        self.assertIn('**只记住一个任务标签**', markdown)
        self.assertNotIn('==只记住', markdown)

    def test_markdown_has_reply_fallback_not_fake_button(self):
        markdown = render_markdown(self.doc)
        self.assertIn("- A.", markdown)
        self.assertIn("- B.", markdown)
        self.assertIn("回复对应选项即可继续", markdown)
        self.assertNotIn("<button", markdown)

    def test_escapes_untrusted_html_everywhere(self):
        changed = copy.deepcopy(self.doc)
        changed["title"] = '</title><script>alert("bad")</script>'
        changed["blocks"][0]["items"][0]["value"] = '<img src=x onerror="alert(1)">'
        changed["blocks"][3]["options"][0]["feedback"] = '" onmouseover="alert(1)'
        changed["lead"] = '**<script>alert(1)</script>**'
        webpage = render_html(validate(changed))
        self.assertNotIn('<img src=x', webpage)
        self.assertNotIn('</title><script>alert', webpage)
        self.assertIn('&lt;img src=x', webpage)
        self.assertIn('&quot; onmouseover=&quot;', webpage)
        self.assertIn('<strong>&lt;script&gt;alert(1)&lt;/script&gt;</strong>', webpage)

    def test_rejects_invalid_choice_options(self):
        changed = copy.deepcopy(self.doc)
        changed["blocks"][3]["options"][1]["id"] = "A"
        with self.assertRaises(ValueError):
            validate(changed)
        changed["blocks"][3]["options"][1]["id"] = "B"
        changed["blocks"][3]["options"][0]["feedback"] = ""
        with self.assertRaises(ValueError):
            validate(changed)

    def test_new_blocks_require_nonempty_content(self):
        changed = copy.deepcopy(self.doc)
        changed["blocks"][2]["body"] = ""
        with self.assertRaises(ValueError):
            validate(changed)
        changed = copy.deepcopy(self.doc)
        changed["blocks"][4]["summary"] = ""
        with self.assertRaises(ValueError):
            validate(changed)

    def test_old_v2_documents_remain_valid(self):
        changed = copy.deepcopy(self.doc)
        changed["blocks"] = changed["blocks"][:2]
        changed["lead"] = "普通文字"
        webpage = render_html(validate(changed))
        self.assertNotIn('<input type="radio"', webpage)
        self.assertIn("普通文字", render_markdown(changed))

    def test_cli_creates_both_and_protects_existing_files(self):
        with tempfile.TemporaryDirectory() as td:
            result = subprocess.run(
                [sys.executable, str(RENDERER), str(EXAMPLE), "--output-dir", td],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(td) / "example-answer.html").is_file())
            self.assertTrue((Path(td) / "example-answer.md").is_file())
            again = subprocess.run(
                [sys.executable, str(RENDERER), str(EXAMPLE), "--output-dir", td],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(again.returncode, 2)
            self.assertIn("already exists", again.stderr)


if __name__ == "__main__":
    unittest.main()
