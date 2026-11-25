#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to entry.txt.

The joke: a blanket, accused of being clingy, answers that it is only
"covering for you" — a double pun, since a blanket literally covers you
and "covering for someone" means standing up for them. The setup is one
short question, the punchline lands in the same line, and it needs no
explanation: everyone at the dinner table has heard a blanket blamed
for being clingy, and the groan arrives right on cue.
"""

import os
import sys

JOKE = "I asked my blanket why it was so clingy. It said, \"I'm just covering for you.\""


def main():
    joke = JOKE
    # Validate before writing anything: 1-140 characters, one line.
    if not joke or len(joke) > 140:
        sys.exit("joke must be 1-140 characters")
    if "\n" in joke or "\r" in joke:
        sys.exit("joke must be a single line")
    if joke != joke.strip():
        sys.exit("joke must not have surrounding whitespace")
    data = joke.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.umask(0o022)
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    except OSError:
        # Fallback only if the primary output dir is unusable.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
