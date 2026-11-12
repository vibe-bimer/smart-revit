---
description: "激活一个非样板视图，可缩放适配、保持当前缩放或框选指定构件。"
---

# 激活视图

`revit_activate_view`

<p class="facts"><span><b>分组</b> 视图、图纸与明细表</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 基座（上游）</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.3</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

激活一个非样板视图，可缩放适配、保持当前缩放或框选指定构件。

[同名发布版页面](../features/revit_activate_view.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.3 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `activate_document` | 否 | `false` | boolean | （开发线契约未提供说明） |
| `view` | 是 | — | string | 视图的准确名称或十进制视图 ID。 |
| `view_type` | 否 | `null` | any | （开发线契约未提供说明） |
| `zoom` | 否 | `"fit"` | any | （开发线契约未提供说明） |

</div>

### 通用参数 {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | 否 | `null` | any | 打开多个模型时，用标题或路径指定目标文档。 |
| `process_id` | 否 | `null` | any | 目标 Revit 进程号。 |

</div>

## 功能说明（注册表原文） {#behavior}

以下保留工具在注册表中声明的英文原文，作为契约来源。

```text
Activate a non-template view. Zoom to fit, preserve zoom, or frame element IDs.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
