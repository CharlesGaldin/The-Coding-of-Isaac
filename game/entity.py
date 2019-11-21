import game.engine as ge

class Moving_Entity:
	
	def __init__(self , position , health , attack , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		self.health = health
		self.pos = position
		self.artwork = artwork
		self.moved = True
		self.attack = attack
	
	def health_change(self , n):
		"""
		n is an integer
		add n to the health of an entity
		"""
		self.health += n

	def attack_enemy(self , target):
		health_change(target , -self.attack)		

class Player(Moving_Entity):

	def __init__(self , position , health = 10 , attack = 2 ):
		Moving_Entity.__init__(self , position , health , attack , "robot")

class Monster(Moving_Entity):
	
	def __init__(self , position , health , attack , artwork):
		Moving_Entity.__init__(self , position ,  health , attack , artwork)

	def move_towards_player(self,x_player,y_player,dynamic_grid):
		if self.pos[1] < x_player:
			ge.move_entity(self,'right',dynamic_grid)
			print("monster moved right")
		elif self.pos[1] > x_player:
			ge.move_entity(self,'left',dynamic_grid)
			print("monster moved left")
		if self.pos[0] > y_player:
			ge.move_entity(self,'up',dynamic_grid)
			print("monster moved up")
		elif self.pos[0] < y_player:
			ge.move_entity(self,'down',dynamic_grid)
			print("monster moved down")
    			

class Unmoving_Entity:

	def __init__(self , position , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		self.position = position
		self.artwork = artwork

class Objective(Unmoving_Entity):
    		
	def __init__(self , position , artwork):
		Unmoving_Entity.__init__(self , position , artwork)

class Obstacle(Unmoving_Entity):
	def __init__(self  , position , artwork):
		Unmoving_Entity.__init__(self , position , artwork)