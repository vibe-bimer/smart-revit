"""The dependency floors are checked, not assumed: the lock, the comparison and the failure paths."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parent.parent.parent / "tools"


@pytest.fixture(scope="module")
def floors():
    spec = importlib.util.spec_from_file_location(
        "dependency_floors", TOOLS / "check_dependency_floors.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_lock(path: Path, packages: dict[str, str]) -> Path:
    blocks = "".join(
        f'[[package]]\nname = "{name}"\nversion = "{version}"\n'
        for name, version in packages.items()
    )
    path.write_text(blocks, encoding="utf-8")
    return path


def test_the_repository_lock_holds_every_floor(floors):
    assert floors.main([]) == 0


def test_the_floor_list_is_not_empty_and_says_why(floors):
    assert floors.FLOORS
    for name, (floor, reason) in floors.FLOORS.items():
        assert floors.parse_version(floor), name
        assert reason.strip(), name


def test_a_version_below_its_floor_fails_and_names_the_package(floors, tmp_path, capsys):
    lock = write_lock(tmp_path / "uv.lock", {"pillow": "12.3.0", "opentelemetry-api": "1.45.2"})
    assert floors.main(["--lock", str(lock)]) == 1
    printed = capsys.readouterr().out
    assert "FAIL pillow is locked at 12.3.0, below its floor of 13.0.0" in printed
    assert "1 of 2 dependency floors do not hold" in printed


def test_a_package_that_is_not_locked_at_all_fails(floors, tmp_path, capsys):
    lock = write_lock(tmp_path / "uv.lock", {"pillow": "13.0.0"})
    assert floors.main(["--lock", str(lock)]) == 1
    printed = capsys.readouterr().out
    assert "opentelemetry-api is locked at no version" in printed


def test_an_unreadable_lock_is_an_error_not_a_pass(floors, tmp_path, capsys):
    broken = tmp_path / "uv.lock"
    broken.write_text("this is not toml = = =", encoding="utf-8")
    assert floors.main(["--lock", str(broken)]) == 2
    assert "cannot read" in capsys.readouterr().err
    assert floors.main(["--lock", str(tmp_path / "absent.lock")]) == 2


def test_versions_compare_as_numbers_not_strings(floors):
    assert floors.parse_version("1.45.10") > floors.parse_version("1.45.9")
    assert floors.parse_version("13.0.0") == (13, 0, 0)
    assert floors.parse_version("1.45.2rc1") == (1, 45, 2)
    assert floors.parse_version("2.0.0.dev3") == (2, 0, 0)


def test_an_unknown_argument_is_refused(floors, capsys):
    assert floors.main(["--nonsense"]) == 2
    assert "usage:" in capsys.readouterr().err
