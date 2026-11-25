"""Write one original one-liner to entry.txt for make.fun's "One Line, One Laugh".

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files.

The line: a midnight fridge raid reframed as an intervention — the
punchline ("isn't a personality") lands in the final clause, needs no
setup beyond the first sentence, and reads cleanly in one pass.
"""

import os

LINE = "My smart fridge staged an intervention last night. Apparently opening it at 2 a.m. isn't a personality."
# 103 characters: inside the 1-200 gate, two sentences, punchline in the last clause.


def main():
    # Gate self-check: 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
