#!/usr/bin/env python3
"""Caesar cipher — encode or decode a message by shifting letters.

Usage:
    python3 caesar-cipher.py encode 3 "hello world"
    python3 caesar-cipher.py decode 3 "khoor zruog"
    python3 caesar-cipher.py brute "khoor zruog"   # try all 25 shifts
"""

import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_char(ch: str, shift: int) -> str:
    """Shift one letter, preserving case; leave other chars untouched."""
    if ch.islower():
        return ALPHABET[(ALPHABET.index(ch) + shift) % 26]
    if ch.isupper():
        return ALPHABET[(ALPHABET.index(ch.lower()) + shift) % 26].upper()
    return ch


def caesar(text: str, shift: int) -> str:
    """Apply a Caesar shift to the whole text."""
    return "".join(shift_char(ch, shift) for ch in text)


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    mode, text = sys.argv[1].lower(), sys.argv[-1]

    if mode == "brute":
        # Try every possible shift and print the candidates.
        for s in range(1, 26):
            print(f"{s:>2}: {caesar(text, -s)}")
    elif mode in ("encode", "decode"):
        shift = int(sys.argv[2]) % 26
        if mode == "decode":
            shift = -shift
        print(caesar(text, shift))
    else:
        print(f"Unknown mode: {mode!r} (use encode, decode or brute)")
        sys.exit(1)


if __name__ == "__main__":
    main()
