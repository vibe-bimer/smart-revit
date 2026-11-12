---
description: "整模型换新 ID：把三维视图可选中的构件重建为一份或多份新模型"
---

# 新模型重建 ID

`revit_rebuild_model_ids`

<p class="facts"><span><b>分组</b> 批量与 ID</span><span><b>类型</b> 动作（需授权）</span><span><b>起始版本</b> 0.8.0</span><span><b>版本</b> 已发布 1.1.2</span><span><b>开发线有同名工具</b> 有</span><span><b>本页契约适用于发布版</b> 是</span><span><b>影响范围</b> 新模型文件；源模型不变</span><span><b>来源</b> 自研（本仓库）</span></p>

整模型换新 ID：把三维视图可选中的构件重建为一份或多份新模型

!!! warning "动作工具默认允许，只读需显式开启"
    动作默认允许；机器策略 `ReadOnly`、工作站 `read-only` 文件或 `REVIT_MCP_READ_ONLY=1` 三者任一打开即拒绝动作（全新安装的机器策略默认只读）。动作连接必须指向单一 Revit 实例；实例中有多个文档时，用 `document` 明确目标。选择、显示和隔离还要求目标文档处于活动状态。

!!! note "使用提示"
    源模型不变；仅复制三维视图可选构件及必要基准，不是完整项目克隆；逐份检查数量与 ID 映射；delta 是额外错位而非目标间距

[同名开发线页面](../platform/revit_rebuild_model_ids.md)

## 与开发线的契约差异 {#contract-diff}

下表由注册表 inputSchema 自动比较得出，不是手写清单。

- 仅发布版有参数 per_copy_deltas
- 仅发布版有参数 warmup_copy

本页是发布版 1.1.2 的契约；开发线上的同名工具参数不同，请勿混用。

## 可复制提示词 {#prompts}

```text
把当前三维视图里能选中的构件重建到 E:\out\copy-{n}.rvt，出 10 份，每份 ID 都不要重复
```

```text
先彩排一次重建，告诉我多少个构件、新 ID 范围，先不要写文件
```

```text
出 24 份，先 warmup 一份垫稳首拷贝，每份的 per_copy_deltas 按试运行量出的间距递增，先彩排
```

## 参数 {#parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `destination_path` | 是 | — | `string` | 新模型路径（.rvt）；含 {n} 时按份编号 |
| `copies` | 否 | `1` | `integer` | 一份新模型连续出多少份（1–50），每份 ID 区间互不重叠 |
| `dry_run` | 否 | `false` | `boolean` | 彩排：在临时新文档中复制并给出映射，不保存目标文件；源模型始终不变 |
| `duplicate_names` | 否 | `"override"` | `string` | 重名处理：override 保留源类型、reuse 沿用新模型版本（批量默认）、rename 旧回退路径 |
| `overwrite` | 否 | `false` | `boolean` | 目标文件已存在时覆盖 |
| `per_copy_deltas` | 否 | `null` | `array<integer> / null` | 每份输出副本前的额外错位：长度等于 copies、每项 0–1000000 整数；是叠加的临时标高数，不是目标间距或绝对 ID，先在该模型上试运行核对 |
| `remove_template_levels` | 否 | `true` | `boolean` | 复制后删掉样板自带标高（默认删） |
| `seed` | 否 | `0` | `integer` | 先创建并移除 N 个临时标高以推进新文档 ID；不同运行使用不同 seed，是否重叠仍须核对映射 |
| `template_path` | 否 | `null` | `string / null` | 起始样板文件（.rte/.rvt）路径；缺省用公制样板 |
| `view` | 否 | `null` | `string / null` | 视图名称（或视图 ID） |
| `warmup_copy` | 否 | `null` | `boolean / null` | 先做一次首拷贝（类型落地与样板清理）再全部删除且不保存，输出副本从稳定状态开始；seed 仍在热身前生效一次 |

</div>

### 通用参数 {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| 参数 {scope=col} | 必填 {scope=col} | 默认值 {scope=col} | 类型 {scope=col} | 说明 {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | 否 | `null` | `string / null` | 文档标题或文件名的不区分大小写子串；读取时用于选择 Revit 实例，多个实例时必须唯一；动作时用于选择实例中已打开的文档，多个文档时必填。未知或歧义目标会被拒绝 |

