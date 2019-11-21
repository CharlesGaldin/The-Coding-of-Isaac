from game.engine import move_entity

def submit(player, userCode, dynamic_grid, static_grid):
    correspondances = {"move" : lambda direction : move_entity(player, direction, dynamic_grid, static_grid), "get_pos": lambda: (player.pos[1], player.pos[0])}
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
