# Conversation composition · V4.2

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

## Semantic grouping

Hierarchy is not larger type, extra titles or a bold phrase in every paragraph. Rank the judgment, supporting explanation and optional object by their information role.

- Keep same-topic paragraphs together when they answer the same question or support the same decision. Use normal paragraph breaks; do not insert a heading between a claim and its explanation or example.
- Create distinct topic groups when the reader must switch to a different question, decision or action. A short content-specific heading can mark that switch; a short reply may need none.
- Use a list for peer facts and numbering for ordered actions. Do not split every sentence into a new section, card or bold label.
- Markdown expresses paragraphs, headings and lists, not exact paragraph or topic gaps. Extra blank lines, invisible characters and raw CSS cannot reliably set host spacing.

## Host-adapted display

- Keep the main judgment, long explanation and key limitations in native Markdown outside the entire widget. This includes long replies, not just concise answers. Supplementary detail may use a genuinely supported disclosure; required instructions and risks stay visible in native text.
- A transparent root does not make widget prose native. Do not wrap the whole lead/reason/key-object/details reply in a renderer, even if its paragraphs are visually unboxed.
- For information objects, use a widget only for a bounded information task with 2–5 slots, such as objects, actions and constraints or a compact comparison. Do not repeat the same material in prose and slots. Charts and relationship diagrams follow the owning visualization Skill's current rules when they make data or relationships clearer; the slot limit does not apply to them. If neither an information object nor a diagram adds clarity, use Markdown alone.
- Use an inline renderer only if the host declares the route and the task benefits from it; read the owning visualization Skill and follow its wrapper, citation and accessibility rules.
- In TRAE, read current `dynamic-ui` and use `PureShowWidget` only if exposed and permitted. Use its role tokens, not the standalone proposals below; do not enlarge text or spacing to compensate for compact typography. See [TRAE adapter](trae-inline-adapter.md).
- In Doubao Work, only if the current host declares it, the fenced start is exactly ` ```html type="renderer" ` and the end is ` ``` `, each on its own line. Ordinary raw HTML does not qualify.
- The object root uses natural height, full available width and safe wrapping under the owning renderer's rules. Do not write standalone HTML files or open browser tabs just to style a chat answer.
- A static visible card is **not** evidence of click handling, new-session loading, native input integration or cross-client support. Native question tools remain the first choice for actual decisions.
- Escape untrusted content. Do not interpolate user text into executable HTML, attributes or script. Static explanatory cards need no script and no fake button.

## Optional standalone export proposals

These are design proposals for explicitly requested standalone exports only, **not official ChatGPT CSS** or screenshot measurements. They do not apply to TRAE, native Markdown or another host's inline renderer. The retained V3 exporter has its own defaults; this table is an optional alternate design, not a request to change that exporter.

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

## Direction example (illustrative)

In this fictional example, **客户说“考虑一下”，不能被摘要改写为“已确认采购”。**

A short explanation should show why the distinction matters: summarization may compress wording, but must not promote an uncertain intention into a commitment.

One optional gray object can hold only concrete status or missing fields not yet listed in the prose (2–5 slots):

> 日期：原文未提供，待确认
>
> 责任人：原文未提供，待确认

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

A historical user report accepted a revised Doubao composition sample as a useful direction. It does not establish current V4.2 acceptance, actual TRAE display or cross-host compatibility. Fresh visual feedback remains separate from static tests, which cannot prove universally better reasoning or aesthetic quality.
