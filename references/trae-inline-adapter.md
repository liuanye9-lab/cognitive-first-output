# TRAE 内联信息对象适配

原生 Markdown 承载主体：判断、必要解释、限制和相关下一步。不要把整个答复放进组件，或把资源当独立网页、应用、下载与用户预览。

[信息对象资源](../assets/trae-information-object.html) 只是受当前工具规范约束的借用示例。仅在分组确有阅读收益时，用 `PureShowWidget` 呈现这一个有信息任务的小对象；正文不重复槽位内容，普通短事实或三步操作保留 Markdown。

## 使用顺序

1. 确认当前会话确实暴露并允许调用 `PureShowWidget`；Skill 提到工具名不等于工具可用或获准调用。
2. 先读当前 `dynamic-ui/SKILL.md`、`tokens/visual-tokens.md`、`templates/manifest.json` 和合适 scene。规范或工具变化时先读新规则，再调整或放弃示例；实际工具契约优先于缓存资源。
3. 核对信息任务与 Token 后，读取片段，按当前任务替换值并进行 HTML 转义。把最终完整片段作为 `widget_code` 交给工具；不主动传 `mode`，不选择 `panel`，不在正文展示源码。

本例借用 `explanation-panel` fallback primitive：一个扁平 `<dl>`，三个槽位分别承担目标、原因和下一步。使用前重新核对当前 manifest、候选材料的适用与排除规则，以及相关 scene；有合适 ready 材料时优先按其指导适配。本例只借用单容器结构，不是流程或机制图，不把普通三步列表或三句解释强行画图。

## 保持约束

- 顺序是 `<style>` 再内容 HTML；Token 在组件选择器之前。没有 DOCTYPE、页面外壳、脚本、外部依赖、导出或假按钮。
- 根带 `data-dynamic-ui-widget` 与消歧的 `data-template="cognitive-first-output-trae-information-object"`；这是示例标识，不是 ready template id，不修改 manifest。
- 只含「记住什么／为什么／下一步」三槽。首槽居首并用正文中等字重作唯一焦点；全宽 `100%`、自然高度、值可 wrap，无额外标题、嵌套卡片、裁剪或滚动。窄屏允许增加视觉行数。
- `:root` 提供 light 默认值，`:root[data-widget-theme="dark"]` 提供 dark 覆盖；宿主设置 `data-widget-theme`。所有颜色、字体、间距、圆角引用当前 Token：中性 `--surface` 与 `--border`，`--radius-card` 为 12px，间距为 `--spacer-12`、`--spacer-16`。
- 字体用当前完整 `--font-sans` 栈，正文 `--text-body` 为 14px/20px，label `--text-caption` 为 12px/18px；标题上限 `--text-title` 为 16px/24px，本例不另加标题。不放大字号绕过规范。

## 能力不足时

工具未暴露、规范不允许或渲染失败时 fallback 到原生 Markdown，保留必要槽位；成功显示则不再重复：

> 记住什么：先找到一个判断
>
> 为什么：减少来回寻找
>
> 下一步：需要时再展开细节

不承诺整段 CSS、客户端样式或截图像素复现，不为普通回复另建应用或浏览器预览。静态校验不等于实际会话显示，也不等于用户视觉接受度；实际显示、真实交互、用户反馈与跨宿主兼容需要分别验证。
