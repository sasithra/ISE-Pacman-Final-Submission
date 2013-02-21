"""
Ghosts
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
import random
import math
from Sprite import Sprite
from maps import Map1
from display import DrawingGenerics
import sys

class Ghost(Sprite):
	"""
	Ghost class
	Inherits from the Sprite class. This class initializes and controls all game logic involving Ghost sprites.
	It interacts with the Canvas that is responsible for drawing each instance of the Ghosts
	and uses the Gameplay class as a controller to interact with other characters in the game.
	"""
	def __init__(self, gameManager, gameCanvas, ID, specs):
		"""
		Initialization
		This method creates a Ghost instance, initializes it and draws it
		
		@param gameCanvas: Reference to the drawing canvas for drawing purposes
		@param specs: Specifies the coordinates, radius, color, tag and speed associated
				with the ghost.
		"""
		# Initialization of the Ghost
		super(Ghost, self).__init__(gameCanvas, specs)
		
		self.gameManager = gameManager
		self.ID = ID
		self.state = DrawingGenerics.GHOST_STATE['Scatter']
		self.stateFlag = self.state
		self.origColor = self.color
		self.frightCycles = 0;
		self.dotLimit = 0
		self.specs = specs
		self.destX = 0
		self.destY = 0
		
		self.xStart = specs['xCenter']
		self.yStart = specs['yCenter']
		
		self.speedNormal = specs['speed']
		self.speedTunnel = specs['speed_tunnel']
		self.speedEaten = specs['speed_eaten']
		self.speedFright = specs['speed_fright']
		
		self.GHOST_START = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
				'yCenter': (14 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING}

		
		self.toggleScatterCycle = 6 * DrawingGenerics.CYCLES_PER_SECOND
		self.toggleChaseCycle = 20 * DrawingGenerics.CYCLES_PER_SECOND
		self.toggleChaseScatter = self.toggleScatterCycle
		
		self.draw()
		self.initGame()
	
	def draw(self):
		"""
		Draw.
		This method interacts with the Canvas to draw the Ghost character.
		
		"""
		self.canvasID = self.gameCanvas.create_rectangle(self.xLeft, self.yTop,
				self.xRight, self.yBottom, fill = self.color, tags = self.tagType)
	
	
	def initGame(self):
		"""
		Initial game settings.
		This method prepares the ghost for the start of a game.
		
		"""
		
		self.started = False
		
		# Ghost starts the game not moving
		self.left = False 
		self.right = False
		self.up = False   
		self.down = False 
		
## If the Pacman is eaten by a ghost, this method resets the ghosts
	def restart(self):
		"""
		Restart.
		Reset the ghost to starting position and conditions.
		
		"""
		
		# Store the dot counter for releasing of the ghost
		self.dotLimit = self.gameManager.getDotsEaten()
		self.stop()
		self.started = False
		
		self.deleteDrawing()
		self.move(self.xStart - self.xCenter, self.yStart - self.yCenter)
		self.draw()
		
		self.scatter()
		self.toggleChaseScatter = self.toggleScatterCycle
		
	def start(self):
		"""
		Start.
		Move the ghost to the starting position outside the ghost enclosure and set it as started.
		
		"""
		self.move(self.GHOST_START['xCenter'] - self.xCenter,
					self.GHOST_START['yCenter'] - self.yCenter)
		self.started_()

## 	
	def started_(self):
		"""
		Started.
		Set ghost initial direction.
		
		"""
		if (self.origColor == 'red'):
			self.left = True
		
		elif (self.origColor == 'cyan'):
			self.right = True
			
		elif (self.origColor == 'pink'):
			self.right = True
		else:
			self.left = True
		self.started = True

## Release the ghost if the number of dots eaten exceeds the minimal amount
	def checkStartingConditions(self):
		"""
		Check Starting Conditions.
		Release the ghost if the number of dots eaten exceeds the minimal amount.
		
		"""
		
		dotsEaten = self.gameManager.getDotsEaten() - self.dotLimit
		
		if self.ID == 1:
			if dotsEaten >= 30:
				self.start()
		elif self.ID == 3:
			if dotsEaten >= 20:
				self.start()
		elif self.ID == 2:
			if dotsEaten >= 10:
				self.start()
		elif self.ID == 4:
			if dotsEaten >= 0:
				self.start()

	def eat(self):
		"""
		Eat.
		This method returns the ghost to the ghost enclosure after being eaten.
		
		@return:: The number of points associated with eating a ghost
		"""
		self.returnToPen()
		return 200
				
	def chase(self):
		"""
		Chase.
		This method set the ghost state to chase and sets the destination tile
		for the ghost.
		
		"""
		self.changeColor(self.origColor)
		self.state = DrawingGenerics.GHOST_STATE['Chase']
		self.stateFlag = self.state
		self.speed = self.speedNormal
		self.destX, self.destY = self.destinationTile()
		self.frightCycles = 0

	def scatter(self):
		"""
		Scatter.
		This method set the ghost state to scatter and sets the destination tile
		for the ghost.
		
		"""
		self.changeColor(self.origColor)
		self.state = DrawingGenerics.GHOST_STATE['Scatter']
		self.stateFlag = self.state
		self.speed = self.speedNormal
		self.destX, self.destY = self.destinationTile()

	def returnToPen(self):
		"""
		Return to Pen.
		This method set the ghost state to eaten and sets the destination tile
		for the ghost.
		
		"""
		self.changeColor("grey")
		self.state = DrawingGenerics.GHOST_STATE['Eaten']
		self.speed = self.speedEaten
		self.destX = 14
		self.destY = 14.5
		
	def fright(self, frightCycles):
		"""
		Fright.
		This method set the ghost state to fright which will last for a limited amount of time.
		
		@param frightCycles: The number of iterations for the ghost to remain in fright mode.
		"""
		self.changeColor(DrawingGenerics.GHOST_FRIGHT_COLOR[1])
		self.state = DrawingGenerics.GHOST_STATE['Fright']
		self.speed = self.speedFright
		self.frightCycles = frightCycles
		self.reverseDirection()
		
	def isInTunnel(self):
		"""
		Is In Tunnel.
		This method determines if the ghost is in the tunnel regions of the map.
		
		@return:: True - If ghost is in the tunnel. False - If ghost is not in the tunnel
		"""
		if (self.yCenter == 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING 
				and (self.xCenter < 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
				or self.xCenter > 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING)):
			return True
		
		return False
			
## When the ghost goes into fright mode, reverse the ghost direction
	def reverseDirection(self):
		"""
		Reverse Direction.
		This method reverses the ghost's current direction.
		
		"""
		if self.left:
			self.left = False
			self.right = True
		elif self.right:
			self.right = False
			self.left = True
		elif self.up:
			self.up = False
			self.down = True
		elif self.down:
			self.down = False
			self.up = True
		else:
			# Currently not moving, do nothing
			pass
	
	def toggleColor(self):
		"""
		Toggle Color.
		This method changes the current ghost color in order to flicker between white and blue
		while in fright mode.
		
		"""
		if self.color == DrawingGenerics.GHOST_FRIGHT_COLOR[1]:
			self.changeColor(DrawingGenerics.GHOST_FRIGHT_COLOR[2])
		else:
			self.changeColor(DrawingGenerics.GHOST_FRIGHT_COLOR[1])

	def toggleState(self):
		"""
		Toggle State.
		This method toggles the Ghost's current state between scatter and chase.
		If the ghost is in neither of these states currently, the stateflag will retain the expected
		state for the ghost so that when it exits its current state it will return to the state
		specified by stateflag instead.
		
		"""
		if self.stateFlag == self.state:
			if self.state == DrawingGenerics.GHOST_STATE['Chase']:
				self.scatter()
				self.reverseDirection()
			elif self.state == DrawingGenerics.GHOST_STATE['Scatter']:
				self.chase()
				self.reverseDirection()
		elif self.stateFlag == DrawingGenerics.GHOST_STATE['Chase']:
			self.stateFlag = DrawingGenerics.GHOST_STATE['Scatter']
		elif self.stateFlag == DrawingGenerics.GHOST_STATE['Scatter']:
			self.stateFlag = DrawingGenerics.GHOST_STATE['Chase']
		
	def returnToNormalState(self):
		"""
		Return to Normal State.
		This method sets the Ghost's current to the one specified by stateflag.
		
		"""
		if self.stateFlag == DrawingGenerics.GHOST_STATE['Scatter']:
			self.scatter()
		elif self.stateFlag == DrawingGenerics.GHOST_STATE['Chase']:
			self.chase()
		
## One iteration for the next ghost move				
	def process(self):
		"""
		Process.
		This method takes care of all the processing for the ghost for the current iteration.
		It takes care of determining the next step based on the current state as well
		as wall avoidance during navigation.
		
		"""
		
		# Toggle the current state if the countdown has expired
		if self.toggleChaseScatter > 0:
			self.toggleChaseScatter -= 1
		else:
			self.toggleState()
			if self.stateFlag == DrawingGenerics.GHOST_STATE['Scatter']:
				self.toggleChaseScatter = self.toggleScatterCycle
			elif self.stateFlag == DrawingGenerics.GHOST_STATE['Chase']:
				self.toggleChaseScatter = self.toggleChaseCycle
		
		# Call the appropriate method for the current state to determine
		# the destination tile
		if self.state == DrawingGenerics.GHOST_STATE['Chase']:
			self.chase()
		elif self.state == DrawingGenerics.GHOST_STATE['Scatter']:
			self.scatter()
		elif self.state == DrawingGenerics.GHOST_STATE['Fright']:
			# Check fright countdown
			if self.frightCycles > 0:
				# Toggle between white and blue at appropriate time
				if self.frightCycles <= 2 * DrawingGenerics.CYCLES_PER_SECOND:
					if self.frightCycles % (DrawingGenerics.CYCLES_PER_SECOND / 4) == 0:
						self.toggleColor()
				self.frightCycles -= 1
			else:
				self.reverseDirection()
				self.returnToNormalState()

		else:
			self.returnToPen()
			# Check if at the starting position
			if (abs(self.xCenter - (self.destX * DrawingGenerics.TILE_SIZE)) < 1 and
					abs(self.yCenter - (self.destY * DrawingGenerics.TILE_SIZE)) < 1): # CHANGED SINCE DEMO
				self.returnToNormalState()
			
		# If ghost is in a tunnel and not in eaten state, tunnel_speed is applied
		if self.isInTunnel() and self.state != DrawingGenerics.GHOST_STATE['Eaten']:
			self.speed  = self.speedTunnel
		
		# Main processing
		if not self.started:
			self.checkStartingConditions()
		else:
			# Moving through a tunnel overides all other operations
			if not self.movingThroughTunnel():
				if not self.inCentreOfTile():
					if self.isPastCentreOfTile() and self.wallAhead():
						self.correctPosition()
						self.setNextDirection()
						self.doMove()
					else:
						self.doMove()
				else:
					self.setNextDirection()
					self.doMove()
		

## Sets the destination of each ghost based on which state it is in
## If chase, follow their specific chase algorithms
## If scatter, send them to their respective corners	
	def destinationTile(self):
		"""
		Destination Tile.
		This method determines the destination tile for the ghost based on its current state.
		
		"""
		self.pacman = self.gameManager.getPacman()
		destXCenter, destYCenter = self.pacman.inTile()

		if(self.state == DrawingGenerics.GHOST_STATE['Chase']):
			if(self.origColor == 'red'):
				# Red's destination is pacman's current tile
				pass
				
			elif(self.origColor == 'pink'):
				# Pink's destination is 4 tiles ahead of pacman
				pacDir = self.pacman.currDirection()
				if(pacDir == 'left'):
					destXCenter = destXCenter - 4
				if(pacDir == 'right'):
					destXCenter = destXCenter + 4
				if(pacDir == 'up'):
					# Overflow issue when pacman is in the upwards direction
					destXCenter = destXCenter - 4
					destYCenter = destYCenter - 4
				if(pacDir == 'down'):
					destYCenter = destYCenter + 4
						
			elif(self.origColor == 'orange'):
				# Orange's destination is pacman's tile if its distance exceeds 8 tiles
				currX, currY = self.inTile()
				distance = self.distance(destXCenter, destYCenter, currX, currY)
				
				upperBound = math.sqrt(math.pow(8,2) + math.pow(8,2))
							
				if (distance <= upperBound):
					destXCenter = 0.5
					destYCenter = 34.5
					
					
			else: #(self.color == 'cyan'):
				# Cyan's destination is a combination of pacman's and red's current tile
				pacDir = self.pacman.currDirection()
				destXCenter, destYCenter = self.pacman.inTile()
				
				if(pacDir == 'left'):
					destXCenter = destXCenter - 2
				if(pacDir == 'right'):
					destXCenter = destXCenter + 2
				if(pacDir == 'up'):
					destXCenter = destXCenter - 2
					destYCenter = destYCenter - 2
				if(pacDir == 'down'):
					destYCenter = destYCenter + 2
				
				# Get the red ghost's tile coordinates
				redXCenter, redYCenter = self.gameManager.getGhosts()[3].inTile()
				
				destXCenter = redXCenter + 2 * (destXCenter - redXCenter)
				destYCenter = redYCenter + 2 * (destYCenter - redYCenter)
			
		# Go to the ghost's corner
		elif(self.state == DrawingGenerics.GHOST_STATE['Scatter']):
			if(self.origColor == 'red'):
				destXCenter = 25.5
				destYCenter = 0.5
			
			elif(self.origColor == 'pink'):
				destXCenter = 2.5
				destYCenter = 0.5
			
			elif(self.origColor == 'orange'):
				destXCenter = 0.5
				destYCenter = 34.5
				
			else:
				destXCenter = 27.5
				destYCenter = 34.5
		
		# Go to the starting location outside the ghost enclosure
		elif(self.state == DrawingGenerics.GHOST_STATE['Eaten']):
			
			destXCenter = 14
			destYCenter = 14.5
				
		return destXCenter,destYCenter					

		
## Sets the next direction the ghost can and will travel to
	def setNextDirection(self):
		"""
		Set Next Direction.
		This method determines and set the next direction for the ghost based on its available moves
		from its current tile.
		
		"""
		dirDict = { 'left': 1, 'right': 2, 'up': 3, 'down': 4 }
		
		mapWalls = self.gameManager.getWalls()
		destX = self.destX
		destY = self.destY
		
		for wall in mapWalls:
			# Check left for a wall
			if self.findOverlappingWith(self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter - DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
				if dirDict.has_key('left'):
					del dirDict['left']
			# Check right for a wall
			if self.findOverlappingWith(self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yTop,
							self.xCenter + DrawingGenerics.TILE_SIZE,
							self.yBottom,
							wall):
				if dirDict.has_key('right'):
					del dirDict['right']
			# Check up for a wall
			if self.findOverlappingWith(self.xLeft,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter - DrawingGenerics.TILE_SIZE,
							wall):
				if dirDict.has_key('up'):
					del dirDict['up']
			# Check down for a wall
			if self.findOverlappingWith(self.xLeft,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							self.xRight,
							self.yCenter + DrawingGenerics.TILE_SIZE,
							wall):
				if dirDict.has_key('down'):
					del dirDict['down']
					
		# Eliminate the reverse direction
		if self.left:
			if dirDict.has_key('right'):
				del dirDict['right']
				
		if self.right:
			if dirDict.has_key('left'):
				del dirDict['left']
		
		if self.up:
			if dirDict.has_key('down'):
				del dirDict['down']
		
		if self.down:
			if dirDict.has_key('up'):
				del dirDict['up']
	
		nextDir = 1
		nextDirection = 'down'
		if (len(dirDict) > 0):
			# Get shortest distance from available moves to the destination
			if not (self.state == DrawingGenerics.GHOST_STATE['Fright']):
				nextDirection = self.shortestDistance(dirDict, destX, destY)
			else:
				# Randomly choose direction
				nextDir = random.randint(1, len(dirDict))
				nextDirection = dirDict.keys()[nextDir-1]
		
		if (nextDirection == 'left'):
			self.left = True
			self.right = False
			self.up = False
			self.down = False
			
		elif (nextDirection == 'right'):
			self.left = False
			self.right = True
			self.up = False
			self.down = False
			
		elif (nextDirection == 'up'):
			self.left = False
			self.right = False
			self.up = True
			self.down = False
		
		else:
			self.left = False
			self.right = False
			self.up = False
			self.down = True
			
## Finding the shortest distance from tiles surrounding the ghost to the destination.
## Next move of the ghost is determined by which direction it still can travel to 
## (no walls/obstructions)	and if that is closest to the destination tile (shortest vector)
## Returns the next direction the ghost should travel based on this.
	def shortestDistance(self, dirDict, destX, destY):
		"""
		Shortest Distance.
		This method determines the shortest distance to the destination based on the available directions.
		
		@param dirDict: The dicitonary containing the available directions.
		@param destX: They x-coordinate for the destination tile.
		@param destY: They y-coordinate for the destination tile.
		@return: nextDir: The direction that results in the shortest distance.
		"""
		xCenter, yCenter = self.inTile()
		
		distance = sys.maxint
		nextTile = DrawingGenerics.TILE_SIZE
		
		#nextDir = 'left'
				
		if(dirDict.has_key('up')):
			distU = self.distance(xCenter, yCenter - 1, destX, destY)
				
			if(distU < distance):
				distance = distU
				nextDir = 'up'
		
		if(dirDict.has_key('left')):
			distL = self.distance(xCenter - 1, yCenter, destX, destY)
				
			if(distL < distance):
				distance = distL
				nextDir = 'left'		
			
		if(dirDict.has_key('down')):
			distD = self.distance(xCenter , yCenter + 1, destX, destY)
					
			if(distD < distance):
				distance = distD
				nextDir = 'down'
		
		if(dirDict.has_key('right')):
			distR = self.distance(xCenter + 1, yCenter, destX, destY)	
				
			if(distR < distance):
				distance = distR
				nextDir = 'right'
		
		return nextDir
				
			
## Helper method to find the distance between center two points			
	def distance(self, x1, y1, x2, y2):
		"""
		Distance.
		This method calculates the distance between two points.
		
		@param x1: They x-coordinate for the first point.
		@param y1: They y-coordinate for the first point.
		@param x2: They x-coordinate for the second point.
		@param y2: They y-coordinate for the second point.
		@return: distance: the euclidean distance between the two points.
		"""
		return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	
	
