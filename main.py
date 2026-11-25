#!/usr/bin/env python3
"""One Line, One Laugh — smart-fridge intervention one-liner.

Writes a single fixed joke line to entry.txt. Fully deterministic:
no randomness, no network, no clock, no input files.
"""

import os
from pathlib import Path

JOKE = (
    "My smart fridge staged an intervention last night. "
    "Apparently opening it at 2 a.m. isn't a personality."
)


def output_path() -> Path:
    """Resolve where entry.txt goes."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> None:
    line = JOKE
    # Self-check: a one-liner must stay within the bounty limits.
    assert 1 <= len(line) <= 200, f"line length {len(line)} out of range"
    assert line == line.strip(), "line must not have leading/trailing spaces"
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    # One line only, terminated by a single newline.
    dest.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {dest}")


if __name__ == "__main__":
    main()
