# Native surface contract · conversation-first V4

## Objective

Make the response itself the deliverable. The answer must not depend on a browser tab, downloaded HTML, local preview, or an attachment. Treat the current Agent interface as the available rendering environment. **A Skill controls instructions; it does not install a new renderer.**

## Capability ladder (try in order)

| Host capability confirmed in this session | Do | Do not |
| --- | --- | --- |
| Rich inline UI/components genuinely supported | Compose a restrained layout inline with native cards, labels, and one question when useful | Output HTML source and claim it became native UI |
| Interactive question tool supported | Ask through the real host question tool; handle the selected response next | Render a fake button in ordinary chat text |
| Markdown rendered in the chat | Use a bold lead, short paragraphs, blockquotes, compact labels or small tables | Promise exact background color, CSS spacing, radius or interactivity |
| Terminal/plain text only | Use one conclusion, spare whitespace, aligned simple labels, A/B/C text if needed | Draw fake clickable controls or ASCII UI furniture |

### Codex

- The host may expose a structured user-input tool; discover its actual availability. The App Server documents a request-user-input tool in supported flows, but that is not proof that every Codex CLI / IDE session exposes it.
- Codex chat and CLI clients control the rendering of its replies. Output Markdown or native supported rich structures. Do not assume raw HTML in a message is executed or shown as an embedded webpage.
- When an interactive tool is not available, ask one useful A/B/C question as text.

### Claude Code

- Interactive Claude Code sessions may offer AskUserQuestion. Use it only when actually available and the answer changes the workflow.
- Claude Code Desktop can preview **running applications** in a browser pane; that is a separate app preview, not proof of custom inline HTML components in the Agent response.
- Claude Code CLI is terminal-first. Use readable direct output; never automatically create a web page for an ordinary answer.

### ChatGPT or another UI-enabled host

- If the system explicitly provides native card, table, selection, or chart components, use those components under the host's rules and tool constraints.
- A host may offer interaction as a tool-call form rather than as an inline message widget. Keep questions integrated in the chat workflow, and never make a false claim that a clickable button is present.

## Minimal inline response patterns

### 1. Direct answer — no visual block

**先把题目压成一个任务标签。** 读原文时只带着“对象、动作、限制”去找证据，不用背完整题干。

### 2. Memory slots — native card if supported; otherwise labeled rows

> **本题要找**
>
> 对象：scientists
>
> 动作：abandon a theory
>
> 限制：after 2015 — why?

The blockquote is a *semantic fallback*, not a guarantee of a gray rounded card.

### 3. Native tool question or text fallback

当你找到原文后，哪个问题更常出现？

- A. 我记得问题，但读不懂关键句。
- B. 我能读懂一部分，却忘了原题在问什么。
- C. 我都能做到，但总是选错对应关系。

请回复 A/B/C。Only use this fallback if a real input UI is unavailable.

## Acceptance checks

1. One-line question: one-line answer, no file created.
2. Complex explanation: entire conclusion, evidence and action appears in message; no standalone HTML or JSON path.
3. Card scenario: real inline container if supported; otherwise compact labeled rows **inside the reply**.
4. Diagnostic scenario: native tool interaction if available; otherwise the question and response mechanism work across turns.
5. User explicitly asks for an interactive HTML deliverable: generate the separate page and explain it is an artifact, not the Agent chat surface.
6. Explicit user requests for plain text or a particular format override the default layout.
7. Never claim a pixel-perfect ChatGPT clone or call separate browser HTML an in-chat preview.

## Primary platform references (checked 2026-10-27)

- OpenAI Codex App Server, user input: https://developers.openai.com/codex/app-server
- OpenAI Codex skills: https://developers.openai.com/codex/build-skills
- Anthropic Claude Code tools: https://code.claude.com/docs/en/tools-reference
- Anthropic Claude Code Desktop browser pane: https://code.claude.com/docs/en/desktop
