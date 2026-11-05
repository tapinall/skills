# /// script
# requires-python = ">=3.11"
# ///
"""Copy shared knowledge from src/shared/ into each skill's references/ folder.

Usage: uv run scripts/sync_shared.py [--check]

Reads src/shared/sync.toml, where each shared file maps to a list of skill
folder names, or ["*"] for every src/tapinall*/ skill. Copies each file to
src/<skill>/references/<file>. With --check, writes nothing and exits 1 when
any copy is missing or differs, so CI can catch an edited copy.
"""

import argparse
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SHARED = SRC / "shared"


def skills() -> list[str]:
    return sorted(p.parent.name for p in SRC.glob("tapinall*/SKILL.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = parser.parse_args()

    try:
        mapping = tomllib.loads((SHARED / "sync.toml").read_text())["files"]
    except (OSError, KeyError, tomllib.TOMLDecodeError) as exc:
        print(f"cannot read src/shared/sync.toml: {exc}", file=sys.stderr)
        return 2

    known = skills()
    drift = []
    for name, targets in mapping.items():
        source = SHARED / name
        if not source.is_file():
            print(f"missing shared file: {source}", file=sys.stderr)
            return 2
        text = source.read_text()
        for skill in known if targets == ["*"] else targets:
            if skill not in known:
                print(f"sync.toml names unknown skill: {skill}", file=sys.stderr)
                return 2
            dest = SRC / skill / "references" / name
            if dest.is_file() and dest.read_text() == text:
                continue
            drift.append(str(dest.relative_to(ROOT)))
            if not args.check:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text)

    verb = "out of date" if args.check else "updated"
    for path in drift:
        print(f"{verb}: {path}")
    if not drift:
        print("all copies current")
    return 1 if args.check and drift else 0


if __name__ == "__main__":
    sys.exit(main())
