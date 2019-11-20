from game.entity import Player, Monster

GRID_SIZE = 15

def init_grid():
	return [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	return dynamic_grid

def player_placement(dynamic_grid):
	p=GRID_SIZE//2
	dynamic_grid[p][p] = Player([p , p])
	return dynamic_grid[p][p]

def update(dynamic_grid):
	pass

def move_entity(entity, direction, dynamic_grid):
	if entity.moved == True:
		pos = [entity.pos[0],entity.pos[1]]
		if direction == 'up':
			if pos[0]==0:
				pass
			else:
				entity.pos[0] -= 1
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
				entity.move = False
		elif direction == 'down':
			if pos[0] == GRID_SIZE-1:
				pass
			else:
				entity.pos[0] += 1
				entity.move = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		elif direction == 'left':
			if pos[1]==0:
				pass
			else:
				entity.pos[1] -= 1
				entity.move = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		elif direction == 'right':
			if pos[1]==GRID_SIZE-1:
				pass
			else:
				entity.pos[1] += 1
				entity.move = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		else:
			raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')
	else:
		print('You already moved this turn')

#def fire(pos, dynamic_grid):
	#if entity.attack == True:
	#	if dynamic_grid[pos[0]][pos[1]] == None :
	#		print('You missed')
	#	else:
	#		pass
