from game.engine import move_entity , entity_attack


def submit(player, userCode, dynamic_grid, static_grid, exit, monsters):
		
	def pos(entity):
			return (entity.pos[1], entity.pos[0])
	
	def pos_monster(monsters):
		position=[]
		for monster in monsters:
			position.append(pos(monster))
		return position
			
	correspondances = {
		"move": lambda direction: move_entity(player, direction, dynamic_grid, static_grid),
		"get_pos_player": lambda: pos(player),
		"get_pos_exit" : lambda: pos(exit),
		"attack": lambda dir: entity_attack(player, dir, dynamic_grid, monsters),
	}
	try:
		check_import(userCode)
		exec(userCode, correspondances)
	except Exception as e:
		print("Error on first code execution:", e)
	return correspondances


def codeJoueur(player, correspondances):
	try:
		correspondances['turn']()
	except Exception as e:
		print("Error during turn() execution", e)

def check_import(userCode):
	if userCode.find('import game') != -1:
		raise ImportError('unauthorized import')
	if userCode.find('from game') != -1:
		raise ImportError('unauthorized import')

#def entity_attack(entity, dir, dynamic_grid, monsters):
#    GRID_SIZE = len(dynamic_grid)
#    position = entity.pos.copy()
#    fireMove = {"up": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}
#    for i in range(entity.range):
#        position[0] += fireMove[dir][0]
#        position[1] += fireMove[dir][1]
#        if position[0] >= GRID_SIZE or position[0] < 0 or position[1] >= GRID_SIZE or position[1] < 0:
#            break
#        if dynamic_grid[position[0]][position[1]] != None:
#            dynamic_grid[position[0]][position[1]].health_change(-entity.attack)
#            if dynamic_grid[position[0]][position[1]].health <= 0:
#                dynamic_grid[position[0]][position[1]].kill(monsters, dynamic_grid)
#	entity.attacked = False
