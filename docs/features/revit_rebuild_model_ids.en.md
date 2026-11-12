---
description: "Copy selectable 3D-view components into one or more new models with fresh IDs"
---

# Rebuild IDs in new models

`revit_rebuild_model_ids`

<p class="facts"><span><b>Group</b> Batch and ids</span><span><b>Kind</b> Action (opt-in)</span><span><b>Since</b> 0.8.0</span><span><b>Version</b> Released 1.1.2</span><span><b>Same-name tool on the development line</b> Yes</span><span><b>This contract applies to the release</b> Yes</span><span><b>Effect</b> New model files; source unchanged</span><span><b>Origin</b> Fork (this repository)</span></p>

Copy selectable 3D-view components into one or more new models with fresh IDs

!!! warning "Actions are allowed by default; read-only is explicit"
    Actions are allowed unless one of three switches is on: the machine policy `ReadOnly`, the workstation `read-only` file, or `REVIT_MCP_READ_ONLY=1`. A fresh install ships with the machine policy read-only. The action connection must address one Revit instance; use `document` when it has multiple open documents. Selection, navigation and isolation also require the target document to be active.

!!! note "Usage notes"
    The source stays unchanged; only selectable 3D-view elements and required datums are copied, not the full project; check every count and ID mapping; a delta is an extra shift, not a target gap

[Same-name development line page](../platform/revit_rebuild_model_ids.md)

## Contract differences from the development line {#contract-diff}

The list below is computed from the registry inputSchema; it is not a hand-written list.

- Parameter per_copy_deltas exists only in the release
- Parameter warmup_copy exists only in the release

This page is the contract of release 1.1.2; the same-name tool on the development line takes different parameters, so do not mix them.

## Copyable prompts {#prompts}

```text
Rebuild the selectable components into E:\out\copy-{n}.rvt, ten copies, no id shared between them
```

```text
Rehearse the rebuild first: how many components, which new id range, write nothing yet
```

```text
Produce 24 copies; warm the first copy away, raise per_copy_deltas per copy from the gap a dry run measured, and rehearse first
```

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `destination_path` | Yes | — | `string` | new model path (.rvt); {n} numbers the copies |
| `copies` | No | `1` | `integer` | how many copies one new model produces (1–50), each in an id block of its own |
| `dry_run` | No | `false` | `boolean` | rehearse in a temporary new document and report the mapping without saving; the source always stays unchanged |
| `duplicate_names` | No | `"override"` | `string` | duplicate names: override keeps the source types, reuse keeps the version the new model holds (the batch default), rename is the legacy path |
| `overwrite` | No | `false` | `boolean` | replace the destination when it exists |
| `per_copy_deltas` | No | `null` | `array<integer> / null` | extra shift before each output copy; exactly one entry per copy, each an integer 0-1000000; an additive temp-level count, not a target gap or an absolute id, so rehearse on the actual model first |
| `remove_template_levels` | No | `true` | `boolean` | drop the template levels after copying (on by default) |
| `seed` | No | `0` | `integer` | create and remove N temporary levels to advance new-document IDs; use different seeds across runs and verify overlap in the mappings |
| `template_path` | No | `null` | `string / null` | starting template (.rte/.rvt); the metric template is used when omitted |
| `view` | No | `null` | `string / null` | view name (or its Revit id) |
| `warmup_copy` | No | `null` | `boolean / null` | run one first copy (types and template cleanup) and delete it all without saving, so the output copies start from a stable state; seed still applies once before the warmup |

</div>

### Common parameters {#common-parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} | Meaning {scope=col} |
| --- | :--: | --- | --- | --- |
| `document` | No | `null` | `string / null` | Case-insensitive document-title or file-name substring. Reads use it to address an instance; it must be unique with multiple instances. Actions use it to choose an open document in the addressed instance; required with multiple open documents. Unknown or ambiguous targets are rejected |

</div>

## Behavior and returned data {#contract}

Rebuild the model into a new document so every element gets a new element ID.

`destination_path` is the new model, with {n} replaced by the copy number when `copies`
exceeds one. `per_copy_deltas` optionally adds temporary seed levels before each delivered
copy: exactly one entry per copy, each a whole number from 0 to 1000000, while `seed` applies
once before everything else. `warmup_copy` runs one extra internal copy first that absorbs the
template cleanup and is discarded, so no delivered copy carries it. Reports the old to new
pairing, the per-file results and the category counts. dry_run reports the plan without
writing files.

## Revit year support {#year-support}

| Revit year | Validation |
| --- | --- |
| 2020 | <span class="state ok">Validated live</span> |
| 2026 | <span class="state part">Build only, not live-tested</span> |
| 2022–2025 / 2027 | <span class="state part">Build only, not live-tested</span> |

Validated live means an execution was recorded on a real workstation. Build only means compilation passed, not live functional validation. Revit 2021 is outside this project's build targets.

---

[All features](index.md) · [Version support matrix](matrix.md) · [Prompt library](prompts.md)
