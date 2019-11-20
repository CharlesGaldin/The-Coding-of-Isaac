import pygame
from pygame.locals import *

#pygame.key.set_repeat(400,30)

def load_images():
	"""
	permet de stocker au début les images dont on aura besoin dans un dictionnaire
	renvoie le dictionnaire
	"""
	images = {}
	#images['gumba'] = pygame.image.load("gumba.png").convert_alpha() #exemple
	#images['background'] = pygame.image.load("fond.jpeg").convert()
	images['robot'] = pygame.image.load("assets/robot.png").convert_alpha()
	images['ground'] = pygame.image.load("assets/ground.png").convert_alpha()
	images['door'] = pygame.image.load("assets/door.png").convert()
	return images


def get_window_size(grid, tile_size):
	width = len(grid[0])
	height = len(grid)
	return width*tile_size, height*tile_size


def create_window(grid,tile_size):
	screen = pygame.display.set_mode((get_window_size(grid, tile_size)))
	pygame.display.init()
	return screen

    			

def display_map(grid,window,tile_size,images,ground_where_empty):
	"""
	images : dico qui contient les images
	affiche le fond et tout ce qui se trouve dans la grille
	"""
	height = len(grid)
	width = len(grid[0])
	for i in range(height):
		for j in range(width):
			if grid[i][j] != None:
				window.blit(images[grid[i][j].artwork],(j*tile_size,i*tile_size))
			elif ground_where_empty:
				window.blit(images['ground'],(j*tile_size,i*tile_size))


##ZONE DE TESTS
def run():
    ##HYPERPARAMETERS##
	height = 20
	width = 20
	tile_size = 30
	grid = [[None for i in range(width)] for j in range(height)]
	###
	play = 1
	grid[5][5] = 'door'
	window = create_window(grid,tile_size)
	banque_images = load_images()
	display_map(grid,window,30,banque_images)

	while play:
		pygame.time.Clock().tick(60) ##Tours de boucles max par seconde
		
		for event in pygame.event.get():
			if event.type == QUIT:
				play = 0
		pygame.display.flip()

#run()