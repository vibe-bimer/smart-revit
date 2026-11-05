---
description: "本仓库自研 14 个工具在新版底座上的移植状态：14 个已接上，0 个待移植。"
---

# 自研工具的移植状态

本仓库自己设计的工具一共 14 个，已全部接到新版底座上（14 个）。这些工具都不改变基座的行为，只通过 fork 注册表追加命令。

| 工具数 | 基座与自研的区分 | 移植状态 |
| --- | --- | --- |
| [设置视图光照](revit_set_view_lighting.md)<br>`revit_set_view_lighting` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [创建标高](revit_create_level.md)<br>`revit_create_level` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [创建楼板](revit_create_floor.md)<br>`revit_create_floor` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [载入族文件](revit_load_family_file.md)<br>`revit_load_family_file` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [创建轴网](revit_create_grid.md)<br>`revit_create_grid` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [创建柱](revit_create_column.md)<br>`revit_create_column` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [创建梁](revit_create_beam.md)<br>`revit_create_beam` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [放置宿主族](revit_place_hosted_family.md)<br>`revit_place_hosted_family` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [跨标高复制构件](revit_copy_elements.md)<br>`revit_copy_elements` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [设置阶段](revit_set_phase.md)<br>`revit_set_phase` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [合并阶段](revit_merge_phases.md)<br>`revit_merge_phases` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [导出构件 ID 台账](revit_export_element_ids.md)<br>`revit_export_element_ids` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [重置构件 ID](revit_reset_element_ids.md)<br>`revit_reset_element_ids` | 自研（本仓库） | <span class="state ok">已移植</span> |
| [重建模型 ID](revit_rebuild_model_ids.md)<br>`revit_rebuild_model_ids` | 自研（本仓库） | <span class="state ok">已移植</span> |

已移植表示快照里能列出并执行；待移植表示实现已在本地版本里，但快照里还没有对应命令。

---

[返回目录](index.md)
