---
description: "Place one door, window or other one-level hosted family of `family` at `x_mm`, `y_mm`. The host is either the wall named by `host_element_id`, or the nearest wall of the placement level whose location line passes within `host_search_radius_mm` of the point; `level` defaults to the level whose elevation is closest to the point. A missing host, a distance over the radius or two equally near walls are refused with the candidates, so the caller can name one. The response reports `fork.hostResolution` ({mode, hostId, distanceMm}), which is why a dry run already shows the wall the family would hang on. `sill_height_mm` writes the family's own INSTANCE_SILL_HEIGHT_PARAM and `flip_facing` calls flipFacing(). `rotation_deg` must be 0: a hosted instance takes its orientation from its host wall, so use `flip_facing` to turn it around. Families that are not one-level hosted are refused: revit_place_family places those, and it is the one that rotates. Nothing is attached to the host, because a door or a window has no attachment target. dry_run returns the same verification block without changing the model."
---

# Place Hosted Family

`revit_place_hosted_family`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.1</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    A named host or the nearest wall, ties and out-of-radius points refused with the candidates, hostResolution reported, sill and flip supported, a non-zero angle and non-hosted families refused.

[Same-name release page](../features/revit_place_hosted_family.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.1.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `family` | Yes | — | string |
| `flip_facing` | No | `null` | any |
| `host_element_id` | No | `null` | any |
| `host_search_radius_mm` | No | `2000` | number |
| `level` | No | `null` | any |
| `rotation_deg` | No | `0` | number |
| `sill_height_mm` | No | `null` | any |
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
Place one door, window or other one-level hosted family of `family` at `x_mm`, `y_mm`.

The host is either the wall named by `host_element_id`, or the nearest wall of the placement
level whose location line passes within `host_search_radius_mm` of the point; `level` defaults
to the level whose elevation is closest to the point. A missing host, a distance over the
radius or two equally near walls are refused with the candidates, so the caller can name one.
The response reports `fork.hostResolution` ({mode, hostId, distanceMm}), which is why a dry
run already shows the wall the family would hang on. `sill_height_mm` writes the family's own
INSTANCE_SILL_HEIGHT_PARAM and `flip_facing` calls flipFacing(). `rotation_deg` must be 0: a
hosted instance takes its orientation from its host wall, so use `flip_facing` to turn it
around. Families that are not one-level hosted are refused: revit_place_family places those,
and it is the one that rotates. Nothing is attached to the host, because a door or a window
has no attachment target. dry_run returns the same verification block without changing the
model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
