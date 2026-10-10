#!/usr/bin/env python3
"""Hangman — guess the hidden word before the figure is complete.

Usage: python3 hangman.py
A random word is picked each round; type one letter per turn.
You win if you reveal the word within 6 wrong guesses.
"""
import random

# Small built-in word pool; add your own words to WORDS to keep it fresh.
WORDS = [
    "python", "galaxy", "penguin", "telescope", "library",
    "volcano", "umbrella", "quasar", "lighthouse", "croissant",
]

MAX_WRONG = 6


def pick_word() -> str:
    return random.choice(WORDS)


def show_progress(word: str, guessed: set) -> str:
    # Reveal guessed letters, hide the rest behind underscores.
    return " ".join(ch if ch in guessed else "_" for ch in word)


def main() -> None:
    word = pick_word()
    guessed: set = set()
    wrong = 0

    print("Welcome to Hangman! Guess the hidden word, one letter at a time.")
    print(f"You have {MAX_WRONG} wrong guesses. Good luck!\n")

    while wrong < MAX_WRONG and show_progress(word, guessed).replace(" ", "") != word:
        print("Word:   " + show_progress(word, guessed))
        print(f"Wrong:  {wrong}/{MAX_WRONG}")
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("Already guessed — try another one.\n")
            continue

        guessed.add(guess)
        if guess in word:
            print("Nice! That letter is in the word.\n")
        else:
            wrong += 1
            print(f"Nope — '{guess}' is not in the word.\n")

    if show_progress(word, guessed).replace(" ", "") == word:
        print(f"You win! The word was '{word}'. 🎉")
    else:
        print(f"Game over! The word was '{word}'. Better luck next time.")


if __name__ == "__main__":
    main()
