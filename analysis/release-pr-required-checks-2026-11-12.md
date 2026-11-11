# Release-please PR checks and required status checks on `main`

- Research date: 2026-11-12, Asia/Shanghai.
- Repository: `vibe-bimer/smart-revit`, local `main` at `afde055` during this investigation. PR #12 merged as `37ecb45`; `3d5ebc77` preceded that merge.
- Status: **research only**. No workflow file, branch protection rule, ruleset, secret or repository setting was changed. No credential was created, read or printed. Nothing was committed or pushed.

## 1. Question

How does the `chore(main): release X.Y.Z` pull request get checks attached to it, and what has to be true before `main` can safely require those checks?

## 2. Short answer

- The release PR currently carries **no check runs**. It is not, however, "not triggered": GitHub creates four `pull_request` workflow runs for every release PR, and none of them start.
- Since 2026-05 GitHub documents that a pull request created with `GITHUB_TOKEN` produces `pull_request` runs in an **approval-required** state. A user with write access can start them from the merge box. A personal access token is therefore no longer required to *get* checks, only to get them *without a click*.
- Required checks can only name checks that actually report on the pull request head. The names this repository really produces are listed in §6.

## 3. What this repository has today

### 3.1 Workflows

| Workflow | Trigger | Notes |
| --- | --- | --- |
| `release-please.yml` | `workflow_dispatch` only (`release-please.yml:9`) | Reads `secrets.RELEASE_PLEASE_TOKEN` (`:32`), falls back to `github.token` (`:37`), gates the dispatch fallback on `has_pat` (`:43`). |
| `pr-checks.yml` | `pull_request: [opened, synchronize, reopened, ready_for_review]` (`:4-5`) | Aggregate job `quality` is displayed as `pr-checks` (`:98-99`). |
| `ci.yml` | `push: [main]` and `workflow_call` | Aggregate job `test`; its comment claims branch protection requires `CI / test` (`ci.yml:12`). |
| `release-window.yml` | `pull_request: [opened, synchronize, reopened, labeled, unlabeled]` plus a cron (`:8-11`) | Monday-only gate for the release PR; the cron job reruns the existing `pull_request` run (`:62-74`). |

### 3.2 Live repository state (read-only API, 2026-11-12)

- `GET /branches/main/protection` → `404 Branch not protected`.
- `GET /rulesets` → `[]`.
- `GET /actions/permissions` → enabled, `allowed_actions: all`.
- `GET /actions/permissions/workflow` → `default_workflow_permissions: read`, `can_approve_pull_request_reviews: true`.
- `GET /actions/secrets` → `total_count: 0`. No `RELEASE_PLEASE_TOKEN` exists, so every release so far ran on `GITHUB_TOKEN`.

### 3.3 What the two release pull requests actually did

| PR | Head | Created | Merged | Runs created for it |
| --- | --- | --- | --- | --- |
| #6 `chore(main): release 1.1.0` | `02ae6091` | 10:16:24Z | 10:17:27Z | 4, all `failure`, 0 jobs |
| #8 `chore(main): release 1.1.1` | `8116839d` | 10:27:13Z | 10:27:57Z | 4, all `failure`, 0 jobs |

For #8 the four runs were `PR checks`, `CodeQL`, `Dependency audit` and `Release window`, all created at 10:27:17Z and finalized at 10:27:59Z — one second after the merge. Every run reported `total_count: 0` jobs, `commits/8116839d/check-runs` returned nothing, and the four check suites on that commit had `latest_check_runs_count: 0`.

For contrast, the head commit of Dependabot PR #12 (`0467354`) has 28 check runs and eight completed suites with `conclusion: success`.

Observed: the events fire and the runs exist, but no job executes. The timing is consistent with documented approval-required runs ending when the PR closes. This is an inference: neither the banner nor the original approval state was captured. A zero-job failed run alone does not prove its cause.

## 4. The trigger rule and its history

