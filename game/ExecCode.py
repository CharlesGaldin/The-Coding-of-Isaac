from game.engine import move_entity , entity_attack
from copy import deepcopy


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
	check_import(userCode)
	exec(userCode, correspondances)
	return correspondances


def codeJoueur(player, correspondances, static_grid):
	try:
		correspondances['turn'](deepcopy(static_grid))
	except Exception as e:
		print("Error during turn() execution", e)

def check_import(userCode):
	if userCode.find('import game') != -1:
		raise ImportError('unauthorized import')
	if userCode.find('from game') != -1:
		raise ImportError('unauthorized import')

