from game.engine import move_entity

def submit(player, userCode, dynamic_grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, dynamic_grid), "getPos" : lambda : pos, "attack" : lambda dir : entitie_attack(player, dir, dynamic_grid)}
    try:
    	exec(userCode, correspondances)
    except Exception as e:
    	print("Error on first code execution:", e)
    return correspondances


def codeJoueur(player, correspondances):
    try:
        correspondances['turn']()
    except Exception as e:
        print("Error during turn() execution", e)

#TO DO:
#   -Fonction attack
#   -Fonction pour obtenir la position des ennemis
#   -Fonction pour obtenir la position de la sortie

def entitie_attack(entitie, dir, dynamic_grid):
    GRID_SIZE = len(dynamic_grid)
    position = entitie.pos.copy()
    fireMove = {"up": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}
    for i in range(entitie.range):
        position[0] += fireMove[dir][0]
        position[1] += fireMove[dir][1]
        if position[0] >= GRID_SIZE or position[0] < 0 or position[1] >= GRID_SIZE or position[1] < 0:
            break
        if dynamic_grid[position[0]][position[1]] != None:
            dynamic_grid[position[0]][position[1]].health_change(-entitie.attack)
       