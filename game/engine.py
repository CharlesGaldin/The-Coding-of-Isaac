from game.entity import Player, Monster
import random

GRID_SIZE = 15

def init_grid():
	return [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

def player_placement(dynamic_grid):
	p=GRID_SIZE//2
	dynamic_grid[p][p] = Player([p , p])
	return dynamic_grid[p][p]

def update(dynamic_grid):
	pass

def move_entity(entity, direction, dynamic_grid):
	#if entity.moved == True:
	pos = [entity.pos[0],entity.pos[1]]
	if direction == 'up':
		if pos[0]==1:
				pass
		else:
			entity.pos[0] -= 1
			dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
			dynamic_grid[pos[0]][pos[1]] = None
			entity.moved = False
	elif direction == 'down':
		if pos[0] == GRID_SIZE-2:
				pass
		else:
			entity.pos[0] += 1
			entity.moved = False
			dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
			dynamic_grid[pos[0]][pos[1]] = None
	elif direction == 'left':
		if pos[1]==1:
				pass
		else:
			entity.pos[1] -= 1
			entity.moved = False
			dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
			dynamic_grid[pos[0]][pos[1]] = None
	elif direction == 'right':
		if pos[1]==GRID_SIZE-2:
				pass
		else:
			entity.pos[1] += 1
			entity.moved = False
			dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
			dynamic_grid[pos[0]][pos[1]] = None
	else:
		raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')
	#else:
		#print('You already moved this turn')

#def fire(pos, dynamic_grid):
	#if entity.attack == True:
	#	if dynamic_grid[pos[0]][pos[1]] == None :
	#		print('You missed')
	#	else:
	#		pass

def monster_pop(dynamic_grid):
	cote = random.randint(0,3)
	case = random.randint(0,GRID_SIZE-1)
	if cote == 0: #haut
		x,y = case,0
	elif cote == 1: #bas
		x,y = case,GRID_SIZE-1
	elif cote == 2: #gauche
		x,y = 0,case
	elif cote == 3: #droite
		x,y = GRID_SIZE-1,case
	new_monster = Monster([y,x],10,10,'goomba')
	dynamic_grid[y][x] = new_monster

	
def update_monster_positions(dynamic_grid,x_player,y_player):
	#dynamic_grid_copy = [[cell for cell in row] for row in dynamic_grid]
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			case = dynamic_grid[i][j]
			if case != None and case.artwork == 'goomba':
				case.move_towards_player(x_player,y_player,dynamic_grid)
	#dynamic_grid = [[cell for cell in row] for row in dynamic_grid_copy]
		
