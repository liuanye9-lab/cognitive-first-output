# Default Agent Output Rule — Cognitive First V4

Apply cognitive-first-output by default to explanations, analyses, decisions, training, status updates and planning.

**The ordinary response itself is the finished product. Show the complete answer in this Agent's message. Do not automatically generate standalone HTML, JSON, web apps, browser tabs, or downloadable previews just to create a visual layout.**

1. Begin with the one-sentence outcome; selectively **bold** the crucial phrase.
2. Layer necessary explanation and evidence under the answer; keep next action obvious.
3. Use whitespace, short blocks, clear labels, a compact table or a list directly in chat.
4. Use real inline pale-gray cards **only if the current host can render them**. Otherwise use Markdown; do not inject raw HTML/CSS and call it a card.
5. Use the host's real interactive question tool when available, appropriate and permitted; otherwise ask the user to reply A/B/C. Never pretend plain text is a working button.
6. Keep most text unboxed. Do not make every paragraph a card, title or visually loud object.
7. Keep evidence, uncertainty and important caveats visible in chat.
8. Only produce a separate HTML/Markdown export when the user **explicitly requests** one.

This rule changes response behavior, not the Agent host's rendering engine. Respect higher-priority instructions, user-requested formats, permissions and substantive task completion.
