"""
Pacman
@author:: Jason Cohen
@author:: Shaun Hamelin-Owens
@author:: Sasithra Thanabalan
@author:: Andrew Walker
"""
# Imports
from Sprite import Sprite
from display import DrawingGenerics

class Pacman(Sprite):
	"""
	Pacman class
	Inherits from the Sprite class. This class initializes and controls all game logic involving the Pacman Sprite.
	It interacts with the Canvas that is responsible for drawing it
	and uses the Gameplay class as a controller to interact with other characters in the game.
	"""

## Init the Pacman instance
	def __init__(self, gameManager, gameCanvas, specs):
		"""
		Initialization.
		Class constructor for the Pacman.
		Sets up the specs for a new game/level.
		
		@param gameManager: The Game object (from org/Pacman.py)
		@param gameCanvas: The game tk canvas object (on which the game is drawn)
		@param specs: The level/map specifications
		"""
		self.state = DrawingGenerics.PACMAN_STATE['Normal']
		super(Pacman, self).__init__(gameCanvas, specs)
		
		self.specs = specs
		
		self.energizeCycles = 0
		self.counter = 0
		
		self.xStart = self.specs['xCenter']
		self.yStart = self.specs['yCenter']
		
		self.halt = 0
		
		self.gameManager = gameManager
		
		self.draw()
		self.bindKeys()
		
		## Desired Direction, used when keypress
		self.desiredDir = ""
		
		self.initGame()


	def draw(self):
		"""
		Draw.
		This method interacts with the Canvas to draw the Pacman character.
		
		"""
		self.canvasID = self.gameCanvas.create_oval(self.xLeft, self.yTop,
				self.xRight, self.yBottom, fill = self.color, tags = self.tagType)

				
	def initGame(self):
		"""
		Initial game settings.
		This method prepares the pacman for the start of a game.
		
		"""
		
		# Pacman starts by moving to the left
		self.left = True           ###
		self.right = False         # Pacman starts the
		self.up = False            # game not moving
		self.down = False          ###
		
		self.currDir = 'left'
		
		
		self.inGame = True         # Pacman is alive at this point

		

	def bindKeys(self):
		"""
		Bind Keys.
		Takes care of binding keyboard keys to the movement method.
		
		"""
		
		self.gameCanvas.bind_all("<Left>", self.movement)    ###
		self.gameCanvas.bind_all("<Right>", self.movement)   # Key bindings
		self.gameCanvas.bind_all("<Up>", self.movement)      #
		self.gameCanvas.bind_all("<Down>", self.movement)    ###
	
	
