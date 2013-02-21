"""
Game Items
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
import sys
from display import DrawingGenerics

class GameItem(object):
	"""
	GameItem class.
	This class contains the methods used in the creation and behaviour of all Game Items.
	It is of the tkinter library and inherits an instance of object.
	"""
	
	def __init__(self, gameCanvas, xL, yT, xR, yB, color, tagType):
		"""
		Initialization.
		This method creates a new Game Item and initializes it.
		
		@param gameCanvas: 
		@param xL: Left X coordinate of the box binding the Game Item.
		@param xR: Right X coordinate of the box binding the Game Item.
		@param yT: Top Y coordinate of the box binding the Game Item.
		@param yB: Bottom Y coordinate of the box binding the Game Item.
		@param color: Color of Game Item.
		@param tagType: tag of the Game Item which will specifiy what item it actually is.
		"""
		# Sets the attributes of the game item.
		self.xLeft = xL
		self.xRight = xR
		self.yTop = yT
		self.yBottom = yB
		self.color = color
		self.tagType = tagType
		self.gameCanvas = gameCanvas
		self.canvasID = None
		
	
	def draw(self):
		"""
		Draw.
		This method draws the Game Item onto the game canvas.
		
		"""
		
		raise NotImplementedError("Draw method not implemented for " + self.tagType)
		
	
	def changeColor(self, color):
		"""
		Change color.
		This method changes the color of the Game Item.
		
		@param color: Color Game Item is to be changed to.
		"""
		# Change the color attribute of the Game Item and reconfigure the Canvas.
		if not self.canvasID is None:
			self.color = color
			self.gameCanvas.itemconfig(self.canvasID, fill = color)
			
		
	def deleteDrawing(self):
		"""
		Delete Drawing.
		This method deletes the Game Item off of the canvas.
		
		"""
		# Deletes from the canvas
		if not self.canvasID is None:
			self.gameCanvas.delete(self.canvasID)
		
	
	def findCurrentOverlappingWith(self, target):
		"""
		Find overlapping with.
		This method checks if the current Game Item is overlapping with the Game Item 
		passed in the parameter.
		
		@param target: Game Item that is checked to be overlapping with this Game Item.
		@return: True - They are overlapping, False - If they are not.
		"""
		if (((self.xLeft <= target.xLeft <= self.xRight
				or self.xLeft <= target.xRight <= self.xRight)
				and (self.yTop <= target.yTop <= self.yBottom
				or self.yTop <= target.yBottom <= self.yBottom))
			or ((target.xLeft <= self.xLeft <= target.xRight
				or target.xLeft <= self.xRight <= target.xRight)
				and (target.yTop <= self.yTop <= target.yBottom
				or target.yTop <= self.yBottom <= target.yBottom))):
			return True
		else:
			return False
	

	def findOverlappingWith(self, xLeft, yTop, xRight, yBottom, target):
		"""
		Find overlapping with.
		This method checks if the current Game Item is overlapping with the Game Item 
		passed in the parameter.
		
		@param xLeft: Left X coordinate of the box binding the Game Item.
		@param xRight: Right X coordinate of the box binding the Game Item.
		@param yTop: Top Y coordinate of the box binding the Game Item.
		@param yBottom: Left X coordinate of the box binding the Game Item.
		@param yBottom: Left X coordinate of the box binding the Game Item.
		@param target: Game Item that is checked to be overlapping with this Game Item.
		@return: True - They are overlapping, False - If they are not.
		"""
		
		# Checks if the items overlap
		if (((xLeft <= target.xLeft <= xRight
				or xLeft <= target.xRight <= xRight)
				and (yTop <= target.yTop <= yBottom
				or yTop <= target.yBottom <= yBottom))
			or ((target.xLeft <= xLeft <= target.xRight
				or target.xLeft <= xRight <= target.xRight)
				and (target.yTop <= yTop <= target.yBottom
				or target.yTop <= yBottom <= target.yBottom))):
			return True
		else:
			return False
			
	
	def getCoord(self):
		"""
		Get Coordinates.
		This method gets the current coordinates of the Game Item.
		
		@return: coordinates of the top left and bottom right corner of the Game Item bounding box.
		"""
		return self.xLeft, self.yTop, self.xRight, self.yBottom
