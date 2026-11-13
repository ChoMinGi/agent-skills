#!/usr/bin/env python3
"""Check copied package files, install entry points, and local Markdown links."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "packages"
MANIFEST = ROOT / "package-hashes.json"
ENTRY_POINTS = [
    "packages/cognitive-partner/cognitive-partner/SKILL.md",
    "packages/decisionguard/skills/decisionguard/SKILL.md",
    "packages/web-feature-demo/SKILL.md",
]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def main() -> int:
    problems: list[str] = []
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    actual = {
        str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in PACKAGES.rglob("*") if p.is_file()
    }
    if actual != expected:
        problems.append("package file list or hashes differ from the source snapshot")
    for rel in ENTRY_POINTS:
        if not (ROOT / rel).is_file():
            problems.append(f"missing install entry point: {rel}")
    for path in [ROOT / "README.md", ROOT / "LICENSES.md", ROOT / "PROVENANCE.md"]:
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            destination = (path.parent / target.split("#", 1)[0]).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                problems.append(f"broken root link: {path.name} -> {target}")
    if problems:
        for problem in problems:
            print("FAIL:", problem)
        return 1
    print(f"PASS: {len(actual)} package files, three install entry points, root links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
