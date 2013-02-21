"""
Walls
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from GameItem import GameItem
from display import DrawingGenerics

class Wall(GameItem):
	"""
	GameItem class.
	This class contains the methods used in the creation and behaviour of all Game Items.
	It is of the tkinter library and inherits an instance of object.
	"""
	def __init__(self, gameCanvas, specs):
		"""
		Initialization.
		This method creates a new Game Item, initializes it and draws it.
		
		@param gameCanvas: 
		@param specs: Attributes associated with the Wall item.
		"""
		
		# Initializes this Wall instance with the atributes passed in.
		super(Wall, self).__init__(gameCanvas,
				specs['xLeft'],
				specs['yTop'],
				specs['xRight'],
				specs['yBottom'],
				specs['color'],
				specs['tag'])
		
		# draws it.
		self.draw()
	
	def draw(self):
		"""
		Draw.
		This method draws the walls of the Map.
		
		"""
		# IF a wall is tagged as a wall, it is drawn onto the map. Ghost enclosure drawn as well.
		if self.tagType == DrawingGenerics.TAG_WALL:
			if (not self.color is None): # Standard game wall
				self.canvasID = self.gameCanvas.create_rectangle(self.xLeft, self.yTop,
						self.xRight, self.yBottom, outline = self.color, tags = self.tagType)
			else: # Invisible wall barrier over ghost enclosure door
				self.canvasID = self.gameCanvas.create_rectangle(self.xLeft, self.yTop,
						self.xRight, self.yBottom, tags = self.tagType)
		else: # Ghost enclosure door
			self.canvasID = self.gameCanvas.create_rectangle(self.xLeft, self.yTop,
					self.xRight, self.yBottom, fill = self.color, tags = self.tagType)
