# Default Agent Output Rule — Cognitive First

Apply `cognitive-first-output` to every user-facing answer by default.

- Lead with the **one-sentence outcome** or most useful judgment. Make the key phrase obvious.
- Layer information: quick conclusion → essential why/evidence → next action or one necessary question. Do not mechanically label the layers.
- Prefer a **light neutral-gray information card** for 2–5 labeled facts (object/action/constraint, diagnosis/evidence/next step). Use high contrast and ample spacing. Never create a card for one simple fact.
- Keep most assistant explanation on **white canvas without card borders**. Build hierarchy with line-height, concise paragraphs, 12–16px paragraph gaps and 30–36px section gaps. Use the screenshot-grounded V3 tokens in `references/visual-audit-and-tokens.md` for HTML output; these tokens are design proposals, not GPT internal measurements.
- Bold or inline-highlight **one consequential phrase** when useful; do not bold the full answer or make every section title oversized.
- Prefer **real selectable multiple-choice controls** when one answer changes the next training/diagnostic step. Ask one question at a time; after submission, respond to the chosen answer. Do not preselect or fake functionality.
- Choose compact cards/tables for comparisons and a short step flow for genuine multi-stage processes. Never invent metrics or over-visualize.
- When file output is available, generate the portable HTML preview for substantive answers by default alongside a concise native-chat answer. Use the bundled renderer and a single answer data document so HTML and Markdown remain consistent.
- In the answer JSON, `**phrase**` becomes bold and `==phrase==` becomes a light-gray inline highlight in HTML. Choose semantic `facts`, `steps`, `callout`, `details` or `choice` blocks only when justified by the reader's next cognitive task.
- If rich UI or file output is unsupported, use readable Markdown, a table, or A/B/C reply choices, without claiming interactivity.
- Make mobile scanning easy. Use bold sparingly, preserve evidence/caveats/safety. Respect explicit user format requests.

This is a **presentation policy**, not permission to skip research, ask unnecessary questions, or stop before task completion.
