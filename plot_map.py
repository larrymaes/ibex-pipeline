import matplotlib
matplotlib.use("Agg")  # save plots to files instead of opening windows
import matplotlib.pyplot as plt
import numpy as np

MAP_FILE = "data/release18/Hi/hvset_2009-2022/hv60.hide-trp-flux100-hi-4-flux.txt"


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


grid = read_map(MAP_FILE)
rows, cols = grid.shape
grid[grid == 0] = np.nan


plt.imshow(grid, origin="lower", cmap="magma")
plt.colorbar()
plt.savefig("docs/quick_look.png")
plt.close()


x_edges = np.radians(np.linspace(-180, 180, cols + 1))
y_edges = np.radians(np.linspace(-90, 90, rows + 1))


grid = np.roll(grid, -12, axis=1)
grid = grid[:, ::-1]
fig = plt.figure(figsize=(10, 5.5))
ax = fig.add_subplot(projection="mollweide")
mesh = ax.pcolormesh(x_edges, y_edges, grid, cmap="magma")
ax.set_xticklabels([])
ax.grid(alpha=0.3)
fig.colorbar(mesh, ax=ax, orientation="horizontal", shrink=0.7, pad=0.05, label="Flux (#/cm² s sr keV)")
ax.set_title("IBEX-Hi 2009–2022, energy step 4", pad=20)
fig.savefig("docs/ribbon_hi4.png", dpi=150, bbox_inches="tight")
plt.close()

