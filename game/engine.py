"""def init_grid(size):
    	grid = [[None for i in range(size)] for j in range(size)]
	return grid

def init_grid_level(level):
	if level == 1:
		return init_grid(15)
"""
from entity import Player, Monster

def player_placement(grid):
	size=len(grid)
	p=size//2
	grid[p][p] = Player([p , p])
	return grid

def update(grid):
	pass

def move_entity(entity, direction):
	pos = [entity.pos[0],entity.pos[1]]
	if direction == 'up':
		if pos[0]==0:
			return 'move not possible'
		else:
			entity.pos[0] -= 1
	elif direction == 'down':
		return move_entity(entity, up)
	elif direction == 'left':
		if pos[1]==0:
			return 'move not possible'
		else:
			entity.pos[1] -= 1