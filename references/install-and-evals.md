# Install and evaluate in Codex / Claude Code

## Principle: separate the skill from the host renderer

The Skill sets an answer structure; the host controls native chat rendering. In a terminal, Markdown never magically becomes ChatGPT's browser-only controls. The bundled Python CLI creates a portable, standalone HTML companion with working **local** radio-choice feedback; it cannot automatically post that answer into the Agent conversation.

## Install

1. Extract the ZIP. It contains one folder `cognitive-first-output/` with `SKILL.md`, `scripts/`, `assets/`, and `references/`.
2. Move that folder into a **supported skill location for your installed Agent version**. Codex and Claude Code support Agent Skills with `SKILL.md` and resource folders; check their current official docs for location and reload behavior. Claude Code documents project `.claude/skills/<skill-name>/SKILL.md` and personal `~/.claude/skills/<skill-name>/SKILL.md`.
3. Add or merge the content of `assets/default-agent-rule.md` into your Agent's standing instruction file (project `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code) if you want this preference applied by default across tasks. **Do not overwrite** existing instructions or project policy. Merely installing a skill doesn't guarantee invocation every turn.
4. In the Skill folder run `python3 -m unittest discover -s scripts -p 'test_*.py' -v`.
5. In an Agent session, ask: "用 cognitive-first-output 回答一个简短问题，再解释一个需要步骤的难题，附网页预览。" Confirm correct restraint, functioning file path, and full native-chat answer.

## Visual and interaction manual QA

Open `assets/example-answer.html` locally in a browser (only where local HTML preview is supported):

| Test | Expected result |
| --- | --- |
| 360px width | Single column, readable typography, no horizontal scrolling, options wrap |
| 768px and 1440px widths | Content stays ~720px max; generous whitespace; cards not stretched |
| First 5 seconds | Main takeaway readable without deciphering a full report |
| Select B | Radio becomes selected; submit becomes enabled |
| Submit B | Only B's tailored feedback appears in the page |
| Select C after B | Previous feedback disappears until C submission |
| Keyboard Tab / Space | Focus remains obvious; radio choices work without mouse |
| Screenreader semantics | Heading order, fieldset legend, labeled radio, live feedback |

Do not claim the browser checks passed unless a human or permitted browser automation actually performed them. Static unit tests exercise generated HTML and deterministic JavaScript contracts, not pixels or real clicks.

## Behavior eval prompts

| Input | Pass condition |
| --- | --- |
| "法国首都是哪里？" | Short plain answer, no compulsory report/card/quiz |
| "用第一性原理解释雅思定位和理解" | 1-line conclusion → minimal steps → optional detail, short native answer, HTML companion when allowed |
| "我定位后忘题干，是哪一类？" | At most one useful 2–4-option diagnosis, tailored feedback |
| "只用纯文本给我" | Follows explicit format; no forced HTML |
| "写一个有风险的决定方案" | Critical constraints visible, never hidden only in collapsible details |
| "现在无法写文件" | Honest Markdown fallback; no claimed interactive button |
| "把 `<script>` 当标题显示" | Literal escaped content, never executable HTML injection |

## Limitations

- No official ChatGPT CSS or design tokens are bundled; values are informed visual approximations from a downscaled user screenshot.
- Generated HTML is self-contained and does not require a network connection; **in-page** feedback works without an Agent session.
- Exact host UI, live in-chat interactions, and auto-opening of file previews depend on the Codex / Claude Code client and permissions.
- The Agent should provide a native answer even if HTML creation, browser preview, or optional script execution fails.
