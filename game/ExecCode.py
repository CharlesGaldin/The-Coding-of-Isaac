from game.engine import move_entity

def submit(player, userCode, grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, grid), "getPos" : lambda : pos}
    exec(userCode, correspondances)
    return correspondances


def codeJoueur(player, correspondances, grid):
    try:
        correspondances['turn']()
    except:
        print(il y a erreur)
