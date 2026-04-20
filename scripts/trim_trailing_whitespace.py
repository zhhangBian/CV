#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


TRAILING_WHITESPACE = re.compile(rb"[ \t]+(?=(?:\r\n|\r|\n|$))")


def trim_file(path_str: str) -> bool:
    path = Path(path_str)
    original = path.read_bytes()
    updated = TRAILING_WHITESPACE.sub(b"", original)
    if updated == original:
        return False
    path.write_bytes(updated)
    print(f"trimmed trailing whitespace: {path}")
    return True


def main(argv: list[str]) -> int:
    modified = False
    had_error = False

    for path_str in argv:
        try:
            modified = trim_file(path_str) or modified
        except OSError as exc:
            print(f"failed to process {path_str}: {exc}", file=sys.stderr)
            had_error = True

    if had_error or modified:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
