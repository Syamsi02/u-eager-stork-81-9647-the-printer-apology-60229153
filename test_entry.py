"""Deterministic checks for The Printer Apology entry.

Run: python3 test_entry.py
Exits non-zero on any failure. No randomness, no network, no clock.
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "output" / "entry.txt"
EXPECTED = (
    "Sorry about the 'out of paper' error. There was paper \u2014 "
    "I just needed five minutes where nobody swore at me."
)


def run_once() -> str:
    result = subprocess.run(
        [sys.executable, "-P", "-s", "main.py"],
        cwd=HERE,
        capture_output=True,
        text=True,
        check=True,
    )
    return OUT.read_text(encoding="utf-8")


def main() -> int:
    first = run_once()
    second = run_once()
    assert first == second, "runs are not deterministic"
    assert first == EXPECTED + "\n", f"unexpected entry text: {first!r}"
    text = first.rstrip("\n")
    assert 1 <= len(text) <= 120, f"length {len(text)} outside 1-120"
    assert text.strip() == text and "\n" not in text
    text.encode("utf-8")
    print(f"OK: {len(text)} characters, {len(text.encode('utf-8'))} bytes, deterministic across 2 runs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
