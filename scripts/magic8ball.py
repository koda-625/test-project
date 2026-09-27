#!/usr/bin/env python3
"""Magic 8-ball — ask a yes-or-no question, get a mystic answer.

Usage:
    ./magic8ball.py "Will it rain today?"
"""
import random
import sys

ANSWERS = [
    # Affirmative
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes, definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    # Non-committal
    "Reply hazy, try again.", "Ask again later.",
    "Better not tell you now.", "Cannot predict now.",
    "Concentrate and ask again.",
    # Negative
    "Don't count on it.", "My reply is no.", "My sources say no.",
    "Outlook not so good.", "Very doubtful.",
]

GREEN, YELLOW, RED, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[0m"

def main() -> None:
    if len(sys.argv) < 2:
        print("Ask me a yes-or-no question, e.g.:")
        print('  ./magic8ball.py "Should I take a nap?"')
        sys.exit(1)
    question = " ".join(sys.argv[1:])
    answer = random.choice(ANSWERS)
    color = GREEN if ANSWERS.index(answer) < 10 else YELLOW if ANSWERS.index(answer) < 15 else RED
    print(f"🎱 You asked: {question}")
    print(f"🎱 The 8-ball says: {color}{answer}{RESET}")

if __name__ == "__main__":
    main()
