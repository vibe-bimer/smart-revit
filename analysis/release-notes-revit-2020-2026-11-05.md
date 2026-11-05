# Revit 2020 in the release notes, dated

- Written: 2026-11-05
- Why: [ADR 0006](../adr/0006-port-on-2026-first-restore-revit-2020-as-required-follow-up.md), Consequences — "The first release after the port carries a visible gap for 2020 workstations, closed in the next release. The release notes must say both the gap and the date."
- Status: the paragraph is written and its landing point is specified. No version section exists yet, so nothing is fixed on disk.

## The gap was in the notes, not the build

Revit 2020 support entered the tree on 2026-09-28 (`14ed865`). The `Debug.R20` and `Release.R20` build configurations followed on 2026-11-03 (`4f161e7`). Both commits are ancestors of `v1.0.0`, tagged 2026-11-04 10:28:33 on `572868c`. So the first release after the port shipped with a 2020 build.

The notes did not say so. The `## [1.0.0]` section of [CHANGELOG.md](../CHANGELOG.md) is upstream's entry of 2026-10-16 and mentions Revit 2020 zero times. The GitLab release job copies that section verbatim into the release description, so the v1.0.0 release page told 2020 users nothing.

That silence is the gap ADR 0006 wanted stated. The date it gets stated is 2026-11-05, which is what the paragraph below carries.

## The paragraph to paste into the release notes

Paste this block, unedited, into the version's `## [x.y.z]` section. It must not contain a `## ` heading of its own: the release job stops at the next one.

```text
Revit 2020 is supported. This note states that where the v1.0.0 notes did not.

Revit 2020 entered the tree on 2026-09-28 (14ed865). The Release.R20 build configurations followed on 2026-11-03 (4f161e7). Both are in v1.0.0, tagged 2026-11-04, so no fork release has shipped without a 2020 build. The v1.0.0 release notes were upstream's 1.0.0 entry of 2026-10-16, and they said nothing about Revit 2020. 2020 users had no statement to read. This note closes that gap, dated 2026-11-05.

Coverage, verified on Revit 2020 (build 20.0.0.377): 92 of the 93 tools are live-verified. revit_sync_document is the exception. It needs a workshared central model and answers "This document has no central model to synchronize." by design.

What differs on 2020: PDF export is refused, because the API needs Revit 2021 or later; use dwg or ifc. revit_duplicate_view runs unattended only in mode: dependent. revit_rebuild_model_ids passes on the acceptance models, but on a model carrying duplicate family-type names it cannot run unattended, because each duplicate opens a modal dialog that blocks the channel. revit_batch_start needs REVIT_MCP_REVIT_EXE_2020 when Revit is installed outside %ProgramFiles%.

What refuses as designed on 2020, with its recorded message: revit_export takes schedules only for format csv; revit_apply_view_template explains a type mismatch; revit_reset_element_ids refuses when dependents would be deleted with it; revit_move reports "1 constrained and unchanged". revit_batch_fetch reads a finished run, but a run produced by the supervisor stays unproven there. Revit 2022 through 2025, and 2027, remain build-only.

The evidence, with ids and verbatim messages, is in docs/validation.md.
```

## Where it has to land

The GitLab release job writes the release description from [CHANGELOG.md](../CHANGELOG.md), not from this file. `.gitlab-ci.yml` lines 415 to 460 run on a `vX.Y.Z` tag, read `CHANGELOG.md`, and extract the version's section with the expression it has always used:

```python
re.search(
    rf"^## \[?{re.escape(version)}\]?[^\n]*\n(.*?)(?=^## |\Z)", changelog, re.S | re.M
)
```

That capture becomes `description` in the `POST /releases` payload. A version with no matching section falls back to `Release {version}.`, so a missing paragraph fails silently rather than loudly.

Three texts currently disagree about who writes that section:

- [CONTRIBUTING.md](../CONTRIBUTING.md) line 205 says release-please owns `CHANGELOG.md` and the version in `server/pyproject.toml`.
- [CHANGELOG.zh.md](../CHANGELOG.zh.md) says the English log must not be edited by hand, and that entries from 1.0.0 up are English only, with the translation still pending.
- release-please runs on GitHub Actions only, through `.github/workflows/release-please.yml`, and this fork does not push its GitHub remote.

One decision is therefore outstanding, and this file does not make it: revive the release-please workflow against a reachable remote, or write the version section by hand at tag time and amend those texts to say so. Either way the paragraph must sit inside the version's own section before the tag, because that section is the only input the release job reads.

## Coverage behind the paragraph

The numbers come from [docs/validation.md](../docs/validation.md), which records each acceptance run with ids and verbatim messages.

- 93 tools: 35 read and 58 action.
- 2020: all 93 called at least once, 92 live-verified. `revit_sync_document` is the exception and stays build-only, because a non-workshared document answers `This document has no central model to synchronize.` by design.
- 2020 rounds: 2026-09-28 and 29, the first full pass, 19 read and 16 action tools against the surface as it stood then; 2026-11-03, the first modelling batch; 2026-11-04, the full sweep on `base-2020.rvt`; 2026-11-05, the nine tools still holding only build evidence, of which eight reached live-verified.
- 2026: 18 read and 17 action tools live-verified, the rest build evidence only.
- 2022 through 2025, and 2027: build evidence only.

## What this file is not

- Not an edit to `CHANGELOG.md` or to the version in `server/pyproject.toml`; release-please owns both.
- Not a release. No tag, no GitLab release, no asset upload.
- Not a claim that 2020 equals 2026. The differences above are real, and the paragraph names them.
