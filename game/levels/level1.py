from game.engine import init_grid, GRID_SIZE
from game.entity import Objective, Obstacle

def init_grid_lv1(): #creation de la grille de jeu du level 1
    grid_lv1 = init_grid()
    grid_lv1[GRID_SIZE-2][GRID_SIZE-2] = Objective([GRID_SIZE-2, GRID_SIZE-2], 'door')
    grid_lv1[0][0] = Obstacle([0,0], 'wall_upper_left_corner')
    grid_lv1[0][GRID_SIZE-1] = Obstacle([0,GRID_SIZE-1], 'wall_upper_right_corner')
    grid_lv1[GRID_SIZE-1][0] = Obstacle([GRID_SIZE-1,0], 'wall_bottom_left_corner')
    grid_lv1[GRID_SIZE-1][GRID_SIZE-1] = Obstacle([GRID_SIZE-1,GRID_SIZE-1], 'wall_bottom_right_corner')
    for i in range(1,GRID_SIZE-1):
        grid_lv1[0][i] = Obstacle([0,i], 'wall_up')
        grid_lv1[GRID_SIZE-1][i] = Obstacle([GRID_SIZE-1,i], 'wall_down')
    for i in range(1,GRID_SIZE-1):
        grid_lv1[i][0] = Obstacle([i,0], 'wall_left')
        grid_lv1[i][GRID_SIZE-1] = Obstacle([i,GRID_SIZE-1], 'wall_right')
    return grid_lv1, grid_lv1[GRID_SIZE-2][GRID_SIZE-2]

