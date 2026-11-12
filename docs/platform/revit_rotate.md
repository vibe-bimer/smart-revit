---
description: "绕穿过 `center_mm` 的竖轴旋转，或不给点时按组合包围盒中心旋转。"
---

# 旋转构件

`revit_rotate`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 基座（上游）</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.4</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

绕穿过 `center_mm` 的竖轴旋转，或不给点时按组合包围盒中心旋转。

[同名发布版页面](../features/revit_rotate.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.4 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `angle_deg` | 是 | — | number | （开发线契约未提供说明） |
| `center_mm` | 否 | `null` | any | （开发线契约未提供说明） |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `element_ids` | 是 | — | array | 要处理的构件 Revit ID 列表。 |

</div>

### 通用参数 {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | 否 | `null` | any | 打开多个模型时，用标题或路径指定目标文档。 |

</div>

## 功能说明（注册表原文） {#behavior}

以下保留工具在注册表中声明的英文原文，作为契约来源。

```text
Rotate elements about a vertical axis through center_mm, or through their combined bounding box center. dry_run rolls back. Group members, pinned, hosted and constrained elements are reported in skipped.inGroup, skipped.pinned, skipped.hosted and skipped.constrained and are not changed; the call is refused if every element is a group member.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
