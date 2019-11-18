class Entity:

	def __init__(self , position , health):
		self.position = position
		self.health = health

class Player(Entity):

	def __init__(self):
		pass

class Monster(Entity):

	def __init__(self):
		pass
