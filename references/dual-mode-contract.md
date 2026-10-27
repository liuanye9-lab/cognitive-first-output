# Portable dual-mode contract

## Decision

Treat visual preview as the **default companion** for substantive answers whenever the Agent can write local files and return a working link/path. The native chat answer must remain self-sufficient (one conclusion, key evidence, next action). Do **not** open a browser tab automatically without the user's request.

Use a single answer JSON document to drive both representations:

- **Native Codex / Claude Code chat:** short human-readable Markdown, not fake radio buttons.
- **Standalone browser HTML:** same content, white canvas, pale-gray rounded information cards, dominant conclusion, optional interactive diagnostic question with local feedback.

For a one-sentence factual response, skip file creation. For explanations, decision support, training, process, or structured comparisons, generate the preview by default.

## Execution

1. Read `assets/example-answer.json` as the schema example.
2. Write an answer JSON with `schema_version: 1`, `title`, `lead`, optional `explanation`, `next_action`, and `blocks`.
3. Run the bundled renderer (Python 3.9+, standard library only):

```bash
python3 scripts/render_preview.py path/to/answer.json --output-dir path/to/output
```

4. Return a native-chat one-sentence conclusion and links/absolute paths to both generated files. If the environment supports embedded HTML preview, show it; otherwise provide a clickable file/link or explain how to open the HTML in a browser.
5. Never claim the HTML interaction automatically sends a message to the Agent. The demo's submit button displays deterministic feedback in the page; subsequent conversation requires the user to tell the Agent their choice.
6. If the environment cannot write files, preserve the same hierarchy in Markdown and say the interactive preview is unavailable.

The renderer refuses to overwrite existing output files unless `--force` is set.

## JSON blocks

| Type | Required fields | Visual treatment |
| --- | --- | --- |
| `facts` | `heading`, `items`: 2–5 `{label,value}` | One soft-gray labeled card |
| `steps` | `heading`, `items`: 2–5 `{title,detail}` | Vertical stages |
| `choice` | `heading`, `question`, `options`: 2–4 `{id,label,feedback}` | Actual radio group, submit, local feedback |
| `text` | `heading`, `body` | Ordinary readable prose |

Allow **at most one** `choice` block. Include it only when a choice changes feedback. IDs must be unique ASCII tokens.

## Design contract · V3 screenshot-grounded tokens

- White page; near-black high-contrast text; pale neutral-gray (`#f6f6f6`) for *selected* working-memory surfaces. Regular paragraphs have no card.
- Reading column `720px` max; 24px desktop and 16px mobile side gutters. Body `16px` / `1.75`, section titles `17px`, lead `19px`, first heading `22–27px`.
- Rounded information surfaces `14px`; 1px subdued border; 16–20px inner padding; compact rows. Substantial spacing between sections, close spacing within one topic.
- Use `**phrase**` for selective bold and `==phrase==` for muted inline highlight. HTML implementation always escapes content; Markdown reduces highlight to bold.
- 2–5 related slots per card; no nested decorative cards. Steps now use a compact vertical numbered list instead of a gray card per stage.
- High-contrast selectable radio inputs, disabled submit before selection, visible tailored feedback after submission.
- Native keyboard focus states; semantic labels; avoid unnecessary animation.
- No invented data, citations, or nonfunctional controls.

See [visual audit & token rationale](visual-audit-and-tokens.md) for the screenshot observations and what cannot be measured from the downscaled image.

## V3 block extensions (backward compatible with `schema_version: 1`)

| Type | Required fields | Presentation |
| --- | --- | --- |
| `callout` | `heading`, `body`; optional `eyebrow` | Subtle gray bordered reminder / principle |
| `details` | `heading`, `summary`, `body` | Native collapsible supplementary explanation |

Never hide decision-critical safety instructions, limitations, evidence, or caveats in `details`. Do not invent an interaction or use `choice` if the answer does not genuinely change the next step. Only use `**` and `==` as inline rich-text syntax; the renderer does not accept arbitrary HTML/Markdown.

## Acceptance tests

1. **Native/web parity:** same title, conclusion, facts, options, and action in both generated representations.
2. **Visual:** one pale-gray card and a readable step sequence; important conclusion remains above the fold.
3. **Interaction:** submit initially disabled; selecting B enables it; submission shows only B's feedback; changing to C clears the old feedback until resubmission.
4. **Security:** untrusted text HTML-escaped; no external runtime/network dependency; malformed JSON rejected.
5. **Responsive:** no sideways overflow at a mobile viewport, option labels wrap, controls remain tappable.
6. **Fallback:** if the terminal/IDE can't render HTML, native Markdown is still complete and honest.

`scripts/test_render_preview.py` checks static contract, backwards compatibility and safety. Visual and interaction checks require opening the generated HTML in a real browser; a passing unit test is **not** proof of visual fidelity or real-click behavior. Screen compare at 360px, 768px, and 1440px and verify keyboard focus, selection, feedback reset, readability, and zero overflow.
