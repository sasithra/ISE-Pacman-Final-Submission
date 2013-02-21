"""
Bonus items module.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from PointItem import PointItem
from display import DrawingGenerics

# Constants
DISAPPEAR_CYCLES = 9 * DrawingGenerics.CYCLES_PER_SECOND

class BonusItem(PointItem):
	"""
	Bonus Item class.
	This class contains the methods used in the creation of Bonus Items.
	It is of the tkinter library and inherits an instance of PointItem.
	"""
	def __init__(self, gameCanvas, specs):
		"""
		Initialization.
		This method creates a new Bonus Item and initializes it.
		
		@param gameCanvas:
		@param specs: Specifies the coordinates, radius, color, tag and points associated
					  with this bonus item.
		"""
	
		# Initialization of the Bonus Item
		super(BonusItem, self).__init__(gameCanvas, specs, specs['points'])
		
		# Flag to indicate if bonus item is eadible
		self.active = False
		
		# Indication of the number of cycles the bonus item has been active
		self.activeCycles = 0
	
	def process(self):
		"""
		Process.
		This method checks if the bonus item is active and if it should be
		deactivated.
		
		"""
		if self.active:
			self.activeCycles += 1
			if self.activeCycles >= DISAPPEAR_CYCLES:
				self.activeCycles = 0
				self.deactivate()
				
	def isActive(self):
		"""
		Is Active.
		This method checks if the bonus item is active.
		
		"""
		return self.active
		
	def activate(self):
		"""
		Activate.
		This method activates the bonus item and draws it.
		
		"""
		if not self.active:
			self.active = True
			self.draw()
		self.activeCycles = 0
			
	def deactivate(self):
		"""
		Deactivate.
		This method deactivates the bonus item and deletes the drawing for it.
		
		"""
		if self.active:
			self.active = False
			self.deleteDrawing()
