def init_grid(size):
    grid = []
    for i in range(size):
        grid += [[]]
        for j in range(size):
            grid[i] += [[' ']]
    return grid

print(init_grid(3))