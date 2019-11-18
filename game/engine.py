def init_grid(size):
    grid = []
    for i in range(size):
        grid += [[]]
        for j in range(size):
            grid[i] += [[None]]
    return grid

def init_grid_level(level):
    if level == 1:
        return init_grid(15)

