"""
This module contains the Login Menu class "LoginMenu".
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""

from display import LoginFrame

class LoginMenu():
	"""
	This class deals with the Login Menu components.
	"""
	def __init__(self, menu_manager):
		"""
		Class contructor for the Login Menu Class. \n
		Initializes the window and menu components. \n
		Sets up keybindings.
		@param menu_manager: The game object (from org/Pacman.py)
		"""
		self.menu_manager = menu_manager
		self.uiCoordinator = menu_manager.uiCoordinator
		self.open_window = False

		self.setupWindow()
		self.setupBinds()

# Setting up keybindings
	def setupBinds(self):
		"""
		Sets up keybindings.
		"""
		self.login_frame.guest.bind("<Button-1>", self.guestPlay)
		self.login_frame.guest.bind("<Return>", self.guestPlay)

		self.login_frame.logon.bind("<Button-1>", self.userLogon)
		self.login_frame.logon.bind("<Return>", self.userLogon)

		self.login_frame.exit.bind("<Button-1>", self.closeGame)
		self.login_frame.exit.bind("<Return>", self.closeGame)

		self.login_frame.new_user.bind("<Button-1>", self.newUser)
		self.login_frame.new_user.bind("<Return>", self.newUser)

		self.login_frame.forgot.bind("<Button-1>", self.forgotPass)
		self.login_frame.forgot.bind("<Return>", self.forgotPass)

		self.login_frame.iuname.bind("<Return>", self.userLogon)
		self.login_frame.ipw.bind("<Return>", self.userLogon)

		self.error_frame.error_button.bind("<Button-1>", self.closeError)
		self.error_frame.error_button.bind("<Return>", self.closeError)
		


# Undo Keybinds
	def unBind(self):
		"""
		Unbind keybindings.
		"""
		self.login_frame.guest.unbind("<Button-1>")
		self.login_frame.logon.unbind("<Button-1>")
		self.login_frame.exit.unbind("<Button-1>")
		self.login_frame.new_user.unbind("<Button-1>")
		self.login_frame.forgot.unbind("<Button-1>")
		self.login_frame.iuname.unbind("<Return>")
		self.login_frame.ipw.unbind("<Return>")
		self.error_frame.error_button.unbind("<Button-1>")
		self.error_frame.error_button.unbind("<Return>")
		self.login_frame.guest.unbind("<Return>")
		self.login_frame.logon.unbind("<Return>")
		self.login_frame.exit.unbind("<Return>")
		self.login_frame.new_user.unbind("<Return>")
		self.login_frame.forgot.unbind("<Return>")

# Setting up menu GUI
	def setupWindow(self):
		"""
		sets up the window.
		"""
		self.main_login_frame = LoginFrame.MLoginFrame(self.uiCoordinator)
		self.login_frame = self.main_login_frame._lf
		self.login_frame.iuname.focus_set()
		self.error_frame = self.main_login_frame._ef

# Logging on
	def userLogon(self, e):
		"""
		Fetchs username and password from entry widget. \n
		With database, check if password corresponds to user. \n
		If they don't match, it opens the error window. \n
		If the username and password match, login to the game, start game with
		the username, destroy login window, unbind keys.
		@param e: Passed by keybinding, not actually used.
		"""
		username = self.login_frame.iuname.get()
		password = self.login_frame.ipw.get()

### Check if password and username exist and match
		if self.menu_manager.con.checkPassword(username, password):
			self.menu_manager.user.username = username
			self.menu_manager.user.highscore = self.menu_manager.con.getScore(username)
			self.menu_manager.runMenu()
			self.unBind()
			self.main_login_frame.root.destroy()

### show Error window
		else:
			self.error_frame.error_message.configure(text = "Wrong Username"
					" or Password")
			self.main_login_frame.liftFrame(self.error_frame.error_frame)
			self.error_frame.error_button.focus_set()
			self.open_window = True

## hide Error window
	def closeError(self, e):
		"""
		Close the error window and set focus on username entry.
		@param e: Passed by keybinding, not actually used.
		"""
		self.main_login_frame.lowerFrame(self.error_frame.error_frame)
		self.login_frame.eraseEntry()
		self.login_frame.iuname.focus_set()
		self.open_window = False

# Open forgot password
	def forgotPass(self, e):
		"""
		Open forgot password window/menu, destroy logon window,unbind keys.
		@param e: Passed by keybinding, not actually used.
		"""
		self.menu_manager.runForgot()
		self.unBind()
		self.main_login_frame.root.destroy()

# Create new user
	def newUser(self, e):
		"""
		Open new user window/menu, unbind keys, destroy window.
		@param e: Passed by keybinding, not actually used.
		"""
		self.menu_manager.runNewUser()
		self.unBind()
		self.main_login_frame.root.destroy()

# Play as a guest
	def guestPlay(self, e):
		"""
		Start game menu as guest, destroy login window, unbind keys, setup 
		guest values.
		@param e: Passed by keybinding, not actually used.
		"""
		self.menu_manager.user.username = "Guest"
		self.menu_manager.user.highscore = 0
		self.menu_manager.runMenu()
		self.unBind()
		self.main_login_frame.root.destroy()

# Exit the game
	def closeGame(self, e):
		"""
		Close the game.
		@param e: Passed by keybinding, not actually used.
		"""
		raise SystemExit
		
