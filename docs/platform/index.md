---
description: "开发线（上游 1.0 基座加本仓库自研工具）的完整工具清单，按分组列出用途、参数与契约差异。"
---

# 新版基座工具目录

这一节记录当前开发线上的工具面，与「功能」一节的已发布版本分开。该线尚未发布：自研工具已全部接上，目录是这条开发线的完整清单。

共 93 个工具：基座 79 个，自研 14 个；读取 35 个，动作 58 个。

## 版本入口 {#versions}

两个目录各自记录一个版本：功能目录跟着当前代码树，开发线尚未发布。下面的数量与状态都从注册表读取，不写死。

| | 功能目录 | 开发线 |
| --- | --- | --- |
| 状态 | 已发布 1.1.4 | 未发布（开发线） |
| 分支 | main | `feat/gitlab-pages` |
| 工具数 | 93 | 93 |
| 目录 | [功能总览](../features/index.md) | index.md |

## 两套工具面 {#catalogs}

功能目录跟着当前代码树，平台目录记录当前开发线，以新版底座为起点，尚未发布。两栏都从同一棵树生成，工具集合因此重合；比发布版 1.1.4 晚加入的工具在各自页面上标为未发布。

| | 功能目录 | 开发线 |
| --- | --- | --- |
| 工具数 | 93 | 93 |
| 读取 | 35 | 35 |
| 动作 | 58 | 58 |
| 已发布 | 已发布 | 未发布 |
| 分支 | main | `feat/gitlab-pages` |

## 基座与自研的区分 {#origin}

每个工具在页面上都带来源标记：基座表示随上游底座而来，自研表示本仓库自己设计。自研 14 项，其中 14 项已接上这条线。

| 分组 | 基座（上游） | 自研（本仓库） |
| --- | --- | --- |
| 连接与实例 | 8 | 0 |
| 查询与统计 | 12 | 0 |
| 编辑原语 | 9 | 12 |
| 文档生命周期 | 6 | 0 |
| 视图、图纸与明细表 | 21 | 1 |
| 族 | 5 | 0 |
| 链接与基准 | 3 | 0 |
| CAD 与 MEP | 4 | 0 |
| 导出与登记 | 4 | 1 |
| 批处理与报告 | 6 | 0 |
| C# 逃生口 | 1 | 0 |
| **合计** | **79** | **14** |

