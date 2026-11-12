---
description: "Read durable run and model status after the initiating client exits."
---

# Batch collection status

`revit_batch_status`

<p class="facts"><span><b>Group</b> Batch and reports</span><span><b>Kind</b> Read</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_batch_status.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `run_id` | Yes | — | string |

</div>

The development-line contract ships no parameter descriptions.

## Behavior (registry text) {#behavior}

```text
Read durable run and model status after the initiating client exits.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
