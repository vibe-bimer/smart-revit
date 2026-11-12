---
description: "Create a level at an elevation, optionally with its floor plan. A level whose name already exists is refused. dry_run returns the same verification block without changing the model."
---

# Create Level

`revit_create_level`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.3</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Remapped onto the fork registry; it can create the matching floor plan view, and a duplicate name is refused with the existing level names and elevations.

[Same-name release page](../features/revit_create_level.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.3.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `create_view` | No | `false` | boolean |
| `dry_run` | No | `false` | boolean |
| `elevation_mm` | Yes | — | number |
| `name` | Yes | — | string |

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
Create a level at an elevation, optionally with its floor plan.

A level whose name already exists is refused. dry_run returns the same verification block
without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
