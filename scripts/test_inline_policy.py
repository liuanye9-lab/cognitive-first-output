"""Static checks for the V4 in-chat-first contract; not a host UI test."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InlineContractTests(unittest.TestCase):
    def test_skill_description_is_inline_first(self):
        src = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Default inline cognitive-first", src)
        self.assertIn("Default result: a complete response", src)
        self.assertIn("Only if the user explicitly requests", src)
        self.assertNotIn("generate the preview by default", src.lower())

    def test_global_rule_forbids_automatic_preview(self):
        src = (ROOT / "assets" / "default-agent-rule.md").read_text(encoding="utf-8")
        self.assertIn("Do not automatically generate standalone HTML", src)
        self.assertIn("Only produce a separate HTML/Markdown export", src)

    def test_optional_export_is_guarded(self):
        src = (ROOT / "references" / "dual-mode-contract.md").read_text(encoding="utf-8")
        self.assertIn("when the user explicitly asks", src)
        self.assertIn("not the chat default", src.lower())

    def test_host_caps_and_fallbacks_are_explicit(self):
        src = (ROOT / "references" / "native-surface-contract.md").read_text(encoding="utf-8")
        for phrase in ("AskUserQuestion", "Markdown", "current Agent", "A/B/C"):
            self.assertIn(phrase, src)

    def test_presentation_examples_are_not_offscreen_requirements(self):
        src = (ROOT / "references" / "install-and-evals.md").read_text(encoding="utf-8")
        self.assertIn("no HTML/JSON file", src)
        self.assertIn("manual behavioral", src)


if __name__ == "__main__":
    unittest.main()
