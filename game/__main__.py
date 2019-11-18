from game.engine import init_grid

GRID_SIZE = 15

class Game:
	def __init__(self):
		self.grid = init_grid(GRID_SIZE)
	
	def run(self):
		print("Hello, world!")


if __name__ == "__main__":
	game = Game()
	game.run()
