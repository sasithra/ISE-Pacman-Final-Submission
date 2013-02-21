"""
Menu frame for the main menu.
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

class MainMenuFrame(FrameMaster.FrameMaster):
	"""
	MainMenuFrame class.
	This class contains the Main menu frame and initializes all the frames in 
	the main menu frame of the game.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self,game):
		"""
		Initialization.
		This method creates a new Main Menu Frame and initializes all the other frames
		related to the main menu.

		@param game: Instance of the current Pacman game.
		"""
		
		# Initialize the Frame Master 
		FrameMaster.FrameMaster.__init__(self)

		#------------------------------------------------------------------------------
		# Create all other static frames and popup frames in the main menu frame
		#------------------------------------------------------------------------------
		self._hf = HighScore(self.root)
		self._if = InstructionFrame(self.root)
		self._mf = MenuFrame(self.root)

class InstructionFrame(Frame):
	"""
	InstructionFrame class.
	This class contains the Instructions menu that pops up when user selects it
	in the main menu frame.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, root):
		"""
		Initialization.
		This method creates a new Instructions Frame, configures its size and 
		defines its components.

		@param root: Root is the tkinter root of an instance of this class.
		"""
		
		#------------------------------------------------------------------------------
		# Configures the rows and columns in the frame.
		#------------------------------------------------------------------------------
		self.instructions_frame = Frame(root, bg = "black", borderwidth = 3,
				relief = RIDGE)
		self.instructions_frame.grid(row = 1, rowspan = 6, column = 2,
				columnspan = 4, sticky = N+S+E+W)
		self.instructions_frame.grid_propagate(False)

		self.instructions_frame.lower()

		instf = self.instructions_frame

		instf.columnconfigure(0, weight = 1)
		
		for i in range(0,7):
			instf.rowconfigure(i, weight = 1)

		#------------------------------------------------------------------------------
		# Write out the gamepaly instructions in the form of Labels.
		#------------------------------------------------------------------------------
		Label(instf, text = "Instructions on how to play:", bg = "black", 
				fg = "yellow").grid(column = 0, row = 0)

		Label(instf, text = "Use the arrow keys to move in the desired" 
				" direction", bg = "black", fg = "yellow").grid(column = 0, row = 1)

		Label(instf, bg = "black", fg = "yellow",
				text = "You must eat all the dots to pass on to the next level."
				).grid(column = 0, row = 2)

		Label(instf, bg = "black", fg = "yellow",
				text = "You start with 3 lives."
				).grid(column = 0, row = 3)

		Label(instf, bg = "black", fg = "yellow",
				text = "Do not touch the ghosts when they are not blue!"
				).grid(column = 0, row = 4)

		Label(instf, bg = "black", fg = "yellow",
				text = "Once you eat an energizer (large dot), you can eat ghosts."
				).grid(column = 0, row = 5)

		#------------------------------------------------------------------------------
		# Configures the close screen button.
		#------------------------------------------------------------------------------
		self.close = Button(instf, text = "Close", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.close.grid(row = i, column = 0, columnspan = 1)

class HighScore(Frame):
	"""
	HighScore class.
	This class contains the High Score menu that updates according to the user profile
	and stores the top high scores of the current user.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, root):
		"""
		Initialization.
		This method creates a new HighScore Frame, configures its size and 
		defines its components.

		@param root: Root is the tkinter root of an instance of this class.
		"""
		
		#------------------------------------------------------------------------------
		# Configures the rows and columns of the frame.
		#------------------------------------------------------------------------------
		self.score_frame = Frame(root, bg = "black", borderwidth = 3, relief = RIDGE)
		self.score_frame.grid(row = 1, rowspan = 6, column = 2, columnspan = 4,
				sticky = N+S+E+W)
		self.score_frame.grid_propagate(False)

		self.score_frame.lower()

		sf = self.score_frame

		sf.columnconfigure(0, weight = 1)
		sf.columnconfigure(1, weight = 1)
		for i in range(0,13):
			sf.rowconfigure(i, weight = 1)

		#------------------------------------------------------------------------------
		# Creates an array or user names and scores.
		#------------------------------------------------------------------------------
		self.user_name = []
		self.user_score = []
		
		#------------------------------------------------------------------------------
		# Creates the high score label.
		#------------------------------------------------------------------------------
		hscore = Label(sf, text = "High Scores", bg = "black", fg = "yellow")
		hscore.grid(row = 0, rowspan = 1, column = 0, columnspan = 2)
		hscore.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Displays the current user's user name.
		#------------------------------------------------------------------------------
		self.user_name_current = Label(sf, text = "Current User", bg = "black",
				fg = "yellow")
		self.user_name_current.grid(row = 1, column = 0)
		self.user_name_current.grid_propagate(False)

		self.user_score_current = Label(sf, text = "0000", bg = "black",
				fg = "yellow")
		self.user_score_current.grid(row = 1, column = 1)
		self.user_score_current.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Top 10 high scores. Displays the usernames of the top 10 users.
		#------------------------------------------------------------------------------
		for j in range(0,10):
			self.user_name.append(Label(sf, text = "#"+str(j+1)+" Empty", bg = "black", fg = "yellow"))
			self.user_name[j].grid(row = (2 + j), column = 0)
			self.user_name[j].grid_propagate(False)

		#------------------------------------------------------------------------------
		# Top 10 high scores. Displays the usernames of the top 10 users.
		#------------------------------------------------------------------------------
		for k in range(0,10):
			self.user_score.append(Label(sf, text = 0, bg = "black", fg = "yellow"))
			self.user_score[k].grid(row = (2 + k), column = 1)
			self.user_score[k].grid_propagate(False)

		#------------------------------------------------------------------------------
		# Top 10 high scores. Displays the close button.
		#------------------------------------------------------------------------------
		self.close_score = Button(sf, text = "Close", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.close_score.grid(row = 12, column = 0, columnspan = 2)

class MenuFrame(MainMenuFrame):
	"""
	MenuFrame class.
	This class contains the main menu frame and defines all of the frames contained in it.
	It is of the tkinter library and inherits an instance of MainMenuFrame.
	"""
	def __init__(self, root):
		"""
		Initialization.
		This method creates a new main menu Frame, configures its size and 
		defines its components.

		@param root: Root is the tkinter root of an instance of this class.
		"""
		#------------------------------------------------------------------------------
		# Configures the rows and columns of this frame.
		#------------------------------------------------------------------------------
		self.menuFrame = Frame(root, bg = "black", borderwidth = 3, relief = 
				RIDGE)
		self.menuFrame.grid(row = 1, rowspan = 6, column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.menuFrame.grid_propagate(False)

		menuFrame = self.menuFrame
		
		i = 0
		while i < 7:
			menuFrame.rowconfigure(i, weight = 1)
			i = i + 1
		menuFrame.columnconfigure(0, weight = 1)
	
		
		#------------------------------------------------------------------------------
		# Configures the Welcome label.
		#------------------------------------------------------------------------------
		welcomeFrame = Frame(menuFrame, bg = "black")
		welcomeFrame.grid(row = 0, sticky = N)
		welcomeFrame.grid_propagate(False)
		welcomeLabel = Label(welcomeFrame, bg = "black", text = "Pacman",
				fg = "yellow")
		welcomeLabel.pack(fill = BOTH, side = TOP)
		self.nameLabel = Label(welcomeFrame, bg = "black", text = "Name",
				fg = "yellow")
		self.nameLabel.pack(fill = BOTH, side = TOP)
		self.nameLabel.pack_propagate(False)


		#------------------------------------------------------------------------------
		# Congigures the play game button.
		#------------------------------------------------------------------------------
		playFrame = Frame(menuFrame, bg = "black")
		playFrame.grid(row = 1, sticky = N+S+E+W)
		playFrame.grid_propagate(False)
		self.playButton = Button(playFrame, text = "Play Game", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.playButton.pack(fill = BOTH, side = TOP)
		self.playButton.pack_propagate(False)

		#------------------------------------------------------------------------------
		# Configures the High score button.
		#------------------------------------------------------------------------------
		scoreFrame = Frame(menuFrame, bg = "black")
		scoreFrame.grid(row = 2, sticky = N+S+E+W)
		scoreFrame.grid_propagate(False)
		self.scoreButton = Button(scoreFrame, text = "High Score", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.scoreButton.pack(fill = BOTH, side = TOP)
		self.scoreButton.pack_propagate(False)

		#------------------------------------------------------------------------------
		# Configures the options button.
		#------------------------------------------------------------------------------
		optionsFrame = Frame(menuFrame, bg = "black")
		optionsFrame.grid(row = 3, sticky = N+S+E+W)
		optionsFrame.grid_propagate(False)
		self.optionsButton = Button(optionsFrame, text = "Options", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.optionsButton.pack(fill = BOTH, side = TOP)
		self.optionsButton.pack_propagate(False)

		#------------------------------------------------------------------------------
		# Configures the Instructions button.
		#------------------------------------------------------------------------------
		instFrame = Frame(menuFrame, bg = "black")
		instFrame.grid(row = 4, sticky = N+S+E+W)
		instFrame.grid_propagate(False)
		self.instButton = Button(instFrame, text = "Instructions", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.instButton.pack(fill = BOTH, side = TOP)
		self.instButton.pack_propagate(False)

		#------------------------------------------------------------------------------
		# Configures the Logout button.
		#------------------------------------------------------------------------------
		logoutFrame = Frame(menuFrame, bg = "black")
		logoutFrame.grid(row = 5, sticky = N+S+E+W)
		logoutFrame.grid_propagate(False)
		self.logout_button = Button(logoutFrame, text = "Log Out", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.logout_button.pack(fill = BOTH, side = TOP)
		self.logout_button.pack_propagate(False)

		#------------------------------------------------------------------------------
		# Configures the Exit button.
		#------------------------------------------------------------------------------
		exitFrame = Frame(menuFrame, bg = "black")
		exitFrame.grid(row = 6, sticky = N+S+E+W)
		exitFrame.grid_propagate(False)
		self.exitButton = Button(exitFrame, text = "Exit", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.exitButton.pack(fill = BOTH, side = TOP)
		self.exitButton.pack_propagate(False)

	#------------------------------------------------------------------------------
	# Helper Method: Sets the user name at the top of the frame.
	#------------------------------------------------------------------------------
	def setName(self, name):
		"""
		Sets the name of the user at the top of the frame.
		@param name: The name to be set.
		"""
		self.nameLabel.configure(text = name)

