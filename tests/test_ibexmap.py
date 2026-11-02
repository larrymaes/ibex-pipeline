from ibexmap import read_map


def test_read_map_shape_and_values(tmp_path):
    fake = tmp_path / "tiny.txt"
    fake.write_text("# 3:2x3:junk\n# h_min=1 h_max=6\n#\n1 2 3\n4 5 6\n")

    grid = read_map(fake)

    assert grid.shape == (2, 3)
    assert grid[1, 2] == 6


def test_read_map_counts_zeros(tmp_path):
    fake = tmp_path / "tiny.txt"
    fake.write_text("# 3:2x3:junk\n# h_min=0 h_max=6\n#\n1 0 3\n4 5 6\n")

    grid = read_map(fake)

    assert (grid == 0).sum() == 1
