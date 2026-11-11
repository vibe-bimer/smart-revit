---
description: "Create a grid line: straight from `start_mm` to `end_mm`, or a three-point arc through `mid_mm`. `label` names the grid (Grid.Name); a grid whose name already exists is refused. Points are [x, y] in millimetres on the horizontal plane. dry_run returns the same verification block without changing the model."
---

# Create Grid

`revit_create_grid`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.1</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Line and three-point arc, duplicate-name refusal, and the batch step vocabulary.

[Same-name release page](../features/revit_create_grid.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.1.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `end_mm` | Yes | — | array |
| `label` | Yes | — | string |
| `mid_mm` | No | `null` | any |
| `start_mm` | Yes | — | array |

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
Create a grid line: straight from `start_mm` to `end_mm`, or a three-point arc through `mid_mm`.

`label` names the grid (Grid.Name); a grid whose name already exists is refused.
Points are [x, y] in millimetres on the horizontal plane. dry_run returns the same
verification block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
