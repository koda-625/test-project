#!/usr/bin/env python3
"""Guess the Number - a tiny terminal guessing game.

The computer picks a random number and you try to guess it.
Difficulty tiers keep it replayable. Run: ./number-guess.py
"""

import random

TIERS = {
    "1": ("Easy", 1, 10, 4),
    "2": ("Medium", 1, 50, 6),
    "3": ("Hard", 1, 100, 7),
}

def play():
    print("== Guess the Number ==")
    for key, (name, lo, hi, tries) in TIERS.items():
        print(f"  {key}. {name}: {lo}-{hi}, {tries} tries")
    tier = input("Pick difficulty [1-3] (default 2): ").strip() or "2"
    name, lo, hi, tries = TIERS.get(tier, TIERS["2"])
    secret = random.randint(lo, hi)
    print(f"\n{name} mode: I picked a number between {lo} and {hi}.")
    for attempt in range(1, tries + 1):
        raw = input(f"Try {attempt}/{tries} > ").strip()
        if not raw.isdigit():
            print("Numbers only, please.")
            continue
        guess = int(raw)
        if guess == secret:
            print(f"You got it in {attempt} {'try' if attempt == 1 else 'tries'}! Nice.")
            return
        hint = "too low" if guess < secret else "too high"
        print(f"  {hint}!")
    print(f"Out of tries - the number was {secret}. Better luck next time!")

if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? [y/N]: ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
