from game.engine import init_grid, player_placement, monster_pop, update_monster_positions, move_entity
from game.levels import level_grid, LAST_LEVEL
from game.entity import Objective

import tkinter as tk
import os
import platform
from game.editor import EditorSetUp

import pygame
import pygame.locals
from game.graphics import get_window_size, create_window, load_images, load_font, display_grid, display_end_screen

from game.ExecCode import codeJoueur, submit

TILE_SIZE = 32

def reset_entities(dynamic_grid): #protocole de mise à jour des entity.moved de toutes les entités ayant fait leur tour
	for row in dynamic_grid:
		for cell in row:
			if cell != None:
				cell.moved = False
				cell.attacked = False
				cell.last_movement = None

class Game:
	def __init__(self):
		self.cur_level = 1
		self.reset_level()
		
		self.editor = EditorSetUp()
		
		win_w, win_h = get_window_size(self.static_grid, TILE_SIZE)
		self.pygame_frame = tk.Frame(self.editor.master, width = win_w, height = win_h)
		self.pygame_frame.pack(side = tk.LEFT)
		
		os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())
		if platform.system == "Windows":
			os.environ['SDL_VIDEODRIVER'] = 'windib'
		self.window = create_window(self.static_grid, TILE_SIZE)
		
		pygame.init()
		self.images = load_images()
		load_font()

		self.correspondances = None
		self.is_code_running = False
		
		self.turn_frames = 15
		self.hurt_frames = 10
		self.attack_frames = 10
		
	
	def reset_level(self):
		if self.cur_level > LAST_LEVEL: return
		self.monsters=[]
		self.static_grid, self.exit = level_grid(self.cur_level)
		self.dynamic_grid = init_grid()
		self.player = player_placement(self.dynamic_grid)
		self.frame_counter = 0
	
	def run(self):
		running = True
		while running:
			pygame.time.Clock().tick(60)
			
			self.editor.update()
			if self.editor.exit_requested:
				running = False
			
			if self.cur_level <= LAST_LEVEL:
				if self.editor.is_submitted:
					self.editor.is_submitted = False
					self.reset_level()
					self.is_code_running = True
					try:
						self.correspondances = submit(self.player, self.editor.user_code, self.dynamic_grid, self.static_grid, self.exit, self.monsters)
					except Exception as e:
						self.editor.error_box(str(e))
						self.is_code_running = False
				
				if self.is_code_running:
					if self.frame_counter % self.turn_frames == 0:
						reset_entities(self.dynamic_grid)
						self.player.hurt = False
						
						if isinstance(self.static_grid[self.player.pos[0]][self.player.pos[1]], Objective):
							self.cur_level += 1
							print(f"Congratulations! Onto level {self.cur_level}!")
							self.reset_level()
							self.is_code_running = False
							
						else:
							codeJoueur(self.player, self.correspondances, self.static_grid)
							
							if self.frame_counter % (3*self.turn_frames) == 0:
								monster_pop(self.dynamic_grid, self.monsters)
								update_monster_positions(self.dynamic_grid, self.static_grid, self.player)
								if self.player.is_dead():
									print("You're dead")
									self.reset_level()
									self.is_code_running = False
					
					if self.player.attacked and self.frame_counter % self.turn_frames <= self.attack_frames/2:
						self.player.artwork = 'robot_attack1'
					elif self.player.hurt and self.frame_counter % self.turn_frames <= self.hurt_frames:
						self.player.artwork = 'robot_hurt'
					elif self.player.attacked and self.frame_counter % self.turn_frames <= self.attack_frames:
						self.player.artwork = 'robot_attack2'
					else:
						self.player.artwork = 'robot'
					
					turn_fraction = (self.frame_counter % self.turn_frames) / self.turn_frames
				else:
					turn_fraction = 0
				
				display_grid(self.static_grid, self.dynamic_grid, self.window, TILE_SIZE, self.images, turn_fraction)
				
			else:
				display_end_screen(self.window, self.images)
			
			pygame.display.flip()
			self.frame_counter += 1
		pygame.quit()
		self.editor.close()


if __name__ == "__main__":
	game = Game()
	game.run()
