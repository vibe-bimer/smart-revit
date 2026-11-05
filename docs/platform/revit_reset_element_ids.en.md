---
description: "Give elements new element IDs by copying each one over its original. The API cannot assign an element ID, so every element is copied, checked and then replaces its original. Elements that cannot be replaced are refused by name, and a real run is refused when any element in the selection is. dry_run returns the same block without keeping the changes."
---

# Reset Element Ids

`revit_reset_element_ids`

<p class="facts"><span><b>Group</b> Editing primitives</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Fork (this repository) · Grafted</span><span><b>Status</b> Unreleased (integration branch)</span><span><b>Release version</b> 1.0.0</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

!!! note "Usage notes"
    Rehearsable, reports the cost in dry_run, and commits each element in its own subtransaction.

[Same-name release page](../features/revit_reset_element_ids.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.0.0.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
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
Give elements new element IDs by copying each one over its original.

The API cannot assign an element ID, so every element is copied, checked and then replaces
its original. Elements that cannot be replaced are refused by name, and a real run is
refused when any element in the selection is. dry_run returns the same block without keeping
the changes.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
