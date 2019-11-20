from game.engine import init_grid, GRID_SIZE
from game.entity import Objective, Obstacle

def init_grid_lv1():
    grid_lv1 = init_grid()
    grid_lv1[GRID_SIZE-2][GRID_SIZE-2] = Objective([GRID_SIZE-2, GRID_SIZE-2], 'door')
    for i in range(GRID_SIZE):
        grid_lv1[0][i] = Obstacle([0,i], 'wall')
        grid_lv1[GRID_SIZE-1][i] = Obstacle([GRID_SIZE-1,i], 'wall')
    for i in range(1,GRID_SIZE-1):
        grid_lv1[i][0] = Obstacle([i,0], 'wall')
        grid_lv1[i][GRID_SIZE-1] = Obstacle([i,GRID_SIZE-1], 'wall')
    return grid_lv1

