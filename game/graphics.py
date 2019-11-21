import pygame
from pygame.locals import *

#pygame.key.set_repeat(400,30)

font = None
def load_font():
	global font
	font = pygame.font.Font(None, 30)

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
	images['wall_upper_left_corner'] = pygame.image.load("assets/wall_upper_left_corner.png").convert()
	images['wall_upper_right_corner'] = pygame.image.load("assets/wall_upper_right_corner.png").convert()
	images['wall_bottom_left_corner'] = pygame.image.load("assets/wall_bottom_left_corner.png").convert()
	images['wall_bottom_right_corner'] = pygame.image.load("assets/wall_bottom_right_corner.png").convert()
	images['wall_up'] = pygame.image.load("assets/wall_up.png").convert()
	images['wall_down'] = pygame.image.load("assets/wall_down.png").convert()
	images['wall_left'] = pygame.image.load("assets/wall_left.png").convert()
	images['wall_right'] = pygame.image.load("assets/wall_right.png").convert()
	images['rock'] = pygame.image.load("assets/rock.png").convert()
	images['goomba'] = pygame.image.load("assets/goomba.png").convert_alpha()
	images['end_screen'] = pygame.image.load("assets/end_screen.gif").convert()
	return images


def get_window_size(grid, tile_size):
	width = len(grid[0])
	height = len(grid)
	return width*tile_size, height*tile_size


def create_window(grid,tile_size):
	screen = pygame.display.set_mode((get_window_size(grid, tile_size)))
	pygame.display.init()
	return screen


def display_tile(tile, x, y, window, tile_size, images, turn_fraction, dynamic):
	if tile == None:
		if not dynamic:
			window.blit(images['ground'], (x,y))
	else:
		if tile.tall_artwork:
			y -= tile_size
		if dynamic and tile.last_movement != None:
			x -= tile.last_movement[1] * tile_size * (1 - turn_fraction)
			y -= tile.last_movement[0] * tile_size * (1 - turn_fraction)
		window.blit(images[tile.artwork], (x,y))

def display_grid(static_grid, dynamic_grid, window, tile_size, images, turn_fraction):
	"""
	images : dico qui contient les images
	Affiche les deux grilles superposées
	"""
	height = len(static_grid)
	width = len(static_grid[0])
	for i in range(height):
		for j in range(width):
			display_tile(static_grid[i][j], j*tile_size, i*tile_size, window, tile_size, images, turn_fraction, False)
	for i in range(height):
		for j in range(width):
			display_tile(dynamic_grid[i][j], j*tile_size, i*tile_size, window, tile_size, images, turn_fraction, True)


# def draw_centered_text(window, text, center_x, center_y):
# 	text_surf = font.render(text, True, pygame.Color(0xff, 0xff, 0xff))
# 	text_w, text_h = text_surf.get_size()
# 	window.blit(text_surf, (center_x-text_w/2, center_y-text_h/2))

def display_end_screen(window, images):
	window.blit(images['end_screen'], (0, 0))


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