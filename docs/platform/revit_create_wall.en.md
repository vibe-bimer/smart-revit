---
description: "Create a straight wall on a named level. XY endpoints and height are in mm; a null wall_type uses the first basic type."
---

# Create Wall

`revit_create_wall`

<p class="facts"><span><b>Group</b> CAD and MEP</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.4</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_create_wall.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.4.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `end_mm` | Yes | — | array |
| `height_mm` | No | `3000` | number |
| `level` | Yes | — | string |
| `start_mm` | Yes | — | array |
| `wall_type` | Yes | — | any |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target open document; needed when several are open. |

</div>

## Behavior (registry text) {#behavior}

```text
Create a straight wall on a named level. XY endpoints and height are in mm; a null wall_type uses the first basic type.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
