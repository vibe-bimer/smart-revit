---
description: "Copy elements inside one model and keep their hosts; every element reports its old id to its new id"
---

# Copy elements

`revit_copy_elements`

<p class="facts"><span><b>Group</b> Editing</span><span><b>Kind</b> Action (opt-in)</span><span><b>Since</b> 1.1.0</span><span><b>Version</b> Released 1.1.4</span><span><b>Same-name tool on the development line</b> Yes</span><span><b>This contract applies to the release</b> Yes</span><span><b>Effect</b> Model elements / parameters</span><span><b>Origin</b> Fork (this repository)</span></p>

Copy elements inside one model and keep their hosts; every element reports its old id to its new id

!!! warning "Actions are allowed by default; read-only is explicit"
    Actions are allowed unless one of three switches is on: the machine policy `ReadOnly`, the workstation `read-only` file, or `REVIT_MCP_READ_ONLY=1`. A fresh install ships with the machine policy read-only. The action connection must address one Revit instance; use `document` when it has multiple open documents. Selection, navigation and isolation also require the target document to be active.

!!! note "Usage notes"
    A hosted element needs its host in the same request or the batch is refused with both ids, because Revit deletes a hosted copy that finds no host; copying destroys nothing, so a refusal is reported per element; CopyElements promises no order, so pairs are proven by category, type and position and the mapping is marked unverified when a pair cannot be proven

[Same-name development line page](../platform/revit_copy_elements.md)

## Copyable prompts {#prompts}

```text
Copy these three columns 3000 mm east
```

```text
Copy this wall and the door on it onto 2F
```

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `element_ids` | Yes | — | `array<integer>` | elements to copy; a hosted element's host has to be listed too |
| `dry_run` | No | `false` | `boolean` | rehearse: copy, report the pairing, then roll back |
| `dx_mm` | No | `0` | `number` | horizontal X offset in millimetres; 0 by default |
| `dy_mm` | No | `0` | `number` | horizontal Y offset in millimetres; 0 by default |
| `dz_mm` | No | `0` | `number` | vertical offset in millimetres; 0 by default, and it adds to the level difference when target_level is given |
| `target_level` | No | `null` | `string / null` | target level name; its height difference becomes dz, added to dz_mm |

</div>

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | `string / null` | Case-insensitive document-title or file-name substring. Reads use it to address an instance; it must be unique with multiple instances. Actions use it to choose an open document in the addressed instance; required with multiple open documents. Unknown or ambiguous targets are rejected |

</div>

## Behavior and returned data {#contract}

Copy elements into the same model, keeping their hosts.

target_level copies onto that level's height instead of the vertical offset; the horizontal
offsets always add on top. A hosted element needs its host in element_ids, because the copy
is one batch and this server never leaves a hosted element without a host.

## Revit year support {#year-support}

| Revit year | Validation |
| --- | --- |
| 2020 | <span class="state ok">Validated live</span> |
| 2026 | <span class="state ok">Validated live</span> |
| 2022–2025 / 2027 | <span class="state part">Build only, not live-tested</span> |

Validated live means an execution was recorded on a real workstation. Build only means compilation passed, not live functional validation. Revit 2021 is outside this project's build targets.

---

[All features](index.md) · [Version support matrix](matrix.md) · [Prompt library](prompts.md)
