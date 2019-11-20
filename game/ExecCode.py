from game.engine import move_entity

def submit(player, userCode, dynamic_grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, dynamic_grid), "getPos" : lambda : pos}
    try:
    	exec(userCode, correspondances)
    except:
    	print("Error on first code execution")
    return correspondances


def codeJoueur(player, correspondances):
    try:
        correspondances['turn']()
    except:
        print("Error during turn() execution")
