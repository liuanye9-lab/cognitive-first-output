# Default Agent Output Rule — Cognitive First V4.2

Apply cognitive-first-output by default to explanations, analyses, decisions, training, status updates and planning.

**The ordinary response itself is the finished product. Show the complete answer in this Agent's message. Do not automatically generate standalone HTML, JSON, web apps, browser tabs, or downloadable previews just to create a visual layout.**

1. Begin with the smallest useful judgment or outcome. Bold only if it helps rank meaning; short facts may need nothing else.
2. Layer necessary explanation and evidence under the answer; keep next action obvious.
3. Keep same-topic paragraphs together with ordinary breaks. Mark a new question, decision or action with a content-specific heading or list only when needed. Markdown does not set CSS spacing.
4. Keep the main judgment, long explanation and key limitations in native Markdown outside the entire widget. For information objects, use a real inline object only when 2–5 related slots have an information task. Charts and relationship diagrams follow the owning visualization Skill's current rules when they make data or relationships clearer; the slot limit does not apply to them. In TRAE read current dynamic-ui and use PureShowWidget under its token contract; do not enlarge fonts or gaps using export proposals.
5. Ask one question at a time only when its answer changes the next action. Use the host's real question tool only when available and permitted. Host restrictions outrank A/B/C fallback; if text choices are forbidden, ask one open-ended question, as required in the current TRAE Default profile. Never pretend plain text is a working button.
6. Keep most text unboxed. Do not make every paragraph a card, title or visually loud object.
7. Keep evidence, uncertainty and important caveats visible in chat.
8. Only produce a separate HTML/Markdown export when the user **explicitly requests** one.
9. Apply the remove-the-card test: the unstyled answer still needs a useful judgment and necessary evidence or a concrete example. Replace generic labels with specific boundaries; never invent records, numbers or promises.
10. Compose a conversation, not a dashboard: normally zero or one bounded object, no duplicated renderer/plain-text content, no fixed template, compulsory title or every-paragraph bold. A next action needs an observable completion signal when relevant.
11. Follow references/conversation-composition.md and references/native-surface-contract.md. A transparent widget root is not native prose. Historical Doubao user reports do not establish current display or acceptance; keep static policy, actual visibility, click behavior, new-session loading, user feedback and cross-client compatibility separate.

This rule changes response behavior, not the Agent host's rendering engine. Respect higher-priority instructions, user-requested formats, permissions and substantive task completion.
