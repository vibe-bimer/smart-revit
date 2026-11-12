---
description: "Set a view's lighting: shadows, sun position, ground plane, background and lighting scheme. View-specific sun and shadow settings; a view that shares them passes the change on. Sun angles come as a pair, and gradient colors need the gradient background. dry_run returns the same verification block without changing the model."
---

# Set View Lighting

`revit_set_view_lighting`

<p class="facts"><span><b>Group</b> Views, sheets and schedules</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.3</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Present on both lines: attached through the fork registry, with the Python tool, the C# build and live validation all in hand.

[Same-name release page](../features/revit_set_view_lighting.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.3.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `background` | No | `null` | any |
| `background_colors` | No | `null` | any |
| `dry_run` | No | `false` | boolean |
| `ground_plane` | No | `null` | any |
| `ground_plane_level` | No | `null` | any |
| `lighting_scheme` | No | `null` | any |
| `shadow_intensity` | No | `null` | any |
| `shadows` | No | `null` | any |
| `sun_altitude_deg` | No | `null` | any |
| `sun_azimuth_deg` | No | `null` | any |
| `sun_date` | No | `null` | any |
| `sun_time` | No | `null` | any |
| `sunlight_intensity` | No | `null` | any |
| `view` | Yes | — | string |

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
Set a view's lighting: shadows, sun position, ground plane, background and lighting scheme.

View-specific sun and shadow settings; a view that shares them passes the change on.
Sun angles come as a pair, and gradient colors need the gradient background.
dry_run returns the same verification block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
