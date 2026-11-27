#!/usr/bin/env python3
"""Sudoku puzzle generator.

Prints a fresh puzzle (dots are blanks) plus its solution.
Usage: python3 sudoku.py [holes]   (default: 40 blanks)
"""
import random
import sys


def solve(grid, shuffle=True):
    """Fill the grid in place with a valid Sudoku solution (backtracking)."""
    empty = next(
        ((r, c) for r in range(9) for c in range(9) if grid[r][c] == 0), None
    )
    if empty is None:
        return True
    r, c = empty
    nums = list(range(1, 10))
    if shuffle:
        random.shuffle(nums)
    for n in nums:
        # Clear, explicit validity check (readability over cleverness).
        if (
            n not in grid[r]
            and all(grid[i][c] != n for i in range(9))
            and all(
                grid[(r // 3) * 3 + dr][(c // 3) * 3 + dc] != n
                for dr in range(3)
                for dc in range(3)
            )
        ):
            grid[r][c] = n
            if solve(grid, shuffle):
                return True
            grid[r][c] = 0
    return False


def show(grid, title):
    print(title)
    for r in range(9):
        row = " ".join(str(v) if v else "." for v in grid[r])
        print("  " + row)
        if r in (2, 5):
            print("  " + "-" * 17)
    print()


def main():
    holes = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    holes = max(0, min(64, holes))

    grid = [[0] * 9 for _ in range(9)]
    solve(grid)  # a random full solution
    solution = [row[:] for row in grid]

    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells[:holes]:
        grid[r][c] = 0

    show(grid, "Puzzle  (. = blank)")
    show(solution, "Solution")


if __name__ == "__main__":
    main()
