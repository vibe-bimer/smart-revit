---
description: "Rebuild the model into a new document so every element gets a new element ID. `destination_path` is the new model, with {n} replaced by the copy number when `copies` exceeds one. Reports the old to new pairing, the per-file results and the category counts. dry_run reports the plan without writing files."
---

# Rebuild Model Ids

`revit_rebuild_model_ids`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.4</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, but the parameters differ</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Supports templates, copies and duplicate-name policies; about a thousand lines, and the last of the fourteen to land.

[Same-name release page](../features/revit_rebuild_model_ids.md)

## Contract differences from the release {#contract-diff}

The table below is computed from the registry inputSchema; it is not a hand-written list.

- Parameter per_copy_deltas exists only in the release
- Parameter warmup_copy exists only in the release

This contract belongs to the development line, not to release 1.1.4; copying these parameters fails on the release.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `copies` | No | `1` | integer |
| `destination_path` | Yes | — | string |
| `dry_run` | No | `false` | boolean |
| `duplicate_names` | No | `"override"` | string |
| `overwrite` | No | `false` | boolean |
| `remove_template_levels` | No | `true` | boolean |
| `seed` | No | `0` | integer |
| `template_path` | No | `null` | any |
| `view` | No | `null` | any |

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
Rebuild the model into a new document so every element gets a new element ID.

`destination_path` is the new model, with {n} replaced by the copy number when `copies`
exceeds one. Reports the old to new pairing, the per-file results and the category counts.
dry_run reports the plan without writing files.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
