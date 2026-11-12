---
description: "Compile and run C# against the live Revit API on the Revit thread. Accepts a method body or a public static Script class with Execute(ScriptContext ctx). Auto mode owns one transaction and undo entry; transaction=\"none\" is refused by default. Needs confirm_token from a first call, which runs nothing; dry_run needs none and forces transaction=\"auto\". A long action can return status=running and jobId when the wait budget expires; it may already have changed the model, and revit_jobs returns its result. Resubmitting repeats the action."
---

# Execute C# Code

`revit_execute_code`

<p class="facts"><span><b>Group</b> C# escape hatch</span><span><b>Kind</b> Action</span><span><b>Base and fork tools</b> Base (upstream)</span><span><b>Status</b> Unreleased (development line)</span><span><b>Release version</b> 1.1.4</span><span><b>Source branch</b> <code>feat/gitlab-pages</code></span><span><b>Source commit</b> <code>50baa705e8da63327ab2bff1e544c76252fddbc9</code></span><span><b>Same-name tool in the release</b> Yes, with identical parameters</span><span><b>This contract applies to the release</b> No</span></p>

[Same-name release page](../features/revit_execute_code.md)

## Contract differences from the release {#contract-diff}

The same-name tool has an identical contract to release 1.1.4.

## Parameters {#parameters}

<div class="rmc-tablewrap" markdown="1">

| Parameter {scope=col} | Required {scope=col} | Default {scope=col} | Type {scope=col} |
| --- | :--: | --- | --- |
| `code` | Yes | — | string |
| `confirm_token` | No | `null` | any |
| `dry_run` | No | `false` | boolean |
| `transaction` | No | `"auto"` | string |

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
Compile and run C# against the live Revit API on the Revit thread. Accepts a method body or a public static Script class with Execute(ScriptContext ctx). Auto mode owns one transaction and undo entry; transaction="none" is refused by default. Needs confirm_token from a first call, which runs nothing; dry_run needs none and forces transaction="auto". A long action can return status=running and jobId when the wait budget expires; it may already have changed the model, and revit_jobs returns its result. Resubmitting repeats the action.
```

---

[Back to the catalog](index.md) · [Fork tool migration status](fork-tools.md)
