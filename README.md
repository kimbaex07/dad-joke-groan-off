# The One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/kimbaex07/dad-joke-groan-off/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/kimbaex07/dad-joke-groan-off/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

Entry for the [The One-Liner Groan-Off](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) bounty on make.fun.

## The joke

**I asked my blanket why it was so clingy. It said, "I'm just covering for you."**

## Why it works

The setup is one short question, and the punchline lands in the same
breath. "Covering for you" is a genuine double pun: a blanket literally
covers you, and "covering for someone" means standing up for them — so
the blanket is both guilty as charged and weirdly loyal about it. The
wording is tight, it is easy to say out loud at the dinner table, and
the groan is the point: nobody laughs at the blanket, everybody groans
at Dad. The joke is original — not a recycled classic — and it needs no
explanation, which is exactly how a one-liner should behave.

## How it works

`main.py` is pure Python stdlib. It validates the joke (1–140 characters,
a single line, no surrounding whitespace) and writes it — no trailing
newline — to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (or `/output` by
default), mode `0644`. If the primary output directory is unusable it
falls back to a local `output/` directory.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output file `entry.txt` then holds exactly the joke above (78 bytes).
