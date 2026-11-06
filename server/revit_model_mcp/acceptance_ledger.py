"""Append-only acceptance facts, projected into the states the site publishes.

Every change to a Revit model is verified twice: once through the MCP channel, once on the screen.
This module keeps those verifications as facts and derives a tool's state from them, so the
published state cannot drift away from its evidence. There is no stored projection: `project()`
recomputes from the log every time, which is why a change to these rules needs no migration.

Free text is data. A record carries only the fields `FIELDS` names, and `project()` reads only
`tool`, `year`, `kind` and `outcome`. Anything a Revit model or an agent wrote - a family name, a
refusal message, a file path - belongs in `detail` or `evidence`, where no rule reads it.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Mapping

FORMAT = "revit-model-mcp.acceptance/v1"
MAX_HOPS = 8
LOCK_TIMEOUT_SECONDS = 5.0

TOOL_NAME = re.compile(r"revit_[a-z0-9_]+\Z")
KINDS = ("dry_run_rollback", "write_verified", "refusal", "file_unchanged", "ui_evidence")
OUTCOMES = ("pass", "fail", "skip")
FIELDS = frozenset({"tool", "year", "kind", "outcome", "detail", "evidence", "derived_from"})


class LedgerError(ValueError):
    """A fact or a ledger that this module refuses to accept."""


def _tool(tool: Any) -> str:
    if not isinstance(tool, str) or not TOOL_NAME.match(tool):
        raise LedgerError("tool must be a revit_ tool name.")
    return tool


def _year(year: Any) -> int:
    if type(year) is not int or not 2020 <= year <= 2027 or year == 2021:
        raise LedgerError("year must be a supported Revit year: 2020 or 2022 through 2027.")
    return year


def _kind(kind: Any) -> str:
    if kind not in KINDS:
        raise LedgerError(f"kind must be one of {', '.join(KINDS)}.")
    return str(kind)


def _outcome(outcome: Any) -> str:
    if outcome not in OUTCOMES:
        raise LedgerError(f"outcome must be one of {', '.join(OUTCOMES)}.")
    return str(outcome)


def _text(value: Any, name: str) -> str:
    if value is None:
        return ""
    if not isinstance(value, str):
        raise LedgerError(f"{name} must be text.")
    return value


def _fact_id(tool: str, year: int, kind: str, outcome: str, evidence: str, detail: str) -> str:
    """Identify a fact by what it asserts, so re-recording it changes nothing.

    The outcome is part of the identity: a later failing assertion is a new fact, not a repeat.
    """
    material = "\x1f".join((tool, str(year), kind, outcome, evidence, detail))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:16]


@contextmanager
def _exclusive(path: Path) -> Iterator[None]:
    """Hold the ledger for one writer, so two agents appending at once cannot interleave."""
    lock = path.with_name(path.name + ".lock")
    deadline = time.monotonic() + LOCK_TIMEOUT_SECONDS
    while True:
        try:
            handle = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise LedgerError(f"ledger is busy: {lock}") from None
            time.sleep(0.01)
            continue
        break
    try:
        os.close(handle)
        yield
    finally:
        lock.unlink(missing_ok=True)


def _read(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise LedgerError(f"{path.name}:{number} is not a JSON fact: {error.msg}.") from None
        if number == 1 and record.get("format") != FORMAT:
            raise LedgerError(
                f"{path.name} was written in another format; start a new ledger for {FORMAT}."
            )
        if number > 1:
            unknown = set(record) - FIELDS - {"id", "recorded_at"}
            if unknown:
                raise LedgerError(
                    f"{path.name}:{number} carries fields no rule reads: "
                    f"{', '.join(sorted(unknown))}. Put free text in detail."
                )
            records.append(record)
    return records


def facts(path: Path) -> list[dict[str, Any]]:
    """Every fact in the ledger, in the order it was recorded."""
    return _read(Path(path))


def _depth(records: list[dict[str, Any]], fact_id: str) -> int:
    """Count how many facts a fact was derived from, so a repair chain cannot run away."""
    by_id = {record["id"]: record for record in records}
    if fact_id not in by_id:
        raise LedgerError(f"derived_from names an unknown fact: {fact_id}.")
    depth = 1
    seen = {fact_id}
    parent = by_id[fact_id].get("derived_from")
    while parent:
        if parent in seen:
            raise LedgerError(f"derived_from forms a cycle at {parent}.")
        if parent not in by_id:
            raise LedgerError(f"derived_from names an unknown fact: {parent}.")
        seen.add(parent)
        depth += 1
        parent = by_id[parent].get("derived_from")
    return depth


def record(
    path: Path,
    *,
    tool: str,
    year: int,
    kind: str,
    outcome: str,
    detail: str = "",
    evidence: str = "",
    derived_from: str | None = None,
) -> str:
    """Append one acceptance fact and return its id. Recording the same fact again is a no-op."""
    path = Path(path)
    tool = _tool(tool)
    year = _year(year)
    kind = _kind(kind)
    outcome = _outcome(outcome)
    detail = _text(detail, "detail")
    evidence = _text(evidence, "evidence")
    if derived_from is not None:
        _text(derived_from, "derived_from")
    fact_id = _fact_id(tool, year, kind, outcome, evidence, detail)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _exclusive(path):
        records = _read(path)
        if any(record["id"] == fact_id for record in records):
            return fact_id
        if derived_from is not None:
            depth = _depth(records, derived_from) + 1
            if depth > MAX_HOPS:
                raise LedgerError(
                    f"this fact would sit {depth} facts deep; the ledger stops at {MAX_HOPS}."
                )
        fact = {
            "id": fact_id,
            "tool": tool,
            "year": year,
            "kind": kind,
            "outcome": outcome,
            "detail": detail,
            "evidence": evidence,
            "derived_from": derived_from,
            "recorded_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        unknown = set(fact) - FIELDS - {"id", "recorded_at"}
        if unknown:
            raise LedgerError(f"unexpected fact fields: {', '.join(sorted(unknown))}.")
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            if handle.tell() == 0:
                handle.write(json.dumps({"format": FORMAT}, sort_keys=True) + "\n")
            handle.write(json.dumps(fact, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
    return fact_id


def project(path: Path) -> dict[str, dict[int, dict[str, Any]]]:
    """Derive the published state of every tool and year from the facts alone."""
    result: dict[str, dict[int, dict[str, Any]]] = {}
    for record in facts(path):
        tool = result.setdefault(record["tool"], {})
        entry = tool.setdefault(record["year"], {"state": "built", "outcomes": {}, "evidence": []})
        entry["outcomes"][record["kind"]] = record["outcome"]
        if record["evidence"]:
            entry["evidence"].append(record["evidence"])
    for years in result.values():
        for entry in years.values():
            passed = all(entry["outcomes"].get(kind) == "pass" for kind in KINDS)
            entry["state"] = "validated" if passed else "built"
            entry["missing"] = [kind for kind in KINDS if kind not in entry["outcomes"]]
    return result


def verify(path: Path, declared: Mapping[str, Mapping[str, str]]) -> list[dict[str, str]]:
    """Compare a published state table against the ledger and report every disagreement."""
    derived = project(path)
    drift: list[dict[str, str]] = []
    for tool, years in sorted(declared.items()):
        for year, state in sorted(years.items()):
            if not str(year).isdigit():
                continue
            actual = derived.get(tool, {}).get(int(year), {}).get("state", "built")
            if state != actual:
                drift.append(
                    {"tool": tool, "year": str(year), "declared": state, "derived": actual}
                )
    return drift


def why(path: Path, tool: str, year: int) -> list[dict[str, Any]]:
    """Every fact behind one tool and year, in the order it was recorded."""
    return [record for record in facts(path) if record["tool"] == tool and record["year"] == year]


def main(argv: list[str] | None = None) -> int:
    """Print the derived states, or the drift against a declared state table in JSON."""
    import argparse

    parser = argparse.ArgumentParser(prog="acceptance_ledger", description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--declared", type=Path, help="tool to year to state, as JSON")
    parser.add_argument("--why", nargs=2, metavar=("TOOL", "YEAR"))
    arguments = parser.parse_args(argv)
    if arguments.why:
        for fact in why(arguments.ledger, arguments.why[0], int(arguments.why[1])):
            print(json.dumps(fact, sort_keys=True))
        return 0
    if arguments.declared:
        declared = json.loads(arguments.declared.read_text(encoding="utf-8"))
        drift = verify(arguments.ledger, declared)
        for row in drift:
            print(
                f"drift  {row['tool']} {row['year']}: published {row['declared']}, "
                f"ledger says {row['derived']}"
            )
        print(f"{len(drift)} disagreements between the site and the ledger")
        return 1 if drift else 0
    print(json.dumps(project(arguments.ledger), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
