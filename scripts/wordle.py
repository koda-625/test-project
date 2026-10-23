#!/usr/bin/env python3
"""Mini Wordle - guess the 5-letter word in 6 tries.

Feedback: uppercase letter = right spot, lowercase = in word, dot = not in word.
Usage: python3 wordle.py
"""

import random

WORDS = [
    "apple", "brave", "crane", "dance", "eager", "flame", "grape", "honey",
    "ivory", "joker", "knock", "lemon", "mango", "noble", "ocean", "piano",
    "quilt", "river", "solar", "tiger", "urban", "vivid", "wheat", "xenon",
    "young", "zebra", "light", "music", "pizza", "rocket",
]

MAX_TRIES = 6


def score(guess, answer):
    # Returns feedback string and the number of exact hits.
    marks, hits = [], 0
    for g, a in zip(guess, answer):
        if g == a:
            marks.append(g.upper())
            hits += 1
        elif g in answer:
            marks.append(g.lower())
        else:
            marks.append(".")
    return "".join(marks), hits


def main():
    answer = random.choice(WORDS)
    print("WORDLE - guess the 5-letter word!")
    print("UPPER = right spot | lower = in word | . = not in word\n")
    for attempt in range(1, MAX_TRIES + 1):
        guess = input(f"Try {attempt}/{MAX_TRIES}: ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print("  Enter exactly 5 letters.")
            continue
        feedback, hits = score(guess, answer)
        print(f"  -> {feedback}")
        if hits == 5:
            print(f"\nYou got it in {attempt} tries!")
            return
    print(f"\nOut of tries. The word was: {answer.upper()}")


if __name__ == "__main__":
    main()
