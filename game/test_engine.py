from game.engine import *
from game.entity import Player
import random

def test_init_grid():
	grid = init_grid() 
	assert len(grid) == GRID_SIZE
	for row in grid:
		assert len(row) == GRID_SIZE
		assert all(cell == None for cell in row)

def count_true(l):
	return sum(l) # True = 1, False = 0

def test_player_placement():
	dynamic_grid = init_grid()
	player = player_placement(dynamic_grid)
	assert isinstance(player, Player)
	assert count_true(isinstance(cell, Player) for row in dynamic_grid for cell in row) == 1

def test_move_entity():
	static_grid = init_grid()
	dynamic_grid = init_grid()
	pos = [3,3]
	player = Player(pos)
	dynamic_grid[pos[0]][pos[1]] = player
	move_entity(player, "right", dynamic_grid, static_grid)
	assert dynamic_grid[3][3] == None
	assert dynamic_grid[3][4] == player
	assert pos == [3,4]

def test_update_monster_positions():
	static_grid = init_grid()
	dynamic_grid = init_grid()
	player = player_placement(dynamic_grid)
	monsterCnt = 4
	monsters = []
	distances = []
	for i in range(monsterCnt):
		x, y = None, None
		while [x, y] == [None, None] or [x, y] == player.pos:
			x, y = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)
		pos = [x, y]
		monster = Monster(pos, 10, 10, "goomba")
		dynamic_grid[x][y] = monster
		monsters.append(monster)
		distances.append((player.pos[0] - pos[0])**2 + (player.pos[1] - pos[1])**2)
	update_monster_positions(dynamic_grid, static_grid, player.pos[1], player.pos[0])
	for i in range(monsterCnt):
		dist = distances[i]
		pos = monsters[i].pos
		new_dist = (player.pos[0] - pos[0])**2 + (player.pos[1] - pos[1])**2
		assert new_dist <= dist
