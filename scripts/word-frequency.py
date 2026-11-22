#!/usr/bin/env python3
"""Word Frequency Analyzer — count the most common words in a text file.

Usage:
    python3 word-frequency.py <file.txt> [top_n]
    echo "hello world hello" | python3 word-frequency.py
"""

import re
import sys
from collections import Counter

# A small stop-word list so the ranking shows the interesting words.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "else",
    "of", "in", "on", "at", "to", "for", "with", "by", "from",
    "is", "are", "was", "were", "be", "been", "being",
    "it", "its", "this", "that", "these", "those",
    "i", "you", "he", "she", "we", "they", "my", "your", "his",
    "her", "our", "their", "as", "not", "no", "so", "do", "does",
}


def count_words(text: str) -> Counter:
    """Return a Counter of lower-cased words, ignoring stop words."""
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(w for w in words if w not in STOP_WORDS)


def main() -> int:
    top_n = 10
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
        if len(sys.argv) > 2:
            top_n = int(sys.argv[2])
    else:
        text = sys.stdin.read()  # read from a pipe or redirect
        if len(sys.argv) > 2:
            top_n = int(sys.argv[2])

    counts = count_words(text)
    total = sum(counts.values())
    print(f"Total words (excl. stop words): {total}")
    print(f"Unique words: {len(counts)}\n")
    for rank, (word, n) in enumerate(counts.most_common(top_n), 1):
        bar = "#" * min(n, 40)  # simple bar chart
        print(f"{rank:>2}. {word:<15} {n:>4} {bar}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
