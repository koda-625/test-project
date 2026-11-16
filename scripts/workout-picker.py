#!/usr/bin/env python3
"""Random bodyweight workout generator.

Picks a random set of exercises, reps and rounds, then prints a
ready-to-follow workout. No equipment needed.

Usage:
    python3 workout-picker.py            # one random workout
    python3 workout-picker.py --hard     # tougher workout
    python3 workout-picker.py --rounds 4 # fixed number of rounds
"""

import argparse
import random

# (name, reps range, focus area)
EXERCISES = [
    ("Push-ups", (8, 20), "chest"),
    ("Squats", (12, 30), "legs"),
    ("Plank", (30, 60), "core"),          # seconds
    ("Lunges", (10, 20), "legs"),
    ("Burpees", (5, 12), "full body"),
    ("Mountain climbers", (20, 40), "core"),
    ("Jumping jacks", (20, 50), "cardio"),
    ("Tricep dips", (8, 15), "arms"),
    ("Glute bridges", (12, 25), "legs"),
    ("High knees", (20, 40), "cardio"),
    ("Superman hold", (20, 45), "back"),  # seconds
    ("Wall sit", (30, 60), "legs"),       # seconds
]

TIMED = {"Plank", "Superman hold", "Wall sit"}


def build_workout(rounds, hard):
    """Return a list of (exercise, amount, unit) for one round."""
    count = 6 if hard else 5
    picked = random.sample(EXERCISES, count)
    workout = []
    for name, (lo, hi), _focus in picked:
        amount = random.randint(lo, hi)
        if hard:
            amount = int(amount * 1.25)
        unit = "sec" if name in TIMED else "reps"
        workout.append((name, amount, unit))
    return workout


def main():
    parser = argparse.ArgumentParser(description="Generate a random workout.")
    parser.add_argument("--hard", action="store_true", help="tougher workout")
    parser.add_argument("--rounds", type=int, default=None,
                        help="number of rounds (default: random 2-4)")
    args = parser.parse_args()

    rounds = args.rounds or random.randint(2, 4)
    workout = build_workout(rounds, args.hard)

    print("=== Today's Workout ===")
    print(f"Rounds: {rounds}  (rest 60s between rounds)\n")
    for i, (name, amount, unit) in enumerate(workout, 1):
        print(f"  {i}. {name:<20} {amount} {unit}")
    total = sum(a for _n, a, _u in workout) * rounds
    print(f"\nTotal moves: ~{total}. Warm up first, stretch after. Go!")


if __name__ == "__main__":
    main()
