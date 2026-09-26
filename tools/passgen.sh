#!/usr/bin/env bash
# passgen.sh - generate a cryptographically random password
#
# Usage:
#   passgen.sh [length] [--no-symbols]
#
# Examples:
#   passgen.sh        # 16-char password with symbols
#   passgen.sh 24     # 24-char password with symbols
#   passgen.sh 12 --no-symbols   # letters + digits only

set -euo pipefail

LEN="${1:-16}"
NO_SYMBOLS=0
if [[ "${2:-}" == "--no-symbols" ]]; then
  NO_SYMBOLS=1
fi

# Length must be a positive integer >= 4
if ! [[ "$LEN" =~ ^[0-9]+$ ]] || [ "$LEN" -lt 4 ]; then
  echo "Usage: $0 [length>=4] [--no-symbols]" >&2
  exit 1
fi

# Build the character set ('-' goes last so tr treats it literally)
CHARS='A-Za-z0-9'
if [ "$NO_SYMBOLS" -eq 0 ]; then
  CHARS+='!@#$%^&*()_=+[]{}-'
fi

# Read random bytes from the OS CSPRNG, keep only wanted chars, trim to length
LC_ALL=C tr -dc "$CHARS" < /dev/urandom | head -c "$LEN"
echo
