# Native surface contract · conversation-first V4.2

## Objective

Make the response itself the deliverable. The answer must not depend on a browser tab, downloaded HTML, local preview, or an attachment. Treat the current Agent interface as the available rendering environment. **A Skill controls instructions; it does not install a new renderer.**

## Capability ladder (subject to current host and mode restrictions)

Main judgment, long explanation and important limitations remain in native conversation Markdown, or plain text in a terminal. Rich rendering is an optional information object, chart or relationship diagram, not an alternate container for the whole reply. Availability alone is not permission to call a tool.

| Host capability confirmed in this session | Do | Do not |
| --- | --- | --- |
| Rich inline UI/components genuinely supported and permitted | Show a useful information object, chart or relationship diagram alongside native prose | Wrap the whole reply or claim HTML source became native UI |
| Interactive question tool supported and permitted | Ask one decision-changing question; handle the response next | Bypass mode restrictions with a fake button or text choices |
| Markdown rendered in the chat | Use a direct judgment, short paragraphs, selective emphasis, lists or small tables | Promise exact background color, CSS spacing, radius or interactivity |
| Terminal/plain text only | Use one conclusion and simple semantic groups; text choices only if allowed | Draw fake clickable controls or ASCII UI furniture |

Host tool restrictions outrank A/B/C text fallback. If no question tool is permitted and text multiple-choice is prohibited, ask one open-ended question. Do not switch modes solely to obtain a decorative input control.

### TRAE: current dynamic-ui route

1. Confirm this session actually exposes and permits `PureShowWidget`; mentioning it in a Skill does not add the tool. Read current `dynamic-ui/SKILL.md`, its tokens, relevant scene and material guidance before rendering.
2. Put judgment, explanation, important limits and relevant next action in native Markdown outside the entire widget. For information objects, render a compact 2–5-slot object only when grouping, comparison or retention becomes clearer. Charts and relationship diagrams follow the owning visualization Skill's current rules when they make data or relationships clearer; the slot limit does not apply to them. Do not repeat the slots in prose or insert the whole lead/reason/key-object/details reply.
3. Submit the final fragment as `widget_code` through the tool, not as HTML fenced text. Do not pass `mode` unless the runtime requires it; never choose `panel`. Follow current wrapper, theme, root, accessibility and safety rules.
4. Current `dynamic-ui` tokens take priority, including custom/fallback objects. Body uses `--text-body` (14px/20px), titles use `--text-title` (16px/24px maximum), and layout uses `--spacer-4`, `--spacer-8`, `--spacer-12`, `--spacer-16`, `--spacer-20`, `--spacer-24` and the documented radius tokens. Read the current definitions; never substitute export proposals or invent larger type/gaps.
5. If the object cannot fit, move detail to native prose or choose a list/table. If the tool is absent, disallowed or fails to render, provide the needed object content in Markdown. Do not duplicate an object that successfully displayed.
6. In the current TRAE Default profile, the host does not permit text multiple-choice as a substitute for its restricted question tools. Ask one open-ended question only if its answer changes the next action; an already clear task needs none.

Read the [TRAE inline adapter](trae-inline-adapter.md) and borrow the [information-object fragment](../assets/trae-information-object.html) only after checking current host rules. It is an example, not a ready material registration, webpage or fixed reply template.

### Codex

- The host may expose a structured user-input tool; discover its actual availability. The App Server documents a request-user-input tool in supported flows, but that is not proof that every Codex CLI / IDE session exposes it.
- Codex chat and CLI clients control the rendering of its replies. Output Markdown or native supported rich structures. Do not assume raw HTML in a message is executed or shown as an embedded webpage.
- When an interactive tool is unavailable or disallowed, ask one useful open-ended question. A/B/C text is an option only if current host rules permit it.

### Claude Code

- Interactive Claude Code sessions may offer AskUserQuestion. Use it only when actually available and the answer changes the workflow.
- Claude Code Desktop can preview **running applications** in a browser pane; that is a separate app preview, not proof of custom inline HTML components in the Agent response.
- Claude Code CLI is terminal-first. Use readable direct output; never automatically create a web page for an ordinary answer.

### Doubao Work: historical user report

A historical user report described a static renderer card as visible and a later composition sample as the right direction. This is not current-session or cross-host acceptance, and does not establish that any current host exposes that route.

1. Read the current doubao-visualization Skill and the relevant renderer contract when applicable. Use the exact host-declared `html type="renderer"` fenced wrapper; ordinary raw HTML is not equivalent.
2. Keep the substantive prose in native Markdown; use the declared renderer only for a bounded information object. Do not write an HTML file, start a server or open a browser just to style the response.
3. If rendering fails or the host route is absent, keep the substantive answer available in Markdown. Do not call a separate browser page an in-chat preview.
4. Use the native question tool for a decision-changing question. Static card visibility does not prove script execution, button clicks or that an in-page form sends answers to chat.
5. See [conversation composition](conversation-composition.md) for rhythm. Its numerical proposals apply only to optional standalone exports, not this inline route or official ChatGPT CSS.

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

### 3. Native tool question or permitted text fallback

Only ask if the answer changes the next action. Prefer a permitted native tool. If the host prohibits text choices, ask “读原文时，你最容易在哪一步卡住？” instead of the options below.

当你找到原文后，哪个问题更常出现？

- A. 我记得问题，但读不懂关键句。
- B. 我能读懂一部分，却忘了原题在问什么。
- C. 我都能做到，但总是选错对应关系。

请回复 A/B/C。Only use this fallback if a real input UI is unavailable or disallowed **and the host permits text multiple-choice**; it is not the current TRAE Default fallback.

## Acceptance checks

1. One-line question: one-line answer, no file created.
2. Complex explanation: judgment, evidence, long explanation and important limitations stay outside the entire widget in native Markdown; relevant action appears in message; no standalone HTML or JSON path.
3. Card scenario: real inline container if supported; otherwise compact labeled rows **inside the reply**.
4. Diagnostic scenario: one question only when decision-changing; use a permitted native tool or permitted text fallback, then adapt across turns. Host restrictions override text choices.
5. User explicitly asks for an interactive HTML deliverable: generate the separate page and explain it is an artifact, not the Agent chat surface.
6. Explicit user requests for plain text or a particular format override the default layout.
7. Never claim a pixel-perfect ChatGPT clone or call separate browser HTML an in-chat preview.

## Primary platform references (checked 2026-10-27)

- OpenAI Codex App Server, user input: https://developers.openai.com/codex/app-server
- OpenAI Codex skills: https://developers.openai.com/codex/build-skills
- Anthropic Claude Code tools: https://code.claude.com/docs/en/tools-reference
- Anthropic Claude Code Desktop browser pane: https://code.claude.com/docs/en/desktop
