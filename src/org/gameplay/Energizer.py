"""
Energizers.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from PointItem import PointItem
from display import DrawingGenerics

# Constants
ENERGIZER_POINTS = 50
TOGGLE_TIME = DrawingGenerics.CYCLES_PER_SECOND / 8

class Energizer(PointItem):
	"""
	Energizer class.
	This class contains the methods used in the creation and behaviour of Energizers.
	It is of the tkinter library and inherits an instance of PointItem.
	"""
	def __init__(self, gameCanvas, specs):
		"""
		Initialization.
		This method creates a new Energizer item, draws it and initializes it.
		
		@param gameCanvas: 
		@param specs: Specifies the attributes of this particular Sprite.
		"""
		# Initialize Energizer
		super(Energizer, self).__init__(gameCanvas, specs, specs['points'])
		
		# Draw and set the time between each color toggle (blinking speed energizer)
		self.draw()
		self.colorToggleTime = TOGGLE_TIME

	#------------------------------------------------------------------------------
	# Helper Method: Determines the process that each energizer goes through 
	# continuously during gameplay.
	#------------------------------------------------------------------------------
	def process(self):
		
		# Determines when to toggle the color from white to black (or vice versa)
		if self.colorToggleTime == 0:
			self.colorToggleTime = TOGGLE_TIME
			self.toggleColor()
		else:
			self.colorToggleTime -= 1
			
	def toggleColor(self):
		"""
		toggleColor.
		This method toggles the color from blue to white (or vice versa) of the Energizer.
		
		"""
		
		# Toggles the color of the Energizer to make it blink during gameplay.
		if self.color == DrawingGenerics.ENERGIZER_COLOR[1]:
			self.changeColor(DrawingGenerics.ENERGIZER_COLOR[2])
		else:
			self.changeColor(DrawingGenerics.ENERGIZER_COLOR[1])
			
	
	#------------------------------------------------------------------------------
	# Helper Method: Resets the color of the Energizer.
	#------------------------------------------------------------------------------
	def resetColor(self):
		# If the color is not right, reset it.
		if self.color != DrawingGenerics.ENERGIZER_COLOR[1]:
			self.changeColor(DrawingGenerics.ENERGIZER_COLOR[1])
