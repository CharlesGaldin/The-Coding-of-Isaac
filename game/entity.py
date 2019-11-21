import game.engine
import random

class Entity:
	def __init__(self, position, artwork, tall_artwork = False):
		self.pos = position
		self.artwork = artwork
		self.tall_artwork = tall_artwork

class Moving_Entity(Entity):
	
	def __init__(self , position , health , attack , fire_range , artwork , tall_artwork = False):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		super().__init__(position, artwork, tall_artwork)
		self.health = health
		self.moved = True
		self.attaked = True
		self.attack = attack
		self.range = fire_range
	
	def health_change(self , n):
		"""
		n is an integer
		add n to the health of an entity
		"""
		self.health += n	

class Player(Moving_Entity):

	def __init__(self , position , health = 10 , attack = 2 , fire_range = 5):
		super().__init__(position , health , attack , fire_range , "robot", tall_artwork = True)

	def is_dead(self):
		return self.health <= 0

class Monster(Moving_Entity):
    
	def __init__(self , position , health , attack , artwork , fire_range = 1 ):
		super().__init__(position ,  health , attack , fire_range , artwork )
		
	def kill(self, monstersList, dynamic_grid):
		i = 0
		while i < len(monstersList):
			if monstersList[i] == self:
				monstersList.pop(i)
				break
			i += 1
		dynamic_grid[self.pos[0]][self.pos[1]] = None

	def move_towards_player(self,x_player,y_player,dynamic_grid,static_grid):
		if random.random() > 1/2:
			if self.pos[1] < x_player:
				game.engine.move_entity(self,'right',dynamic_grid,static_grid)
			elif self.pos[1] > x_player:
				game.engine.move_entity(self,'left',dynamic_grid,static_grid)
		else:
			if self.pos[0] > y_player:
				game.engine.move_entity(self,'up',dynamic_grid,static_grid)
			elif self.pos[0] < y_player:
				game.engine.move_entity(self,'down',dynamic_grid,static_grid)

	def attack_player(self,player):
		if (self.pos[0] == player.pos[0] and abs(self.pos[1]-player.pos[1]) == 1) or (self.pos[1] == player.pos[1] and abs(self.pos[0]-player.pos[0])==1):
			player.health-=self.attack
			print("Vie :",player.health)
    	
	
	
    	

class Unmoving_Entity(Entity):
	def __init__(self , position , artwork, tall_artwork = False):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		super().__init__(position, artwork, tall_artwork)

class Objective(Unmoving_Entity):

	def __init__(self , position , artwork):
		super().__init__(position , artwork, tall_artwork = True)

class Obstacle(Unmoving_Entity):
	instances_Obstacle = []

	def __init__(self  , position , artwork):
		super().__init__(position , artwork)
