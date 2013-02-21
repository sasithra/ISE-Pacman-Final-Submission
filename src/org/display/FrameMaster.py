"""
Some general methods for frames.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
try:
	from tkinter import *
except:
	from Tkinter import *

class FrameMaster(Frame):
	"""
	Frame Master class.
	This class contains the methods used in the creation and interaction of all Frames used 
	in this game.
	It is of the tkinter library and inherits an instance of tkinter Frame.

	"""
	def __init__(self):
		"""
		Initialization.
		This method creates a new FrameMaster, configures the rows and columns involved 
		in this frame and intializes the ErrorFrame and BackFrame involved in most
		frames in this game.
		
		"""
		#------------------------------------------------------------------------------
		# Initializes tkinter Frame
		#------------------------------------------------------------------------------
		Frame.__init__(self)

		self.root = Frame()
		self.root.grid(row = 0, column = 0, sticky = N+S+E+W)
		self.root.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configures rows and columns and creates instance of Error and Back Frames.
		#------------------------------------------------------------------------------
		i = 0
		j = 0
		while i < 8:
			self.root.columnconfigure(i, weight = 1)
			i = i + 1

		while j < 8:
			self.root.rowconfigure(j, weight = 1)
			j = j + 1

		self.root.grid_propagate(False)

		self._ef = ErrorFrame(self.root)
		self._bf = BackFrame(self.root)

	#------------------------------------------------------------------------------
	# Helper method: Brings the Frame in question up.
	#------------------------------------------------------------------------------
	def liftFrame(self, frame):
		"""
		Lifts a frame to the top (visible).
		@param frame: The frame to be lifted
		"""
		frame.lift()

	#------------------------------------------------------------------------------
	# Helper method: Takes the Frame in question down.
	#------------------------------------------------------------------------------
	def lowerFrame(self, frame):
		"""
		Lowers a frame to the top (visible).
		@param frame: The frame to be lowered.
		"""
		frame.lower()

class ErrorFrame(FrameMaster):
	"""
	Error Frame class.
	This class contains the methods used in the creation and interaction of an error popup
	Frame in the game.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, main):
		"""
		Initialization.
		This method creates and cofigures(row and column)an Error Frame popup its Canvas 
		Buttons and all other related Canvas Labels related to the Frame.
		
		@param main: Instance of the FrameMaster class that this class is used in.
		"""
		#------------------------------------------------------------------------------
		# Configuring this tkinter Frame.
		#------------------------------------------------------------------------------
		self.error_frame = Frame(main, bg = "black", borderwidth = 3, relief = RIDGE)
		self.error_frame.grid(row = 3, rowspan = 2,  column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.error_frame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the rows and columns for this frame.
		#------------------------------------------------------------------------------
		for i in range(0,1):
			self.error_frame.rowconfigure(i, weight = 1)
		self.error_frame.columnconfigure(0, weight = 1)

		#------------------------------------------------------------------------------
		# Configuring Try again entry.
		#------------------------------------------------------------------------------
		self.error_message = Label(self.error_frame, fg = "yellow", bg = "black")
		self.error_message.grid(row = 0, column = 0)

		self.error_button = Button(self.error_frame, text = "Try Again", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.error_button.grid(row = 1, column = 0)

		self.error_frame.lower()

#### Background Frame ####
class BackFrame(FrameMaster):
	"""
	Background Frame class.
	This class creates a background frame.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, root):
		"""
		Initialization.
		This method creates and cofigures background related to the Frame.
		
		@param root: Root is an instance of the Frame Master class that this class is used in.
		"""
		#------------------------------------------------------------------------------
		# Configuring the background frame.
		#------------------------------------------------------------------------------
		self.back_frame = Frame(root, bg = "black", borderwidth = 3, relief = RIDGE)
		self.back_frame.grid(row = 0, rowspan = 8, column = 0, columnspan = 8, 
				sticky = N+S+E+W)
		self.back_frame.grid_propagate(False)
