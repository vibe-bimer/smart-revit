---
description: "按曲线与标高创建梁，端点不做吸附；结构用途按枚举写入，竖向偏移先写族的标高参数再退到移动实例。"
---

# 创建梁

`revit_create_beam`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.0.0</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    走曲线加标高的重载、端点不吸附、结构用途按枚举写入、竖向偏移先写族的标高参数再退到移动实例。

按曲线与标高创建梁，端点不做吸附；结构用途按枚举写入，竖向偏移先写族的标高参数再退到移动实例。

[同名发布版页面](../features/revit_create_beam.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.0.0 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `end_mm` | 是 | — | array | （开发线契约未提供说明） |
| `family` | 是 | — | string | （开发线契约未提供说明） |
| `level` | 是 | — | string | （开发线契约未提供说明） |
| `start_mm` | 是 | — | array | （开发线契约未提供说明） |
| `structural_usage` | 否 | `null` | any | （开发线契约未提供说明） |
| `type_name` | 否 | `null` | any | （开发线契约未提供说明） |
| `z_offset_mm` | 否 | `0` | number | （开发线契约未提供说明） |

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
Place one structural beam of `family` (optionally `type_name`) along the axis `start_mm`-`end_mm`.

`level` is the reference level of the framing, and the two axis points are [x, y] in
millimetres. The placement uses the curve-and-level overload, so the level and the axis are
both given explicitly; the axis is not snapped, because Revit has no snapping API and
SetEndReference only acts on an end the model already joined. `structural_usage` writes
FamilyInstance.StructuralUsage. `z_offset_mm` is the vertical offset above the reference
level: the tool writes it through the elevation parameters that carry it, and only a write that
lifts the bounding box counts, because a family can take the value and keep the beam on its
level; the instance moves instead when no parameter lifts it, and the call fails when neither
route works, so a refused offset never passes as a beam placed on the level. The read-back names
the parameter holding the offset or leaves it out when the geometry carries the shift. dry_run
returns the same verification block without changing the model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
