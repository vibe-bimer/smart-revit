---
description: "同一模型内复制构件并保留宿主：门窗跟着墙一起复制，逐件回报旧 ID → 新 ID（mm）"
---

# 复制构件

`revit_copy_elements`

<p class="facts"><span><b>分组</b> 编辑</span><span><b>类型</b> 动作（需授权）</span><span><b>起始版本</b> 0.11.0</span><span><b>版本</b> 未发布（1.0.0）</span><span><b>集成分支有同名工具</b> 没有</span><span><b>本页契约适用于发布版</b> 是</span><span><b>影响范围</b> 模型构件 / 参数</span><span><b>来源</b> 自研（本仓库）</span></p>

同一模型内复制构件并保留宿主：门窗跟着墙一起复制，逐件回报旧 ID → 新 ID（mm）

!!! warning "动作工具默认允许，只读需显式开启"
    动作默认允许；机器策略 `ReadOnly`、工作站 `read-only` 文件或 `REVIT_MCP_READ_ONLY=1` 三者任一打开即拒绝动作（全新安装的机器策略默认只读）。动作连接必须指向单一 Revit 实例；实例中有多个文档时，用 `document` 明确目标。选择、显示和隔离还要求目标文档处于活动状态。

!!! note "使用提示"
    宿主族构件的宿主必须在同一个请求里，否则整批拒绝并点名（Revit 会在粘贴结束时删掉找不到新宿主的构件）；复制不销毁任何东西，因此按构件报失败而不是整批拒绝；CopyElements 不保证顺序，按类别 + 类型 + 位置配对，配不准就把 idMappingVerified 标成 false

## 可复制提示词 {#prompts}

```text
把 1F 上这三根柱往东复制 3000mm
```

```text
把这面墙和它上面的门一起复制到 2F
```

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `element_ids` | 是 | — | `array<integer>` | 要复制的构件；其中每个宿主族构件的宿主也要列进来 |
| `dry_run` | 否 | `false` | `boolean` | 彩排：复制后回滚，只回报将要得到的 ID 配对 |
| `dx_mm` | 否 | `0` | `number` | 水平 X 偏移（mm），默认 0 |
| `dy_mm` | 否 | `0` | `number` | 水平 Y 偏移（mm），默认 0 |
| `dz_mm` | 否 | `0` | `number` | 竖向偏移（mm），默认 0；给了 target_level 时叠在标高差上 |
| `target_level` | 否 | `null` | `string / null` | 目标标高名；给了就按标高差求 dz，与 dz_mm 相加 |

</div>

### 通用参数 {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | 否 | `null` | `string / null` | 文档标题或文件名的不区分大小写子串；读取时用于选择 Revit 实例，多个实例时必须唯一；动作时用于选择实例中已打开的文档，多个文档时必填。未知或歧义目标会被拒绝 |

</div>

## 功能说明与返回结果 {#contract}

在同一模型内复制构件，并保留它们与宿主的关系。

使用会把构件重新宿主的那条复制重载：门窗等宿主族构件必须连同宿主一起放进 `element_ids`，否则整个请求会被拒绝，并点名缺的是哪个宿主——Revit 在粘贴结束时会删掉找不到新宿主的构件，而静默丢构件比拒绝更糟。

复制不会销毁任何东西，因此失败按构件逐个报告，而不是整批拒绝：每件都给出旧 ID 到新 ID 的配对，或者它失败的原因。

返回的数据包含 `count`、`idMapping`（旧 ID 到新 ID），以及 `fork.idMappingVerified`；`CopyElements` 只返回新 ID 集合、不保证顺序也不给映射，所以配对按「类别 + 类型 + 位置」验证，无法证明配对时该字段为 `false`，并在 `fork.ineligible` 里列出没拿到的构件与原因。

`target_level` 按目标标高与该构件所在标高的高差求竖向位移，与 `dz_mm` 相加；一批构件跨多个标高时无法用一个位移表达，会要求改用 `dz_mm` 或按标高分开复制。

`dx_mm` / `dy_mm` / `dz_mm` 是直接给的平移量，默认 0；复制的 `Transform` 是纯平移，没有重载接受目标标高。

`dry_run` 会执行复制再回滚，在不改动模型的情况下返回同样的配对结果。

## Revit 年份支持 {#year-support}

| Revit 年份 | 验证状态 |
| --- | --- |
| 2020 | <span class="state ok">已实测</span> |
| 2026 | <span class="state ok">已实测</span> |
| 2022–2025 / 2027 | <span class="state part">仅构建，未实测</span> |

已实测表示记录过真机执行；仅构建表示通过编译，不代表已完成真机功能验证。Revit 2021 不在本项目构建范围。

---

[全部功能](index.md) · [版本支持矩阵](matrix.md) · [提示词库](prompts.md)
