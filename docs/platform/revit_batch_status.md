---
description: "在发起客户端退出后仍可读取运行与模型状态。"
---

# 批量收集状态

`revit_batch_status`

<p class="facts"><span><b>分组</b> 批处理与报告</span><span><b>类型</b> 读取</span><span><b>基座与自研的区分</b> 基座（上游）</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.3</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

在发起客户端退出后仍可读取运行与模型状态。

[同名发布版页面](../features/revit_batch_status.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.3 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} |
| --- | :--: | --- | --- |
| `run_id` | 是 | — | string |

</div>

开发线契约未提供参数说明。

## 功能说明（注册表原文） {#behavior}

以下保留工具在注册表中声明的英文原文，作为契约来源。

```text
Read durable run and model status after the initiating client exits.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
