#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a person
from 1800, using only words they would know: a library, a post office,
roads, light, ink. The sentence is the entry; the program only carries it,
and it checks the gate itself before writing: one sentence, 1-200 chars.

Chosen sentence (157 chars), every word predating 1800, verified in
CANDIDATES-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.md:
  "It is a library with no walls and a post office with no horses,
   joined by roads of light, where a word you write is read across
   the sea before the ink dries."
"""

import os

SENTENCE = (
    "It is a library with no walls and a post office with no horses, "
    "joined by roads of light, where a word you write is read across "
    "the sea before the ink dries."
)

def main():
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, "sentence must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
