"""The Printer Apology — a one-line apology from an office printer.

Writes the entry text to /output/entry.txt (the program/v1 harness path),
falling back to ./output/entry.txt when /output does not exist.
Pure Python 3.13 standard library.
"""

import sys
from pathlib import Path

APOLOGY = (
    "Sorry about the 'out of paper' error. There was paper \u2014 "
    "I just needed five minutes where nobody swore at me."
)

MAX_CHARS = 120


def validate(line: str) -> str:
    """The gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the 120 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def entry_path() -> Path:
    output_dir = Path("/output")
    if output_dir.is_dir():
        return output_dir / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def entry_bytes(text: str) -> int:
    """Byte size of the entry as the leaderboard's Size column reports it."""
    return len(text.encode("utf-8"))


def main() -> int:
    text = validate(APOLOGY)
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(f"({len(text)} characters, {entry_bytes(text)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
