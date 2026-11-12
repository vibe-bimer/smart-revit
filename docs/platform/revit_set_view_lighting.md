---
description: "设置一个视图的阴影、太阳位置、地平面、背景与渲染光照方案；响应给出改动前后的读数与变化项清单。"
---

# 设置视图光照

`revit_set_view_lighting`

<p class="facts"><span><b>分组</b> 视图、图纸与明细表</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.4</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    在两条线上都在：fork 注册表接上兜底钩子，Python 工具、C# 编译与真机验证齐备。

设置一个视图的阴影、太阳位置、地平面、背景与渲染光照方案；响应给出改动前后的读数与变化项清单。

[同名发布版页面](../features/revit_set_view_lighting.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.4 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `background` | 否 | `null` | any | （开发线契约未提供说明） |
| `background_colors` | 否 | `null` | any | （开发线契约未提供说明） |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `ground_plane` | 否 | `null` | any | （开发线契约未提供说明） |
| `ground_plane_level` | 否 | `null` | any | （开发线契约未提供说明） |
| `lighting_scheme` | 否 | `null` | any | （开发线契约未提供说明） |
| `shadow_intensity` | 否 | `null` | any | （开发线契约未提供说明） |
| `shadows` | 否 | `null` | any | （开发线契约未提供说明） |
| `sun_altitude_deg` | 否 | `null` | any | （开发线契约未提供说明） |
| `sun_azimuth_deg` | 否 | `null` | any | （开发线契约未提供说明） |
| `sun_date` | 否 | `null` | any | （开发线契约未提供说明） |
| `sun_time` | 否 | `null` | any | （开发线契约未提供说明） |
| `sunlight_intensity` | 否 | `null` | any | （开发线契约未提供说明） |
| `view` | 是 | — | string | 视图的准确名称或十进制视图 ID。 |

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
Set a view's lighting: shadows, sun position, ground plane, background and lighting scheme.

View-specific sun and shadow settings; a view that shares them passes the change on.
Sun angles come as a pair, and gradient colors need the gradient background.
dry_run returns the same verification block without changing the model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
