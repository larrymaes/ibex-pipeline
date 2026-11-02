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
