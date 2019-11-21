class Moving_Entity:
	
	def __init__(self , position , health , attack , fire_range , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		self.health = health
		self.pos = position
		self.artwork = artwork
		self.moved = True
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
		Moving_Entity.__init__(self , position , health , attack , fire_range , "robot")

class Monster(Moving_Entity):
	instances_Monster = []

	def __init__(self , position , health , attack , artwork , fire_range = 1 ):
		Moving_Entity.__init__(self , position ,  health , attack , fire_range , artwork )
		self.instances_monster.append(self)
	
	def __del__(self):
	  	self.instances.remove(self)

class Unmoving_Entity:

	def __init__(self , position , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		self.pos = position
		self.artwork = artwork

class Objective(Unmoving_Entity):
	instances_Objective = []

	def __init__(self , position , artwork):
		Unmoving_Entity.__init__(self , position , artwork)
		self.instances_objective.append(self)

class Obstacle(Unmoving_Entity):
	instances_Obstacle = []

	def __init__(self  , position , artwork):
		Unmoving_Entity.__init__(self , position , artwork)
		self.instances_objective.append(self)