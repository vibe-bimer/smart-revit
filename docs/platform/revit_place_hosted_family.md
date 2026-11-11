---
description: "把单层宿主族放到墙面上，点名宿主或就近找墙；并列与超半径被拒并列出候选。"
---

# 放置宿主族

`revit_place_hosted_family`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.1</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    点名宿主或就近找墙、并列与超半径被拒并列出候选、回报 hostResolution、支持窗台与翻转、非零角度与非单层宿主族被拒。

把单层宿主族放到墙面上，点名宿主或就近找墙；并列与超半径被拒并列出候选。

[同名发布版页面](../features/revit_place_hosted_family.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.1 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `family` | 是 | — | string | （开发线契约未提供说明） |
| `flip_facing` | 否 | `null` | any | （开发线契约未提供说明） |
| `host_element_id` | 否 | `null` | any | （开发线契约未提供说明） |
| `host_search_radius_mm` | 否 | `2000` | number | （开发线契约未提供说明） |
| `level` | 否 | `null` | any | （开发线契约未提供说明） |
| `rotation_deg` | 否 | `0` | number | （开发线契约未提供说明） |
| `sill_height_mm` | 否 | `null` | any | （开发线契约未提供说明） |
| `type_name` | 否 | `null` | any | （开发线契约未提供说明） |
| `x_mm` | 是 | — | number | （开发线契约未提供说明） |
| `y_mm` | 是 | — | number | （开发线契约未提供说明） |

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
Place one door, window or other one-level hosted family of `family` at `x_mm`, `y_mm`.

The host is either the wall named by `host_element_id`, or the nearest wall of the placement
level whose location line passes within `host_search_radius_mm` of the point; `level` defaults
to the level whose elevation is closest to the point. A missing host, a distance over the
radius or two equally near walls are refused with the candidates, so the caller can name one.
The response reports `fork.hostResolution` ({mode, hostId, distanceMm}), which is why a dry
run already shows the wall the family would hang on. `sill_height_mm` writes the family's own
INSTANCE_SILL_HEIGHT_PARAM and `flip_facing` calls flipFacing(). `rotation_deg` must be 0: a
hosted instance takes its orientation from its host wall, so use `flip_facing` to turn it
around. Families that are not one-level hosted are refused: revit_place_family places those,
and it is the one that rotates. Nothing is attached to the host, because a door or a window
has no attachment target. dry_run returns the same verification block without changing the
model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
