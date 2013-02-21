"""
Frame for the new user menu.
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

from display import FrameMaster

class NewUserFrame(FrameMaster.FrameMaster):
	"""
	NewUserFrame class.
	This class contains the main new user Frame and initialized all the other Frames in the 
	Gameplay Frame.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, game):
		"""
		Initialization.
		New user frame object containing frames
		
		@param game: 
		"""
		
		# Initializes the FrameMaster class.
		FrameMaster.FrameMaster.__init__(self)

		# Initializes an instance of the new frame.
		self._nf = NewFrame(self.root)

class NewFrame(NewUserFrame):
	"""
	NewFrame class.
	This class contains the main new Frame, configures its size and initializes all the 
	fields of entry and its functional components.
	It is of the tkinter library and inherits an instance of NewUserFrame.
	"""
	def __init__(self, main_new_user_frame):
		"""
		Initialization.
		This method creates a new user frame and initializes all the other 
		frames related to the creating a new user.
		
		@param main_new_user_frame: Instance of the main user frame class ot be used here.
		"""
		#------------------------------------------------------------------------------
		# Creates the frame and configures the rows and columns of this frame.
		#------------------------------------------------------------------------------
		self.new_frame = Frame(main_new_user_frame, bg = "black", borderwidth = 3, relief = 
				RIDGE)
		self.new_frame.grid(row = 1, rowspan = 6, column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.new_frame.grid_propagate(False)

		root = self.new_frame

		for i in range(0,7):
			root.rowconfigure(i, weight = 1)
		for j in range(0,2):
			root.columnconfigure(j, weight = 1)

		#------------------------------------------------------------------------------
		# Creates and configures the new user label.
		#------------------------------------------------------------------------------
		welcomeFrame = Frame(root, height = 100, width = 200)
		welcome = Label(welcomeFrame, text = "New User", bg = "black",
				fg = "yellow")
		welcome.pack(fill = BOTH, side = TOP)
		welcomeFrame.grid(row = 0, column = 0, columnspan = 2,
				sticky = N)
		welcomeFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Create and configures the new user field to be entered.
		#------------------------------------------------------------------------------
		unameFrame = Frame(root, height = 100, width = 200)
		uname = Label(unameFrame, text = "User Name:", bg = "black",
				fg = "yellow")
		uname.pack(fill = BOTH, side = TOP)
		self.iuname = Entry(unameFrame)
		self.iuname.pack(fill = BOTH, side = TOP)
		unameFrame.grid(row = 1, column = 0, columnspan = 2,
				sticky = N)
		unameFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Creates and connfigures the password field to be filled out. Similar "*" 
		# character displayed for added security.
		#------------------------------------------------------------------------------
		password_frame = Frame(root, height = 100, width = 200)
		password_frame.grid(row = 2, column = 0, columnspan = 2, sticky = N)
		password_frame.grid_propagate(False)
		pw = Label(password_frame, text = "Password", bg = "black", fg = "yellow")
		pw.pack(fill = BOTH, side = TOP)

		self.ipw = Entry(password_frame, show = "*")
		self.ipw.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Creates and configures the password re entry field to be filled out. Similar
		# "*" character displayed for added security.
		#------------------------------------------------------------------------------
		Label(password_frame, text = "Retype Password", bg = "black",
				fg = "yellow").pack(fill = BOTH, side = TOP)

		self.ipw_check = Entry(password_frame, show = "*")
		self.ipw_check.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Creates and configures the real name field to be filled out. 
		#------------------------------------------------------------------------------
		realname_frame = Frame(root, height = 100, width = 200, bg = "black")
		realname_frame.grid(row = 3, column = 0, columnspan = 2, sticky = N)
		realname_frame.grid_propagate(False)
		Label(realname_frame, text = "Enter your real name", bg = "black",
				fg = "yellow").pack(fill = BOTH, side = TOP)
		self.realname = Entry(realname_frame)
		self.realname.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Creates and configures the Security question entry field to be filled out. 
		#------------------------------------------------------------------------------
		questionFrame = Frame(root, height = 100, width = 200)
		question = Label(questionFrame, text = "Security Question:", bg = "black",
				fg = "yellow")
		question.pack(fill = BOTH, side = TOP)
		self.iquestion = Entry(questionFrame)
		self.iquestion.pack(fill = BOTH, side = TOP)
		questionFrame.grid(row = 4, column = 0, columnspan = 2,
				sticky = N)
		questionFrame.grid_propagate(False)
		
		#------------------------------------------------------------------------------
		# Creates and configures the Security answer entry field to be filled out. 
		#------------------------------------------------------------------------------
		self.ianswer = Entry(questionFrame)
		self.ianswer.pack(fill = BOTH, side = BOTTOM)
		answer = Label(questionFrame, text = "Answer:", bg = "black", fg = "yellow")
		answer.pack(fill = BOTH, side = BOTTOM)

		#------------------------------------------------------------------------------
		# Creates and configures the Create new user button.
		#------------------------------------------------------------------------------
		buttonFrame = Frame(root, bg = "black", height = 100, width = 200)
		buttonFrame.grid(row = 5, column = 0, columnspan = 2, sticky = N+S+E+W)
		self.newButton = Button(buttonFrame, text = "Create New User", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.newButton.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Creates and configures the exit button.
		#------------------------------------------------------------------------------
		exitFrame = Frame(root, height = 100, width = 200, bg = "black")
		self.exit = Button(exitFrame, text = "Exit", bg = "black", fg = "yellow", 
				highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red",
				width = 10)
		self.exit.pack(fill = BOTH)
		exitFrame.grid(row = 6, column = 0, rowspan = 1, columnspan = 2,
				sticky = N+S+E+W)
		exitFrame.grid_propagate(False)
