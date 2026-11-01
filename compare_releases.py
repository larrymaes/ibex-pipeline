from pathlib import Path

import numpy as np


def read_map(path):
    with open(path) as f:
        lines = f.read().splitlines()
    parts = lines[0][2:].split(":")
    n_header = int(parts[0])
    shape_parts = parts[1].split("x")
    rows = int(shape_parts[0])
    cols = int(shape_parts[1])

    values = []
    for line in lines[n_header:]:
        for word in line.split():
            values.append(float(word))
    grid = np.array(values)
    return grid.reshape(rows, cols)


report = []
report.append("| File | Changed pixels | Median % change | Newly missing | Newly observed |")
report.append("|---|---:|---:|---:|---:|")

for old_path in sorted(Path("data/release16/Hi/hvset_2009A").glob("*.txt")):
    new_path = Path(str(old_path).replace("release16", "release18"))
    old = read_map(old_path)
    new = read_map(new_path)

    # Count changed pixels
    diff = np.abs(new - old)
    changed = (diff > 0.0001).sum()

    # Newly missing / newly observed
    newly_missing = ((old != 0) & (new == 0)).sum()
    newly_observed = ((old == 0) & (new != 0)).sum()

    # Median % change for pixels observed in both
    both = (old != 0) & (new != 0)
    pct = 100 * (new[both] - old[both]) / old[both]
    median_pct = np.median(pct)

    report.append(f"| {old_path.name} | {changed} | {median_pct:+.2f}% | {newly_missing} | {newly_observed} |")

with open("docs/compare_r16_r18.md", "w") as f:
    f.write("\n".join(report) + "\n")

print(f"Compared {len(report) - 2} file pairs. Report saved to docs/compare_r16_r18.md")
