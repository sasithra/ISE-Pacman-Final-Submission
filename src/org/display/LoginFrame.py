"""
Login frame for the login menu.
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

class MLoginFrame(FrameMaster.FrameMaster):
	"""
	MLoginFrame class.
	This class contains the main Login Frame and initializes all the other Frames in the login 
	phase of the game.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, game):
		"""
		Initialization.
		This method creates a new Login Game Frame frame and initializes all the other 
		frames related to the login frame.
		
		@param game: Instance of the current Pacman game.
		"""
		# Initializing the Framemaster
		FrameMaster.FrameMaster.__init__(self)

		#------------------------------------------------------------------------------
		# Creating all other static frames and popup frames in the main gameplay frame
		#------------------------------------------------------------------------------
		self._ef = ErrorFrame(self.root)
		self._lf = LoginFrame(self.root)

class ErrorFrame(MLoginFrame):
	"""
	ErrorFrame class.
	This class contains the ErrorFrame of the login, which pops up if an erroneous task
	was attempted by the user.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, main):
		"""
		Initialization.
		Initializes this "error frame" popup window, configures its size and 
		defines its fields.

		@param main: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of this error popup Frame.
		#------------------------------------------------------------------------------
		self.error_frame = Frame(main, bg = "black", borderwidth = 3, relief = RIDGE)
		self.error_frame.grid(row = 3, rowspan = 2,  column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.error_frame.grid_propagate(False)

		for i in range(0,1):
			self.error_frame.rowconfigure(i, weight = 1)
		self.error_frame.columnconfigure(0, weight = 1)

		self.error_message = Label(self.error_frame, fg = "yellow", bg = "black")
		self.error_message.grid(row = 0, column = 0)

		#------------------------------------------------------------------------------
		# Configuring the Try again button.
		#------------------------------------------------------------------------------
		self.error_button = Button(self.error_frame, text = "Try Again", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.error_button.grid(row = 1, column = 0)

		self.error_frame.lower()
		
class LoginFrame(MLoginFrame):
	"""
	LoginFrame class.
	This class contains main login frame at the beginning of the game.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, main_login_frame):
		"""
		Initialization.
		Initializes this "Login Frame" window, configures its size and 
		defines its fields.

		@param main_login_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of this loging frame.
		#------------------------------------------------------------------------------
		self.login_frame = Frame(main_login_frame, bg = "black", borderwidth = 3, relief = 
				RIDGE)
		self.login_frame.grid(row = 1, rowspan = 6, column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.login_frame.grid_propagate(False)

		root = self.login_frame

		i = 0
		j = 0
		while i < 6:
			root.rowconfigure(i, weight = 1)
			i = i + 1

		while j < 2:
			root.columnconfigure(j, weight = 1)
			j = j + 1

		#------------------------------------------------------------------------------
		# Configuring the Welcome message at the top of this frame.
		#------------------------------------------------------------------------------
		welcomeFrame = Frame(root, height = 100, width = 200)
		welcome = Label(welcomeFrame, text = "Pacman", bg = "black",
				fg = "yellow")
		welcome.pack(fill = BOTH, side = TOP)
		welcomeFrame.grid(row = 0, column = 0, columnspan = 2,
				sticky = N)
		welcomeFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the User name field entry.
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

		self.ipw = Entry(unameFrame, show = "*")
		self.ipw.pack(fill = BOTH, side = BOTTOM)
		pw = Label(unameFrame, text = "Password", bg = "black", fg = "yellow")
		pw.pack(fill = BOTH, side = BOTTOM)
		
		
		#------------------------------------------------------------------------------
		# Configuring the Log on button.
		#------------------------------------------------------------------------------
		logonFrame = Frame(root, height = 50, width = 100, bg = "black")
		self.logon = Button(logonFrame, text = "Log On", bg = "black", fg = "yellow", 
				highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.logon.pack(fill = BOTH, side = TOP)
		logonFrame.grid(row = 2, column = 0, rowspan = 1, columnspan = 1,
				sticky = N+S+E+W)
		logonFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the play as Guest button.
		#------------------------------------------------------------------------------
		guestFrame = Frame(root, height = 50, width = 100, bg = "black")
		self.guest = Button(guestFrame, text = "Guest", bg = "black", fg = "yellow", 
				highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.guest.pack(fill = BOTH, side = TOP)
		guestFrame.grid(row = 2, column = 1, rowspan = 1, columnspan = 1,
				sticky = N+S+E+W)
		guestFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the Forgot Password button.
		#------------------------------------------------------------------------------
		forgotFrame = Frame(root, height = 50, width = 200, bg = "black")
		self.forgot = Button(forgotFrame, text = "Forgot Password", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground = "red",
				width = 10)
		self.forgot.pack(fill = BOTH )
		forgotFrame.grid(row = 3, column = 0, rowspan = 1, columnspan = 2,
				sticky = N+S+E+W)
		forgotFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the Create new user button.
		#------------------------------------------------------------------------------
		new_user_frame = Frame(root, bg = "black")
		new_user_frame.grid(row = 4, column = 0, rowspan = 1, columnspan = 2,
				sticky = N+S+E+W)
		new_user_frame.grid_propagate(False)
		self.new_user = Button(new_user_frame, text = "New User", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red", width = 10)
		self.new_user.pack(fill = BOTH)

		#------------------------------------------------------------------------------
		# Configuring the exit button.
		#------------------------------------------------------------------------------
		exitFrame = Frame(root, height = 100, width = 200, bg = "black")
		self.exit = Button(exitFrame, text = "Exit", bg = "black", fg = "yellow", 
				highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red",
				width = 10)
		self.exit.pack(fill = BOTH)
		exitFrame.grid(row = 5, column = 0, rowspan = 1, columnspan = 2,
				sticky = N+S+E+W)
		exitFrame.grid_propagate(False)

	#------------------------------------------------------------------------------
	# Helper Method: Erases the text that has been inputted into the entry fields.
	#------------------------------------------------------------------------------
	def eraseEntry(self):
		"""
		Erases the text in the name and password fields.
		"""
		self.iuname.delete(0, END)
		self.ipw.delete(0, END)
