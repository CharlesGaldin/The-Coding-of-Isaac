from game.entity import Player, Monster

GRID_SIZE = 15

def init_grid():
	grid = [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	return grid

def init_grid_level(level):
	if level == 1:
		return init_grid()

def player_placement(grid):
	p=GRID_SIZE//2
	grid[p][p] = Player([p , p])
	return grid[p][p]

def update(grid):
	pass

def move_entity(entity, direction, grid):
	if entity.moved == True:
		pos = [entity.pos[0],entity.pos[1]]
		if direction == 'up':
			if pos[0]==0:
				raise NameError('Move not possible')
			else:
				entity.pos[0] -= 1
				grid[entity.pos[0]][entity.pos[1]] = grid[pos[0]][pos[1]]
				grid[pos[0]][pos[1]] = None
				entity.move = False
		elif direction == 'down':
			if pos[0] == GRID_SIZE-1:
				raise NameError('Move not possible')
			else:
				entity.pos[0] += 1
				entity.move = False
				grid[entity.pos[0]][entity.pos[1]] = grid[pos[0]][pos[1]]
				grid[pos[0]][pos[1]] = None
		elif direction == 'left':
			if pos[1]==0:
				raise NameError('Move not possible')
			else:
				entity.pos[1] -= 1
				entity.move = False
				grid[entity.pos[0]][entity.pos[1]] = grid[pos[0]][pos[1]]
				grid[pos[0]][pos[1]] = None
		elif direction == 'right':
			if pos[1]==GRID_SIZE-1:
				raise NameError('Move not possible')
			else:
				entity.pos[1] += 1
				entity.move = False
				grid[entity.pos[0]][entity.pos[1]] = grid[pos[0]][pos[1]]
				grid[pos[0]][pos[1]] = None
		else:
			raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')
	else:
		print('You already moved this turn')

#def fire(pos, grid):
	#if entity.attack == True:
	#	if grid[pos[0]][pos[1]] == None :
	#		print('You missed')
	#	else:
	#		pass
