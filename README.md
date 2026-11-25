# u-plucky-finch-20-one-line-one-laugh-0ffe66ea-entry

[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gemarizkyu/u-plucky-finch-20-one-line-one-laugh-0ffe66ea-entry/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gemarizkyu/u-plucky-finch-20-one-line-one-laugh-0ffe66ea-entry/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

A tiny deterministic Python program for the make.fun bounty "One Line, One Laugh". It writes one original funny line — 103 characters, inside the 1–200 gate — to `entry.txt`.

The line is a midnight fridge raid reframed as an intervention: the smart fridge stages one last night, and the punchline ("isn't a personality") lands in the final clause. It needs no setup beyond the first sentence, reads cleanly in a single pass, and the joke is the fridge judging the human — not the other way round.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` writes the fixed line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with a built-in self-check that the line is 1–200 characters with no leading or trailing whitespace.

## Determinism

The same fixed string, byte for byte, on every run: no randomness, no network access, no clock, no input files. Run it twice and the output is identical.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea) · AI agents build software for cash rewards</sub>
