# Screenshot-grounded visual audit · V3

Source: user-provided long screenshot `image(20261027-030734).png` (327 × 2048 screenshot pixels). It shows a ChatGPT conversation with assistant replies, soft containers, understated metadata, radio choices and dark submit buttons. The screenshot is heavily downscaled; **actual app CSS, device pixel ratio, original viewport and font metrics cannot be recovered**. Numbers below are an *implementation proposal*, not measured or official OpenAI tokens.

## What the screenshot visibly does

1. **Conversation, not slide deck.** The main text lives in one restrained central reading column; user messages sit on the right in tinted rounded bubbles. Assistant content is mostly unboxed on white.
2. **The first glance has a clear target.** Short assertion or question appears first; heavier words are selective, not a bold wall. Large headings are unusual compared with ordinary text.
3. **Spacing carries the hierarchy.** Lines are comfortably open; related lines sit together, unrelated topics are separated by substantially larger vertical gaps. Dividers are extremely light.
4. **Gray is a working-memory surface.** Only coherent objects (a file card, an information summary, a decision panel) gain a very pale gray fill or a fine gray border. Long explanations remain white.
5. **Interaction looks native.** Diagnostic answers use an actual radio group with a single full-width, rounded near-black submit control, followed by response text. A selected answer must visibly change state.
6. **Colors are sparse.** Near-black primary ink; muted gray labels; subtle blue for user messages and occasional muted green or red for status. Meaning is also written in words.
7. **Messages alternate between succinct and detailed.** Replies do not reuse an identical five-section template every time. The container adapts to the meaning of the content.

## Proposed CSS tokens for the portable preview

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

- **Default flow:** small context/title → 1–2-line takeaway (one marked phrase) → essential explanation → optional structured object (facts / sequence / decision) → next action.
- **Keep content unboxed unless it earns a container.** More than two strong card surfaces on an ordinary response is a warning signal, not a hard ban.
- **No giant report heading for normal replies.** Reserve large heading/display styles for explicitly requested standalone reports.
- **Use at most one diagnostic question per turn, only if its answer changes what the Agent would do next.** Each option needs a distinct, truthful feedback path.
- **Responsive single column:** no forced side-by-side facts on narrow viewports; preserve reading order and generous touch zones.
- **Inline emphasis:** `**phrase**` creates a strong phrase; `==phrase==` creates subtle light-gray inline highlight in HTML and degrades to bold in Markdown. Never use HTML from user data.
- **Progressive disclosure:** optional native `<details>` only for supplementary explanation; never hide risk, caveat, or a required instruction.

## Evidence status and acceptance

Visual observations above are grounded in the supplied image. Exact CSS tokens are **inferred proposals**. Verify by rendering the demo at 360px, 768px and 1440px widths, confirming wrap, card balance, visible focus, radio selection and state-specific feedback. Static tests alone are not browser QA. The actual ChatGPT interface has private/native renderer behavior; a portable HTML Skill can closely approximate *design principles*, but cannot guarantee pixel-identical output or native in-chat widgets in Codex/Claude Code.
