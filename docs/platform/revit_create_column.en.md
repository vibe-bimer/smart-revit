---
description: "Place one structural column of `family` (optionally `type_name`) at `x_mm`, `y_mm` on `level`. The top is either `top_level` or `height_mm` above the base (3000 mm when neither is given). Base and top levels and both offsets are written by the tool itself, because they are ElementId-valued parameters that revit_set_parameter refuses on purpose. The column is not attached to anything: no attachment is attempted. dry_run returns the same verification block without changing the model."
---

# Create Column

`revit_create_column`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.1</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    The tool writes both levels and both offsets, the top is a level or a height, nothing is attached, and a missing type lists the ones that exist.

[Same-name release page](../features/revit_create_column.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.1.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `base_offset_mm` | No | `0` | number |
| `dry_run` | No | `false` | boolean |
| `family` | Yes | — | string |
| `height_mm` | No | `null` | any |
| `level` | Yes | — | string |
| `rotation_deg` | No | `0` | number |
| `top_level` | No | `null` | any |
| `top_offset_mm` | No | `0` | number |
| `type_name` | No | `null` | any |
| `x_mm` | Yes | — | number |
| `y_mm` | Yes | — | number |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `document` | No | `null` | any |

</div>

The development-line contract ships no parameter descriptions.

## Behavior (registry text) {#behavior}

```text
Place one structural column of `family` (optionally `type_name`) at `x_mm`, `y_mm` on `level`.

The top is either `top_level` or `height_mm` above the base (3000 mm when neither is given).
Base and top levels and both offsets are written by the tool itself, because they are
ElementId-valued parameters that revit_set_parameter refuses on purpose. The column is not
attached to anything: no attachment is attempted. dry_run returns the same verification
block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
