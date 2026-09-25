#!/usr/bin/env python3
"""Roll dice in NdM notation. Usage: dice.py 2d6 [2d6 ...]"""
import random
import re
import sys

def roll(spec):
    m = re.fullmatch(r"(\d*)d(\d+)", spec.strip())
    if not m:
        return f"{spec}: invalid (use NdM, e.g. 2d6)"
    n, sides = int(m.group(1) or 1), int(m.group(2))
    rolls = [random.randint(1, sides) for _ in range(n)]
    return f"{spec}: {rolls} = {sum(rolls)}"

if __name__ == "__main__":
    specs = sys.argv[1:] or ["1d6"]
    for s in specs:
        print(roll(s))
