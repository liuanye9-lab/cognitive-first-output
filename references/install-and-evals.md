# Install and evaluate · V4.2 conversation composition

## Deployment

1. Extract the ZIP. One cognitive-first-output folder contains SKILL.md, assets, references and scripts.
2. **Replace the older V3/V4 skill** in the location supported by your current Agent only when installation/update is authorized. Local editing or packaging does not authorize global installation, Git commits or pushing. Avoid two active copies with identical skill names; preserve rollback outside active skill roots or in version control.
3. Merge, rather than overwrite, assets/default-agent-rule.md into the project's AGENTS.md (Codex) or CLAUDE.md (Claude Code) if you require this style for all tasks. Check precedence against higher-priority instructions.
4. Reload or refresh the Agent's skills as supported by its client. Installing a skill alone may not trigger it automatically for every reply.
5. Verify the actual response in its **current chat window**, not an HTML preview in a browser.

## Behavioral acceptance tests (run in the actual target host)

| User prompt | Required result |
| --- | --- |
| “法国的首都是哪里？” | Single short response; no file, preview, quiz |
| “解释为什么 Agent 常常需要追问用户” | Useful judgment, concrete example and key limitations in native Markdown outside the entire widget; no compulsory question or plan; no HTML/JSON file |
| “用灰色卡片总结对象、动作、限制” | One 2–5-slot information object only if permitted and clearer than Markdown; in TRAE use current dynamic-ui and PureShowWidget; no duplicated prose or external link |
| “比较这两个方案” | Exact differences in a compact table or permitted object; judgment and important tradeoffs remain in native prose |
| “直接执行这个已明确的任务” | Execute without decorative questions; report evidence and an observable completion signal |
| “当前只有 Markdown，让回复像截图” | Semantic grouping only; no promised CSS, fake controls or renderer call |
| “出一道判断我注意力问题的选择题” | One decision-changing question via a permitted native tool; if text choices are forbidden, one open-ended question; genuine next-turn adaptation |
| “给我建议，但这个方案有重要限制” | Keep uncertainty and key limitations visible in native Markdown; no tiny metadata or hidden disclosure |
| “用纯文本回答” | Plain text wins, no card or file |
| “专门制作一个可单独打开的 HTML 交互页面” | **This case only:** export requested HTML/Markdown and give links |

## Known platform boundary

- Host display determines typography, spacing, cards, and interactivity. The Skill cannot force exact ChatGPT widgets into a terminal or IDE.
- TRAE body prose stays outside PureShowWidget. Current dynamic-ui typography, spacer, theme and radius tokens override optional standalone export proposals; a transparent widget root still uses compact widget type.
- Tool availability is not permission. Host/mode restrictions outrank A/B/C fallback; the current TRAE Default profile requires an open-ended fallback when its question tool is not permitted.
- Codex App Server documents an experimental user-input request tool in supported hosts; do not assume it exists in every session.
- Claude Code documents AskUserQuestion; Claude Code Desktop can preview an app in a browser pane, distinct from native message HTML.
- The optional web renderer remains a standalone file. Its radio selection only updates the web page and never automatically replies to the Agent.

See native-surface-contract.md for decision rules and official documentation references.

## V4.2 composition acceptance

- Historical user report: an isolated Doubao card was unsatisfactory; a revised sample with a concrete judgment, mostly unboxed explanation and one boundary object was described as the right direction. This is not full behavioral or cross-client acceptance, current TRAE display evidence or current V4.2 user approval.
- Test ordinary facts, substantive explanation, a comparison, uncertainty, a clear execution request and explicit plain text. Do not force each into the same three-section template.
- For long explanation plus an information object, inspect the physical boundary: judgment, reasons and key limitations must remain outside the entire widget, not merely outside an inner card. Check that slots do not repeat the prose.
- Check same-topic paragraphs stay grouped and topic changes have semantic headings or lists when needed. Hierarchy does not require larger type, fixed sections, every-paragraph bold or more cards.
- For the illustrative customer-summary case, preserve “考虑一下” as tentative; never rewrite it as “确认采购”. A next action should make the verification criterion visible.
- In the actual host, check the first-screen judgment, selective emphasis, one bounded object, wrapping and substantive completeness. Native questions need a real response and subsequent adaptation.
- Record static-policy tests, exporter tests, user visual feedback, real-click tests, new-session loading and cross-client checks separately. No passing string assertion proves improved reasoning or UI parity.
- V4.2 changes instructions and composition resources, not the retained V3 exporter, dual-mode contract or example export assets. The exporter remains opt-in.

## Exporter regression tests

In the Skill root:

```bash
PYTHONPYCACHEPREFIX=/tmp/cognitive-first-output-pycache python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

These are code and static-policy tests. They cannot prove what the host visually renders, that a particular question tool is available, or that a real interaction has been clicked. Perform manual behavioral evaluations above in the actual target host and record display and user feedback separately. Do not claim native UI parity from static or exporter tests.
