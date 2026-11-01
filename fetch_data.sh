#!/usr/bin/env bash
set -euo pipefail

BASE_URL="https://cdaweb.gsfc.nasa.gov/pub/data/ibex"

echo "Fetching 2009A 6-month map datasets..."
for release in 16 18; do
    for step in 2 3 4 5 6; do
        for kind in flux fexp; do
            FILE="release${release}/Hi/hvset_2009A/hv60.hide-trp-flux100-hi-${step}-${kind}.txt"

            if [ ! -f "data/$FILE" ]; then
                echo "Downloading: $FILE"
                curl -fsSL --create-dirs -o "data/$FILE" "$BASE_URL/$FILE"
            else
                echo "Already downloaded, skipping: $FILE"
            fi
        done
    done
done

echo "Fetching 14-year combined map datasets..."
for step in 2 3 4 5 6; do
    FILE="release18/Hi/hvset_2009-2022/hv60.hide-trp-flux100-hi-${step}-flux.txt"

    if [ ! -f "data/$FILE" ]; then
        echo "Downloading: $FILE"
        curl -fsSL --create-dirs -o "data/$FILE" "$BASE_URL/$FILE"
    else
        echo "Already downloaded, skipping: $FILE"
    fi
done

echo "Downlink complete."
