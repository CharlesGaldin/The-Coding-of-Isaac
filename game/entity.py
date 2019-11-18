class Moving_Entity:
	
	def __init__(self , health , position , artwork):

		self.health = health
		self.pos = position
		self.artwork = artwork
	
	def health_change(self , n):
		"""
		n is an integer
		add n to the health of an entity
		"""
		self.health += n
			

class Player(Moving_Entity):

	def __init__(self , position , health = 10 ):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		Moving_Entity.__init__(self , position , health, "robot")

class Monster(Moving_Entity):
	
	def __init__(self , health , artwork):
		"""
		position de la forme : [pos_y , pos_x]
		"""
		Moving_Entity.__init__(self , health , artwork)

class Unmoving_entity:

	def __init__(self):
		pass

class Obstacle:
	def __init__(self):
		pass