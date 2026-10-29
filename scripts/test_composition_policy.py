"""V4.2 static instruction regression; not a visual or reasoning benchmark."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CompositionContractTests(unittest.TestCase):
    def source(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_version_and_content_gate(self):
        src = self.source("SKILL.md")
        for relative in (
            "SKILL.md",
            "references/conversation-composition.md",
            "references/native-surface-contract.md",
            "references/visual-audit-and-tokens.md",
            "references/install-and-evals.md",
            "assets/default-agent-rule.md",
            "agents/openai.yaml",
        ):
            with self.subTest(relative=relative):
                self.assertIn("V4.2", self.source(relative))
        self.assertIn("Content before decoration", src)
        self.assertIn("Remove-the-card test", src)
        self.assertIn("operational boundary", src)
        self.assertIn("observable completion signal", src)

    def test_composition_resource_is_linked_and_exists(self):
        src = self.source("SKILL.md")
        for relative in (
            "references/conversation-composition.md",
            "references/trae-inline-adapter.md",
            "assets/trae-information-object.html",
        ):
            self.assertIn(relative, src)
        for relative in re.findall(r"\]\(([^)]+)\)", src):
            if not relative.startswith(("https://", "http://", "#")):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_restraint_and_no_duplicate_content(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn("zero or one", src)
        self.assertIn("Keep most explanation unboxed", src)
        self.assertIn("Do not repeat the same material", src)
        self.assertIn("not a fixed template", src)
        self.assertIn("Hierarchy is not larger type", src)
        self.assertIn("same-topic paragraphs", src)
        self.assertIn("topic groups", src)

    def test_widget_boundary_is_explicit(self):
        # G1 is a parent-verified historical widget mismatch, not a new replay.
        src = self.source("references/conversation-composition.md")
        self.assertIn("outside the entire widget", src)
        self.assertIn("judgment, long explanation and key limitations", src)
        self.assertIn("2–5 slots", src)
        self.assertIn("transparent root does not make widget prose native", src)

    def test_slot_budget_does_not_gate_charts_or_relationship_diagrams(self):
        # Static routing check, not proof of a rendered chart or model behavior.
        for relative in (
            "SKILL.md",
            "references/conversation-composition.md",
            "references/native-surface-contract.md",
            "references/visual-audit-and-tokens.md",
            "assets/default-agent-rule.md",
            "agents/openai.yaml",
        ):
            with self.subTest(relative=relative):
                src = self.source(relative)
                self.assertIn("For information objects,", src)
                self.assertIn(
                    "Charts and relationship diagrams follow the owning visualization Skill's current rules",
                    src,
                )
                self.assertIn("outside the entire widget", src)
        self.assertNotIn(
            "use `PureShowWidget` only for an information object",
            self.source("SKILL.md"),
        )
        self.assertNotIn(
            "Use a widget only for a bounded information task",
            self.source("references/conversation-composition.md"),
        )

    def test_renderer_is_distinct_from_raw_html_and_export(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn('```html type="renderer"', src)
        self.assertIn("Ordinary raw HTML does not qualify", src)
        self.assertIn("Do not write standalone HTML files", src)
        self.assertIn("Escape untrusted content", src)
        host = self.source("references/native-surface-contract.md")
        self.assertIn("Doubao Work: historical user report", host)
        self.assertIn("not current-session or cross-host acceptance", host)

    def test_proposals_are_not_official_measurements(self):
        src = self.source("references/conversation-composition.md")
        self.assertIn("not official ChatGPT CSS", src)
        proposal = src.split("## Optional standalone export proposals", 1)[1].split("\n## ", 1)[0]
        self.assertIn("explicitly requested standalone exports only", proposal)
        self.assertIn("do not apply to TRAE", proposal)
        self.assertIn("20px / 1.75", proposal)
        self.assertIn("17px / 1.85", proposal)
        host = self.source("references/native-surface-contract.md")
        for phrase in ("PureShowWidget", "--text-body", "14px/20px", "--text-title", "16px/24px", "--spacer-16"):
            self.assertIn(phrase, host)

    def test_current_screenshot_is_structure_evidence_only(self):
        src = self.source("references/visual-audit-and-tokens.md")
        self.assertIn("9618d255-7386-47c5-a5a4-ef68fbf415fc_e0d93876-0d97-41c6-b0f1-91901e5afe8d_image.png", src)
        self.assertIn("522 × 2048", src)
        self.assertIn("image(20261027-030734).png", src)
        self.assertIn("327 × 2048", src)
        self.assertIn("observable structure only", src)
        self.assertIn("not measured or official", src)

    def test_question_fallback_obeys_host_restrictions(self):
        src = self.source("SKILL.md")
        self.assertIn("one question at a time", src)
        self.assertIn("Host tool restrictions override the A/B/C fallback", src)
        self.assertIn("open-ended question", src)
        host = self.source("references/native-surface-contract.md")
        self.assertIn("Default", host)
        self.assertIn("does not permit text multiple-choice", host)

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
        self.assertIn("V4.2", src)
        self.assertIn("remove-the-card test", src)
        self.assertIn("not a dashboard", src)
        self.assertIn("Do not automatically generate standalone HTML", src)
        self.assertIn("Only produce a separate HTML/Markdown export", src)


if __name__ == "__main__":
    unittest.main()
