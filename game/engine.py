def init_grid(size):
	grid = []
	for i in range(size):
		grid += [[]]
		j=0
		while j < size:
			grid[i] += [[None]]
			j +=1
	return grid

def init_grid_level(level):
	if level == 1:
		return init_grid(15)

from game.entity import Player, Monster

def player_placement(grid):
	size=len(grid)
	p=size//2
	grid[p][p] = Player(10)
	return grid

def update(grid):
	pass