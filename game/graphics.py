import pygame
from pygame.locals import *
import os

print(os.getcwd())

pygame.init()
#pygame.key.set_repeat(400,30)



def create_window(window_height,window_width,tile_size):
	"""
	window_size/widh : nombre de cases de la grille en hauteur/
	"""
	return pygame.display.set_mode((window_width*tile_size,window_height*tile_size))

def display_map(grid,window,tile_size):
    
	height = len(grid)
	width = len(grid[0])
	gumba = pygame.image.load("gumba.png").convert()
	for i in range(height):
			for j in range(width):
					window.blit(gumba,(j*tile_size,i*tile_size))


    					
    					



play = 1
window = create_window(20,20,20)
display_map([[0 for i in range(20)] for j in range(20)],window,30)
while play:
	pygame.time.Clock().tick(60) ##Tours de boucles max par seconde
	
	for event in pygame.event.get():
		if event.type == QUIT:
			play = 0
	pygame.display.flip()


