#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, recorded by a cat, to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only. No network, no randomness:
two runs produce byte-identical output.
"""

import os

GREETING = (
    "You've reached Miso. I'm knocking things off the shelf \u2014 "
    "leave a message after the beep, or just open the tuna."
)

# The gate requires 1-120 characters; fail loudly instead of
# silently shipping an entry the scorer would reject.
assert 1 <= len(GREETING) <= 120, f"greeting is {len(GREETING)} chars"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(GREETING + "\n")


if __name__ == "__main__":
    main()
