---
description: "在指定位置创建结构柱，顶底由标高或高度与偏移决定；不做附着，类型不存在时列出可用类型。"
---

# 创建柱

`revit_create_column`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（集成分支）</span><span><b>发布版版本</b> 1.0.0</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    顶底标高与偏移由工具写、柱顶给标高或高度、不做附着、类型不存在列出可用类型。

在指定位置创建结构柱，顶底由标高或高度与偏移决定；不做附着，类型不存在时列出可用类型。

[同名发布版页面](../features/revit_create_column.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.0.0 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `base_offset_mm` | 否 | `0` | number | （集成分支契约未提供说明） |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `family` | 是 | — | string | （集成分支契约未提供说明） |
| `height_mm` | 否 | `null` | any | （集成分支契约未提供说明） |
| `level` | 是 | — | string | （集成分支契约未提供说明） |
| `rotation_deg` | 否 | `0` | number | （集成分支契约未提供说明） |
| `top_level` | 否 | `null` | any | （集成分支契约未提供说明） |
| `top_offset_mm` | 否 | `0` | number | （集成分支契约未提供说明） |
| `type_name` | 否 | `null` | any | （集成分支契约未提供说明） |
| `x_mm` | 是 | — | number | （集成分支契约未提供说明） |
| `y_mm` | 是 | — | number | （集成分支契约未提供说明） |

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
Place one structural column of `family` (optionally `type_name`) at `x_mm`, `y_mm` on `level`.

The top is either `top_level` or `height_mm` above the base (3000 mm when neither is given).
Base and top levels and both offsets are written by the tool itself, because they are
ElementId-valued parameters that revit_set_parameter refuses on purpose. The column is not
attached to anything: no attachment is attempted. dry_run returns the same verification
block without changing the model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
