---
description: "Export PDF, DWG, IFC or schedule CSV files on the Revit workstation; dry_run returns planned file names. Replacing existing files (overwrite=true) needs a confirm_token from a first call. A long action can return status=running and jobId when the wait budget expires; it may already have changed the model, and revit_jobs returns its result. Resubmitting repeats the action."
---

# Export Model Files

`revit_export`

<p class="facts"><span><b>Group</b> Export and registers</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.3</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_export.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.3.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `all_sheets` | No | `false` | boolean |
| `confirm_token` | No | `null` | any |
| `dry_run` | No | `false` | boolean |
| `format` | Yes | — | string |
| `options` | No | `null` | any |
| `output_dir` | No | `null` | any |
| `overwrite` | No | `false` | boolean |
| `sheet_set` | No | `null` | any |
| `sheets` | No | `null` | any |
| `views` | No | `null` | any |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target open document; needed when several are open. |
| `timeout_seconds` | No | `1800` | integer | (not documented in the development-line contract) |

</div>

## Behavior (registry text) {#behavior}

```text
Export PDF, DWG, IFC or schedule CSV files on the Revit workstation; dry_run returns planned file names. Replacing existing files (overwrite=true) needs a confirm_token from a first call. A long action can return status=running and jobId when the wait budget expires; it may already have changed the model, and revit_jobs returns its result. Resubmitting repeats the action.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
