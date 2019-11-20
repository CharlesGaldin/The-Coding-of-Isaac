from game.engine import move_entity

def codeJoueur(player, userCode, grid):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, direction, grid), "getPos" : lambda : pos}
    try:
        exec(userCode, correspondances)
        turn()
    except:
        pass