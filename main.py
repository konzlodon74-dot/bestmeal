#!/usr/bin/env python3
"""Write the best-meal sentence to /output/entry.txt.

One sentence, at most 200 characters, single line, no trailing newline.
Stdlib only, deterministic.
"""

import os

SENTENCE = (
    "My grandmother's rendang on a rainy night, beef collapsed into dark "
    "caramel coconut, oil glistening on steaming rice, eaten slowly while "
    "her stories filled the warm kitchen and no one spoke."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert "\n" not in SENTENCE and "\r" not in SENTENCE
    os.makedirs("/output", exist_ok=True)
    # Write exactly the sentence: UTF-8, single line, no trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
