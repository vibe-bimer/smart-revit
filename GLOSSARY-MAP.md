# Glossary map

This repository uses the multi-context layout: every context has its own vocabulary, and this page points at where each one is written down.

One shared glossary serves every context today. The table below says which part of the repository it covers, so a reader never has to guess whether a second file exists.

## Contexts

| Context | What it names | Glossary |
| --- | --- | --- |
| add-in and Core | the C# layer, Revit API access, jobs, contracts, policy and activity types | [GLOSSARY.md](GLOSSARY.md) |
| server | the Python process, MCP tools, transports and channels | [GLOSSARY.md](GLOSSARY.md) |
| fork layer | the actions this fork adds and the registry that claims them | [GLOSSARY.md](GLOSSARY.md) |
| repository process | commits, releases, gates and the issue tracker | [GLOSSARY.md](GLOSSARY.md) |

Decisions live in [`adr/`](adr/), not in `docs/adr/`. Every page under `docs/` is a published bilingual site page, so engineering records stay out of it.

## When a context earns its own glossary

A context gets its own `GLOSSARY.md` beside it when one of two things happens:

- it uses a word the shared glossary does not define, or
- it reads a shared word differently from the shared definition.

Add the new file to the table above in the same change. Until then, the shared glossary is the only source, and a missing per-context file is expected rather than a gap to report.
