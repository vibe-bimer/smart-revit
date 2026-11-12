---
description: "生成本地 xlsx 问题登记表，含构件快照与审阅文档；已有同名输出文件时拒绝执行。"
---

# 生成问题登记表

`revit_issue_register`

<p class="facts"><span><b>分组</b> 导出与登记</span><span><b>类型</b> 读取</span><span><b>基座与自研的区分</b> 基座（上游）</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.4</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

生成本地 xlsx 问题登记表，含构件快照与审阅文档；已有同名输出文件时拒绝执行。

[同名发布版页面](../features/revit_issue_register.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.4 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `issues` | 是 | — | array | （开发线契约未提供说明） |
| `output_path` | 是 | — | string | New .xlsx issue register path, resolved on the machine running this server; existing files are refused. |
| `pixel_size` | 否 | `900` | integer | PNG size in pixels along the fitted dimension, 32 to 4000 (default 1600); Revit rejects smaller images. |
| `project` | 是 | — | object | （开发线契约未提供说明） |

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
Write a new local .xlsx issue register with element snapshots and review documents. Takes 1 to 60 issues; captures at most 25 snapshots (by severity) within a 210-second budget, and failed snapshots become cell notes. Snapshots need local or SSH transport. Existing output files are refused. A non-empty skipped list means the result is incomplete; skippedCount counts all skipped entries.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
