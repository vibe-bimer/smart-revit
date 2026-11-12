---
description: "从磁盘载入一个族文件，可只载入其中一个类型；路径不存在时给出最近匹配。"
---

# 载入族文件

`revit_load_family_file`

<p class="facts"><span><b>分组</b> 编辑原语</span><span><b>类型</b> 动作</span><span><b>基座与自研的区分</b> 自研（本仓库） · 已移植</span><span><b>状态</b> 未发布（开发线）</span><span><b>发布版版本</b> 1.1.3</span><span><b>来源分支</b> <code>feat/gitlab-pages</code></span><span><b>来源提交</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>发布版有同名工具</b> 有，参数一致</span><span><b>本页契约适用于发布版</b> 否</span></p>

!!! note "使用提示"
    单文件、可选定点类型、总是带族载入选项、路径不存在报最近匹配。

从磁盘载入一个族文件，可只载入其中一个类型；路径不存在时给出最近匹配。

[同名发布版页面](../features/revit_load_family_file.md)

## 与发布版的契约差异 {#contract-diff}

同名工具的契约与发布版 1.1.3 一致。

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `dry_run` | 否 | `false` | boolean | 只排练：执行后回滚，返回同样的验证块。 |
| `overwrite_parameters` | 否 | `false` | boolean | （开发线契约未提供说明） |
| `path` | 是 | — | string | （开发线契约未提供说明） |
| `type_name` | 否 | `null` | any | （开发线契约未提供说明） |

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
Load one family file from the workstation: the whole family, or the single type `type_name`.

The load always carries the family load options, so it never waits on Revit's own dialog.
An existing family is reused, and its parameter values are left alone unless
`overwrite_parameters` is true. The response reports `state` ("new" or "existing") and every
type the family now offers. A path that does not exist is refused with the closest filenames
beside it. dry_run returns the same verification block without changing the model.
```

---

[返回目录](index.md) · [自研工具的移植状态](fork-tools.md)
