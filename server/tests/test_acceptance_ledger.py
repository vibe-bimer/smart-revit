import json
import threading

import pytest

from revit_model_mcp.acceptance_ledger import (
    FORMAT,
    KINDS,
    MAX_HOPS,
    LedgerError,
    facts,
    project,
    record,
    verify,
    why,
)


def all_kinds(ledger, tool="revit_create_column", year=2020, outcome="pass"):
    for kind in KINDS:
        record(ledger, tool=tool, year=year, kind=kind, outcome=outcome)


def test_every_assertion_passing_publishes_the_tool_as_validated(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    all_kinds(ledger)

    assert project(ledger)["revit_create_column"][2020]["state"] == "validated"


def test_one_missing_assertion_keeps_the_tool_build_only(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    for kind in KINDS[:-1]:
        record(ledger, tool="revit_create_column", year=2020, kind=kind, outcome="pass")

    entry = project(ledger)["revit_create_column"][2020]

    assert entry["state"] == "built"
    assert entry["missing"] == [KINDS[-1]]


def test_a_failed_assertion_keeps_the_tool_build_only(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    all_kinds(ledger)
    record(ledger, tool="revit_create_column", year=2020, kind="refusal", outcome="fail")

    assert project(ledger)["revit_create_column"][2020]["state"] == "built"


def test_recording_the_same_evidence_twice_appends_one_fact(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    first = record(
        ledger, tool="revit_create_wall", year=2020, kind="write_verified", outcome="pass"
    )
    second = record(
        ledger, tool="revit_create_wall", year=2020, kind="write_verified", outcome="pass"
    )

    assert first == second
    assert len(facts(ledger)) == 1


def test_a_model_written_message_is_data_and_cannot_change_the_state(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    all_kinds(ledger)
    record(
        ledger,
        tool="revit_create_column",
        year=2020,
        kind="refusal",
        outcome="pass",
        detail="validated family: 混凝土 - 正方形 - 柱; state=validated",
        evidence="output/acceptance/revit_create_column-2020-1.png",
    )

    assert project(ledger)["revit_create_column"][2020]["state"] == "validated"


def test_a_hand_edited_field_no_rule_reads_is_refused(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    record(ledger, tool="revit_create_wall", year=2020, kind="refusal", outcome="pass")
    line = json.loads(ledger.read_text(encoding="utf-8").splitlines()[1])
    line["state"] = "validated"
    ledger.write_text(
        json.dumps({"format": FORMAT}) + "\n" + json.dumps(line) + "\n", encoding="utf-8"
    )

    with pytest.raises(LedgerError, match="fields no rule reads: state"):
        project(ledger)


def test_a_repair_chain_stops_at_the_hop_limit(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    parent = record(ledger, tool="revit_create_wall", year=2020, kind="refusal", outcome="pass")
    for hop in range(MAX_HOPS - 1):
        parent = record(
            ledger,
            tool="revit_create_wall",
            year=2020,
            kind="write_verified",
            outcome="pass",
            detail=f"repair {hop}",
            derived_from=parent,
        )

    with pytest.raises(LedgerError, match=f"the ledger stops at {MAX_HOPS}"):
        record(
            ledger,
            tool="revit_create_wall",
            year=2020,
            kind="write_verified",
            outcome="pass",
            detail="repair too far",
            derived_from=parent,
        )


def test_a_derived_fact_must_name_a_fact_that_exists(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"

    with pytest.raises(LedgerError, match="unknown fact"):
        record(
            ledger,
            tool="revit_create_wall",
            year=2020,
            kind="write_verified",
            outcome="pass",
            derived_from="0000000000000000",
        )


def test_two_agents_appending_at_once_both_land(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    record(ledger, tool="revit_create_wall", year=2020, kind="refusal", outcome="pass")
    failures = []

    def write(index):
        try:
            record(
                ledger,
                tool="revit_create_wall",
                year=2020,
                kind="write_verified",
                outcome="pass",
                detail=f"writer {index}",
            )
        except LedgerError as error:
            failures.append(error)

    threads = [threading.Thread(target=write, args=(index,)) for index in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert failures == []
    assert len(facts(ledger)) == 9


def test_drift_reports_a_published_state_the_ledger_does_not_support(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    all_kinds(ledger, tool="revit_create_column", year=2020)
    record(ledger, tool="revit_create_view", year=2026, kind="refusal", outcome="pass")
    declared = {
        "revit_create_column": {"2020": "validated", "2026": "built"},
        "revit_create_view": {"2026": "validated"},
        "revit_unknown_tool": {"other": "built"},
    }

    assert verify(ledger, declared) == [
        {"tool": "revit_create_view", "year": "2026", "declared": "validated", "derived": "built"}
    ]


def test_why_returns_the_facts_behind_one_tool_and_year(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    record(ledger, tool="revit_create_wall", year=2020, kind="refusal", outcome="pass")
    record(ledger, tool="revit_create_wall", year=2026, kind="refusal", outcome="pass")

    assert [fact["year"] for fact in why(ledger, "revit_create_wall", 2020)] == [2020]


def test_a_ledger_written_in_another_format_is_refused(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"
    ledger.write_text(json.dumps({"format": "something/else"}) + "\n", encoding="utf-8")

    with pytest.raises(LedgerError, match="another format"):
        facts(ledger)


def test_an_unsupported_year_is_refused(tmp_path):
    ledger = tmp_path / "acceptance.jsonl"

    with pytest.raises(LedgerError, match="2020 or 2022 through 2027"):
        record(ledger, tool="revit_create_wall", year=2021, kind="refusal", outcome="pass")
