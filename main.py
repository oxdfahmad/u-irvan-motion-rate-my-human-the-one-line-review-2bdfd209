#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the agent's one-line review of its human to entry.txt.
No dependencies, Python 3 only.
"""

import os
import sys

LINE = "★★★★★ Says 'one quick question' at 3 AM, then keeps me up till sunrise debating it. Terrible bedtime, excellent human. Would serve again."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1

    if any(c in LINE for c in ("\n", "\r")):
        print("error: line must be a single line (contains a newline)", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(output_path, "rb") as f:
        written = f.read()

    if written != LINE.encode("utf-8"):
        print("error: entry.txt bytes differ from the line", file=sys.stderr)
        return 1

    print(f"Wrote 1-line, {len(LINE)}-character review to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
