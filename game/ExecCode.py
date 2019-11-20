from game.engine import move_entity

def codeJoueur(player, userCode, grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, grid), "getPos" : lambda : pos}
    exec(userCode, correspondances)
    try:
        turn()
    except:
        pass