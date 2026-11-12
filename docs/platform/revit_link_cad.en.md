---
description: "Link or import a DWG into a plan view on the Revit workstation. Returns CAD layers and extents in mm."
---

# Link CAD Drawing

`revit_link_cad`

<p class="facts"><span><b>Group</b> CAD and MEP</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_link_cad.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `dry_run` | No | `false` | boolean |
| `layers` | No | `null` | any |
| `level` | No | `null` | any |
| `link` | No | `true` | boolean |
| `origin` | No | `"internal"` | string |
| `path` | Yes | — | string |
| `units` | No | `"auto"` | string |
| `view` | No | `null` | any |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target open document; needed when several are open. |
| `timeout_seconds` | No | `600` | integer | (not documented in the development-line contract) |

</div>

## Behavior (registry text) {#behavior}

```text
Link or import a DWG into a plan view on the Revit workstation. Returns CAD layers and extents in mm.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
