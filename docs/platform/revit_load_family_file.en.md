---
description: "Load one family file from the workstation: the whole family, or the single type `type_name`. The load always carries the family load options, so it never waits on Revit's own dialog. An existing family is reused, and its parameter values are left alone unless `overwrite_parameters` is true. The response reports `state` (\"new\" or \"existing\") and every type the family now offers. A path that does not exist is refused with the closest filenames beside it. dry_run returns the same verification block without changing the model."
---

# Load Family File

`revit_load_family_file`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.3</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    One file, an optional single type, the load options always supplied, and the closest names for a missing path.

[Same-name release page](../features/revit_load_family_file.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.3.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `overwrite_parameters` | No | `false` | boolean |
| `path` | Yes | — | string |
| `type_name` | No | `null` | any |

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
Load one family file from the workstation: the whole family, or the single type `type_name`.

The load always carries the family load options, so it never waits on Revit's own dialog.
An existing family is reused, and its parameter values are left alone unless
`overwrite_parameters` is true. The response reports `state` ("new" or "existing") and every
type the family now offers. A path that does not exist is refused with the closest filenames
beside it. dry_run returns the same verification block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
