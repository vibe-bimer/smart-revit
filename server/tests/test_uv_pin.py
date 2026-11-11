"""The uv pin lives in five places and must be one version everywhere."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def version_in(path: str, pattern: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    match = re.search(pattern, text, flags=re.MULTILINE)
    assert match, f"{path} states no uv version"
    return match.group(1)


def test_every_uv_pin_names_the_same_version() -> None:
    expected = version_in(".github/requirements/uv.in", r"^uv==(\d+\.\d+\.\d+)$")
    pins = {
        ".github/requirements/uv.txt": version_in(
            ".github/requirements/uv.txt", r"^uv==(\d+\.\d+\.\d+) \\$"
        ),
        ".github/workflows/ci.yml": version_in(
            ".github/workflows/ci.yml", r"^\s+version: '(\d+\.\d+\.\d+)'"
        ),
        ".github/workflows/pr-checks.yml": version_in(
            ".github/workflows/pr-checks.yml", r"^\s+version: '(\d+\.\d+\.\d+)'"
        ),
        ".gitlab-ci.yml": version_in(".gitlab-ci.yml", r"^  UV_VERSION: '(\d+\.\d+\.\d+)'"),
    }
    assert pins == {path: expected for path in pins}, pins
