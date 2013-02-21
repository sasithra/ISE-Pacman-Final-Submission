"""
Sprites
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from GameItem import GameItem
from display import DrawingGenerics

class Sprite(GameItem):
	"""
	Sprite class.
	This class contains the methods used in the creation and behaviour of all the Sprite
	items in this game.
	It is of the tkinter library and inherits an instance of GameItem.
	"""
	def __init__(self, gameCanvas, specs):
		"""
		Initialization.
		This method creates a new Sprite item and initializes it.
		
		@param gameCanvas: 
		@param specs: Specifies the attributes of this particular Sprite.
		"""
		# Attributes of the Sprite.
		self.xCenter = specs['xCenter']
		self.yCenter = specs['yCenter']
		self.radius = specs['radius']
		self.speed = specs['speed']
		
		# Initialization
		super(Sprite, self).__init__(gameCanvas,
				self.xCenter - self.radius,
				self.yCenter - self.radius,
				self.xCenter + self.radius,
				self.yCenter + self.radius,
				specs['color'],
				specs['tag'])
	
	
	def draw(self):
		"""
		Draw.
		This method draws the Sprite item.
		
		"""
		
		raise NotImplementedError("Draw method not implemented for " + self.tagType)

		
	def eat(self):
		"""
		Eat.
		This method is used when a Sprite is to eat a different Item.
		
		"""
		
		raise NotImplementedError("Eat method not implemented for " + self.tagType)
		
		
## Next move (on current game iteration)
	def doMove(self):
		"""
		Do Move.
		This method moves the Sprite.
		
		"""
		
		## Sprite is redrawn at the appropriate deltax
		## and his coordinates are updated
		if self.left:
			self.move(-self.speed, 0)
		elif self.right:
			self.move(self.speed, 0)
		elif self.up:
			self.move(0, -self.speed)
		elif self.down:
			self.move(0, self.speed)

			
## Update Sprite's border coordinates as well as center coordinates
## and display the updated position
	def move(self, xRelative, yRelative):
		"""
		Move.
		This method updates Sprite's border coordinates as well as center coordinates 
		and display the updated position.
		
		@param xRelative: The distance that the Sprite has travelled in the X direction.
		@param yRelative: The distance that the Sprite has travelled in the Y direction.
		"""
		
		# Calculates new coordinates for the top left corner and bottom right corner of the Sprite's bounding box.
		self.xLeft = self.xLeft + xRelative
		self.xRight = self.xRight + xRelative
		self.yTop = self.yTop + yRelative
		self.yBottom = self.yBottom + yRelative
		
		# stores the previous centers for future calculations.
		prevXCenter = self.xCenter
		prevYCenter = self.yCenter
		
		# Finds the new distance from the previous centers of the Sprite.
		self.xCenter += xRelative
		self.yCenter += yRelative
		
		# Correct the Sprite's horizontal position if it is within a threshold of the tile center
		if (abs((self.xCenter % DrawingGenerics.TILE_SIZE) - DrawingGenerics.TILE_CENTERING) < 1):
			self.xCenter = (int(self.xCenter / DrawingGenerics.TILE_SIZE) * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
			self.xLeft = self.xCenter - self.radius
			self.xRight = self.xCenter + self.radius
		# Correct the Sprite's vertical position if it is within a threshold of the tile center
		if (abs((self.yCenter % DrawingGenerics.TILE_SIZE) - DrawingGenerics.TILE_CENTERING) < 1):
			self.yCenter = (int(self.yCenter / DrawingGenerics.TILE_SIZE) * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
			self.yTop = self.yCenter - self.radius
			self.yBottom = self.yCenter + self.radius
		
		# Move the Sprite in the game canvas
		self.gameCanvas.move(self.canvasID, self.xCenter - prevXCenter, self.yCenter - prevYCenter)
		
		
## Stop all of the Sprite's movement directions
	def stop(self):		
		"""
		Stop.
		This method stops all of the Sprite's movement directions.
		
		"""
		# Set all directions to false.
		self.left = False
		self.right = False
		self.up = False
		self.down = False
	
	
## If Sprite is entering a tunnel, move it to through to the opposite side
	def movingThroughTunnel(self):
		"""
		Moving through the Tunnel.
		This method is used to move the Sprite to the opposite end of the Map if it is 
		calculated to be moving through the tunnel.
		
		"""
		
		## Check if going through left side tunnel, move to entrance of right
		if self.xCenter < 0 and self.left:
			self.move(DrawingGenerics.MAP_WIDTH, 0)
			return True
		## Check if going through right tunnel, move to entrance of left
		elif self.xCenter > DrawingGenerics.MAP_WIDTH and self.right:
			self.move(-DrawingGenerics.MAP_WIDTH, 0)
			return True
		else:
			return False
	
	def isPastCentreOfTile(self):
		"""
		Is past center.
		This method checks if the Sprite is currently ahead the center of a tile or behind the center 
		of a tile.
		
		"""
		
		# Takes the current tile that the Sprite is located in.
		inTileX, inTileY = self.inTile()
		
		# If the Sprite is travelling to the left, find out if its past center of its current tile.
		if self.left:
			if self.xCenter - (inTileX * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING) < 0:
				return True
			else:
				return False
				
		# If the Sprite is travelling to the right, find out if its past center of its current tile.
		elif self.right: 
			if self.xCenter - (inTileX * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING) > 0:
				return True
			else:
				return False

		# If the Sprite is travelling to the up, find out if its past center of its current tile.
		elif self.up: 
			if self.yCenter - (inTileY * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING) < 0:
				return True
			else:
				return False
				
		# If the Sprite is travelling to the down, find out if its past center of its current tile.
		elif self.down: 
			if self.yCenter - (inTileY * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING) > 0:
				return True
			else:
				return False
		
		else: 
			return False
	
	def correctPosition(self):
		"""
		Correct positioning.
		This method moves the Sprite to the center of it's current tile to overcome fractional distances.
		
		"""
		inTileX, inTileY = self.inTile()
		
		self.move(inTileX * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING - self.xCenter, 
					inTileY * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING - self.yCenter)
	
	def inTile(self):
		"""
		In Tile.
		This method returns the tile that the Sprite is currently in.
		
		@return: X tile and Y tile that the Sprite is currently in.
		"""
		xTile = int(self.xCenter / DrawingGenerics.TILE_SIZE)
		yTile = int(self.yCenter / DrawingGenerics.TILE_SIZE)
		return xTile, yTile
	
	
	def inCentreOfTile(self):
		"""
		In Center of Tile.
		This method checks if the Sprite is in the center of the tile it is currently at.
		
		@return: True - If Sprite is in the center of tile, False - If Sprite is not in the center of the tile
		"""
		if ((self.xCenter % DrawingGenerics.TILE_SIZE == DrawingGenerics.TILE_CENTERING)
				and (self.yCenter % DrawingGenerics.TILE_SIZE == DrawingGenerics.TILE_CENTERING)):
			return True
		else:
			return False
			
			
## Look for wall collisions head on, turning collisions are taken care
## of in the changeDirection method
	def wallAhead(self):
		"""
		Wall Ahead
		This method checks one tile ahead of the current sprite to see if there is a wall barrier
		
		@return: True - If a wall one tile ahead of Sprite, False - If no wall one tile ahead of Sprite
		"""
		
		mapWalls = self.gameManager.getWalls()
		
		## Check to the left
		if self.left:
			for wall in mapWalls:
				if self.findOverlappingWith(self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
					return True

		## Check to the right
		elif self.right:
			for wall in mapWalls:
				if self.findOverlappingWith(self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
					return True
						
		## Check above
		elif self.up:
			for wall in mapWalls:
				if self.findOverlappingWith(self.xLeft,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							wall):
					return True
					
		## Check below
		elif self.down:
			for wall in mapWalls:
				if self.findOverlappingWith(self.xLeft,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							wall):
					return True
		## Currently not moving, movement ahead not authorized
		else:
			return True
		
		# If this point is reached, the Sprite has a direction and no wall
		# was detected straight ahead of it
		return False	
			
