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

## 2. Diagnostic multiple-choice

**User:** 读原文后又忘记题干，我该怎么办？

**Fast layer:** 先判断是“保持任务失败”还是“理解原文困难”。

**Ask one question:**

“定位到原文后，如果立刻回看题目，你通常会怎样？”

- A. 能想起要找什么，也基本读懂原文。
- B. 能想起要找什么，但读不懂关键句。
- C. 读懂一些原文，却忘了题目问什么。

**Platform:** Prefer real radio options with a **提交** action when supported. On text-only surfaces ask the user to reply A/B/C. No fake button.

**After selection:** A → speed and evidence alignment; B → sentence parsing; C → task-label retention. Mark these as tentative hypotheses.

**Test:** Each option changes the next step; exactly one question; no default selection.

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
