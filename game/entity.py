class Moving_Entity:
    
	def __init__(self , health ):
		self.health = health
		#self.artwork = artwork
	
	def health_change(self , n):
    	# n is an integer
		# add n to the health of an entity
		self.health += n

class Player(Moving_Entity):

	def __init__(self , health):
		Moving_Entity.__init__(self , health )

class Monster(Moving_Entity):

	def __init__(self):
		pass

class Unmoving_entity:

	def __init__(self):
		pass


unit = Player(10)
unit.health_change(2)
print(unit.health)