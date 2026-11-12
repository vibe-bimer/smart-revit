---
description: "Copy elements into the same model, keeping their hosts. target_level copies onto that level's height instead of the vertical offset; the horizontal offsets always add on top. A hosted element needs its host in element_ids, because the copy is one batch and this server never leaves a hosted element without a host."
---

# Copy Elements

`revit_copy_elements`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Only the overload that re-hosts, the duplicate-type handler always set, hosts required in the same batch, and an element-by-element pairing with idMappingVerified.

[Same-name release page](../features/revit_copy_elements.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `dx_mm` | No | `0` | number |
| `dy_mm` | No | `0` | number |
| `dz_mm` | No | `0` | number |
| `element_ids` | Yes | — | array |
| `target_level` | No | `null` | any |

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
Copy elements into the same model, keeping their hosts.

target_level copies onto that level's height instead of the vertical offset; the horizontal
offsets always add on top. A hosted element needs its host in element_ids, because the copy
is one batch and this server never leaves a hosted element without a host.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
