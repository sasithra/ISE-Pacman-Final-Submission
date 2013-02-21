"""
Dots module.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from PointItem import PointItem

# Constants
DOT_POINTS = 10

class Dot(PointItem):
	"""
	Dot class.
	This class contains the methods used in the creation of Dots.
	It is of the tkinter library and inherits an instance of PointItem.
	"""
	def __init__(self, gameCanvas, specs):
		"""
		Initialization.
		This method creates a new Dot, initializes it and draws it.
		
		@param gameCanvas: 
		@param specs: Specifies the coordinates, radius, color, tag and points associated
					  with this dot.
		"""
	
		# Initialization of the Dot
		super(Dot, self).__init__(gameCanvas, specs, specs['points'])
		
		# Draw the Dot
		self.draw()
