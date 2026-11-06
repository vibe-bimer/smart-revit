"""Fail when a locked package sits below the version that closed a published advisory.

The fork's audit job lives in GitHub Actions, and the GitHub remote is read-only here, so the advisory that
prompted a bump is only caught on the GitLab pipeline if something checks it there. This check is that
something: it reads `server/uv.lock` with the standard library, needs no network, and asserts one floor per
package that already had an advisory worth pinning.

A floor is a version, not a range: the lock has to be at or above it, whatever else changed around it.

Exit codes: 0 every floor holds, 1 a floor is violated, 2 the check could not read the lock.
"""

from __future__ import annotations

import sys
from pathlib import Path

import tomllib

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
LOCK_PATH = REPOSITORY_ROOT / "server" / "uv.lock"

# Each floor is the release that closed an advisory this repository actually received, with the advisory
# named so a future reader can tell a real bound from a number someone liked.
FLOORS: dict[str, tuple[str, str]] = {
    "pillow": ("13.0.0", "39 advisories, all closed in 13.0.0 (issue #41)"),
    "opentelemetry-api": ("1.45.1", "CVE-2026-114603, closed in 1.45.1 (issue #41)"),
}


def parse_version(text: str) -> tuple[int, ...]:
    """Turn `13.0.0` or `1.45.2rc1` into comparable numbers, ignoring any pre-release tail."""
    numbers: list[int] = []
    for part in text.split("."):
        digits = ""
        for character in part:
            if not character.isdigit():
                break
            digits += character
        if not digits:
            break
        numbers.append(int(digits))
    return tuple(numbers)


def locked_versions(lock_path: Path = LOCK_PATH) -> dict[str, str]:
    """Read every package name and version out of a uv lock file."""
    document = tomllib.loads(lock_path.read_text(encoding="utf-8"))
    versions: dict[str, str] = {}
    for package in document.get("package", []):
        name = package.get("name")
        version = package.get("version")
        if isinstance(name, str) and isinstance(version, str):
            versions[name] = version
    return versions


def check(
    versions: dict[str, str], floors: dict[str, tuple[str, str]] = FLOORS
) -> tuple[list[str], list[str], list[str]]:
    """Split the floors into holding, violated and unreadable."""
    holding: list[str] = []
    violated: list[str] = []
    missing: list[str] = []
    for name, (floor, reason) in sorted(floors.items()):
        locked = versions.get(name)
        if locked is None:
            missing.append(
                f"{name} is locked at no version, and its floor is {floor} ({reason})"
            )
            continue
        if parse_version(locked) < parse_version(floor):
            violated.append(
                f"{name} is locked at {locked}, below its floor of {floor} ({reason})"
            )
            continue
        holding.append(f"{name} {locked} >= {floor}")
    return holding, violated, missing


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    lock_path = LOCK_PATH
    if arguments:
        if len(arguments) != 2 or arguments[0] != "--lock":
            print("usage: check_dependency_floors.py [--lock PATH]", file=sys.stderr)
            return 2
        lock_path = Path(arguments[1])
    try:
        versions = locked_versions(lock_path)
    except (OSError, tomllib.TOMLDecodeError) as error:
        print(f"FAIL cannot read {lock_path}: {error}", file=sys.stderr)
        return 2
    holding, violated, missing = check(versions)
    for line in holding:
        print(f"floor  {line}")
    for line in violated:
        print(f"FAIL {line}")
    for line in missing:
        print(f"FAIL {line}")
    if violated or missing:
        print(
            f"FAIL {len(violated) + len(missing)} of {len(FLOORS)} dependency floors do not hold",
            flush=True,
        )
        return 1
    print(f"OK {len(holding)} dependency floors hold in {lock_path.name}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
