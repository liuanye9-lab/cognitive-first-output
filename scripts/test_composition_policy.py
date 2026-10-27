"""V4.1 static instruction regression; not a visual or reasoning benchmark."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CompositionContractTests(unittest.TestCase):
    def source(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_version_and_content_gate(self):
        src = self.source("SKILL.md")
        self.assertIn("V4.1", src)
        self.assertIn("Content before decoration", src)
        self.assertIn("Remove-the-card test", src)
        self.assertIn("operational boundary", src)
        self.assertIn("observable completion signal", src)

    def test_composition_resource_is_linked_and_exists(self):
        src = self.source("SKILL.md")
        self.assertIn("references/conversation-composition.md", src)
        for relative in re.findall(r"\]\(([^)]+)\)", src):
            if not relative.startswith(("https://", "http://", "#")):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_restraint_and_no_duplicate_content(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn("zero or one", src)
        self.assertIn("Keep most explanation unboxed", src)
        self.assertIn("Do not repeat the same material", src)
        self.assertIn("not a fixed template", src)

    def test_renderer_is_distinct_from_raw_html_and_export(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn('```html type="renderer"', src)
        self.assertIn("Ordinary raw HTML does not qualify", src)
        self.assertIn("Do not write standalone HTML files", src)
        self.assertIn("Escape untrusted content", src)
        host = self.source("references/native-surface-contract.md")
        self.assertIn("Doubao Work: confirmed inline renderer route", host)
        self.assertIn("user-reported evidence for this session", host)

    def test_proposals_are_not_official_measurements(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn("not official ChatGPT CSS", src)
        self.assertIn("740px", src)
        self.assertIn("#f7f7f8", src)
        self.assertIn("12px radius", src)

    def test_example_keeps_tentative_state_and_marks_missing_fields(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn("illustrative", src)
        self.assertIn("考虑一下", src)
        self.assertIn("待确认", src)
        self.assertIn("not a real customer record", src)
        self.assertIn("no added commitment", src)

    def test_policy_and_visual_acceptance_are_not_conflated(self):
        src = self.source("references/install-and-evals.md")
        self.assertIn("No passing string assertion proves", src)
        self.assertIn("new-session loading", src)
        self.assertIn("not full behavioral or cross-client acceptance", src)

    def test_default_rule_transfers_gate_not_fixed_example(self):
        src = self.source("assets/default-agent-rule.md")
        self.assertIn("V4.1", src)
        self.assertIn("remove-the-card test", src)
        self.assertIn("not a dashboard", src)
        self.assertIn("Do not automatically generate standalone HTML", src)
        self.assertIn("Only produce a separate HTML/Markdown export", src)


if __name__ == "__main__":
    unittest.main()
