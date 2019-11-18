from game.entity import Player, Monster

GRID_SIZE = 15

def init_grid():
    grid = [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	return grid

def init_grid_level(level):
	if level == 1:
		return init_grid(15)

def player_placement(grid):
	p=GRID_SIZE//2
	grid[p][p] = Player([p , p])
	return grid

def update(grid):
	pass

def move_entity(entity, direction):
	pos = [entity.pos[0],entity.pos[1]]
	if direction == 'up':
		if pos[0]==0:
			raise NameError('Move not possible')
		else:
			entity.pos[0] -= 1
	elif move == 'down':
    		if pos[0] == GRID_SIZE-1:
			raise NameError('Move not possible')
		else:
    		entity.pos[0] += 1
	elif move == 'left':
		if pos[1]==0:
			raise NameError('Move not possible')
		else:
			entity.pos[1] -= 1
	elif move == 'right':
		if pos[1]==GRID_SIZE-1:
    		raise NameError('Move not possible')
		else:
			entity.pos[1] += 1
	else:
		raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')