# Optional export contract · V4 (not the chat default)

## Invocation guard

Read this contract **only** when the user explicitly asks for a separate HTML page, downloadable visual preview, standalone interactive web artifact, or file export. Do not infer such a request from "make your reply clearer", "visualize this response", or "use the Skill" alone.

The default answer always appears fully in the **current conversation**. An HTML page is an optional secondary artifact, never a substitute for that answer. The user should not need to open a file to understand the conclusion and next action.

## Reuse of the V3 exporter

When a separate webpage is explicitly requested, create one JSON answer document following assets/example-answer.json. It supports these semantic blocks:

| Block | Content | HTML presentation |
| --- | --- | --- |
| facts | 2–5 label/value pairs | One light-gray rounded card |
| steps | Ordered short stages | Compact vertical sequence |
| text | Heading and explanatory body | Unboxed prose |
| callout | Label and short principle | One restrained gray callout |
| details | Optional extra explanation | Collapsible disclosure |
| choice | One question with 2–4 options and feedback | Real radio inputs, local submit feedback |

Then run:

```bash
python3 scripts/render_preview.py path/to/answer.json --output-dir ./output
```

The renderer emits HTML and Markdown. It refuses to overwrite without --force. The exported page is self-contained. The in-page choice **does not connect to the Agent conversation**, and its local feedback must not be misrepresented as ChatGPT/Codex/Claude native controls.

Use **phrase** for bold and ==phrase== for subtle gray highlight inside the JSON content. The exporter safely escapes HTML. Do not invent numbers, sources, true selections, or interactive affordances.

## Screenshot-inspired tokens for optional HTML

- White canvas, max 720px reading width, 16px body/1.75 line height.
- Pale neutral-gray #f6f6f6 for selected bounded information cards, not all paragraphs.
- Compact 2–5 label/value memory slots, 14px radius and comfortable padding.
- Restrained bold. Real radio selection only where a true interactive page is delivered.
- Layout responsive on 360px–1440px width; verify in browser if claiming visual QA.

For complete rationale see visual-audit-and-tokens.md. Exporter tests validate structural behavior but cannot prove pixel-level fidelity or actual browser clicking.
