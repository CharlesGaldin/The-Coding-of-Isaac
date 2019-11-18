def init_grid(size):
	grid = [[None for i in range(size)] for j in range(size)]
	return grid

def init_grid_level(level):
	if level == 1:
		return init_grid(15)

from entity import Player, Monster

def player_placement(grid):
	size=len(grid)
	p=size//2
	grid[p][p] = Player(10)
	return grid

def update(grid):
	pass

print(init_grid(3))
