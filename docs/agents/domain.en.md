# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Layout: single-context

This is a single-context repository: one `GLOSSARY.md` at the repository root serves the whole repository, and the architecture decision records live in `adr/` at the root. There is no `GLOSSARY-MAP.md` and no per-subproject glossary. The glossary content gets written when the first term is actually settled; this setup does not ship an empty one.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root. Its terminology is authoritative.
- **`GLOSSARY-MAP.md`** at the repo root if it exists — it points at one `GLOSSARY.md` per context. Read each one relevant to the topic. (This repository has none today.)
- **`adr/`** — read ADRs that touch the area you're about to work in. This repository keeps decision records at `adr/` in the repository root, not at `docs/adr/`: every page under `docs/` is a published bilingual site page, while an ADR is an engineering record, written in English and kept out of the navigation. Read the `docs/adr/` paths in the diagrams below as `adr/`.
- **`docs/adr/`** — neither upstream nor this fork uses that location; treat anything found there as context-specific decisions. In multi-context repos, also check `src/<context>/docs/adr/` for context-scoped decisions.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo (this repository):

```
/
├── GLOSSARY.md
├── adr/
│   ├── 0001-base-on-upstream-with-a-bounded-fork-layer.md
│   └── 0003-ship-read-only-by-default-through-the-policy.md
└── src/
```

Multi-context repo (presence of `GLOSSARY-MAP.md` at the root):

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                  ← context-specific decisions
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
