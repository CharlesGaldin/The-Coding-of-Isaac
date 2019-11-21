from game.engine import init_grid, player_placement, monster_pop
from game.level1 import init_grid_lv1

import tkinter as tk
import os
import platform
from game.editor import EditorSetUp

import pygame
import pygame.locals
from game.graphics import get_window_size, create_window, load_images, display_map

from game.ExecCode import codeJoueur, submit

TILE_SIZE = 32

class Game:
	def __init__(self):
		self.reset_level()
		
		self.editor = EditorSetUp()
		
		win_w, win_h = get_window_size(self.static_grid, TILE_SIZE)
		self.pygame_frame = tk.Frame(self.editor.master, width = win_w, height = win_h)
		self.pygame_frame.pack(side = tk.LEFT)
		
		os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())
		if platform.system == "Windows":
			os.environ['SDL_VIDEODRIVER'] = 'windib'
		self.window = create_window(self.static_grid, TILE_SIZE)
		
		self.images = load_images()

		self.correspondances = None
		self.is_code_running = False
	
	def reset_level(self):
		self.static_grid, self.exit = init_grid_lv1()
		self.dynamic_grid = init_grid()
		self.player = player_placement(self.dynamic_grid)
	
	def run(self):
		running = True
		frame_counter = 0
		while running:
			pygame.time.Clock().tick(60)
			
			self.editor.update()
			if self.editor.exit_requested:
				running = False
			
			if self.editor.is_submitted:
				self.editor.is_submitted = False
				self.reset_level()
				self.is_code_running = True
				self.correspondances = submit(self.player, self.editor.user_code, self.dynamic_grid, self.static_grid, self.exit)
			
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					running = False
			
			if self.is_code_running:
				if frame_counter % 15 == 0:
					codeJoueur(self.player, self.correspondances)
					
					if frame_counter % 240 == 0:
						monster_pop(self.dynamic_grid)
			
			display_map(self.static_grid, self.window, TILE_SIZE, self.images, True)
			display_map(self.dynamic_grid, self.window, TILE_SIZE, self.images, False)
			
			pygame.display.flip()
			frame_counter += 1
		pygame.quit()
		self.editor.close()


if __name__ == "__main__":
	game = Game()
	game.run()
