def codeJoueur(player, userCode):
    def pos() :
        p = player.pos()
        return tuple(p)
    correspondances = {"move" : lambda direction : move_entity(player, grille, direction), "getPos" : lambda : pos}
    exec(userCode, correspondances)