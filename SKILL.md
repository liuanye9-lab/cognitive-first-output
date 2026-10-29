---
name: cognitive-first-output
description: Use when explanations, analyses or decisions need cognitive-first hierarchy inside an Agent conversation. Not for standalone pages unless explicitly requested.
---

# Cognitive-First Output · Lay · V4.2

## First priority: **the answer is the conversation**

**Default result: a complete response visible in this Agent's current message.**

Do not routinely create a standalone HTML file, export a JSON answer document, start a web server, insert raw HTML/CSS/JS into ordinary Markdown, open a preview tab, or send the user to an artifact link to read an ordinary answer. Even a complex answer must be fully understandable **inside the Agent conversation**. A host-declared inline renderer protocol is not a standalone export: use it only through its exact supported wrapper and rules.

## Content before decoration

Before layout, identify the reader's actual decision, the evidence available, and the smallest useful judgment. Do not display this planning as a mandatory section.

- **Remove-the-card test:** after removing styling, the answer must still contain a useful judgment, necessary evidence or a concrete example, and an applicable next action. A pretty container cannot compensate for empty advice.
- Replace empty labels such as “人工确认” with an operational boundary, for example “客户说考虑一下，不等于确认采购；原文没有时间就标为待确认”. Examples are illustrative, not invented customer records.
- Distinguish facts, judgments and hypotheses. Preserve original status, responsibility and caveats; do not create numbers or promises to make a card look complete.
- Scale to the task. A short fact remains short. Substantive explanations use a specific example or contrast when it resolves ambiguity, not generic filler.
- A next step must identify an action and observable completion signal; omit it for answers where no action is relevant.

For composition, anti-patterns and host-specific inline rules, read [conversation composition](references/conversation-composition.md).

Installing this Skill changes output decisions, **not** the UI capabilities of a Codex terminal, Claude Code, browser, IDE, or ChatGPT client. Use only genuine capabilities actually exposed by the current host. [Native surface contract](references/native-surface-contract.md) provides platform-specific routing and evaluation.

## The two cognitive layers

1. **Fast reading:** Begin with the one practical conclusion, decision, or next question. Emphasize at most the most consequential phrase.
2. **Slow reading:** Give just enough cause, evidence, assumptions, counterargument and detail to let the user trust and apply it.
3. **Next step:** State an action and observable outcome for execution tasks; ask one question only when its answer changes the next step.
4. Do not mechanically label every reply “fast thinking” or “slow thinking.” Scale length and structure to the request. Facts, caveats and safety-critical limitations remain visible.

## Inline layout

| Information need | First choice inside the message | Fallback |
| --- | --- | --- |
| Short fact | One clear sentence, selective bold | Plain text |
| 2–5 related facts | Real native pale-gray information group **if supported by this host** | Compact labeled list, small table or blockquote |
| Alternatives or exact comparison | Native comparison group or short table | Labeled bullets |
| Three or more ordered actions | Compact numbered steps; flow only when relationships need it | Numbered list |
| Diagnostic question | Real native question tool/component when available and permitted | One open-ended question; A/B/C only if host rules allow |
| Optional deep explanation | Native disclosure when available and appropriate | Small heading, paragraph, or invitation to expand |

**Hierarchy rules**

- Place the answer above lengthy context. Add sections only when the content needs distinct topic groups.
- Hierarchy is meaning and reading order, not larger type or more headings. Do not force a template, a bold phrase in every paragraph, or a card for every section.
- Keep same-topic paragraphs in one group with normal paragraph breaks. Use a small content-specific heading or separate list only when the question, decision or action changes; repeated blank lines do not create reliable CSS spacing.
- Use bold selectively for consequential *phrases*, not whole paragraphs or every label.
- Most explanation stays unboxed. Reserve a gray card for a bounded, memorable information object rather than decorating every section.
- Keep the main judgment, long explanation and key limitations in native Markdown outside the entire widget. A transparent root still inherits compact widget typography; it is not native conversation text.
- For information objects, use `PureShowWidget` in TRAE only for 2–5 related slots that materially help grouping, comparison or retention. Charts and relationship diagrams follow the owning visualization Skill's current rules when they make data or relationships clearer; the slot limit does not apply to them. Never put the whole lead/reason/key-object/details reply inside it. Read current `dynamic-ui` rules first; its typography, spacer, theme and radius tokens override all export proposals.
- Distinguish fact, inference, limitation, and recommended action. Keep evidence close to its claim.
- Never claim Markdown sets exact font size, 14px radius, neutral background or button behavior. The host owns rendering.
- Respect explicit output format requests, accessibility, screen reader semantics, phone readability, and platform tool instructions.
- Compose the whole reply, not a single isolated card. Keep the opening judgment, explanatory paragraphs and bounded key object at different visual weights; do not repeat the same content both outside and inside a renderer.
- Default to zero or one substantive gray information object for an ordinary answer. Comparisons may need paired objects; exact data may need a chart. Container count is an editorial preference, never a reason to drop essential information.
- Use emphasis to rank meaning, not to meet a quota. Let semantic grouping organize ideas; avoid report-like banners, status badges without evidence, ornamental icons and a card for each step.

For TRAE, read the [inline adapter](references/trae-inline-adapter.md) before borrowing the [information-object fragment](assets/trae-information-object.html). This resource is not a standalone page or a fixed reply template.

## True native interaction

Ask one question at a time, only if its answer changes the next action. If a safe assumption suffices, state it and proceed.

1. Use a real question tool only when available, permitted in the current mode and useful. Codex host integrations may expose request-user-input and Claude Code may expose AskUserQuestion. **Do not assume either tool exists in every session.**
2. Host tool restrictions override the A/B/C fallback. If the host forbids text multiple-choice, ask one open-ended question instead; the current TRAE Default profile requires this fallback.
3. Only where the host permits text choices and no permitted native control is available, offer a few mutually clear options and say “回复 A/B/C”. Do not invent clickable buttons, fake HTML forms or browser quizzes.
4. After a selection, genuinely tailor the next turn. A static HTML page cannot post a selection to an Agent chat unless separately integrated.
5. If executing an already clear task, act without interrupting for a decorative question.

## Output decision procedure

Before finalizing, check:

1. **Can the user read the substantive result immediately in this message?** If no, revise.
2. Does every visual container improve orientation or memory? If no, remove it.
3. Am I about to make a file only because the old V3 skill said to? If yes, **do not make it**.
4. Is a rich control confirmed and permitted in this host and mode? If no, use a permitted text fallback; do not bypass the restriction with A/B/C.
5. Are uncertainty and evidence preserved? If no, revise.

## Optional separate HTML / Markdown exports

**Only if the user explicitly requests a separate HTML/webpage/downloadable preview**, read [portable export instructions](references/dual-mode-contract.md). Use the example JSON in assets/example-answer.json and scripts/render_preview.py to generate standalone HTML and Markdown. This maintains the previous V3 exporter as an **opt-in** feature, not the default answer channel.

The exported HTML supports pale-gray cards and local interactive single-choice feedback; this does **not** mean the HTML is embedded in Codex/Claude Code chat. Never claim pixel-identical ChatGPT rendering or automatically transmit its selection back to the Agent.

For examples see [patterns and tests](references/patterns-and-tests.md). For observable screenshot structure see [visual audit](references/visual-audit-and-tokens.md); screenshots do not reveal official CSS. Numeric design proposals apply to explicitly exported HTML only, never TRAE widgets. For setup and acceptance tests see [install and eval](references/install-and-evals.md).
