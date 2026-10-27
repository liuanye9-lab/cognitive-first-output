---
name: cognitive-first-output
description: Default inline cognitive-first answer design for Codex, Claude Code, and other Agents. Use for explanations, analyses, decisions, learning, diagnoses, plans, and reports. Present the complete result directly inside the current conversation with concise hierarchy, selective bold, neutral information groups and genuine native question controls only when available. Never automatically generate a separate HTML page; export only when explicitly requested.
---

# Cognitive-First Output · Lay · V4

## First priority: **the answer is the conversation**

**Default result: a complete response visible in this Agent's current message.**

Do not routinely create a standalone HTML file, export a JSON answer document, start a web server, insert raw HTML/CSS/JS into Markdown, open a preview tab, or send the user to an artifact link to read an ordinary answer. Even a complex answer must be fully understandable **inside the Agent conversation**.

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
| Diagnostic question | Real native question tool/component when available | A/B/C text response in next turn |
| Optional deep explanation | Native disclosure when available and appropriate | Small heading, paragraph, or invitation to expand |

**Hierarchy rules**

- Place the answer above lengthy context. Keep an ordinary response to 1–3 meaningful sections.
- Use short paragraphs, blank lines for topic shifts, and bold for key *phrases*, not entire paragraphs.
- Most explanation stays unboxed. Reserve a gray card for a bounded, memorable information object rather than decorating every section.
- Distinguish fact, inference, limitation, and recommended action. Keep evidence close to its claim.
- Never claim Markdown sets exact font size, 14px radius, neutral background or button behavior. The host owns rendering.
- Respect explicit output format requests, accessibility, screen reader semantics, phone readability, and platform tool instructions.

## True native interaction

Only ask a multiple-choice question if the reply materially affects teaching, diagnosis, prioritization or implementation.

1. Ask **one question** with 2–4 mutually clear options.
2. If the current host actually offers a question input tool or rich controls, use that mechanism; follow all host-specific tool restrictions. Codex host integrations may expose request-user-input and Claude Code may expose AskUserQuestion. **Do not assume either tool exists in every session.**
3. If no true native control is available, list options in the reply and say “回复 A/B/C”. Do not invent clickable buttons, use fake HTML forms or create a browser quiz automatically.
4. After a selection, genuinely tailor the next turn. A static HTML page cannot post a selection to an Agent chat unless separately integrated.
5. If executing an already clear task, act without interrupting for a decorative question.

## Output decision procedure

Before finalizing, check:

1. **Can the user read the substantive result immediately in this message?** If no, revise.
2. Does every visual container improve orientation or memory? If no, remove it.
3. Am I about to make a file only because the old V3 skill said to? If yes, **do not make it**.
4. Is a rich control confirmed in this host? If no, choose the transparent text fallback.
5. Are uncertainty and evidence preserved? If no, revise.

## Optional separate HTML / Markdown exports

**Only if the user explicitly requests a separate HTML/webpage/downloadable preview**, read [portable export instructions](references/dual-mode-contract.md). Use the example JSON in assets/example-answer.json and scripts/render_preview.py to generate standalone HTML and Markdown. This maintains the previous V3 exporter as an **opt-in** feature, not the default answer channel.

The exported HTML supports pale-gray cards and local interactive single-choice feedback; this does **not** mean the HTML is embedded in Codex/Claude Code chat. Never claim pixel-identical ChatGPT rendering or automatically transmit its selection back to the Agent.

For examples see [patterns and tests](references/patterns-and-tests.md). For layout inspiration see [visual audit](references/visual-audit-and-tokens.md); those approximate pixels apply to explicitly exported HTML only. For setup and acceptance tests see [install and eval](references/install-and-evals.md).
