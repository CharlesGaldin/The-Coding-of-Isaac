from game.engine import move_entity

def submit(player, userCode, dynamic_grid, static_grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, dynamic_grid, static_grid), "getPos" : lambda : pos}
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
