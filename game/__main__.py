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

class Game:
	def __init__(self):
		self.static_grid = init_grid_lv1()
		self.dynamic_grid = init_grid()
		self.player = player_placement(self.dynamic_grid)
		
		self.editor = EditorSetUp()
		
		win_w, win_h = get_window_size(self.static_grid, 30)
		self.pygame_frame = tk.Frame(self.editor.master, width = win_w, height = win_h)
		self.pygame_frame.pack(side = tk.LEFT)
		
		os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())
		if platform.system == "Windows":
			os.environ['SDL_VIDEODRIVER'] = 'windib'
		self.window = create_window(self.static_grid, 30)
		
		self.images = load_images()

		self.correspondances = None
	
	def run(self):
		running = True
		frame_counter = 0
		isCompiled = False
		while running:
			pygame.time.Clock().tick(60)
			
			self.editor.update()
			if self.editor.exit_requested:
				running = False
			
			for event in pygame.event.get():
				if event.type == pygame.locals.QUIT:
					running = False

			if frame_counter % 15 == 0 and self.editor.isSubmitted:
				codeJoueur(self.player, self.editor.userCode, self.dynamic_grid)

				if frame_counter % 240 == 0:
					monster_pop(self.dynamic_grid)
			
			display_map(self.static_grid, self.window, 30, self.images, True)
			display_map(self.dynamic_grid, self.window, 30, self.images, False)

			if self.editor.isSubmitted and not isCompiled:
				isCompiled = True
				self.correspondances = submit(self.player, self.editor.userCode, self.grid)

			if self.editor.isSubmitted and isCompiled:
				codeJoueur(self.player, self.correspondances)

			pygame.display.flip()
			frame_counter += 1
		pygame.quit()
		self.editor.close()


if __name__ == "__main__":
	game = Game()
	game.run()
