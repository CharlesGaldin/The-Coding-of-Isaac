from game.engine import init_grid, monster_pop, update_monster_positions, move_entity, player_placement
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
pop = False

# Resets flags on entities at beginning of turns
def reset_entities(dynamic_grid):
	for row in dynamic_grid:
		for cell in row:
			if cell != None:
				cell.moved = False
				cell.attacked = False
				cell.last_movement = None

# Contains the entire state for the game
class Game:
	def __init__(self):
		# Loads level 1 from levels.py
		self.cur_level = 1
		self.reset_level()
		
		# Loads Tkinter code from editor.py
		self.editor = EditorSetUp()
		
		# Creates a Tkinter frame to run Pygame in
		win_w, win_h = get_window_size(self.static_grid, TILE_SIZE)
		self.pygame_frame = tk.Frame(self.editor.master, width = win_w, height = win_h)
		self.pygame_frame.pack(side = tk.LEFT)
		
		# Starts Pygame using graphics.py
		os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())
		if platform.system == "Windows":
			os.environ['SDL_VIDEODRIVER'] = 'windib'
		self.window = create_window(self.static_grid, TILE_SIZE)
		
		# Loads assets
		pygame.init()
		self.images = load_images()
		load_font()
		
		# Initializes data for running user code
		self.correspondances = None
		self.is_code_running = False
		
		# Animation duration constants
		self.turn_frames = 3
		self.hurt_frames = 1
		self.attack_frames = 1
		
	
	# Resets level based on self.cur_level, using levels.py
	def reset_level(self):
		if self.cur_level > LAST_LEVEL: return # We're on the end screen
		self.monsters=[]
		self.static_grid, self.dynamic_grid, self.exit, player_pos= level_grid(self.cur_level, self.monsters)
		self.player = player_placement(self.dynamic_grid, player_pos[0], player_pos[1])
		self.frame_counter = 0
	
	# Main game loop
	def run(self):
		running = True
		while running:
			pygame.time.Clock().tick(60) # Run at 60 FPS
			
			# Update GUI
			self.editor.update()
			if self.editor.exit_requested:
				running = False
			
			# If we're playing a level
			if self.cur_level <= LAST_LEVEL:
				# If we just submitted a new user code
				if self.editor.is_submitted:
					self.editor.is_submitted = False
					self.reset_level()
					self.is_code_running = True
					try:
						self.correspondances = submit(self.player, self.editor.user_code, self.dynamic_grid, self.static_grid, self.exit, self.monsters)
					except Exception as e:
						# Display the error
						self.editor.error_box(str(e))
						self.is_code_running = False
				
				# If the user's code is currently running
				if self.is_code_running:
					# If we're at the beginning of a turn:
					if self.frame_counter % self.turn_frames == 0:
						# Reset entity flags
						reset_entities(self.dynamic_grid)
						self.player.hurt = False
						
						# If we reached the objective
						if isinstance(self.static_grid[self.player.pos[0]][self.player.pos[1]], Objective):
							self.cur_level += 1
							print(f"Congratulations! Onto level {self.cur_level}!")
							self.reset_level()
							self.is_code_running = False
							
						else:
							# Run the user's code
							try:
								codeJoueur(self.player, self.correspondances, self.static_grid)
							except Exception as e:
								self.editor.error_box(str(e))
								self.is_code_running = False
							
							# Every three turns, update monsters
							if self.frame_counter % (3*self.turn_frames) == 0:
								monster_pop(self.dynamic_grid, self.monsters, pop)
								update_monster_positions(self.dynamic_grid, self.static_grid, self.player)
								if self.player.is_dead():
									print("You're dead")
									self.reset_level()
									self.is_code_running = False
					
					# Select correct artwork for player
					if self.player.attacked and self.frame_counter % self.turn_frames <= self.attack_frames/2:
						self.player.artwork = 'robot_attack1'
					elif self.player.hurt and self.frame_counter % self.turn_frames <= self.hurt_frames:
						self.player.artwork = 'robot_hurt'
					elif self.player.attacked and self.frame_counter % self.turn_frames <= self.attack_frames:
						self.player.artwork = 'robot_attack2'
					else:
						self.player.artwork = 'robot'
					
					# A real between 0 and 1 describing the fraction of a turn that has elapsed
					turn_fraction = (self.frame_counter % self.turn_frames) / self.turn_frames
				else:
					turn_fraction = 0
				
				# Display the game grid
				display_grid(self.static_grid, self.dynamic_grid, self.window, TILE_SIZE, self.images, turn_fraction, self.player.health)
				
			else: # We're on the end screen
				display_end_screen(self.window, self.images)
			
			pygame.display.flip()
			self.frame_counter += 1
		pygame.quit()
		self.editor.close()


# Start game
if __name__ == "__main__":
	game = Game()
	game.run()
