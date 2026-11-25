#!/usr/bin/env python3
"""Invent a Word We Need entry: one coined word + one-line definition
(<=140 chars).

The word is "roomnesia": the act of walking into a room and instantly
forgetting why you went there. It names a gap English has no word
for — a moment everyone recognises at once — and is sayable,
spellable and memorable.
"""
import os

LINE = (
    "Roomnesia (n.) — the act of walking into a room and instantly "
    "forgetting why you came in."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