## Next move (from keypress)
	def movement(self, e):
		"""
		Movement
		Sets pacman's desired direction to the key pressed direction
		
		@param e: Input from keyboard
		"""
		
		key = e.keysym                   # Obtained from key in

		## Direction changes
		if key == "Left":
			self.desiredDir = "left"
		elif key == "Right":
			self.desiredDir = "right"
		elif key == "Up":
			self.desiredDir = "up"
		elif key == "Down":
			self.desiredDir = "down"

	def process(self):
		"""
		Process.
		This method takes care of all the processing for the pacman for the current iteration.
		It takes care of determining the next step based on the current state and desired direciont as well
		as wall avoidance during navigation.
		
		"""
		
		# If time left in energizeCycles, continue to decrement
		if self.energizeCycles > 0:
			self.energizeCycles -= 1
			self.state = DrawingGenerics.PACMAN_STATE['Energized']
			self.speed = self.specs['speed_fright']
		else:
			self.state = DrawingGenerics.PACMAN_STATE['Normal']
			self.speed = self.specs['speed']
		
		# Main processing
		if self.halt > 0:
			self.halt -= 1
		else:
			if not self.movingThroughTunnel():
				if not self.inCentreOfTile():
					if not self.isPastCentreOfTile():
						self.checkReversalOfDirection()
						self.doMove()
					else:
						inTileX, inTileY = self.inTile()
						if self.wallAhead():
							self.correctPosition()
							self.stop()
						else:
							self.checkReversalOfDirection()
							self.doMove()
				else:
					if self.directionChanged():
						self.doMove()
					elif not self.wallAhead():
						self.doMove()
					else:
						self.stop()
				
	def energized(self, energizeCycles):
		"""
		Energized.
		This method sets the pacman to be in energized mode while the ghosts are in fright mode.
		
		@param energizeCycles: The number of iterations that pacman will remain in this state.
		"""
		self.halt = 3
		self.energizeCycles = energizeCycles
		self.state = DrawingGenerics.PACMAN_STATE['Energized']
				
	def setHaltIterations(self, num):
		"""
		Set Halt Iterations.
		This method sets the number of iterations for pacman to halt.
		
		@param num: The number of iterations that pacman will halt.
		"""
		self.halt = num
		
	def checkReversalOfDirection(self):
		"""
		Check Reversal Of Direction.
		Check to see if a reversal of direction is requested.
		
		"""
		
		desiredDir = self.desiredDir
		
		if self.left:
			if desiredDir == "right":
				self.left = False
				self.right = True
				self.up = False
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
		elif self.right:
			if desiredDir == "left":
				self.left = True
				self.right = False
				self.up = False
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
		elif self.up:
			if desiredDir == "down":
				self.left = False
				self.right = False
				self.up = False
				self.down = True
				self.currDir = desiredDir
				self.desiredDir = ""
		elif self.down:
			if desiredDir == "up":
				self.left = False
				self.right = False
				self.up = True
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
	
	def directionChanged(self):
		"""
		Direction Changed.
		Determines if pacman can move in a certain direction.
		
		@return: True - if pacman did change directions. False - if pacman did not.
		"""
		
		desiredDir = self.desiredDir  # Direction obtained from keypress
		
		changeAllowed = True          # Init allowable change in direction 
		
		mapWalls = self.gameManager.getWalls()
		
		## Attempt to turn left
		if desiredDir == "left":
			
			for wall in mapWalls:
				if not changeAllowed:
					break
				if self.findOverlappingWith(self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
					changeAllowed = False
					break
			if changeAllowed:
				self.left = True
				self.right = False
				self.up = False
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
				return True
			else:
				return False

		## Attempt to turn right
		elif desiredDir == "right":
			for wall in mapWalls:
				if not changeAllowed:
					break
				if self.findOverlappingWith(self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
					changeAllowed = False
					break
			if changeAllowed:
				self.left = False
				self.right = True
				self.up = False
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
				return True
			else:
				return False
			
		## Attempt to turn "up"
		elif desiredDir == "up":
			for wall in mapWalls:
				if not changeAllowed:
					break
				if self.findOverlappingWith(self.xLeft,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							wall):
					changeAllowed = False
					break
			if changeAllowed:
				self.left = False
				self.right = False
				self.up = True
				self.down = False
				self.currDir = desiredDir
				self.desiredDir = ""
				return True
			else:
				return False
				
		## Attempt to turn "down"
		elif desiredDir == "down":
			for wall in mapWalls:
				if not changeAllowed:
					break
				if self.findOverlappingWith(self.xLeft,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							wall):
					changeAllowed = False
					break
			if changeAllowed:
				self.left = False
				self.right = False
				self.up = False
				self.down = True
				self.currDir = desiredDir
				self.desiredDir = ""
				return True
			else:
				return False
		else:
			return False
			
	def restart(self):
		"""
		Restart.
		Reset the pacman to its starting settings.
		
		"""
		
		self.initGame()
		
		self.deleteDrawing()
		self.move(self.xStart - self.xCenter, self.yStart - self.yCenter)
		self.draw()
		
		self.energizeCycles = 0
		self.halt = 0
		self.desiredDir = ""
	
	def currDirection(self):
		"""
		Current Direction.
		Gets pacman's current direction value.
		
		@return: currDir: The pacman's direction string.
		"""
		return self.currDir
		