</div>

## 功能说明与返回结果 {#contract}

将三维视图中可选择的构件复制到新模型，为每个构件生成新 ID，因为 Revit 不允许指定构件 ID。

绝不会修改已打开的模型：结果写入工作站上的 `destination_path`，源模型保持原样。
`view` 指定要读取的三维视图；不提供时使用第一个非透视三维视图，而且只复制该视图中可选择的构件。
标高、轴网和参照平面会一起复制，以便解析宿主关系；相机、太阳路径、剖面框、视图以及没有类别的构件不会复制，并会在 `excluded` 中报告。
视图、图纸、明细表、注释、阶段、工作集、MEP 系统以及未被选中的宿主都不会复制，因此结果只包含几何形状、类型和参数。
返回的数据包含 `destinationPath`、`saved`、`count`、`sourceView`、`sourceElementCount`、`datumCount`、`sourceCategoryCounts`、`copiedCategoryCounts`、`newIdMin`／`newIdMax`、`idMapping`（旧 ID 到新 ID 的映射，已按类别和类型验证），以及 `excluded` 中列出的被排除构件和各自的原因。
`overwrite` 用于替换已有文件；`template_path` 用于从指定模板开始复制，而不是使用默认公制模板；`remove_template_levels` 用于移除模板自身的标高。
`seed` 会在复制前向新模型添加相应数量的临时标高，再将它们移除，以使新 ID 位于独立的编号区段；否则，对相同源模型重建两次会产生相同 ID。因此，当需要各副本的 ID 互不重叠时，应为每次复制传入不同的 `seed`（例如 0、1000、2000）。
`duplicate_names` 决定新项目中已有与粘贴来源同名对象时如何处理：`override` 会以“确定”回答 Revit 的提示，使副本保留源模型自身的类型；`rename` 会先重命名模板中的对象，随后再移除它们，但速度较慢，并且在 Revit 拒绝删除某些对象时可能失败。
`copies` 指定从同一个新模型写出的文件数量：各副本包含相同构件，但各有自己的 ID，因为每个副本的 ID 都从前一个副本的 ID 区段之后开始。文件写入 `destination_path`，其中的 `{n}` 会替换为副本编号；路径不含 `{n}` 时，则在扩展名前追加编号。每个副本的映射会在 `copyResults` 中报告，各副本每个阶段的耗时会写入插件日志。
`warmup_copy=true` 会在输出副本之前先完整做一次首拷贝（连同类型落地与样板清理），随后把复制出的构件全部删除且不保存任何文件：首拷贝的一次性消耗落在这次热身上，真正的输出副本从稳定的文档状态开始。`seed` 仍在热身副本之前生效一次；热身副本若有构件删不干净，运行停止且不写任何输出文件。
`per_copy_deltas` 按份数给出额外错位：列表长度必须等于 `copies`，每一项是 0 到 1000000 的整数，表示对应输出副本之前额外创建并随即移除的临时标高数量。错位叠加在文档当前 ID 计数之上，不是目标间距，也不是绝对 ID：副本间的基础步长、以及 delta 折算成 ID 偏移的比例都随模型变化，须先在目标模型上试运行量出实际区间再决定序列；错位非负，间距无法小于该模型的基础步长。未启用热身时，`seed` 与第一个 delta 之和不能超出整数范围。提供 `per_copy_deltas` 或 `warmup_copy` 任一项即进入严格批次：某份副本的映射不完整，或其 ID 区间与前一副本重叠，整批停止且不再退回逐构件复制。
`dry_run` 会执行复制并报告映射，但不保存文件。

## Revit 年份支持 {#year-support}

| Revit 年份 | 验证状态 |
| --- | --- |
| 2020 | <span class="state ok">已实测</span> |
| 2026 | <span class="state part">仅构建，未实测</span> |
| 2022–2025 / 2027 | <span class="state part">仅构建，未实测</span> |

已实测表示记录过真机执行；仅构建表示通过编译，不代表已完成真机功能验证。Revit 2021 不在本项目构建范围。

---

[全部功能](index.md) · [版本支持矩阵](matrix.md) · [提示词库](prompts.md)
