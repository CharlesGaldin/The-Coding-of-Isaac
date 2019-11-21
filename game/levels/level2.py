from game.engine import init_grid, GRID_SIZE
from game.entity import Objective, Obstacle

def init_grid_lv2(): #creation de la grille de jeu du level 2
    grid = init_grid()
    grid[GRID_SIZE//2][GRID_SIZE-2] = Objective([GRID_SIZE//2, GRID_SIZE-2], 'door')
    grid[0][0] = Obstacle([0,0], 'wall_upper_left_corner')
    grid[0][GRID_SIZE-1] = Obstacle([0,GRID_SIZE-1], 'wall_upper_right_corner')
    grid[GRID_SIZE-1][0] = Obstacle([GRID_SIZE-1,0], 'wall_bottom_left_corner')
    grid[GRID_SIZE-1][GRID_SIZE-1] = Obstacle([GRID_SIZE-1,GRID_SIZE-1], 'wall_bottom_right_corner')
    for i in range(1,GRID_SIZE-1):
        grid[0][i] = Obstacle([0,i], 'wall_up')
        grid[GRID_SIZE-1][i] = Obstacle([GRID_SIZE-1,i], 'wall_down')
    for i in range(1,GRID_SIZE-1):
        grid[i][0] = Obstacle([i,0], 'wall_left')
        grid[i][GRID_SIZE-1] = Obstacle([i,GRID_SIZE-1], 'wall_right')
    for i in range(3,GRID_SIZE-3):
        grid[i][GRID_SIZE//2 + 2] = Obstacle([i, GRID_SIZE//2 + 2], 'rock')
    return grid
