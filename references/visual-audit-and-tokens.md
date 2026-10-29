# Screenshot-grounded visual audit · V4.2

Current source: user-provided `9618d255-7386-47c5-a5a4-ef68fbf415fc_e0d93876-0d97-41c6-b0f1-91901e5afe8d_image.png` (522 × 2048 screenshot pixels), observed on 2026-10-30. It supports observable structure only; **actual app CSS, device pixel ratio, original viewport and font metrics cannot be recovered**. Visible controls do not prove click handling or responses sent to an Agent.

Historical source: `image(20261027-030734).png` (327 × 2048) informed the earlier audit and portable V3 preview proposals. That historical description is not a fresh audit of the old image, a measurement of the current image or a pixel comparison between them. Numerical design proposals below are not measured or official OpenAI tokens.

## What the current screenshot visibly does

1. **Conversation, not a whole-reply card.** Assistant explanations lie mostly on the white reading surface; user messages sit on the right in tinted bubbles.
2. **Judgment precedes detail.** Replies open with a brief judgment or question and then explain. Emphasis selects meaningful phrases rather than bolding every paragraph.
3. **Groups follow cognitive tasks.** Related explanations stay together; a different question or next action gains visible separation and sometimes a content-specific heading. The hierarchy is not just larger text.
4. **Objects have an information task.** Pale or finely bordered groups hold linked facts such as “研究目的／研究发现／研究结论” or “目标／问题／行动／下一步”. These are observed examples, not mandatory reply columns.
5. **Controls have visible appearance only.** Single-choice and submit styling appears alongside later replies. A single image cannot establish real clicking, script execution or input delivery.
6. **Length varies with the task.** Short and detailed replies coexist; long explanations are not consistently inside one container. No fixed five-section template should be inferred.

## Host adaptation, not CSS reconstruction

- Keep judgment, long explanation and key limitations in native Markdown outside the entire widget. A transparent widget root still inherits compact type and is not a substitute for the conversation surface.
- For information objects, use `PureShowWidget` only for a bounded 2–5-slot object that materially helps grouping, comparison or retention. Charts and relationship diagrams follow the owning visualization Skill's current rules when they make data or relationships clearer; the slot limit does not apply to them. Do not repeat the object's facts in surrounding prose.
- Read current `dynamic-ui` tokens first. Its `--text-body` (14px/20px), `--text-title` (16px/24px maximum), spacer and radius roles govern the widget; do not enlarge them to approximate the screenshot.
- Use normal Markdown paragraph breaks within one topic and meaningful headings/lists when switching tasks. Markdown does not set CSS gaps, font metrics, gray fills or corners.
- Historical Doubao user reports, current screenshot observations and current host rendering tests are different evidence. None establishes current V4.2 user acceptance or cross-host parity.

## Proposed CSS tokens for the portable preview

Use only for explicitly requested standalone exports, never TRAE or other inline widgets. These historical proposals explain the retained V3 preview; they do not override current host rules or request exporter changes. The alternate 20/17 typography proposal in [conversation composition](conversation-composition.md) is also export-only.

| Aspect | Proposed token | Reason / test |
| --- | --- | --- |
| Reading column | `--content-width: 720px` | Single-column and comfortable line length; compare at 1440px desktop |
| Page gutter | `24px` desktop; `16px` mobile | No horizontal scroll at 360px |
| Main body | `16px / 1.75` | Chinese paragraph readability; 2–5 lines per chunk |
| Main title | `clamp(22px, 3vw, 27px) / 1.35`, weight 660 | Visible hierarchy without report-style oversized headline |
| Lead / decision | `19px / 1.65`, weight 450; selective **strong** at 680 | One emphasized phrase rather than entire bold paragraph |
| Section title | `17px / 1.5`, weight 680 | Just over body size |
| Secondary info | `13–14px / 1.65`, muted gray | File labels, status, hints only; not critical claims |
| Type tracking | `-0.01em` headings; `0` body | Avoid tightly packed Chinese characters |
| Spacing scale | `4, 8, 12, 16, 24, 32, 48, 64px` | Use a rhythm; don't improvise each gap |
| Paragraph gap | `12–16px` | Paragraphs stay connected within a section |
| Section gap | `30–36px` | Next cognitive task looks separate |
| Gray information card | `#f6f6f6`, 1px `#ebebeb` border, radius `14px`, padding `16–20px` | Soft affordance; no heavy shadow |
| Choice card | white, 1px `#e8e8e8` border, radius `14px`, padding `18px` | Group the question, not everything around it |
| Options | min-height `44px`, `18–20px` radio, gap `10–12px` | Keyboard & mobile tap targets |
| Submit | near-black `#171717`, white text, min-height `44px`, pill radius | Primary call-to-action; clear enabled/disabled states |
| Focus | visible high-contrast blue outline `3px` | Keyboard accessibility |

Suggested colors: `--ink:#171717`, `--muted:#686868`, `--surface:#f6f6f6`, `--line:#e8e8e8`, `--white:#fff`, `--user:#edf4ff`, `--accent:#1558b0`. Favor contrast over perfectly matching the screenshot tint.

## Layout grammar

- **Flexible flow:** useful judgment → necessary explanation → optional information object → relevant next action. Omit irrelevant stages; do not require a title or marked phrase.
- **Keep content unboxed unless it earns a container.** More than two strong card surfaces on an ordinary response is a warning signal, not a hard ban.
- **No giant report heading for normal replies.** Reserve large heading/display styles for explicitly requested standalone reports.
- **Use at most one diagnostic question per turn, only if its answer changes what the Agent would do next.** Each option needs a distinct, truthful feedback path.
- **Responsive single column:** no forced side-by-side facts on narrow viewports; preserve reading order and generous touch zones.
- **Inline emphasis:** `**phrase**` marks selective importance in Markdown. The retained optional exporter alone supports `==phrase==` as an HTML highlight degrading to bold; it is not native Markdown CSS. Never use HTML from user data.
- **Progressive disclosure:** use a genuinely supported native disclosure only for supplementary detail. Exported HTML may use `<details>`; never assume a chat host supports it or hide a risk, caveat or required instruction.

## Evidence status and acceptance

Current visual observations establish structure, not CSS or functioning controls. For an explicitly requested export, verify the preview at 360px, 768px and 1440px widths, including wrap, focus, selection and feedback. For an inline object, test the actual host separately. Static policy checks, exporter regression, browser QA, actual chat display, real interaction, new-session loading and user visual feedback are distinct evidence. A portable preview cannot guarantee pixel-identical ChatGPT output or cross-host native widgets.
