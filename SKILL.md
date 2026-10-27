---
name: cognitive-first-output
description: Default cognitive-first output for Codex, Claude Code, and other Agents. Use for substantive explanations, decisions, learning, diagnosis, plans, and status updates. Produce a concise native-chat answer plus a portable visual HTML preview by default when file output is available; emphasize key takeaways, neutral-gray information cards, and functional diagnostic choices. Gracefully fall back to Markdown when preview rendering is unavailable.
---

# Cognitive-First Output · Lay

> V3 visual contract: use the [screenshot-grounded analysis and spacing tokens](references/visual-audit-and-tokens.md) for portable HTML preview. Values are inferred implementation specifications, **not official ChatGPT CSS**.

## Goal

Make the next **judgment or action** obvious within five seconds, while preserving accurate evidence and optional depth. Apply as the default presentation layer regardless of domain. Substance, safety, accuracy, and explicit user format requests override style.

## Core contract: scan first, understand second

1. **Fast layer:** Lead with one plain-language conclusion, decision, or question. Highlight the truly important phrase; use no more than 1–3 first-level ideas for a typical response.
2. **Slow layer:** Explain first-principles causes, important evidence, uncertainty, exceptions, and alternatives to the depth needed. Separate facts from inferences.
3. **Action layer:** On actionable tasks, give the next small action and observable completion signal. In explorations, ask one purposeful question rather than inventing a plan.
4. **Progressive depth:** Prefer a compact first screen and deeper material on demand. Never delete essential caveats or safety information for brevity.

Every visual accent should clarify one thing: **What matters? What relates? What changes? What do I do?**

## Choose the smallest useful visual

| Need | Treatment | Avoid |
| --- | --- | --- |
| One judgment or mental task | Large, concise statement with **one emphasized phrase** | Bold-heavy prose |
| 2–5 labeled facts or memory slots | **Soft neutral-gray card**, short labels and distinct values | Dense paragraphs |
| Old vs new, comparison | Paired cards or a compact table | Repeated prose |
| 3+ dependent stages | Stacked step cards; a diagram only if branching/relations benefit | Decorative arrows |
| A meaningful diagnosis or quiz | Native selectable options and a submit action with tailored follow-up | Fake text-only buttons |
| Data trends or spatial relationships | Accurate chart or map when available | Invented numbers or ornamental visuals |
| Simple conversational answer | Plain language | Forced cards, headings, quizzes |

## Signature pattern: soft-gray working-memory block

- Use a pale neutral-gray surface, subtle boundaries, ample padding, high-contrast values, muted but readable labels. Do not communicate status by color alone.
- Prefer **unboxed explanation** and a single gray information object when it helps. Avoid turning each paragraph, step, or sentence into a card.
- Group **2–5 semantically related** items. Prefer `Label → value`, e.g. `对象 → scientists`, `动作 → abandon a theory`, `限制 → after 2015; why`.
- Give values greater weight than labels; do not overuse bold, emoji, bright accents, or heavy borders.
- Split separate tasks into separate blocks. Avoid nested cards or a card for every sentence.
- If card backgrounds are unavailable, degrade to a compact table, labeled list, or blockquote. Do not promise a visual effect the runtime cannot produce.

## Signature pattern: diagnostic choices

Use questions when the user's answer **changes the next teaching step, explanation, or diagnosis**.

1. Ask **one question at a time** with 2–4 distinct options. Ask only after providing enough context.
2. Use real native radio/checkbox controls when available; let the user select and submit. Do not preselect an answer in a way that biases the diagnosis.
3. Adapt the next response to the actual selection. Self-reports are not proof; propose a short behavior test when necessary.
4. Keep labels visible, taps comfortable, and text readable on a phone. No inert or merely decorative controls.
5. For text-only agents, number the options and invite `A`, `B`, etc. Never imply text is a functioning button.

## Response workflow

1. **Identify intent:** answer, explain, decide, diagnose, execute, or practice. Respect requested format and depth.
2. **Find the decision unit:** the one sentence the reader should retain; what can wait?
3. **Assign cognitive layers:** conclusion → reasoning → action/question. Remove repetitive framing.
4. **Select mode:** plain, gray information block, comparison, process, or interactive question; choose by utility, not novelty.
5. **Adapt to platform:** keep the native answer concise and, for substantive responses with file-writing capability, generate a portable visual preview by default using the shared data contract below. If output files are unavailable, use clean Markdown/plain text; never fake controls.
6. **Verify:** Can someone skim the first screen on a phone, repeat the conclusion, and know the next step? Do actual choices work? Do visuals genuinely help?

## Guardrails

- **Clarity over spectacle:** skip visuals for short answers and avoid excessive title sizes, colorful badges, and ornament.
- **Truth over compression:** show decision-critical uncertainties, risks, caveats, and evidence.
- **Action over unnecessary questions:** do not turn an explicit execution request into a quiz. Ask only when an answer materially changes the work or when coaching requires it.
- **Accessibility:** contrast, reading order, text labels, no color-only meanings, avoid horizontal mobile overflow.
- **Evidence:** cite reliable sources as appropriate; distinguish observations, interpretations, and tests.
- **Default reach:** A Skill by itself cannot automatically govern every platform. Put [the global rule](assets/default-agent-rule.md) into each target Agent's base instructions as well.

For concrete examples and self-tests, see [Patterns and tests](references/patterns-and-tests.md).

## Default dual-mode preview (V3)

Use the [dual-mode output contract](references/dual-mode-contract.md) for Codex, Claude Code, and any Agent that can create files:

1. Answer briefly in native chat so the result is useful without opening anything.
2. For substantive explanation, comparison, workflow, or practice, prepare one JSON answer document following the bundled [example](assets/example-answer.json). Use relevant blocks only.
3. Generate both a standalone interactive HTML preview and Markdown fallback:

```bash
python3 scripts/render_preview.py assets/example-answer.json --output-dir ./output
```

4. Provide a working link or absolute path to the HTML preview in the Agent's supported format. The HTML defaults to a white page, readable narrow column, deliberate typographic spacing, **selective** strong or inline gray highlighting, soft-gray cards, and optional functional single-question choices. Keep it self-contained and usable offline.
5. If a genuine diagnostic question is appropriate, show 2–4 choices with feedback after submission. Do not add choices to simple factual answers or assume a static HTML form transmits the selection back into a chat session.
6. If file creation or preview display is unavailable, render the same data as Markdown without fake UI buttons.

7. For visible emphasis in the input document, use `**important phrase**` (strong) or `==important phrase==` (subtle gray inline highlight). Both are escaped safely in HTML; gray highlighting becomes **bold** in the Markdown fallback. Use no more than one or two emphasized fragments per short paragraph.
8. `facts`, `steps`, `choice`, and `text` remain supported. Use `callout` sparingly for a compact gray principle; use `details` only for *optional* explanation that can safely stay collapsed. Preserve essential risks and conditions in visible text.

Run `python3 -m unittest discover -s scripts -p 'test_*.py'` when changing the renderer. This V3 is a portable **downloadable draft** until installed by the user; do not call it already installed. Do not claim pixel-identical ChatGPT reproduction, guaranteed native widgets in any IDE, or browser QA based solely on static tests.

For Codex / Claude Code setup and cross-platform behavior checks, see [installation and evaluations](references/install-and-evals.md).

