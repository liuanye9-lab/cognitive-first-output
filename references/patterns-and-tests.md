# Patterns and tests

## 1. Neutral-gray memory slots — IELTS reading

**User:** 定位到题目之后，还是忘了自己在找什么。

**Fast layer:** **不要背整个英文题干，只保留一个中文任务标签。**

**Soft-gray card** — render as a real neutral surface only when supported:

| 信息槽 | 内容 |
| --- | --- |
| 对象 | scientists（科学家） |
| 动作 | abandon a theory（放弃理论） |
| 限制 / 目标 | after 2015 → why? |

**Slow layer:** 精读前复述“找2015年之后放弃理论的原因”。定位时只找位置，理解时才集中精力判断原因。

**Action:** 用一句中文复述当前要寻找的信息，而不是逐词翻译。

**Test:** Object/action/constraint visible in one glance on a phone.

## 2. Diagnostic question

**User:** 读原文后又忘记题干，我该怎么办？

**Fast layer:** 先收集线索，验证“保持任务失败”或“理解原文困难”的假设。

**Platform first:** Before presenting any options, confirm that the current host actually exposes a native question tool and permits it in the current mode. Availability alone is not permission. Choose exactly one branch:

1. **Native allowed:** Use the real, permitted question tool first, with the question and choices below under its supported input contract. Do not repeat them as a text quiz.
2. **Text allowed, no permitted native tool:** Only if the host explicitly permits text multiple-choice, show the question and A/B/C choices below and say "回复 A/B/C".
3. **Text forbidden or permission unknown, no permitted native tool:** Ask only the open-ended question below. Do not show choices, or list them first and explain restrictions afterward.

**Ask exactly one question:**

“定位到原文后，如果立刻回看题目，你通常会怎样？”

**Choices (native or explicitly permitted text-choice branch only):**

- A. 能想起要找什么，也基本读懂原文。
- B. 能想起要找什么，但读不懂关键句。
- C. 读懂一些原文，却忘了题目问什么。

**After response:** A → test speed and evidence alignment; B → test sentence parsing; C → test task-label retention. Treat these as hypotheses to verify, not diagnoses from a selection. For an open-ended answer, choose a matching hypothesis or leave it unresolved; verify it with a concrete reading attempt before drawing a conclusion.

**Test:** Check host availability and permission before any options; exercise native allowed, text allowed and text forbidden branches. Each rendered branch has exactly one question, no default selection or fake button; only permitted branches show choices, and every answer leads to a hypothesis to verify.

## 3. Process — attention route

If the sequence itself matters, present the following as short stacked stages:

1. 读题：对象 / 动作 / 限制
2. 压缩：只保留任务标签
3. 定位：寻找相关区间
4. 精读：理解主干与证据
5. 匹配：回看限制，判断答案

**Test:** Every stage identifies a mental judgment or observable action. If a simple list is enough, skip the diagram.

## 4. Simple answer — no visual

**User:** IELTS 代表什么？

**Response:** **IELTS** 是 International English Language Testing System，也就是国际英语语言测试系统。

**Test:** No card, chart, quiz, or multi-section layout.

## Acceptance checks

1. **Five-second skim:** The first visible lines reveal the point and next action.
2. **Visual utility:** Remove any element that doesn't improve understanding.
3. **Truthful prominence:** Importance determines visual weight; avoid uniform emphasis.
4. **Real interactions:** No inert buttons, and a selection actually changes follow-up.
5. **Fallback:** Text-only Agents express the same relationships accurately.
6. **Mobile:** Avoid wide tables if stacked labels are easier.
7. **Evidence:** Distinguish findings, hypothesis, self-report, and verification.
8. **Faithfulness:** User instructions, safety, accuracy, citations, and scope win over aesthetics.
