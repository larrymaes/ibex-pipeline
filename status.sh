#!/usr/bin/env bash
set -uo pipefail

cd "$(dirname "$0")" || exit

echo "# IBEX pipeline status — $(date)"
echo

echo "## Last successful run"
if [ -f logs/last_success ]; then
    last=$(cat logs/last_success)
    now_s=$(date +%s)
    last_s=$(date -d "$last" +%s)
    age_h=$(( (now_s - last_s) / 3600 ))

    if (( age_h > 26 )); then
        echo "- STALE: $last ($age_h hours ago)"
    else
        echo "- OK: $last ($age_h hours ago)"
    fi
else
    echo "- NEVER: No record of a successful execution found."
fi
echo

echo "## Data"
count=$(find data -name '*.txt' | wc -l)
echo "- $count of 25 map files present"
echo

echo "## Storage"
echo "- data: $(du -sh data | cut -f1)"
echo "- free disk space: $(df -h --output=avail . | tail -1 | tr -d ' ')"
echo "- logs: $(du -sh logs | cut -f1)"
echo

echo "## Problems in the logs (last 7 days)"
recent=$(find logs -name 'pipeline_*.log' -mtime -7)
if [ -n "$recent" ]; then
    # shellcheck disable=SC2086
    fails=$(grep -h "FAILED" $recent | wc -l)
    echo "- $fails failed run(s)"
    # shellcheck disable=SC2086
    grep -h "FAILED\|PROBLEM" $recent | tail -5 | sed 's/^/    /'
else
    echo "- no logs in the last 7 days"
fi
