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
	images['background'] = pygame.image.load("fond.jpeg").convert()
	images['robot'] = pygame.image.load("robot.png").convert_alpha()
	images['ground'] = pygame.image.load("ground.png").convert_alpha()
	return images


def create_window(grid,tile_size):
	"""
	window_size/widh : nombre de cases de la grille en hauteur/
	renvoie la fenetre de jeu
	"""
	height = len(grid)
	width = len(grid[0])
	pygame.init()
	return pygame.display.set_mode((width*tile_size,height*tile_size))

    			

def display_map(grid,window,tile_size,images):
	"""
	images : dico qui contient les images
	affiche le fond et tout ce qui se trouve dans la grille
	"""
	window.blit(images['background'],(-30,-30))
	height = len(grid)
	width = len(grid[0])
	for i in range(height):
		for j in range(width):
			window.blit(images['ground'],(j*tile_size,i*tile_size))
			if grid[i][j] != None:
				window.blit(images[grid[i][j]],(j*tile_size,i*tile_size))
			#window.blit(images['gumba'],(j*tile_size,i*tile_size))


	pygame.display.flip()


	
    						
    					


##ZONE DE TESTS
def run():
    ##HYPERPARAMETERS##
	height = 20
	width = 20
	tile_size = 30
	grid = [[None for i in range(width)] for j in range(height)]
	###
	play = 1
	grid[5][5] = 'robot'
	window = create_window(grid,tile_size)
	banque_images = load_images()
	display_map(grid,window,30,banque_images)

	while play:
		pygame.time.Clock().tick(60) ##Tours de boucles max par seconde
		
		for event in pygame.event.get():
			if event.type == QUIT:
				play = 0
		pygame.display.flip()

run()