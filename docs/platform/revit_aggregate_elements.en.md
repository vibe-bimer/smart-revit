---
description: "Summarize matching elements by one or two fields, with optional sum and average. Lengths use mm, areas m2, volumes m3. For area totals, group by level and select the area scheme. A non-empty skipped list means the result is incomplete; skippedCount counts all skipped entries."
---

# Aggregate Elements

`revit_aggregate_elements`

<p class="facts"><span><b>Group</b> Query and totals</span><span><b>Kind</b> Read</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.4</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_aggregate_elements.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.4.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `area_scheme` | No | `null` | any | Exact area-scheme name, case-insensitive. |
| `categories` | No | `null` | any | (not documented in the development-line contract) |
| `family` | No | `null` | any | (not documented in the development-line contract) |
| `group_by` | Yes | — | array | One or two distinct fields (e.g. category, family, type, level) or exact localized parameter names. |
| `level` | No | `null` | any | (not documented in the development-line contract) |
| `parameter_filters` | No | `null` | any | AND-combined filters: parameter (exact localized name), operator (equals, contains, greater, less, empty, not-empty, exists) and value. Numbers use mm, m2, m3 or display units. |
| `phase` | No | `null` | any | (not documented in the development-line contract) |
| `sum_field` | No | `null` | any | Numeric field or parameter name to sum and average per group; lengths in mm, areas m2, volumes m3. |
| `type_name` | No | `null` | any | Exact type name, case-insensitive. |
| `view` | No | `null` | any | Exact non-template view name; limits the search to that view. |
| `workset` | No | `null` | any | (not documented in the development-line contract) |

</div>

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target document; needed when several Revit instances run. |
| `process_id` | No | `null` | any | Revit process ID; takes precedence over document. |
| `timeout_seconds` | No | `120` | integer | Seconds to wait for a result (default 120). |

</div>

## Behavior (registry text) {#behavior}

```text
Summarize matching elements by one or two fields, with optional sum and average. Lengths use mm, areas m2, volumes m3. For area totals, group by level and select the area scheme. A non-empty skipped list means the result is incomplete; skippedCount counts all skipped entries.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
