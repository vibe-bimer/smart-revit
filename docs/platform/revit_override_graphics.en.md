---
description: "Colour elements in selected model views; reset restores overrides saved in this Revit session."
---

# Highlight Elements

`revit_override_graphics`

<p class="facts"><span><b>Group</b> Views, sheets and schedules</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.2</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_override_graphics.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.2.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `color` | No | `"#FF0000"` | string |
| `dry_run` | No | `false` | boolean |
| `element_ids` | Yes | — | array |
| `fill` | No | `true` | boolean |
| `halftone_others` | No | `false` | boolean |
| `line_weight` | No | `null` | any |
| `reset` | No | `false` | boolean |
| `transparency` | No | `0` | integer |
| `views` | No | `"active"` | any |

</div>

The development-line contract ships no parameter descriptions.

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | any | Title or file name substring of the target open document; needed when several are open. |

</div>

## Behavior (registry text) {#behavior}

```text
Colour elements in selected model views; reset restores overrides saved in this Revit session.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
