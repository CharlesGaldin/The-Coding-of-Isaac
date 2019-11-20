class Moving_Entity:
	
	def __init__(self , position , health , attack , artwork):

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
		"""
		position de la forme : [pos_y , pos_x]
		"""
		Moving_Entity.__init__(self , position , health , attack , "robot")

class Monster(Moving_Entity):
	
	def __init__(self , position , health , attack , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		Moving_Entity.__init__(self , position ,  health , attack , artwork)

class Unmoving_entity:

	def __init__(self , position):
		self.position = position

class Objective:
    	
	def __init__()

class Obstacle:
	def __init__(self):
		pass