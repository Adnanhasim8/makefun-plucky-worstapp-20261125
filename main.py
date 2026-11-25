#!/usr/bin/env python3
"""NapTrack: the worst app idea ever pitched.

Writes one sentence (at most 240 characters) pitching a specific useless
app to /output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = (
    "NapTrack uses AI to detect the exact second you fall asleep, "
    "then wakes you up to confirm you were asleep, "
    "so for $4.99 a month you never miss a single nap again."
)


def main() -> None:
    # Gate: exactly one line, 1-240 characters, non-empty, no trailing junk.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Gate the file we actually wrote, not just the constant.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 240, "written entry must be 1-240 characters"


if __name__ == "__main__":
    main()
