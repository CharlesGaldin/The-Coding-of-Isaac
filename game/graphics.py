import pygame
from pygame.locals import *

#pygame.key.set_repeat(400,30)

def load_images():
    #"""permet de stocker au début les images dont on aura besoin dans un dictionnaire"""
	images = {}
	images['gumba'] = pygame.image.load("gumba.png").convert_alpha() #exemple
	images['background'] = pygame.image.load("fond.jpeg").convert()
	return images


def create_window(window_height,window_width,tile_size):
	"""
	window_size/widh : nombre de cases de la grille en hauteur/
	"""
	pygame.init()
	return pygame.display.set_mode((window_width*tile_size,window_height*tile_size))

def display_map(grid,window,tile_size,images):
    #"""images : dico qui contient les images"""
	window.blit(images['background'],(-30,-30))
	height = len(grid)
	width = len(grid[0])
	for i in range(height):
			for j in range(width):
					window.blit(images['gumba'],(j*tile_size,i*tile_size))

	pygame.display.flip()


	
    						
    					


##ZONE DE TESTS
def run():
	play = 1
	window = create_window(20,20,30)
	display_map([[0 for i in range(20)] for j in range(20)],window,30,load_images())
	while play:
		pygame.time.Clock().tick(60) ##Tours de boucles max par seconde
		
		for event in pygame.event.get():
			if event.type == QUIT:
				play = 0
		pygame.display.flip()

#run()