"""
Point items.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from GameItem import GameItem
from display import DrawingGenerics

class PointItem(GameItem):
	"""
	PointItem class.
	This class contains the methods used in the creation of any point item.
	It is of the tkinter library and inherits an instance of GameItem.
	"""
	def __init__(self, gameCanvas, specs, points):
		"""
		Initialization.
		This method creates a new Point item with xCenter, yCenter and radius attributes, 
		and initializes it.
		
		@param gameCanvas: The game tk canvas object (on which the game is drawn)
		@param specs: Specifies the coordinates, radius, color, tag and points associated
					  with this dot.
		@param points: Amount of points assigned to this instance.
		"""
		# Declare the attributes of the point.
		self.points = points
		self.xCenter = specs['xCenter']
		self.yCenter = specs['yCenter']
		radius = specs['radius']
		
		# Initialize this instance of the point class.
		super(PointItem, self).__init__(gameCanvas,
				self.xCenter - radius,
				self.yCenter - radius,
				self.xCenter + radius,
				self.yCenter + radius,
				specs['color'],
				specs['tag'])
		
		
	def setPoints(self, points):
		"""
		Set Points.
		Takes points values and assigns the points attribute of this instance to it.
		
		@param points: Int value of the points to be assigned to this point item. 
		"""
		self.points = points;
	
	
	def getPoints(self):
		"""
		Get Points.
		Returns the points attributed to this particular instance of a point item.
		
		@return: points assigned to this item.
		"""
		return self.points;
	
	
	def draw(self):
		"""
		Draw.
		Draws the point on the tkinter Canvas of the game.
		
		"""
		self.canvasID = self.gameCanvas.create_oval(self.xLeft, self.yTop,
				self.xRight, self.yBottom, fill = self.color, tags = self.tagType)
				
	
	def eat(self):
		"""
		Eat.
		Deletes the drawing of this particular point item from the tkinter Canvas and 
		returns the most recent points values.
		
		@return: points assigned to this item.
		"""
		self.deleteDrawing()
		return self.points
	
	
	def inTile(self):
		"""
		In Tile.
		Takes the top left coordinates and top right coordinates of the item, finds its
		center, and returns the tile in which that center is located in.
		
		@return: points assigned to this item.
		"""
		xTile = int(self.xCenter / DrawingGenerics.TILE_SIZE)
		yTile = int(self.yCenter / DrawingGenerics.TILE_SIZE)
		return xTile, yTile
