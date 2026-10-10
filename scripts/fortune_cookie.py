#!/usr/bin/env python3
"""fortune_cookie.py — crack open a digital fortune cookie.

Usage: ./fortune_cookie.py [N]   (print N fortunes, default 1)
"""

import random
import sys

FORTUNES = [
    "A fresh start will put you on your way.",
    "Discontent is the first step in the progress of a machine — or a person.",
    "A short stranger will soon enter your life with answers.",
    "The fortune you seek is in another cookie.",
    "Never test the depth of water with both feet.",
    "Keep it simple: small wins compound into big outcomes.",
    "A smile is your passport into the hearts of others.",
    "You will debug it on the first try. (This one may be lying.)",
    "Fortune favors the well-rested.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Someone will share their lunch with you this week.",
    "Your hard work will soon pay off in a surprising way.",
    "Adventure awaits — take the long way home today.",
    "You will write code that works on the first run.",
    "Patience is a virtue; pizza is a reward.",
    "A new opportunity will knock twice. Answer the first knock.",
]

# Lucky numbers: two single digits pulled from the ether
def lucky_numbers():
    return random.sample(range(10), 2)

def main():
    try:
        count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    except ValueError:
        print("Usage: ./fortune_cookie.py [N]")
        return 1
    if count < 1:
        count = 1
    for i in range(count):
        fortune = random.choice(FORTUNES)
        a, b = lucky_numbers()
        print(f"\n🥠 Fortune #{i + 1}:")
        print(f"   {fortune}")
        print(f"   Lucky numbers: {a}, {b}")
    print()
    return 0

if __name__ == "__main__":
    sys.exit(main())
