#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note entry.

Writes one patch-note line to the output file. The line keeps the
canonical changelog opening, names a specific and unexpected fix
(47 minutes, 2014), and trusts the reader to supply the embarrassing
thing instead of explaining the joke.

The program checks its own line before writing: UTF-8 text, a single
line, 1 to 160 characters, not only white space. It uses only the
standard library, touches no network, and writes identical bytes on
every run.
"""

import os
import sys

ENTRY = "Fixed an issue where closing your eyes opened a 47-minute replay of that embarrassing thing from 2014 instead of sleep."
MAX_CHARS = 160


def check(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters; limit is {MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    check(ENTRY)
    folder = os.path.dirname(out_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != ENTRY:
        raise SystemExit("written text does not match the entry")
    print(f"wrote {len(back)} characters to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
