from game.engine import init_grid, player_placement
from game.graphics import create_window, load_images, display_map
import pygame
import pygame.locals

import threading
from game.editor import EditorSetUp

GRID_SIZE = 15

class Game:
	def __init__(self):
		self.grid = init_grid(GRID_SIZE)
		self.player = player_placement(self.grid)
		self.window = create_window(self.grid, 30)
		self.images = load_images()
		
		def tkthread():
			self.editor = EditorSetUp()
			self.editor.run()
		
		threading.Thread(target=tkthread).start()
	
	def run(self):
		running = True
		display_map(self.grid, self.window, 30, self.images)
		while running:
			pygame.time.Clock().tick(60)
			
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					running = False
			pygame.display.flip()
		pygame.quit()


if __name__ == "__main__":
	game = Game()
	game.run()
