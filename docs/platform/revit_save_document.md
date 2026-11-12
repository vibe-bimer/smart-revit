---
description: "保存文档；需要先取得确认令牌，首次调用不改变任何内容。"
---

# 保存文档

`revit_save_document`

<p class="facts"><span><b>分组</b> 文档生命周期</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 基座（上游）</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.4</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

保存文档；需要先取得确认令牌，首次调用不改变任何内容。

[同名发布版页面](../features/revit_save_document.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.4 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `compact` | 否 | `false` | boolean | （开发线契约未提供说明） |
| `confirm_token` | 否 | `null` | any | 首次调用返回的确认令牌，用于确认破坏性操作。 |
| `overwrite` | 否 | `false` | boolean | （开发线契约未提供说明） |
| `save_as` | 否 | `null` | any | （开发线契约未提供说明） |

</div>

### 通用参数 {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | 是 | — | string | 打开多个模型时，用标题或路径指定目标文档。 |
| `process_id` | 否 | `null` | any | 目标 Revit 进程号。 |

</div>

## 功能说明（注册表原文） {#behavior}

以下保留工具在注册表中声明的英文原文，作为契约来源。

```text
Save a document. Needs confirm_token from a first call, which changes nothing.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
