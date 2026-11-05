---
description: "Write the element identifier register of the drawn components to a workbook, read-only. `fields` picks the columns and `path` names the file, which must not already exist; without one the workbook goes to Documents/RevitModelMcp/Exports with a timestamp. Non-component categories are reported under skippedCategories and the list is capped at 50,000 rows. The workbook is written on the Revit workstation; nothing is downloaded."
---

# Export Element Ids

`revit_export_element_ids`

<p class="facts"><span><b>Group</b> Export and registers</span><span><b>Kind</b> Read</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.0.0</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Writes an xlsx register and reads system members and connectors.

[Same-name release page](../features/revit_export_element_ids.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.0.0.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `fields` | No | `null` | any |
| `path` | No | `null` | any |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `document` | No | `null` | any |
| `timeout_seconds` | No | `120` | integer |

</div>

The development-line contract ships no parameter descriptions.

## Behavior (registry text) {#behavior}

```text
Write the element identifier register of the drawn components to a workbook, read-only.

`fields` picks the columns and `path` names the file, which must not already exist; without
one the workbook goes to Documents/RevitModelMcp/Exports with a timestamp. Non-component
categories are reported under skippedCategories and the list is capped at 50,000 rows.
The workbook is written on the Revit workstation; nothing is downloaded.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
