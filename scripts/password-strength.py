#!/usr/bin/env python3
"""Password strength checker.

Prompts for a password (input hidden), rates its strength from 0-5 based on
length and character variety, and prints friendly improvement tips.
Usage: python3 password-strength.py
"""

import getpass
import re
import string


def score_password(pw):
    """Return (score, tips) for the given password."""
    score = 0
    tips = []

    # Length checks: longer is stronger.
    if len(pw) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")
    if len(pw) >= 12:
        score += 1

    # Character variety checks.
    checks = [
        (r"[a-z]", "a lowercase letter"),
        (r"[A-Z]", "an uppercase letter"),
        (r"[0-9]", "a digit"),
        (r"[^A-Za-z0-9]", "a symbol (e.g. ! ? #)"),
    ]
    for pattern, label in checks:
        if re.search(pattern, pw):
            score += 1
        else:
            tips.append(f"Add {label}.")

    # Penalize passwords made of a single repeated character.
    if len(set(pw)) == 1 and pw:
        score = 0
        tips.append("Avoid repeating the same character.")

    return min(score, 5), tips


def main():
    pw = getpass.getpass("Enter a password to check (hidden): ")
    if not pw:
        print("No password entered. Nothing to check.")
        return

    score, tips = score_password(pw)
    labels = ["Very weak", "Weak", "Fair", "Good", "Strong", "Excellent"]
    bar = "#" * score + "-" * (5 - score)
    print(f"Strength: [{bar}] {score}/5 - {labels[score]}")

    if tips:
        print("Tips to improve:")
        for tip in tips:
            print(f"  - {tip}")
    else:
        print("Nice work - nothing to improve!")


if __name__ == "__main__":
    main()
