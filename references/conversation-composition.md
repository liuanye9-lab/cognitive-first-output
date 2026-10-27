# Conversation composition · V4.1

## Purpose

Improve the whole answer, not the decoration of an isolated card. Use this contract after understanding the reader's decision and obtaining necessary evidence. Explicit user format, host rules, safety and substantive accuracy take precedence.

## Content gate

- Apply the **remove-the-card test**: without styling, the reply still has a useful judgment, necessary explanation or evidence, and a relevant action or boundary. Do not substitute generic labels for thought.
- Turn vague advice into an operational distinction. “人工确认” is weak; “客户说考虑一下，不等于确认采购；原文没有日期就标为待确认” is actionable.
- Use a concrete example or counterexample when it disambiguates the judgment. Label examples as illustrative. Never manufacture business records, dates, figures or evidence.
- Keep facts, judgments and hypotheses distinguishable. Preserve original status words and caveats.
- Add a next action only when relevant, with an observable completion signal. Do not attach a compulsory question or plan to every answer.

## Editorial rhythm

1. Open with a useful judgment in ordinary conversational prose. Emphasize the consequential phrase, not the whole paragraph.
2. Explain the reason with short, mostly unboxed paragraphs. Related thoughts sit close together; topic changes have more whitespace.
3. Give one bounded object prominence only if it helps retention: a decision boundary, evidence contrast, compact comparison or a few coherent memory slots.
4. Finish with the smallest relevant action or necessary limitation. Do not repeat a full summary when nothing is added.

This is a composition grammar, not a fixed template. Short facts may need only one sentence; exact comparisons may need a table; sequences may need numbering; long requested reports can be longer.

For an ordinary answer, prefer **zero or one** substantive gray information object. Do not box every paragraph or stage. Avoid dashboard banners, ornamental icons, unsupported status badges and equal visual weight for unrelated information. Keep most explanation unboxed. Do not repeat the same material outside and inside a renderer.

## Host-adapted display

- Use Markdown for ordinary concise answers, or the current host's actual native components.
- Use an inline renderer only if the host declares the route and the task benefits from it; read the owning visualization Skill and follow its wrapper, citation and accessibility rules.
- In Doubao Work, the host-declared fenced start is exactly ` ```html type="renderer" ` and the end is ` ``` `, each on its own line. Ordinary raw HTML does not qualify.
- Use a transparent, natural-height root, `width:100%`, `box-sizing:border-box`, and safe wrapping. Do not write standalone HTML files or open browser tabs just to style a chat answer.
- A static visible card is **not** evidence of click handling, new-session loading, native input integration or cross-client support. Native question tools remain the first choice for actual decisions.
- Escape untrusted content. Do not interpolate user text into executable HTML, attributes or script. Static explanatory cards need no script and no fake button.

## Proposed inline tokens

These are implementation proposals tuned to the user-approved sample, **not official ChatGPT CSS**, and not guarantees for host typography. Apply only when a confirmed renderer lets you control them.

| Element | Proposal | Purpose |
| --- | --- | --- |
| Reading width | max 740px; fluid width | One readable column, no forced full-screen stretching |
| Main judgment | 20px / 1.75; weight 400; selective strong 650 | Separate meaning through emphasis, not a bold wall |
| Explanatory text | 17px / 1.85 | Comfortable Chinese reading |
| Section heading | 19px / 1.55; weight 650 | Noticeable but restrained |
| Paragraph gap | 14–20px | Keep one idea connected |
| Topic gap | 28–32px | Mark a change of cognitive task |
| Key object | #f7f7f8; 12px radius; 18px 22px padding | One gentle memory anchor, no heavy shadow |
| Key-object value | 18px / 1.75; weight 600 | Prioritize the actual distinction |
| Secondary label | 14px / 1.6; muted readable gray | Context without competing with the judgment |

On narrow viewports, wrap rather than forcing paired columns. Important caveats cannot be reduced to unreadable metadata. Do not use color as the only status signal.

## Approved direction example (illustrative)

**客户说“考虑一下”，不能被摘要改写为“已确认采购”。**

A short explanation should show why the distinction matters: summarization may compress wording, but must not promote an uncertain intention into a commitment.

One optional gray object can hold the exact boundary:

> “客户说考虑一下” ≠ “客户已确认采购”
>
> Preserve the original state. Missing dates and responsibility stay “待确认”.

A relevant next step is to check a single redacted record against the source. Completion means no added commitment, no omitted condition, and missing fields explicitly marked. This is not a real customer record.

Do not copy this example into unrelated topics. Transfer the content gate and rhythm instead.

## Acceptance and evidence

- First glance: the judgment is findable without reading every label.
- Substance: removing styling does not remove the answer's usefulness.
- Retention: the emphasized object has a concrete distinction, not a generic slogan.
- Reading: unboxed prose, topic spacing and minimal containers create a conversation rather than a dashboard.
- Evidence: original uncertainty and source mapping remain visible.
- Action: where relevant, the next step has an observable completion signal.
- Host: distinguish static policy tests, exporter regression, browser rendering, actual chat display, real interactions and cross-client tests.

The user accepted this direction in the current conversation after seeing a revised sample. Further everyday use still needs feedback; static tests cannot prove universally better reasoning or aesthetic quality.
