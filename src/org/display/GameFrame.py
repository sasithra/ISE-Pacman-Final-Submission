"""
Frame for the gameplay.
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

from display import DrawingGenerics
from display import FrameMaster


########## Holding the Game Frame #############
class MGameFrame(FrameMaster.FrameMaster):
	"""
	MGameFrame class.
	This class contains the main GameFrame and initialized all the other Frames in the 
	Gameplay Frame.
	It is of the tkinter library and inherits an instance of FrameMaster.

	"""
	def __init__(self, game):
		"""
		Initialization.
		This method creates a new Main Game Frame frame and initializes all the other 
		frames related to the gameplay frame.
		
		@param game: Instance of the current Pacman game.
		"""
		# Initialize tkinter Frame
		FrameMaster.FrameMaster.__init__(self)

		#------------------------------------------------------------------------------
		# Create all other static frames and popup frames in the main gameplay frame
		#------------------------------------------------------------------------------
		self._cf = closeFrame(self.root)
		self._hf = HelpFrame(self.root)
		self._mf = mainFrame(self.root)
		self._if = InfoFrame(self.root)
		self._sf = ScoreFrame(self.root)
		self._lf = LivesFrame(self.root)
		self._gf = GameFrame(self.root)


class mainFrame(Frame):
	"""
	mainFrame class.
	This class contains the initialization and configuration of the return to main menu which 
	pops up when the user selects the menu button in the infoFrame menu.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes this "return to main menu" popup window, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of this "return to main menu" popup Frame.
		#------------------------------------------------------------------------------
		self.main_frame = Frame(main_game_frame, bg = "black", borderwidth = 3, 
				relief = RIDGE)
		self.main_frame.grid(row = 0, rowspan = 8, column = 0, columnspan = 8)

		self.main_frame.rowconfigure(0, weight = 1)
		self.main_frame.rowconfigure(1, weight = 1)
		self.main_frame.rowconfigure(2, weight = 1)

		self.main_frame.columnconfigure(0, weight = 1)
		self.main_frame.columnconfigure(0, weight = 1)

		root = self.main_frame

		#------------------------------------------------------------------------------
		# Configuring the confirmation to return to main menu field.
		#------------------------------------------------------------------------------
		close_message = Label(root, text = "Are you sure you want to return" 
				" to the main menu?", bg = "black", fg = "yellow")
		close_message_2 = Label(root, text = "This action will quit the current"
				" game", bg = "black", fg = "yellow")
		
		#------------------------------------------------------------------------------
		# Configuring the Stay in Game button.
		#------------------------------------------------------------------------------
		self.no = Button(root, text = "Stay in Game", bg = "black", fg = "yellow",
				width = 15, highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")
		
		#------------------------------------------------------------------------------
		# Configuring the return to main menu button.
		#------------------------------------------------------------------------------
		self.yes = Button(root, text = "Return to Main Menu", bg = "black", fg = "yellow",
				width = 15, highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")

		#------------------------------------------------------------------------------
		# Configuring the close message fields.
		#------------------------------------------------------------------------------
		close_message.grid(row = 0, column = 0, columnspan = 2, sticky = N+S+E+W)
		close_message_2.grid(row = 1, column = 0, columnspan = 2, sticky = N+S+E+W)
		self.no.grid(row = 2, column = 0, columnspan = 1, sticky = N+S+E+W)
		self.yes.grid(row = 2, column = 1, columnspan = 1, sticky = N+S+E+W)

class closeFrame(Frame):
	"""
	closeFrame class.
	This class contains the initialization and configuration of the close frame which pops up 
	when the user selects the quit button in the infoFrame menu.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes this "quit" popup window, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of this frame.
		#------------------------------------------------------------------------------
		self.close_frame = Frame(main_game_frame, bg = "black", borderwidth = 3, relief = RIDGE)
		self.close_frame.grid(row = 0, rowspan = 8, column = 0, columnspan = 8)

		self.close_frame.rowconfigure(0, weight = 1)
		self.close_frame.rowconfigure(1, weight = 1)
		self.close_frame.columnconfigure(0, weight = 1)
		self.close_frame.columnconfigure(1, weight = 1)

		root = self.close_frame
		
		#------------------------------------------------------------------------------
		# Configuring the close message fields.
		#------------------------------------------------------------------------------
		close_message = Label(root, text = "Are you sure you want to quit?",
				bg = "black", fg = "yellow", relief = RIDGE)
		
		#------------------------------------------------------------------------------
		# Configuring the "Stay in Game" and "Exit Game" button fields.
		#------------------------------------------------------------------------------
		self.no = Button(root, text = "Stay in Game", bg = "black", fg = "yellow",
				width = 8, highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")
		self.yes = Button(root, text = "Exit Game", bg = "black", fg = "yellow",
				width = 8, highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")

		#------------------------------------------------------------------------------
		# Configuring the close message fields.
		#------------------------------------------------------------------------------
		close_message.grid(row = 0, column = 0, columnspan = 2, sticky = N+S+E+W)
		self.no.grid(row = 1, column = 0, columnspan = 1, sticky = N+S+E+W)
		self.yes.grid(row = 1, column = 1, columnspan = 1, sticky = N+S+E+W)

#### Help dialog frame ####
class HelpFrame(Frame):
	"""
	HelpFrame class.
	This class contains the initialization and configuration of the help frame which pops 
	up when the user selects the help button in the infoFrame menu.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes this "Help" popup window, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of this frame.
		#------------------------------------------------------------------------------
		self.help_frame = Frame(main_game_frame, bg = "black", borderwidth = 3, relief = RIDGE)
		self.help_frame.grid(row = 0, rowspan = 8, column = 0, columnspan = 8)

		self.help_frame.rowconfigure(0, weight = 1)
		self.help_frame.rowconfigure(1, weight = 1)

		self.help_frame.columnconfigure(0, weight = 1)
		self.help_frame.columnconfigure(1, weight = 1)
		self.help_frame.columnconfigure(2, weight = 1)

		root = self.help_frame

		#------------------------------------------------------------------------------
		# Configuring the help message fields.
		#------------------------------------------------------------------------------
		welcome = Label(root, text = "Welcome to the Pacman help file.", 
				bg = "black", fg = "yellow", relief = RIDGE)

		#------------------------------------------------------------------------------
		# Configuring the close message fields.
		#------------------------------------------------------------------------------
		self.close = Button(root, text = "Close", bg = "black", fg = "yellow",
				width = 5, highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")

		welcome.grid(row = 0, column = 0, columnspan = 3, sticky = N+S+E+W)
		self.close.grid(row = 1, column = 1, columnspan = 1, sticky = N+S+E+W)

		
class GameFrame(Frame, Canvas):
	"""
	GameFrame class.
	This class contains the initialization and configuration of the gameplay frame.
	It is of the tkinter library and inherits an instance of Frame and Canvas.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes this gameplay frame, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring this gameplay frame.
		#------------------------------------------------------------------------------
		gameFrame = Frame(main_game_frame, bg = "black", borderwidth = 3, relief = RIDGE)
		gameFrame.grid(row = 1, column = 0, columnspan = 7, rowspan = 7,
				sticky = N+S+E+W)
		gameFrame.grid_propagate(False)

		root = gameFrame

		#------------------------------------------------------------------------------
		# Configuring the Canvas used in this frame.
		#------------------------------------------------------------------------------
		self.gf = Canvas(root, width = DrawingGenerics.MAP_WIDTH + 1,
				height = DrawingGenerics.MAP_HEIGHT,
				bg = "black",
				highlightthickness = 0)
		self.gf.place(x = 100, y = -35)
		self.gf.focus_get()

class InfoFrame(Frame):
	"""
	InfoFrame class.
	This class contains the initialization and configuration of the info frame in the gameplay
	consisting of the pause, help, menu and exit options.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes the info frame, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of info frame.
		#------------------------------------------------------------------------------
		infoFrame = Frame(main_game_frame, bg = "black", borderwidth = 3, relief = RIDGE)
		infoFrame.grid(row = 1, column = 7, columnspan = 1, rowspan = 7,
				sticky = N+S+E+W)
		infoFrame.grid_propagate(False)

		root = infoFrame
		
		root.columnconfigure(0, weight = 1)

		i = 0
		while i < 4:
			root.rowconfigure(i, weight = 1)
			i = i + 1
			
		#------------------------------------------------------------------------------
		# Setting the variable that determines when text of these options turn red.
		#------------------------------------------------------------------------------
		self.pause_red = False
		self.help_red = False
		self.exit_red = False
		self.main_red = False

		
		#------------------------------------------------------------------------------
		# Configure the Pause button.
		#------------------------------------------------------------------------------
		self.pause = Button(root, text = "Pause", fg = "yellow", bg = "black", 
				highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")
		self.pause.grid(row = 0, column = 0)

		#------------------------------------------------------------------------------
		# Configure the Menu button.
		#------------------------------------------------------------------------------
		self.options = Button(root, text = "Menu", fg = "yellow", bg = "black",
				highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")
		self.options.grid(row = 1, column = 0)

		#------------------------------------------------------------------------------
		# Configure the Help button.
		#------------------------------------------------------------------------------
		self.hhelp = Button(root, text = "Help", fg = "yellow", bg = "black", 
				highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = "red")
		self.hhelp.grid(row = 2, column = 0)

		#------------------------------------------------------------------------------
		# Configure the Exit button.
		#------------------------------------------------------------------------------
		self.exit = Button(root, text = "Exit", fg = "yellow", bg = "black",
				highlightcolor = "red", highlightbackground = 
				"yellow", activebackground = "black", activeforeground = 
				"red")
		self.exit.grid(row = 3, column = 0)

	#------------------------------------------------------------------------------
	# Helper method: If main is pressed, change the font color to red.
	#------------------------------------------------------------------------------
	def mainPress(self):
		"""
		This method changes the color of the main menu button when the menu is open.
		"""
		if (not self.main_red):
			self.options.configure(fg = "red")
			self.main_red = True
		elif (self.main_red):
			self.options.configure(fg = "yellow")
			self.main_red = False

	#------------------------------------------------------------------------------
	# Helper method: If main is pressed, change the font color to red.
	#------------------------------------------------------------------------------
	def exitPress(self):
		"""
		This method changes the color of the exit button when the menu is open.
		"""
		if (not self.exit_red):
			self.exit.configure(fg = "red")
			self.exit_red = True
		elif (self.exit_red):
			self.exit.configure(fg = "yellow")
			self.exit_red = False

	#------------------------------------------------------------------------------
	# Helper method: If help is pressed, change the font color to red.
	#------------------------------------------------------------------------------
	def helpPress(self):
		"""
		This method changes the color of the help button when the menu is open.
		"""
		if (not self.help_red):
			self.hhelp.configure(fg = "red")
			self.help_red = True
		elif (self.help_red):
			self.hhelp.configure(fg = "yellow")
			self.help_red = False

	#------------------------------------------------------------------------------
	# Helper method: If pause is pressed, change the font color to red.
	#------------------------------------------------------------------------------
	def pausePress(self):
		"""
		This method changes the color of the pause button when the menu is open.
		"""
		if (not self.pause_red):
			self.pause.configure(text = "Paused", fg = "red")
			self.pause_red = True
		elif (self.pause_red):
			self.pause.configure(text = "Pause", fg = "yellow")
			self.pause_red = False

class ScoreFrame(Frame):
	"""
	ScoreFrame class.
	This class contains the initialization and configuration of the score frame in the gameplay
	consisting of the current username, the current game score and the most recent high score.
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, main_game_frame):
		"""
		Initialization.
		Initializes the score frame, configures its size and 
		defines its components.

		@param main_game_frame: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns if the score frame.
		#------------------------------------------------------------------------------
		scoreFrame = Frame(main_game_frame, bg = "black", borderwidth = 3, relief = RIDGE)
		scoreFrame.grid(row = 0, column = 4, columnspan = 4, rowspan = 1,
				sticky = N+S+E+W)
		scoreFrame.grid_propagate(False)

		root = scoreFrame
		
		root.rowconfigure(0, weight = 1)
		root.rowconfigure(1, weight = 1)
		
		i = 0
		while i < 4:
			root.columnconfigure(i, weight = 1)
			i = i + 1
		
		#------------------------------------------------------------------------------
		# Setting up the score display variables of score frame.
		#------------------------------------------------------------------------------
		self.scoreText = StringVar()
		self.highscoreText = StringVar()
		
		self.scoreText.set("0000")
		self.highscoreText.set("0000")
		
		#------------------------------------------------------------------------------
		# Configuring the text to be displayed in this frame. 
		# (Name, score, High Score)
		#------------------------------------------------------------------------------
		self.name = Label(root, text = "Name", fg = "yellow", bg = "black")
		self.name.grid(row = 0, column = 0, columnspan = 4, sticky = N+S+E+W)

		self.score = Label(root, text = "Score:", fg = "yellow", bg = "black")
		self.score.grid(row = 1, column = 0, columnspan = 1, sticky = E)

		self.dscore = Label(root, textvariable = self.scoreText, fg = "yellow", bg = "black")
		self.dscore.grid(row = 1, column = 1, columnspan = 1, sticky = N+S+E+W)

		self.hscore = Label(root, text = "High Score:", fg = "yellow", bg = "black")
		self.hscore.grid(row = 1, column = 2, columnspan = 1, sticky = E)

		self.dhscore = Label(root, textvariable = self.highscoreText, fg = "yellow", bg = "black")
		self.dhscore.grid(row = 1, column = 3, columnspan = 1, sticky = N+S+E+W)

	#------------------------------------------------------------------------------
	# Helper Method: Updates the score as the game is being played. High Score is 
	#				 updated if the current score surpasses previous one.
	#------------------------------------------------------------------------------
	def updateScore(self, score):
		"""
		Update the score shown in the score frame.
		@param score: The updated score
		"""
		self.scoreText.set(score)
		if (int(self.scoreText.get()) >= int(self.highscoreText.get())):
			self.highscoreText.set(score)
		
class LivesFrame(Frame, Canvas):
	"""
	LivesFrame class.
	This class contains the initialization and configuration of the lives frame in the gameplay
	displaying the current lives remaining. 
	It is of the tkinter library and inherits an instance of Frame.
	"""
	def __init__(self, root):
		"""
		Initialization.
		Initializes the lives frame, configures its size and 
		defines its components.

		@param root: Instance of the MGameFrame.
		"""
		
		#------------------------------------------------------------------------------
		# Configuring the rows and columns of lives frame.
		#------------------------------------------------------------------------------
		livesFrame = Frame(root, bg = "black", borderwidth = 3, relief = RIDGE)
		livesFrame.grid(row = 0, column = 0, columnspan = 4, rowspan = 1,
				sticky = N+S+E+W)
		livesFrame.grid_propagate(False)
		
		livesFrame.rowconfigure(0, weight = 1)
		livesFrame.rowconfigure(1, weight = 1)
		livesFrame.columnconfigure(0, weight = 1)
		
		#------------------------------------------------------------------------------
		# Dividing the lives frame into a title frame and a lives canvas frame.
		#------------------------------------------------------------------------------
		titleFrame = Frame(livesFrame, bg = "black", borderwidth = 0)
		titleFrame.grid(row = 0, column = 0, sticky = N+S+E+W)
		titleFrame.grid_propagate(False)
		titleFrame.rowconfigure(0, weight = 1)
		titleFrame.columnconfigure(0, weight = 1)
		
		canvasFrame = Frame(livesFrame, bg = "black", borderwidth = 0)
		canvasFrame.grid(row = 1, column = 0, sticky = N+S+E+W)
		canvasFrame.grid_propagate(False)
		canvasFrame.rowconfigure(0, weight = 1)
		canvasFrame.columnconfigure(0, weight = 1)
		
		#------------------------------------------------------------------------------
		# Configuring the text and pacman characters to indicate how many lives remain.
		#------------------------------------------------------------------------------
		title = Label(titleFrame, text = "Lives", fg = "yellow", bg = "black")
		title.grid(row = 0, column = 0, sticky = N+S+E+W)
		title.grid_propagate(False)
		
		self.canvas = Canvas(canvasFrame,
				bg = "black",
				highlightthickness = 0)
		self.canvas.grid(row = 1, column = 0, sticky = N+S+E+W)
		
		self.lifeItemID = []
		
		#------------------------------------------------------------------------------
		# Add 3 lives at the beginning of a game.
		#------------------------------------------------------------------------------
		for i in range(0,3):
			self.addLife()
		
		
	def removeLife(self):
		"""
		Remove Pacman lives.
		Removes a life from the lifeItem counter when Pacman dies.

		"""
		
		#------------------------------------------------------------------------------
		# Pop lives from lifeItemID as a life is lost.
		#------------------------------------------------------------------------------
		if not len(self.lifeItemID) == 0:
			self.canvas.delete(self.lifeItemID.pop())
		
	def addLife(self):
		"""
		Remove Pacman lives.
		Removes a life from the lifeItem counter when Pacman dies.

		"""
		
		#------------------------------------------------------------------------------
		# Draws additional lives as a life is gained ( at 10000 and 100000 points).
		#------------------------------------------------------------------------------
		self.lifeItemID.append(self.canvas.create_oval(2 * len(self.lifeItemID) * DrawingGenerics.PACMAN_RADIUS,
					0,
					2 * (len(self.lifeItemID)+1) * DrawingGenerics.PACMAN_RADIUS,
					2 * DrawingGenerics.PACMAN_RADIUS,
					fill = DrawingGenerics.PACMAN_COLOR,
					tag = DrawingGenerics.TAG_PACMAN))

		
