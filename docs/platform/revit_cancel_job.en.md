---
description: "Request cancellation of an action jobId. Process-models stops before the next model and marks unstarted models cancelled; a single running Revit operation finishes, and completed changes stay committed."
---

# Cancel Action Job

`revit_cancel_job`

<p class="facts"><span><b>Group</b> Connection and instances</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.3</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_cancel_job.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.3.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `job_id` | Yes | — | string |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target open document; needed when several are open. |
| `process_id` | No | `null` | any | (not documented in the development-line contract) |

</div>

## Behavior (registry text) {#behavior}

```text
Request cancellation of an action jobId. Process-models stops before the next model and marks unstarted models cancelled; a single running Revit operation finishes, and completed changes stay committed.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
