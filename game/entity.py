class Moving_Entity:
    
	def __init__(self , health , artwork):
		self.health = health
		#self.artwork = artwork
	
	def health_change(self , n):
    	# n is an integer
		# add n to the health of an entity
		self.health += n
		
class Player(Moving_Entity):

	def __init__(self , health):
		Moving_Entity.__init__(self , health , "assets/robot.png")

class Monster(Moving_Entity):

	def __init__(self , health , artwork):
		Moving_Entity.__init__(self , health , artwork)

class Unmoving_entity:

	def __init__(self):
		pass

class Obstacle:
    	def __init__(self):
			pass