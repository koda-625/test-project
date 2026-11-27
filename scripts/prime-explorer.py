#!/usr/bin/env python3
"""Prime Explorer — list primes, test primality, find the nth prime.

Usage:
    python3 prime-explorer.py            # interactive prompt
    python3 prime-explorer.py 100        # primes up to 100
    python3 prime-explorer.py --nth 25   # the 25th prime
    python3 prime-explorer.py --check 97 # is 97 prime?
"""

import argparse
import math
import sys


def is_prime(n: int) -> bool:
    """Return True if n is prime (trial division up to sqrt(n))."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primes_up_to(limit: int) -> list[int]:
    """All primes <= limit, via the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = [False] * len(range(i * i, limit + 1, i))
    return [n for n, prime in enumerate(sieve) if prime]


def nth_prime(n: int) -> int:
    """The nth prime (1-indexed): nth_prime(1) == 2."""
    if n < 1:
        raise ValueError("n must be >= 1")
    count, candidate = 0, 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser(description="Explore prime numbers.")
    parser.add_argument("limit", nargs="?", type=int, help="list primes up to LIMIT")
    parser.add_argument("--nth", type=int, help="print the NTH prime")
    parser.add_argument("--check", type=int, help="test whether N is prime")
    args = parser.parse_args()

    if args.check is not None:
        print(f"{args.check} is {'prime' if is_prime(args.check) else 'not prime'}.")
    elif args.nth is not None:
        print(f"The {args.nth}th prime is {nth_prime(args.nth)}.")
    elif args.limit is not None:
        primes = primes_up_to(args.limit)
        print(f"Primes up to {args.limit} ({len(primes)} found):")
        print(" ".join(map(str, primes)))
    else:
        # Interactive mode.
        while True:
            try:
                raw = input("Enter a number (or 'q' to quit): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if raw.lower() in ("q", "quit", "exit"):
                break
            if not raw.lstrip("-").isdigit():
                print("Please enter an integer.")
                continue
            n = int(raw)
            print(f"  {n} is {'prime' if is_prime(n) else 'not prime'}.")
            if n >= 2:
                print(f"  Primes up to {n}: {len(primes_up_to(n))} found.")


if __name__ == "__main__":
    main()
