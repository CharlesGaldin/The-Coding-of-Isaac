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

class Monster(Moving_Entity):
	
	def __init__(self , position , health , attack , artwork , fire_range = 1 ):
		super().__init__(position ,  health , attack , fire_range , artwork )

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
	def __init__(self  , position , artwork):
		super().__init__(position , artwork)