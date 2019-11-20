from game.engine import init_grid, GRID_SIZE
from game.entity import Objective

def init_grid_lv1():
    grid_lv1 = init_grid()
    grid_lv1[GRID_SIZE-1][GRID_SIZE-1] = Objective([GRID_SIZE-1, GRID_SIZE-1], 'door')
    return grid_lv1