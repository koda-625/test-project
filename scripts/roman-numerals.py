#!/usr/bin/env python3
"""Roman numeral converter: numbers <-> Roman numerals (1-3999).

Usage:
    python roman-numerals.py 42        # -> XLII
    python roman-numerals.py XLII      # -> 42
    python roman-numerals.py           # interactive mode
"""

import sys

# Ordered value -> symbol pairs, including subtractive forms.
ROMAN_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

ROMAN_VALUES = {symbol: value for value, symbol in ROMAN_TABLE}


def to_roman(number: int) -> str:
    """Convert an integer (1-3999) to a Roman numeral string."""
    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999")
    result = []
    for value, symbol in ROMAN_TABLE:
        while number >= value:
            result.append(symbol)
            number -= value
    return "".join(result)


def from_roman(text: str) -> int:
    """Convert a Roman numeral string back to an integer."""
    text = text.upper().strip()
    if not text or any(ch not in ROMAN_VALUES for ch in text):
        raise ValueError("Not a valid Roman numeral")
    total, prev = 0, 0
    # Scan right to left: a smaller value before a larger one subtracts.
    for ch in reversed(text):
        value = ROMAN_VALUES[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    # Round-trip check rejects malformed input like "IIII" or "VV".
    if to_roman(total) != text:
        raise ValueError("Not a valid Roman numeral")
    return total


def convert(arg: str) -> str:
    """Detect the input type and convert it, returning a display line."""
    if arg.isdigit():
        return f"{arg} -> {to_roman(int(arg))}"
    return f"{arg.upper()} -> {from_roman(arg)}"


def main() -> None:
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(convert(arg))
        return
    print("Roman numeral converter (1-3999). Type a number or numeral, or 'q' to quit.")
    while True:
        line = input("> ").strip()
        if line.lower() in ("q", "quit", "exit"):
            break
        if not line:
            continue
        try:
            print(convert(line))
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
