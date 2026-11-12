---
description: "Read displayed schedule header and body cell text, with paging. A non-empty skipped list means the result is incomplete; skippedCount counts all skipped entries."
---

# Read Schedule Data

`revit_schedule_data`

<p class="facts"><span><b>Group</b> Query and totals</span><span><b>Kind</b> Read</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.4</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_schedule_data.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.4.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `max_rows` | No | `500` | integer | (not documented in the development-line contract) |
| `offset` | No | `0` | integer | (not documented in the development-line contract) |
| `schedule` | Yes | — | string | Exact schedule name or decimal Revit view ID. (Use the id when two schedules share a name.) |

</div>

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target document; needed when several Revit instances run. |
| `process_id` | No | `null` | any | Revit process ID; takes precedence over document. |

</div>

## Behavior (registry text) {#behavior}

```text
Read displayed schedule header and body cell text, with paging. A non-empty skipped list means the result is incomplete; skippedCount counts all skipped entries.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
