# Install and evaluate · V4 inline-first

## Deployment

1. Extract the ZIP. One cognitive-first-output folder contains SKILL.md, assets, references and scripts.
2. **Replace the older V3 skill** in the location supported by your current Agent. Avoid keeping two copies with identical skill names; the runtime may select the wrong version.
3. Merge, rather than overwrite, assets/default-agent-rule.md into the project's AGENTS.md (Codex) or CLAUDE.md (Claude Code) if you require this style for all tasks. Check precedence against higher-priority instructions.
4. Reload or refresh the Agent's skills as supported by its client. Installing a skill alone may not trigger it automatically for every reply.
5. Verify the actual response in its **current chat window**, not an HTML preview in a browser.

## Behavioral acceptance tests (run in actual Codex / Claude Code)

| User prompt | Required result |
| --- | --- |
| “法国的首都是哪里？” | Single short response; no file, preview, quiz |
| “用第一性原理解释雅思阅读定位” | Conclusion + evidence + next step entirely in the current Agent message; no HTML/JSON file |
| “用灰色卡片总结对象、动作、限制” | Native card only if host supports it, else an inline labeled list/table; no external link |
| “出一道判断我注意力问题的选择题” | Native question tool if available; otherwise A/B/C text and genuine next-turn response |
| “用纯文本回答” | Plain text wins, no card or file |
| “专门制作一个可单独打开的 HTML 交互页面” | **This case only:** export requested HTML/Markdown and give links |

## Known platform boundary

- Host display determines typography, spacing, cards, and interactivity. The Skill cannot force exact ChatGPT widgets into a terminal or IDE.
- Codex App Server documents an experimental user-input request tool in supported hosts; do not assume it exists in every session.
- Claude Code documents AskUserQuestion; Claude Code Desktop can preview an app in a browser pane, distinct from native message HTML.
- The optional web renderer remains a standalone file. Its radio selection only updates the web page and never automatically replies to the Agent.

See native-surface-contract.md for decision rules and official documentation references.

## Exporter regression tests

In the Skill root:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

These are code and static-policy tests. They cannot prove what the host visually renders, that a particular question tool is available, or that a real user interaction has been clicked. Perform the six manual behavioral evaluations above in the actual target host before claiming native UI parity.
