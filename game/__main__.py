from game.engine import init_grid, player_placement
from game.graphics import get_window_size, create_window, load_images, display_map
import pygame
import pygame.locals
import tkinter as tk
import os
import platform
from game.ExecCode import codeJoueur

import threading
from game.editor import EditorSetUp

class Game:
	def __init__(self):
		self.grid = init_grid()
		self.player = player_placement(self.grid)

		self.window = create_window(self.grid, 30)
		self.images = load_images()
		
		self.editor = EditorSetUp()
		
		win_w, win_h = get_window_size(self.grid, 30)
		self.pygame_frame = tk.Frame(self.editor.master, width = win_w, height = win_h)
		self.pygame_frame.pack(side = tk.LEFT)
		
		os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())
		if platform.system == "Windows":
			os.environ['SDL_VIDEODRIVER'] = 'windib'
		self.window = create_window(self.grid, 30)
		
		self.images = load_images()
	
	def run(self):
		running = True
		display_map(self.grid, self.window, 30, self.images)
		while running:
			display_map(self.grid, self.window, 30, self.images)
			pygame.time.Clock().tick(60)
			
			self.editor.update()
			if self.editor.exit_requested:
				running = False
			
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					running = False
			
			if self.editor.isSubmitted:
				codeJoueur(self.player, self.editor.userCode, self.grid)

			pygame.display.flip()
		pygame.quit()
		self.editor.close()


if __name__ == "__main__":
	game = Game()
	game.run()
