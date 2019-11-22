from game.engine import init_grid, GRID_SIZE
from game.entity import Objective, Obstacle, Monster

LAST_LEVEL = 3

def place_walls(grid):
    grid[0][0] = Obstacle([0,0], 'wall_upper_left_corner')
    grid[0][GRID_SIZE-1] = Obstacle([0,GRID_SIZE-1], 'wall_upper_right_corner')
    grid[GRID_SIZE-1][0] = Obstacle([GRID_SIZE-1,0], 'wall_bottom_left_corner')
    grid[GRID_SIZE-1][GRID_SIZE-1] = Obstacle([GRID_SIZE-1,GRID_SIZE-1], 'wall_bottom_right_corner')
    for i in range(1,GRID_SIZE-1):
        grid[0][i] = Obstacle([0,i], 'wall_up')
        grid[GRID_SIZE-1][i] = Obstacle([GRID_SIZE-1,i], 'wall_down')
        grid[i][0] = Obstacle([i,0], 'wall_left')
        grid[i][GRID_SIZE-1] = Obstacle([i,GRID_SIZE-1], 'wall_right')

def level_grid(level, monster_list):                   #creation de la grille de jeu du niveau choisi
    if level == 1:
        grid = init_grid()
        dynamic_grid = init_grid()
        place_walls(grid)
        grid[GRID_SIZE-2][GRID_SIZE-2] = Objective([GRID_SIZE-2, GRID_SIZE-2], 'door')
        return grid, dynamic_grid, grid[GRID_SIZE-2][GRID_SIZE-2]
    elif level == 2:
        grid = init_grid()
        dynamic_grid = init_grid()
        place_walls(grid)
        grid[GRID_SIZE//2][GRID_SIZE-2] = Objective([GRID_SIZE//2, GRID_SIZE-2], 'door')
        for i in range(3,GRID_SIZE-3):
            grid[i][GRID_SIZE//2 + 2] = Obstacle([i, GRID_SIZE//2 + 2], 'rock')
        return grid, dynamic_grid, grid[GRID_SIZE//2][GRID_SIZE-2]
    elif level == 3:
        grid = init_grid()
        dynamic_grid = init_grid()
        dynamic_grid[GRID_SIZE//2 + 1][1] = Monster([GRID_SIZE//2 + 1, 1], 1, 1, 'slime')
        dynamic_grid[GRID_SIZE//2 - 1][1] = Monster([GRID_SIZE//2 - 1, 1], 1, 1, 'slime')
        monster_list.append(dynamic_grid[GRID_SIZE//2 + 1][1])
        monster_list.append(dynamic_grid[GRID_SIZE//2 - 1][1])
        place_walls(grid)
        grid[GRID_SIZE//2][1] = Objective([GRID_SIZE//2, 1], 'door')
        for i in range(2,GRID_SIZE-2):
            grid[i][2] = Obstacle([i,2], 'rock')
            grid[2][i] = Obstacle([2,i], 'rock')
            grid[i][GRID_SIZE-3] = Obstacle([i,GRID_SIZE-3], 'rock')
            grid[GRID_SIZE-3][i] = Obstacle([GRID_SIZE-3,i], 'rock')
        for i in range(4,GRID_SIZE-4):
            grid[i][4] = Obstacle([i,4], 'rock')
            grid[4][i] = Obstacle([4,i], 'rock')
            grid[i][GRID_SIZE-5] = Obstacle([i,GRID_SIZE-5], 'rock')
            grid[GRID_SIZE-5][i] = Obstacle([GRID_SIZE-5,i], 'rock')
        grid[GRID_SIZE//2-1][4] = None
        grid[GRID_SIZE//2+1][4] = None
        grid[GRID_SIZE//2-1][GRID_SIZE-5] = None
        grid[GRID_SIZE//2+1][GRID_SIZE-5] = None
        grid[2][GRID_SIZE//2-2] = None
        grid[2][GRID_SIZE//2+2] = None
        grid[GRID_SIZE-3][GRID_SIZE//2-2] = None
        grid[GRID_SIZE-3][GRID_SIZE//2+2] = None
        return grid, dynamic_grid, grid[GRID_SIZE//2][1]
    elif level == 4:
        grid = init_grid()
        dynamic_grid = init_grid()
        grid = place_walls(grid)

        
        return grid, dynamic_grid, grid[GRID_SIZE//2][1]

