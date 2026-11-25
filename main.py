#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line — a hopeless tech support agent speaking to a
desperate customer — to /output/entry.txt.

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 199
characters, not only whitespace.
"""

import os

LINE = (
    "Your presentation starts in ten minutes, so I've turned it off and "
    "on again four times — your computer just seems to be going "
    "through something. Give it space."
)


def validate(text):
    """Check the sealed gate: 1-199 chars, non-blank, valid UTF-8."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 199:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")  # raises on non-UTF-8-encodable text
    return True


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    if not validate(LINE):
        raise SystemExit(
            "gate failed: line must be 1-199 non-blank UTF-8 characters "
            f"(got {len(LINE)} chars)"
        )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
