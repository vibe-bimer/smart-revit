---
description: "按模板重建模型与副本的构件 ID，支持重名策略。"
---

# 重建模型 ID

`revit_rebuild_model_ids`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.0.0</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    支持模板、副本与重名策略；约一千行，是这十四项里最后落地的一项。

按模板重建模型与副本的构件 ID，支持重名策略。

[同名发布版页面](../features/revit_rebuild_model_ids.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.0.0 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `copies` | 否 | `1` | integer | （开发线契约未提供说明） |
| `destination_path` | 是 | — | string | （开发线契约未提供说明） |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `duplicate_names` | 否 | `"override"` | string | （开发线契约未提供说明） |
| `overwrite` | 否 | `false` | boolean | （开发线契约未提供说明） |
| `remove_template_levels` | 否 | `true` | boolean | （开发线契约未提供说明） |
| `seed` | 否 | `0` | integer | （开发线契约未提供说明） |
| `template_path` | 否 | `null` | any | （开发线契约未提供说明） |
| `view` | 否 | `null` | any | 视图的准确名称或十进制视图 ID。 |

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
Rebuild the model into a new document so every element gets a new element ID.

`destination_path` is the new model, with {n} replaced by the copy number when `copies`
exceeds one. Reports the old to new pairing, the per-file results and the category counts.
dry_run reports the plan without writing files.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