[自研工具的移植状态](fork-tools.md) · [集成规格与决策记录](https://github.com/vibe-bimer/smart-revit/issues/4)

## 分组统计 {#groups}

| 分组 | 工具数 | 读取 | 动作 |
| --- | ---: | ---: | ---: |
| [连接与实例](#group-core) | 8 | 6 | 2 |
| [查询与统计](#group-read) | 12 | 12 | 0 |
| [编辑原语](#group-actions) | 21 | 0 | 21 |
| [文档生命周期](#group-documents) | 6 | 0 | 6 |
| [视图、图纸与明细表](#group-views-sheets) | 22 | 7 | 15 |
| [族](#group-family) | 5 | 1 | 4 |
| [链接与基准](#group-links) | 3 | 1 | 2 |
| [CAD 与 MEP](#group-cad-mep) | 4 | 0 | 4 |
| [导出与登记](#group-export) | 5 | 3 | 2 |
| [批处理与报告](#group-batch) | 6 | 5 | 1 |
| [C# 逃生口](#group-code) | 1 | 0 | 1 |

按视图、图纸、明细表与视口显示浏览：见 [按模型对象浏览](#objects)。

## 按模型对象浏览 {#objects}

同一批视图相关工具按操作的模型对象再分一次，方便先找对象再找工具；上面的分组表与下面的逐项文档保持原样。

### 视图 {#objects-views}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [激活视图](revit_activate_view.md)<br>`revit_activate_view` | 动作 | <span class="state part">基座（上游）</span> |
| [应用视图样板](revit_apply_view_template.md)<br>`revit_apply_view_template` | 动作 | <span class="state part">基座（上游）</span> |
| [关闭视图](revit_close_views.md)<br>`revit_close_views` | 动作 | <span class="state part">基座（上游）</span> |
| [创建视图](revit_create_view.md)<br>`revit_create_view` | 动作 | <span class="state part">基座（上游）</span> |
| [复制视图](revit_duplicate_view.md)<br>`revit_duplicate_view` | 动作 | <span class="state part">基座（上游）</span> |
| [导出视图为 PNG](revit_export_view.md)<br>`revit_export_view` | 读取 | <span class="state part">基座（上游）</span> |
| [视图列表](revit_list_views.md)<br>`revit_list_views` | 读取 | <span class="state part">基座（上游）</span> |
| [设置视图光照](revit_set_view_lighting.md)<br>`revit_set_view_lighting` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [设置视图可见性](revit_set_view_visibility.md)<br>`revit_set_view_visibility` | 动作 | <span class="state part">基座（上游）</span> |
| [视图构件](revit_view_elements.md)<br>`revit_view_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [视图信息](revit_view_info.md)<br>`revit_view_info` | 读取 | <span class="state part">基座（上游）</span> |
| [视图摘要](revit_view_summary.md)<br>`revit_view_summary` | 读取 | <span class="state part">基座（上游）</span> |
| [视图警告](revit_view_warnings.md)<br>`revit_view_warnings` | 读取 | <span class="state part">基座（上游）</span> |

### 图纸 {#objects-sheets}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [创建图纸](revit_create_sheet.md)<br>`revit_create_sheet` | 动作 | <span class="state part">基座（上游）</span> |
| [在图纸上布置视图](revit_place_views_on_sheet.md)<br>`revit_place_views_on_sheet` | 动作 | <span class="state part">基座（上游）</span> |

### 明细表 {#objects-schedules}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [读取明细表数据](revit_schedule_data.md)<br>`revit_schedule_data` | 读取 | <span class="state part">基座（上游）</span> |
| [创建明细表](revit_create_schedule.md)<br>`revit_create_schedule` | 动作 | <span class="state part">基座（上游）</span> |

### 视口与显示 {#objects-view-display}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [截取构件画面](revit_capture_elements.md)<br>`revit_capture_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [隔离构件](revit_isolate.md)<br>`revit_isolate` | 动作 | <span class="state part">基座（上游）</span> |
| [高亮构件](revit_override_graphics.md)<br>`revit_override_graphics` | 动作 | <span class="state part">基座（上游）</span> |
| [选择构件](revit_select.md)<br>`revit_select` | 动作 | <span class="state part">基座（上游）</span> |
| [显示构件](revit_show.md)<br>`revit_show` | 动作 | <span class="state part">基座（上游）</span> |
| [标注构件](revit_tag_elements.md)<br>`revit_tag_elements` | 动作 | <span class="state part">基座（上游）</span> |

## 连接与实例 {#group-core}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [取消动作任务](revit_cancel_job.md)<br>`revit_cancel_job` | 动作 | <span class="state part">基座（上游）</span> |
| [文档信息](revit_document_info.md)<br>`revit_document_info` | 读取 | <span class="state part">基座（上游）</span> |
| [文档列表](revit_documents.md)<br>`revit_documents` | 读取 | <span class="state part">基座（上游）</span> |
| [任务列表](revit_jobs.md)<br>`revit_jobs` | 读取 | <span class="state part">基座（上游）</span> |
| [实例列表](revit_list_instances.md)<br>`revit_list_instances` | 读取 | <span class="state part">基座（上游）</span> |
| [连接检查](revit_ping.md)<br>`revit_ping` | 读取 | <span class="state part">基座（上游）</span> |
| [界面状态](revit_ui_state.md)<br>`revit_ui_state` | 读取 | <span class="state part">基座（上游）</span> |
| [撤销上一个动作](revit_undo_last.md)<br>`revit_undo_last` | 动作 | <span class="state part">基座（上游）</span> |

## 查询与统计 {#group-read}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [聚合统计](revit_aggregate_elements.md)<br>`revit_aggregate_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [构件详情](revit_element_details.md)<br>`revit_element_details` | 读取 | <span class="state part">基座（上游）</span> |
| [链接状态](revit_links_status.md)<br>`revit_links_status` | 读取 | <span class="state part">基座（上游）</span> |
| [目录列表](revit_list_catalog.md)<br>`revit_list_catalog` | 读取 | <span class="state part">基座（上游）</span> |
| [关系列表](revit_list_relations.md)<br>`revit_list_relations` | 读取 | <span class="state part">基座（上游）</span> |
| [警告列表](revit_list_warnings.md)<br>`revit_list_warnings` | 读取 | <span class="state part">基座（上游）</span> |
| [模型健康检查](revit_model_health.md)<br>`revit_model_health` | 读取 | <span class="state part">基座（上游）</span> |
| [模型快照](revit_model_snapshot.md)<br>`revit_model_snapshot` | 读取 | <span class="state part">基座（上游）</span> |
| [参数填充检查](revit_parameter_fill_check.md)<br>`revit_parameter_fill_check` | 读取 | <span class="state part">基座（上游）</span> |
| [查询构件](revit_query_elements.md)<br>`revit_query_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [读取明细表数据](revit_schedule_data.md)<br>`revit_schedule_data` | 读取 | <span class="state part">基座（上游）</span> |
| [共享坐标](revit_shared_coordinates.md)<br>`revit_shared_coordinates` | 读取 | <span class="state part">基座（上游）</span> |

## 编辑原语 {#group-actions}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [更改构件类型](revit_change_type.md)<br>`revit_change_type` | 动作 | <span class="state part">基座（上游）</span> |
| [复制构件](revit_copy.md)<br>`revit_copy` | 动作 | <span class="state part">基座（上游）</span> |
| [跨标高复制构件](revit_copy_elements.md)<br>`revit_copy_elements` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [创建梁](revit_create_beam.md)<br>`revit_create_beam` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [创建柱](revit_create_column.md)<br>`revit_create_column` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [创建楼板](revit_create_floor.md)<br>`revit_create_floor` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [创建轴网](revit_create_grid.md)<br>`revit_create_grid` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [创建标高](revit_create_level.md)<br>`revit_create_level` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [删除构件](revit_delete.md)<br>`revit_delete` | 动作 | <span class="state part">基座（上游）</span> |
| [载入族文件](revit_load_family_file.md)<br>`revit_load_family_file` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [合并阶段](revit_merge_phases.md)<br>`revit_merge_phases` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [镜像构件](revit_mirror.md)<br>`revit_mirror` | 动作 | <span class="state part">基座（上游）</span> |
| [移动构件](revit_move.md)<br>`revit_move` | 动作 | <span class="state part">基座（上游）</span> |
| [放置宿主族](revit_place_hosted_family.md)<br>`revit_place_hosted_family` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [重建模型 ID](revit_rebuild_model_ids.md)<br>`revit_rebuild_model_ids` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [重置构件 ID](revit_reset_element_ids.md)<br>`revit_reset_element_ids` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [旋转构件](revit_rotate.md)<br>`revit_rotate` | 动作 | <span class="state part">基座（上游）</span> |
| [批量执行动作](revit_run_actions.md)<br>`revit_run_actions` | 动作 | <span class="state part">基座（上游）</span> |
| [设置参数](revit_set_parameter.md)<br>`revit_set_parameter` | 动作 | <span class="state part">基座（上游）</span> |
| [设置阶段](revit_set_phase.md)<br>`revit_set_phase` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [批量更新参数](revit_update_parameters.md)<br>`revit_update_parameters` | 动作 | <span class="state part">基座（上游）</span> |

## 文档生命周期 {#group-documents}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [激活文档](revit_activate_document.md)<br>`revit_activate_document` | 动作 | <span class="state part">基座（上游）</span> |
| [关闭文档](revit_close_document.md)<br>`revit_close_document` | 动作 | <span class="state part">基座（上游）</span> |
| [新建文档](revit_new_document.md)<br>`revit_new_document` | 动作 | <span class="state part">基座（上游）</span> |
| [打开文档](revit_open_document.md)<br>`revit_open_document` | 动作 | <span class="state part">基座（上游）</span> |
| [保存文档](revit_save_document.md)<br>`revit_save_document` | 动作 | <span class="state part">基座（上游）</span> |
| [同步文档](revit_sync_document.md)<br>`revit_sync_document` | 动作 | <span class="state part">基座（上游）</span> |

## 视图、图纸与明细表 {#group-views-sheets}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [激活视图](revit_activate_view.md)<br>`revit_activate_view` | 动作 | <span class="state part">基座（上游）</span> |
| [应用视图样板](revit_apply_view_template.md)<br>`revit_apply_view_template` | 动作 | <span class="state part">基座（上游）</span> |
| [截取构件画面](revit_capture_elements.md)<br>`revit_capture_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [关闭视图](revit_close_views.md)<br>`revit_close_views` | 动作 | <span class="state part">基座（上游）</span> |
| [创建明细表](revit_create_schedule.md)<br>`revit_create_schedule` | 动作 | <span class="state part">基座（上游）</span> |
| [创建图纸](revit_create_sheet.md)<br>`revit_create_sheet` | 动作 | <span class="state part">基座（上游）</span> |
| [创建视图](revit_create_view.md)<br>`revit_create_view` | 动作 | <span class="state part">基座（上游）</span> |
| [复制视图](revit_duplicate_view.md)<br>`revit_duplicate_view` | 动作 | <span class="state part">基座（上游）</span> |
| [导出视图为 PNG](revit_export_view.md)<br>`revit_export_view` | 读取 | <span class="state part">基座（上游）</span> |
| [隔离构件](revit_isolate.md)<br>`revit_isolate` | 动作 | <span class="state part">基座（上游）</span> |
| [视图列表](revit_list_views.md)<br>`revit_list_views` | 读取 | <span class="state part">基座（上游）</span> |
| [高亮构件](revit_override_graphics.md)<br>`revit_override_graphics` | 动作 | <span class="state part">基座（上游）</span> |
| [在图纸上布置视图](revit_place_views_on_sheet.md)<br>`revit_place_views_on_sheet` | 动作 | <span class="state part">基座（上游）</span> |
| [选择构件](revit_select.md)<br>`revit_select` | 动作 | <span class="state part">基座（上游）</span> |
| [设置视图光照](revit_set_view_lighting.md)<br>`revit_set_view_lighting` | 动作 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [设置视图可见性](revit_set_view_visibility.md)<br>`revit_set_view_visibility` | 动作 | <span class="state part">基座（上游）</span> |
| [显示构件](revit_show.md)<br>`revit_show` | 动作 | <span class="state part">基座（上游）</span> |
| [标注构件](revit_tag_elements.md)<br>`revit_tag_elements` | 动作 | <span class="state part">基座（上游）</span> |
| [视图构件](revit_view_elements.md)<br>`revit_view_elements` | 读取 | <span class="state part">基座（上游）</span> |
| [视图信息](revit_view_info.md)<br>`revit_view_info` | 读取 | <span class="state part">基座（上游）</span> |
| [视图摘要](revit_view_summary.md)<br>`revit_view_summary` | 读取 | <span class="state part">基座（上游）</span> |
| [视图警告](revit_view_warnings.md)<br>`revit_view_warnings` | 读取 | <span class="state part">基座（上游）</span> |

## 族 {#group-family}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [编辑族](revit_edit_families.md)<br>`revit_edit_families` | 动作 | <span class="state part">基座（上游）</span> |
| [审核族](revit_family_audit.md)<br>`revit_family_audit` | 读取 | <span class="state part">基座（上游）</span> |
| [载入族](revit_load_family.md)<br>`revit_load_family` | 动作 | <span class="state part">基座（上游）</span> |
| [批量放置族](revit_place_families.md)<br>`revit_place_families` | 动作 | <span class="state part">基座（上游）</span> |
| [放置族](revit_place_family.md)<br>`revit_place_family` | 动作 | <span class="state part">基座（上游）</span> |

## 链接与基准 {#group-links}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [对齐链接基准](revit_align_link_datums.md)<br>`revit_align_link_datums` | 动作 | <span class="state part">基座（上游）</span> |
| [比较链接基准](revit_compare_link_datums.md)<br>`revit_compare_link_datums` | 读取 | <span class="state part">基座（上游）</span> |
| [移除链接](revit_remove_links.md)<br>`revit_remove_links` | 动作 | <span class="state part">基座（上游）</span> |

## CAD 与 MEP {#group-cad-mep}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [创建 MEP 管线](revit_create_mep_run.md)<br>`revit_create_mep_run` | 动作 | <span class="state part">基座（上游）</span> |
| [创建墙](revit_create_wall.md)<br>`revit_create_wall` | 动作 | <span class="state part">基座（上游）</span> |
| [链接 CAD](revit_link_cad.md)<br>`revit_link_cad` | 动作 | <span class="state part">基座（上游）</span> |
| [从 CAD 建墙](revit_walls_from_cad.md)<br>`revit_walls_from_cad` | 动作 | <span class="state part">基座（上游）</span> |

## 导出与登记 {#group-export}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [导出模型文件](revit_export.md)<br>`revit_export` | 动作 | <span class="state part">基座（上游）</span> |
| [导出构件 ID 台账](revit_export_element_ids.md)<br>`revit_export_element_ids` | 读取 | <span class="state ok">自研（本仓库）</span> <span class="state ok">已移植</span> |
| [导出 NWC](revit_export_nwc.md)<br>`revit_export_nwc` | 动作 | <span class="state part">基座（上游）</span> |
| [生成问题登记表](revit_issue_register.md)<br>`revit_issue_register` | 读取 | <span class="state part">基座（上游）</span> |
| [检查 NWC 设置](revit_nwc_settings_check.md)<br>`revit_nwc_settings_check` | 读取 | <span class="state part">基座（上游）</span> |

## 批处理与报告 {#group-batch}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [取消批量收集](revit_batch_cancel.md)<br>`revit_batch_cancel` | 读取 | <span class="state part">基座（上游）</span> |
| [取回批量快照](revit_batch_fetch.md)<br>`revit_batch_fetch` | 读取 | <span class="state part">基座（上游）</span> |
| [开始批量收集](revit_batch_start.md)<br>`revit_batch_start` | 读取 | <span class="state part">基座（上游）</span> |
| [批量收集状态](revit_batch_status.md)<br>`revit_batch_status` | 读取 | <span class="state part">基座（上游）</span> |
| [生成快照报告](revit_build_report.md)<br>`revit_build_report` | 读取 | <span class="state part">基座（上游）</span> |
| [批处理模型](revit_process_models.md)<br>`revit_process_models` | 动作 | <span class="state part">基座（上游）</span> |

## C# 逃生口 {#group-code}

| 工具数 | 类型 | 基座与自研的区分 |
| --- | --- | --- |
| [执行 C# 代码](revit_execute_code.md)<br>`revit_execute_code` | 动作 | <span class="state part">基座（上游）</span> |

## 状态说明 {#status}

这里的工具都已在 Python 注册表里注册，参数与描述直接来自注册表；C# 侧的每个自研工具都在 2020 与 2026 两个年份编译并真机验收过。契约以注册表为准，验收记录见「真机验收」。