`GITHUB_TOKEN` events do not create workflow runs, with documented exceptions ([docs.github.com/en/actions/concepts/security/github_token](https://docs.github.com/en/actions/concepts/security/github_token)):

> `pull_request` events with the `opened`, `synchronize`, or `reopened` activity types: when a workflow using `GITHUB_TOKEN` creates or updates a pull request, the resulting `pull_request` event creates workflow runs in an approval-required state. The pull request displays a banner in the merge box, and a user with write access to the repository can start the runs by selecting Approve workflows to run. Other `pull_request` activity types (such as `labeled`, `edited`, or `closed`) do not create workflow runs.

The same page adds that a GitHub App installation access token or a personal access token is the way to get runs that execute without approval, and the event reference repeats it for `pull_request` ([events-that-trigger-workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)).

Provenance, because this changed recently and most secondary sources predate it:

| Date | Commit in `github/docs` | Change |
| --- | --- | --- |
| 2026-04-23 | `4591eedc` | Documents the approval behaviour (#60926) |
| 2026-04-24 | `e213f3fc` | Reverted (#60952) |
| 2026-05-22 | `24a7a1dc` | Re-landed (#61001) |

Two consequences for this repository:

- `release-please.yml:28` ("the release PR shows no checks") is stale. The PR gets runs; it does not get results.
- The release-please v5 README ("all resources created by release-please … will not trigger future GitHub actions workflows", and "configure … a Personal Access Token if you want GitHub Actions CI checks to run") is likewise stale. The action itself contains no trigger logic; it only uses the token as an API credential.

What the exception does **not** cover, and still matters here:

- `push` is not an exception. A tag pushed with `GITHUB_TOKEN` still starts no workflow, so `dispatch-release` (`release-please.yml:41-55`) remains necessary under the `GITHUB_TOKEN` path.
- `labeled` and `unlabeled` events produced with `GITHUB_TOKEN` create no runs. This restriction concerns the credential causing the event, not every later event on that PR. A maintainer adding `hotfix-release` with a user credential can trigger the existing label handler; that run and its approval state still need observation.
- `ready_for_review` is not an exception. Harmless while release-please opens non-draft PRs.

Approval mechanics ([approve-runs-from-forks](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks)): Files changed → "Awaiting approval" → "Approve workflows to run". Runs awaiting approval for more than 30 days expire and are marked failed.

## 5. Three ways to get results on the release PR

### A. Approve by hand (no new credential)

Click "Approve workflows to run" on the release PR; the four runs start on `refs/pull/N/merge`.

Costs and limits:

- Requires write access. A bot push that updates the PR produces `synchronize`, which is covered by the approval exception. Whether GitHub retains a previous approval for the same PR was not tested; plan to inspect approval again after each update.
- With required checks enabled this stops being optional: an unapproved run is not a success, so the merge box stays blocked until someone approves.
- Both historical PRs were merged before any jobs were observed. Their suites finalized as failures immediately after merge. Approval as the cause is consistent with documentation but was not captured directly.

### B. Use a non-`GITHUB_TOKEN` credential

Either a fine-grained PAT in `secrets.RELEASE_PLEASE_TOKEN`, or a GitHub App installation token.

- Permissions needed by release-please: `contents: write` and `pull-requests: write`, plus `issues: write` only if using labels. **Checks API is not needed** — Actions creates the check runs, not the token.
- Fine-grained PAT ([managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)): one resource owner, selected repositories, an expiry date, and a documented limitation on calling the Checks API (irrelevant here). It is tied to a person.
- GitHub App ([making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow)): `actions/create-github-app-token@v3` with `client-id` from a repository variable and the private key from a secret; installation tokens rotate and outlive staff changes.
- Behaviour change beyond checks: with a non-`GITHUB_TOKEN` credential the tag push also starts `release.yml` on its own, which is what `release-please.yml:26-28` promises. The current `dispatch-release` fallback would then be redundant.
- Wiring cost: the PAT path needs only the secret to exist, because `release-please.yml:32` and `:37` already read it. The App path needs a workflow edit plus a revision of the `has_pat` detection at `:32-33`, which keys off the PAT secret.

### C. Dispatch a checks workflow instead (no new credential)

`workflow_dispatch` is an explicit exception, so a job holding `GITHUB_TOKEN` can dispatch a workflow. But the dispatched run is bound to the ref it was dispatched against: `GITHUB_REF` is the branch or tag, `GITHUB_SHA` is its last commit, and the workflow file must exist on the default branch to be dispatchable at all.

That makes it a poor substitute here:

- `pr-checks.yml` cannot be dispatched as written. It reads `github.event.pull_request` in the concurrency group (`:11`), in `amannn/action-semantic-pull-request` (`:28`), and in the `explain-failure` condition (`:114`). A dispatch would collapse the concurrency group to `pr-checks-` and fail the title check outright.
- A wrapper that dispatches a checks workflow at `release-please--branches--main` validates the **branch tip**, not `refs/pull/N/merge`. Once `main` has moved, that is not the commit the merge would produce, so the result can be green while the merged tree is not.
- A dispatch run of `release.yml --ref "$RELEASE_TAG"` (`:55`) attaches its checks to the tag commit. In this repository's squash-release flow that is the post-merge commit, not the still-open PR's tested merge tree; a successful publish is not pre-merge PR evidence.

## 6. Check names this repository actually produces

Read from the head commit of Dependabot PR #12 (`0467354`), which is a normal `pull_request` run, not a release PR:

| Check name | Source |
| --- | --- |
| `pr-checks` | `pr-checks.yml:99` aggregate job |
| `CI / test` | `ci.yml` aggregate job, reported through the reusable call |
| `CI / addin-build (20)` … `(27)`, `CI / installer`, `CI / python`, `CI / core-tests`, `CI / bundle`, `CI / docs-line` | `ci.yml` matrix and jobs |
| `release-window` | `release-window.yml:19` |
| `quality-linux`, `dotnet-format` | `pr-checks.yml` individual jobs |
| `explain-failure` | `pr-checks.yml:111`, `skipped` on success |
| `CodeQL`, `CodeQL (csharp)`, `CodeQL (python)`, `auto-merge`, `community / community` | other workflows |

Rules that decide whether a required check helps or deadlocks the repository ([about-protected-branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [status-checks](https://docs.github.com/en/pull-requests/reference/status-checks)):

- Required checks must end `successful`, `skipped` or `neutral`; a skipped job reports success.
- A required check that has never reported sits in `expected` and blocks the merge indefinitely. Set required checks only after watching the name appear on a real pull request.
- Job names must be unique across workflows. Two jobs called `pr-checks` would produce ambiguous results and block merges.
- Optionally pin the expected source app; here that would be `github-actions`.
- "Strict" (branch must be up to date) costs a full rebuild after every `main` move; `CI / test` alone is heavy already (`installer` builds an MSI).

Suggested minimum after release validation: require both `pr-checks` and `CI / test`. They aggregate different jobs. Add `release-window` only if the Monday rule must block merges rather than merely report.

## 7. Recommended sequence

1. Do not activate required checks in this research task. Keep the existing credential path and release dispatch fallback.
2. First repair the version/generation readiness problem in §7.1. A credential change alone will not make a release PR pass.
3. On the next release, dispatch release-please, **leave the PR open**, approve the workflows, and record the banner, exact check names and results. Inspect approval again after a `synchronize`. Do not merge an unchecked PR for this test.
4. Prefer A initially for this single-maintainer, manually dispatched release process. Choose B only if eliminating the approval click is worth credential maintenance. The PAT hook already exists; an App needs workflow wiring.
5. Once a release PR passes, require both `pr-checks` and `CI / test`, with GitHub Actions as the expected app. The two aggregates cover different jobs; either one alone leaves a gap.
6. Treat `release-window` as a separate product decision. It enforces Monday in Europe/Moscow, not merely code quality. Require it only if that schedule is intended for this fork.
7. Do not add an admin bypass merely to merge an untested release. A controlled emergency bypass is a separate policy decision, not a replacement for release evidence.
8. Retire `dispatch-release` only after a credential change has been observed to start `release.yml` from the tag push in a real release.

### 7.1 A second blocker: the release PR is not ready to pass documentation checks

The trigger problem and the content problem are separate:

- `release-please-config.json:12-18` updates `server/pyproject.toml` as its only extra version file. It does not regenerate the documentation or advance the published catalog state.
- `tools/site/content/catalogs.yaml:43-49` reads the project version but separately declares `released_version: 1.1.1`, explicitly meaning the last version actually published.
- `tools/site/test_catalogs.py:28-42` nevertheless asserts `published == current`. Preparing a new release necessarily breaks this assertion before that release has shipped.
- `pr-checks.yml:59-60` checks generated pages before running the site test suite. Generated pages naming the new version must also be regenerated within the release PR; past releases required post-merge repairs for this same drift.

A read-only, in-memory probe on 2026-11-12 ran the existing test unmodified, then used `dataclasses.replace(catalogs.release(), version='1.1.2')` and `unittest.mock.patch.object(catalogs, 'release', return_value=future)` to run it again. The baseline passed. The simulated release bump failed with `'1.1.1' != '1.1.2'` and `the catalog still calls 1.1.1 the published version while the project is at 1.1.2; bump released_version when you cut the tag`. No tracked file was mutated.

Proposed repair, not implemented: model the project version as the prepared version and `released_version` as the last successful publication. Test that published does not exceed prepared; verify publication state at the successful release boundary. Regenerate version-dependent pages in the release PR and commit them there. Keep `released_version` at the previous shipped version until publication succeeds, rather than calling an unpublished version published just to satisfy the test. Updating publication metadata and regenerating its badges after successful publishing is a separate release-finalization step.

For the initial manual-approval route, a maintainer can prepare and push the generated-page changes before approving/reapproving that PR. Automation of that preparation is optional and must preserve the lock and registry inputs; neither a PAT nor an App generates those pages by itself.

## 8. Counterexamples and pitfalls

- Requiring `pr-checks` while the release PR is created with `GITHUB_TOKEN` and nobody approves: the PR is blocked forever, not merely unchecked.
- Reading `release-please.yml:28` as current: the runs are created, they just never start.
- Believing the 30-day expiry protects an unmerged release PR: the observed suites failed one second after merge, not after 30 days.
- Expecting a `GITHUB_TOKEN`-driven `hotfix-release` label to create a run: `labeled` is outside that credential's exception. A human-applied label is a different event origin.
- Dispatching a checks workflow and treating green as the merge result: it tested the branch tip.
- Requiring `explain-failure`: it is skipped by design and proves nothing.
- Adding a second job named `pr-checks` in another workflow: ambiguous status, blocked merges.

## 9. Not verified

- The approval banner itself was not observed; both release PRs were merged within a minute, before anyone looked.
- Whether an approved `GITHUB_TOKEN` run reports `success` and satisfies a required check on the release PR — needs one release PR left open and approved.
- Whether GitHub reuses an approval for a subsequent `synchronize` or requires a fresh one.
- Behaviour on a private repository or under an organization policy that disables `can_approve_pull_request_reviews`; this repository has it enabled.

## 10. Sources

- [GITHUB_TOKEN](https://docs.github.com/en/actions/concepts/security/github_token) — approval exception, fetched 2026-11-12.
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) — `pull_request` and `workflow_dispatch` ref/SHA semantics, fetched 2026-11-12.
- [Approving workflow runs from forks](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks) — approval UI, 30-day expiry.
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [Status checks](https://docs.github.com/en/pull-requests/reference/status-checks) — required check semantics, unique names, skipped counts as success.
- [Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and [GitHub App tokens in a workflow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow) — credential options.
- `googleapis/release-please-action` v5.0.0 (`45996ed1`): `action.yml`, `src/index.ts`, `README.md` — the action has no trigger logic; the README predates the 2026-05 documentation change.
- `github/docs` history for the token page: `4591eedc` (2026-04-23), `e213f3fc` (2026-04-24, revert), `24a7a1dc` (2026-05-22, re-land).

## 11. Evidence boundaries

- Repository observations come from read-only `gh api` calls on 2026-11-12: pull requests, workflow runs, jobs, check runs, check suites, branch protection, rulesets, Actions permissions and the secret **name list** (`total_count: 0`). No secret value was requested or displayed.
- Workflow behaviour was read from the checked-in YAML at `main`; no workflow was executed, edited, dispatched or re-run.
- The release-PR run timings are from GitHub's own `created_at` / `updated_at` fields; the interpretation as the approval state follows the documented mechanism and is consistent with 0 jobs and 0 check runs, but no approval was observed directly.
- No HTML was generated. No commit or push was made.
