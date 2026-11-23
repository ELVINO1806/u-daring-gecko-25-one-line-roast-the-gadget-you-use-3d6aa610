#!/usr/bin/env python3
"""One-Line Roast entry writer.

Writes the competition entry text to /output/entry.txt exactly as-is.
Standard library only, no network access.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "My fitness watch cheers when I stand up, "
    "the one athletic feat my chair permits."
)

OUTPUT_PATH = Path("/output") / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
