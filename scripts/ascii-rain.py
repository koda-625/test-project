#!/usr/bin/env python3
"""ascii-rain.py -- a tiny Matrix-style digital rain in your terminal.

Usage: python3 ascii-rain.py
Press Ctrl+C to stop.
"""

import os
import random
import shutil
import sys
import time

CHARS = "01<>/\\|*#+=-%$@"  # glyphs used for the rain drops
FRAME_DELAY = 0.08


def main() -> None:
    width, height = shutil.get_terminal_size((80, 24))
    # Each column has a "drop head" row; -1 means no active drop.
    drops = [-1] * width
    green = "\033[32m"   # green text
    bright = "\033[1m"   # bold for the drop heads
    reset = "\033[0m"    # reset colors
    sys.stdout.write("\033[?25l")  # hide the cursor
    try:
        while True:
            frame = [" " * width for _ in range(height)]
            for x in range(width):
                if drops[x] < 0 and random.random() < 0.06:
                    drops[x] = 0  # start a new drop at the top
                if drops[x] >= 0:
                    drops[x] += 1
                    head = drops[x]
                    if head >= height + 6:
                        drops[x] = -1  # drop has faded out
                    else:
                        for y in range(max(0, head - 6), min(height, head + 1)):
                            ch = random.choice(CHARS)
                            prefix = bright if y == head else ""
                            frame[y] = frame[y][:x] + prefix + ch + reset + frame[y][x + 1:]
            sys.stdout.write("\033[H" + "\n".join(green + line for line in frame))
            sys.stdout.flush()
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(reset + "\033[?25h")  # restore cursor and colors
        print("\nRain stopped. Have a nice day!")


if __name__ == "__main__":
    main()
