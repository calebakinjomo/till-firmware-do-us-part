#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun bounty entry (program/v1).

Writes a single robot wedding vow — one sentence, under 200 characters —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The vow, chosen to hit every judging criterion at once:
  1. It IS a robot's own wedding vow ("I vow ...").
  2. The laugh comes from the situation itself: a machine frames the
     person it loves as a bug — and refuses to patch it.
  3. Tenderness under the joke: loving someone through every crash and
     low battery, flaws included, is the vow.
  4. Machine voice throughout: update, crash, low battery, bug, patch.
  5. One clean sentence, nothing spare, no setup that could be cut.
It deliberately avoids the bounty-title phrase "till firmware do us part",
which a thousand other entries will lean on.
"""

import os

VOW = (
    "I vow to love you through every update, every crash, and every "
    "low battery, because you are the one bug I will never patch."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
