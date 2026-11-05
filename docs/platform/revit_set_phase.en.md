---
description: "Set the creation and demolition phase of elements. An empty string clears a phase and null leaves it alone; at least one must be given. dry_run returns the same verification block without changing the model."
---

# Set Phase

`revit_set_phase`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (integration branch)</span><span><b>Release version</b> 1.0.0</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Revit cannot create or rename phases, so it only assigns existing ones.

[Same-name release page](../features/revit_set_phase.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.0.0.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `created_phase` | No | `null` | any |
| `demolished_phase` | No | `null` | any |
| `dry_run` | No | `false` | boolean |
| `element_ids` | Yes | — | array |

</div>

The branch contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `document` | No | `null` | any |

</div>

The branch contract ships no parameter descriptions.

## Behavior (registry text) {#behavior}

```text
Set the creation and demolition phase of elements.

An empty string clears a phase and null leaves it alone; at least one must be given.
dry_run returns the same verification block without changing the model.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
