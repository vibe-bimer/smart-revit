---
description: "在给定标高的闭合轮廓上创建楼板；`dry_run` 会回滚。"
---

# 创建楼板

`revit_create_floor`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.3</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    按新契约重映射到 fork 注册表，带 dry_run 与验证块。

在给定标高的闭合轮廓上创建楼板；`dry_run` 会回滚。

[同名发布版页面](../features/revit_create_floor.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.3 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `floor_type` | 否 | `null` | any | （开发线契约未提供说明） |
| `level` | 是 | — | string | （开发线契约未提供说明） |
| `points_mm` | 是 | — | array | （开发线契约未提供说明） |

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
Create a floor from a closed boundary on a level.

`points_mm` is the polygon, three vertices or more, each [x, y] in millimetres; consecutive
duplicates are refused. dry_run returns the same verification block without changing the model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
