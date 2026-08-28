#!/usr/bin/env python3
"""Keep Claude and ChatGPT/Codex plugin packaging aligned with canonical skills."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CODEX_SKILLS_DIR = ROOT / "plugins" / "point-marketing" / "skills"
MANIFESTS = (
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / "plugins" / "point-marketing" / ".codex-plugin" / "plugin.json",
)
VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
VERSION_FIELD_RE = re.compile(r'("version"\s*:\s*")([^"]+)(")', re.MULTILINE)


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def parse_version(raw: str) -> tuple[int, int, int]:
    match = VERSION_RE.fullmatch(raw)
    if not match:
        raise ValueError(f"expected semantic version X.Y.Z, got {raw!r}")
    return tuple(int(part) for part in match.groups())


def format_version(version: tuple[int, int, int]) -> str:
    return ".".join(str(part) for part in version)


def manifest_version(path: Path, revision: str | None = None) -> tuple[int, int, int]:
    if revision:
        relative = path.relative_to(ROOT).as_posix()
        raw = run_git("show", f"{revision}:{relative}")
        data = json.loads(raw)
    else:
        data = json.loads(path.read_text())
    return parse_version(data["version"])


def write_manifest_version(path: Path, version: tuple[int, int, int]) -> bool:
    raw = path.read_text()
    replacement = format_version(version)
    updated, count = VERSION_FIELD_RE.subn(rf"\g<1>{replacement}\g<3>", raw, count=1)
    if count != 1:
        raise ValueError(f"could not find exactly one version field in {path.relative_to(ROOT)}")
    if updated == raw:
        return False
    path.write_text(updated)
    return True


def canonical_skills() -> list[str]:
    return sorted(
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def expected_link_target(name: str) -> str:
    return os.path.relpath(SKILLS_DIR / name, CODEX_SKILLS_DIR)


def link_issues() -> list[str]:
    expected = set(canonical_skills())
    issues: list[str] = []

    for name in sorted(expected):
        link = CODEX_SKILLS_DIR / name
        target = expected_link_target(name)
        if not link.is_symlink():
            issues.append(f"missing symlink: {link.relative_to(ROOT)} -> {target}")
        elif os.readlink(link) != target:
            issues.append(
                f"wrong symlink: {link.relative_to(ROOT)} -> {os.readlink(link)}; expected {target}"
            )

    for entry in sorted(CODEX_SKILLS_DIR.iterdir()):
        if entry.name not in expected:
            kind = "stale symlink" if entry.is_symlink() else "unexpected entry"
            issues.append(f"{kind}: {entry.relative_to(ROOT)}")

    return issues


def sync_links() -> list[str]:
    expected = set(canonical_skills())
    changes: list[str] = []
    CODEX_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in sorted(CODEX_SKILLS_DIR.iterdir()):
        if entry.name in expected:
            continue
        if not entry.is_symlink():
            raise RuntimeError(f"refusing to remove non-symlink {entry.relative_to(ROOT)}")
        entry.unlink()
        changes.append(f"removed stale link {entry.relative_to(ROOT)}")

    for name in sorted(expected):
        link = CODEX_SKILLS_DIR / name
        target = expected_link_target(name)
        if link.is_symlink() and os.readlink(link) == target:
            continue
        if link.exists() and not link.is_symlink():
            raise RuntimeError(f"refusing to replace non-symlink {link.relative_to(ROOT)}")
        if link.is_symlink():
            link.unlink()
        link.symlink_to(target)
        changes.append(f"linked {link.relative_to(ROOT)} -> {target}")

    return changes


def changed_plugin_content(base: str | None) -> bool:
    paths = ["skills", "plugins/point-marketing/skills"]
    if base:
        output = run_git("diff", "--name-only", f"{base}...HEAD", "--", *paths)
    else:
        output = run_git("diff", "--name-only", "HEAD", "--", *paths)
    return bool(output)


def baseline_versions(base: str | None) -> list[tuple[int, int, int]]:
    revision = base or "HEAD"
    return [manifest_version(path, revision) for path in MANIFESTS]


def validate(base: str | None) -> list[str]:
    issues = link_issues()
    current = [manifest_version(path) for path in MANIFESTS]
    if len(set(current)) != 1:
        rendered = ", ".join(format_version(version) for version in current)
        issues.append(f"native plugin manifest versions differ: {rendered}")

    if changed_plugin_content(base):
        baseline = max(baseline_versions(base))
        if min(current) <= baseline:
            issues.append(
                "plugin content changed without a version bump "
                f"above {format_version(baseline)}"
            )
    return issues


def synchronize(target_version: str | None) -> list[str]:
    had_link_drift = bool(link_issues())
    content_changed = had_link_drift or changed_plugin_content(None)
    current = [manifest_version(path) for path in MANIFESTS]
    baseline = max(baseline_versions(None))

    if target_version:
        target = parse_version(target_version)
        if target < max(current):
            raise ValueError("--version cannot move a native plugin manifest backwards")
    else:
        target = max(current)
        if content_changed and target <= baseline:
            target = (baseline[0], baseline[1], baseline[2] + 1)

    changes = sync_links()
    for path in MANIFESTS:
        if write_manifest_version(path, target):
            changes.append(
                f"set {path.relative_to(ROOT)} version to {format_version(target)}"
            )
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    parser.add_argument(
        "--base",
        help="Git revision used to verify that changed plugin content includes a version bump",
    )
    parser.add_argument(
        "--version",
        help="set an explicit aligned version instead of the automatic patch bump",
    )
    args = parser.parse_args()

    if args.check and args.version:
        parser.error("--check and --version cannot be used together")

    try:
        if args.check:
            issues = validate(args.base)
            if issues:
                for issue in issues:
                    print(f"ERROR: {issue}", file=sys.stderr)
                return 1
            print("Plugin packaging is synchronized.")
            return 0

        changes = synchronize(args.version)
        issues = validate(None)
        if issues:
            for issue in issues:
                print(f"ERROR: {issue}", file=sys.stderr)
            return 1
        if changes:
            print("\n".join(changes))
        else:
            print("Plugin packaging was already synchronized.")
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
