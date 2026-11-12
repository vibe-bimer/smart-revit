---
description: "Activate an already open document by title or path reference."
---

# Activate Document

`revit_activate_document`

<p class="facts"><span><b>Group</b> Document lifecycle</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_activate_document.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

No additional business parameters; use the common parameters below.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `document` | Yes | — | string |
| `process_id` | No | `null` | any |

</div>

The development-line contract ships no parameter descriptions.

## Behavior (registry text) {#behavior}

```text
Activate an already open document by title or path reference.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
