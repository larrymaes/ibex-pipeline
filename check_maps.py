import sys
from pathlib import Path

import numpy as np

problems = 0
total_files = 0

print("Initializing IBEX map data verification sequence...")

for path in sorted(Path("data").rglob("*.txt")):
    total_files = total_files + 1
    with open(path) as f:
        lines = f.read().splitlines()

    parts = lines[0][2:].split(":")
    n_header = int(parts[0])
    shape_parts = parts[1].split("x")
    rows = int(shape_parts[0])
    cols = int(shape_parts[1])

    h_min = 0
    h_max = 0
    for line in lines[:n_header]:
        for word in line.split():
            if word.startswith("h_min="):
                h_min = float(word[6:])
            elif word.startswith("h_max="):
                h_max = float(word[6:])

    values = []
    for line in lines[n_header:]:
        for word in line.split():
            values.append(float(word))
    grid = np.array(values)

    issues = []
    unobserved = (grid == 0).sum()
    if abs(grid.size - (rows * cols)) > 0.0001:
        issues.append(f"expected {rows * cols} values, found {grid.size}")
    if abs(grid.min() - h_min) > 0.0001:
        issues.append(f"min {grid.min():.6f} doesn't match header h_min {h_min:.6f}")
    if abs(grid.max() - h_max) > 0.0001:
        issues.append(f"max {grid.max():.6f} doesn't match header h_max {h_max:.6f}")
    if (grid < 0).sum() > 0:
        issues.append(f"{(grid < 0).sum()} negative values")

    name = path.relative_to("data")
    if issues:
        problems = problems + 1
        print(f"PROBLEM  {name}: {'; '.join(issues)}")
    else:
        print(f"OK       {name}  {grid.size} values, {unobserved} unobserved")

print("-" * 80)
print(
    f"Verification Complete: {total_files} files checked. {problems} problems detected."
)

if problems > 0:
    print("Pipeline error status triggered due to compromised telemetry.")
    sys.exit(1)
else:
    print("All archived maps healthy. Core data pipeline green.")
    sys.exit(0)
