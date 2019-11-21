from game.entity import Player, Monster , Obstacle , Objective
import random

GRID_SIZE = 15

def init_grid(): #renvoie une grille carrée de taille GRID_SIZE*GRID_SIZE remplie de None
	return [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

def player_placement(dynamic_grid): #place le joueur au début de la partie
	p=GRID_SIZE//2
	dynamic_grid[p][p] = Player([p , p]) #joueur placé au milieu de la grille
	return dynamic_grid[p][p]

def update(dynamic_grid):  #ne fait rien et ne sert a rien pour l'instant, à développer
	pass

def move_entity(entity, direction, dynamic_grid, static_grid):
	"""
	INPUT: 
		prend en arg une entity, un string et la grille dynamique
	OUTPUT:
		mets à jour la grille dynamique et la position du joueur
	RETURN:
		uniquement en cas d'erreur, renvoie l'erreur rencontrée
	"""
	if entity.moved == True:  #verification que le joueur n'ai pas déja bougé ce tour là
		pos = [entity.pos[0],entity.pos[1]]
		if direction == 'up':
			if pos[0]==1 or dynamic_grid[pos[0]-1][pos[1]] != None or isinstance(static_grid[pos[0]-1][pos[1]], Obstacle) == True:
				pass
			else:
				entity.pos[0] -= 1
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
				entity.moved = False
		elif direction == 'down':
			if pos[0] == GRID_SIZE-2 or dynamic_grid[pos[0]+1][pos[1]] != None or isinstance(static_grid[pos[0]+1][pos[1]], Obstacle) == True:
				pass
			else:
				entity.pos[0] += 1
				entity.moved = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		elif direction == 'left':
			if pos[1]==1 or dynamic_grid[pos[0]][pos[1]-1] != None or isinstance(static_grid[pos[0]][pos[1]-1], Obstacle) == True:
				pass
			else:
				entity.pos[1] -= 1
				entity.moved = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		elif direction == 'right':
			if pos[1]==GRID_SIZE-2 or dynamic_grid[pos[0]][pos[1]+1] != None or isinstance(static_grid[pos[0]][pos[1]+1], Obstacle) == True:
				pass
			else:
				entity.pos[1] += 1
				entity.moved = False
				dynamic_grid[entity.pos[0]][entity.pos[1]] = dynamic_grid[pos[0]][pos[1]]
				dynamic_grid[pos[0]][pos[1]] = None
		else:
			raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')
	else:
		if isinstance(entity, Player):
			print('You already moved this turn')

#def fire(pos, dynamic_grid):
	#if entity.attack == True:
	#	if dynamic_grid[pos[0]][pos[1]] == None :
	#		print('You missed')
	#	else:
	#		pass

def monster_pop(dynamic_grid,monsters):
	cote = random.randint(0,3)
	case = random.randint(1,GRID_SIZE-2)
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
	monsters.append(new_monster)
	
def update_monster_positions(dynamic_grid,static_grid,player):
    	#dynamic_grid_copy = [[cell for cell in row] for row in dynamic_grid]
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			case = dynamic_grid[i][j]
			if case != None and case.artwork == 'goomba':
				case.move_towards_player(player.pos[1],player.pos[0],dynamic_grid,static_grid)
				case.attack_player(player)
	#dynamic_grid = [[cell for cell in row] for row in dynamic_grid_copy]


    
		
def entity_attack(entity, dir, dynamic_grid, monsters):
	GRID_SIZE = len(dynamic_grid)
	position = entity.pos.copy()
	fireMove = {"up": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}
	if entity.attacked == True:    #vérification que le joueur n'a pas déjà attaqué ce tour là
		if dir in fireMove:
			for i in range(entity.range):
				position[0] += fireMove[dir][0]
				position[1] += fireMove[dir][1]
				if position[0] >= GRID_SIZE or position[0] < 0 or position[1] >= GRID_SIZE or position[1] < 0:
					break
				if dynamic_grid[position[0]][position[1]] != None:
					dynamic_grid[position[0]][position[1]].health_change(-entity.attack)
					if dynamic_grid[position[0]][position[1]].health <= 0:
						dynamic_grid[position[0]][position[1]].kill(monsters, dynamic_grid)
			entity.attacked = False
		else:
			raise NameError('Attribute not recogized, please choose between "right", "left", "up" and "down"')
	else:
		if isinstance(entity, Player):
			print('You already attacked this turn')	