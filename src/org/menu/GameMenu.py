"""
This module contains the Game Menu class "GameMenu"
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""

from display import MenuFrame
from gameplay import Gameplay


#### The main game menu functionality ####
class GameMenu():

	"""
	This class deals with the game menu components.
	"""

	def __init__(self, menu_manager):

		"""
		Class constructor for the Game Menu class. \n
		Initialises the window and menu components. \n
		Sets up keybindings.
		@param menu_manager: The game object (from org/Pacman.py)
		"""

		self.menu_manager = menu_manager
		self.uiCoordinator = menu_manager.uiCoordinator
		self.highscore = menu_manager.user.highscore
		self.name = menu_manager.user.username
		self.high_scores = menu_manager.con.getHighscores("DESC")
		self.level = menu_manager.level
		self.open_window = False

		self.setupWindow()
		self.setupInfo()
		self.setupBinds()

## Setting up keybindings
	def setupBinds(self):

		"""
		Sets up the Key bindings.
		"""

		self.menu_window.exitButton.bind("<Button-1>", self.closeGame)
		self.menu_window.exitButton.bind("<Return>", self.closeGame)

		self.menu_window.playButton.bind("<Button-1>", self.playGame)
		self.menu_window.playButton.bind("<Return>", self.playGame)

		self.menu_window.scoreButton.bind("<Button-1>", self.openScore)
		self.menu_window.scoreButton.bind("<Return>", self.openScore)

		self.menu_window.instButton.bind("<Button-1>", self.openInstructions)
		self.menu_window.instButton.bind("<Return>", self.openInstructions)

		self.menu_window.optionsButton.bind("<Button-1>", self.openOptions)
		self.menu_window.optionsButton.bind("<Return>", self.openOptions)

		self.score_window.close_score.bind("<Button-1>", self.openScore)
		self.score_window.close_score.bind("<Return>", self.openScore)

		self.instructions_window.close.bind("<Button-1>", self.openInstructions)
		self.instructions_window.close.bind("<Return>", self.openInstructions)

		self.menu_window.logout_button.bind("<Button-1>", self.logOut)
		self.menu_window.logout_button.bind("<Return>", self.logOut)

	def unBind(self):

		"""
		Unbinds keys.
		"""

		self.menu_window.exitButton.unbind("<Button-1>")
		self.menu_window.playButton.unbind("<Button-1>")
		self.menu_window.scoreButton.unbind("<Button-1>")
		self.menu_window.instButton.unbind("<Button-1>")
		self.menu_window.optionsButton.unbind("<Button-1>")
		self.score_window.close_score.unbind("<Button-1>")
		self.instructions_window.close.unbind("<Button-1>")
		self.menu_window.logout_button.unbind("<Button-1>")
		self.menu_window.exitButton.unbind("<Return>")
		self.menu_window.playButton.unbind("<Return>")
		self.menu_window.scoreButton.unbind("<Return>")
		self.menu_window.instButton.unbind("<Return>")
		self.menu_window.optionsButton.unbind("<Return>")
		self.score_window.close_score.unbind("<Return>")
		self.instructions_window.close.unbind("<Return>")
		self.menu_window.logout_button.unbind("<Return>")

## Setting up the main menu GUI
	def setupWindow(self):

		"""
		Sets up the window.
		"""

		self.main_menu_window = MenuFrame.MainMenuFrame(self.uiCoordinator)
		self.menu_window = self.main_menu_window._mf
		self.score_window = self.main_menu_window._hf
		self.instructions_window = self.main_menu_window._if
		self.menu_window.playButton.focus_set()

## Setting up the personal infor for display
	def setupInfo(self):

		"""
		Sets up and displays user information (username, highscore) for 
		the high scores table.
		"""

		self.menu_window.setName(self.name)
		self.score_window.user_name_current.configure(text = self.name)
		self.score_window.user_score_current.configure(text = self.highscore)


		field = "id"
		high_scores = []
		high_names = []
		ID = True
		for i in self.high_scores:
			for j in i:
				try:
					if field == "id":
						id_ = int(j)
						field = "name"
					elif field == "name":
						high_names.append(str(j))
						field = "score"
					elif field == "score":
						high_scores.append(int(j))
						field = "id"
				except:
					ID = False
					print "Error setupInfo (gamemenu)"
					high_names.append(j)
		for k in range(0, len(high_names)):
			self.score_window.user_name[k].configure(text = "#"+str(k+1)+" " +high_names[k])
			self.score_window.user_score[k].configure(text = high_scores[k])

## Starting gameplay
	def playGame(self, e):

		"""
		Starts the game play, remove keybinds, destroy menu window.
		@param e: Passed by keybinding, not actually used.
		"""

		self.unBind()
		self.main_menu_window.root.destroy()
		self.menu_manager.runGame()

## Open options
	def openOptions(self, e):

		"""
		Open the options menu, remove keybinds, destroy menu window.
		@param e: Passed by keybinding, not actually used.
		"""

		self.unBind()
		self.menu_manager.runOptions()
		self.main_menu_window.root.destroy()

## Log Out
	def logOut(self, e):

		"""
		Log out the user, start runLogin, remove keybinds, destroy menu window.
		@param e: Passed by keybinding, not actually used.
		"""

		self.unBind()
		self.menu_manager.runLogin()
		self.main_menu_window.root.destroy()

## Show high scores
	def openScore(self, e):

		"""
		Open the high score frame, set focus on the close button for the high
		score frame.
		@param e: Passed by keybinding, not actually used.
		"""

		if (not self.open_window):
			self.open_window = True
			self.score_window.close_score.focus_set()
			self.main_menu_window.liftFrame(self.score_window.score_frame)
		elif (self.open_window):
			self.open_window = False
			self.menu_window.playButton.focus_set()
			self.main_menu_window.lowerFrame(self.score_window.score_frame)

## Show game instructions
	def openInstructions(self, e):

		"""
		Open the Instructions window, set focus on the close button.
		@param e: Passed by keybinding, not actually used.
		"""

		if (not self.open_window):
			self.open_window = True
			self.instructions_window.close.focus_set()
			self.main_menu_window.liftFrame(self.instructions_window.instructions_frame)
		elif (self.open_window):
			self.open_window = False
			self.menu_window.playButton.focus_set()
			self.main_menu_window.lowerFrame(self.instructions_window.instructions_frame)

## Exit the game
	def closeGame(self, e):

		"""
		Exits the game.
		"""

		raise SystemExit

