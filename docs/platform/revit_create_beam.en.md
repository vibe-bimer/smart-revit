---
description: "Place one structural beam of `family` (optionally `type_name`) along the axis `start_mm`-`end_mm`. `level` is the reference level of the framing, and the two axis points are [x, y] in millimetres. The placement uses the curve-and-level overload, so the level and the axis are both given explicitly; the axis is not snapped, because Revit has no snapping API and SetEndReference only acts on an end the model already joined. `structural_usage` writes FamilyInstance.StructuralUsage. `z_offset_mm` is the vertical offset above the reference level: the tool writes it through the elevation parameters that carry it, and only a write that lifts the bounding box counts, because a family can take the value and keep the beam on its level; the instance moves instead when no parameter lifts it, and the call fails when neither route works, so a refused offset never passes as a beam placed on the level. The read-back names the parameter holding the offset or leaves it out when the geometry carries the shift. dry_run returns the same verification block without changing the model."
---

# Create Beam

`revit_create_beam`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    The curve-and-level overload, an axis that is never snapped, structural usage written from the enum, and the vertical offset through the family's elevation parameter with a move as the fallback.

[Same-name release page](../features/revit_create_beam.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `end_mm` | Yes | — | array |
| `family` | Yes | — | string |
| `level` | Yes | — | string |
| `start_mm` | Yes | — | array |
| `structural_usage` | No | `null` | any |
| `type_name` | No | `null` | any |
| `z_offset_mm` | No | `0` | number |

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
Place one structural beam of `family` (optionally `type_name`) along the axis `start_mm`-`end_mm`.

`level` is the reference level of the framing, and the two axis points are [x, y] in
millimetres. The placement uses the curve-and-level overload, so the level and the axis are
both given explicitly; the axis is not snapped, because Revit has no snapping API and
SetEndReference only acts on an end the model already joined. `structural_usage` writes
FamilyInstance.StructuralUsage. `z_offset_mm` is the vertical offset above the reference
level: the tool writes it through the elevation parameters that carry it, and only a write that
lifts the bounding box counts, because a family can take the value and keep the beam on its
level; the instance moves instead when no parameter lifts it, and the call fails when neither
route works, so a refused offset never passes as a beam placed on the level. The read-back names
the parameter holding the offset or leaves it out when the geometry carries the shift. dry_run
returns the same verification block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
