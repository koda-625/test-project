#!/usr/bin/env bash
# countdown.sh — a tiny terminal countdown timer with a beep at the end.
# Usage: countdown.sh 90        -> counts down 90 seconds
#        countdown.sh 5m        -> counts down 5 minutes (m/h/s suffixes)

set -euo pipefail

usage() { echo "usage: $(basename "$0") <seconds|Ns|Nm|Nh>"; exit 1; }
[[ $# -eq 1 ]] || usage

# Parse input like "90", "30s", "5m", "2h" into seconds
raw="$1"
case "$raw" in
  *[hH]) total=$(( ${raw%[hH]} * 3600 )) ;;
  *[mM]) total=$(( ${raw%[mM]} * 60 )) ;;
  *[sS]) total=$(( ${raw%[sS]} )) ;;
  *)     total=$(( raw )) ;;
esac
(( total > 0 )) || usage

echo "Counting down from $(date -u -d "@$total" +%H:%M:%S) — Ctrl+C to cancel"

while (( total > 0 )); do
  printf '\rTime left: %02d:%02d:%02d' \
    $(( total / 3600 )) $(( (total % 3600) / 60 )) $(( total % 60 ))
  sleep 1
  total=$(( total - 1 ))
done

printf '\rTime left: 00:00:00\n⏰ Time is up!\n'
# Beep a few times (terminal bell) as an alarm
for _ in 1 2 3; do printf '\a'; sleep 0.4; done
