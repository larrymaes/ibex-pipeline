#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

mkdir -p logs
LOG="logs/pipeline_$(date +%Y-%m-%d).log"
exec >> "$LOG" 2>&1

exec 9> logs/.lock
if ! flock -n 9; then
    echo "$(date) another run is still going, skipping"
    exit 0
fi
echo "=== $(date) pipeline start ==="

trap 'echo "=== $(date) FAILED at line $LINENO ==="' ERR

PYTHON="$HOME/micromamba/envs/ibex/bin/python"
./fetch_data.sh
"$PYTHON" check_maps.py
"$PYTHON" compare_releases.py
"$PYTHON" plot_map.py

date > logs/last_success
echo "=== $(date) pipeline OK ==="
