"""
This module contains the New User Menu class "NewUserMenu".
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
from display import NewUserFrame

class NewUserMenu():
	"""
	This class deals with the New User Menu components.
	"""
	def __init__(self, menu_manager):
		"""
		Class contructor for the New User Menu Class. \n
		Initializes the window and menu components. \n
		Sets up keybindings.
		@param menu_manager: The game object (from org/Pacman.py)
		"""
		self.menu_manager = menu_manager
		self.uiCoordinator = menu_manager.uiCoordinator
		self.open_window = False

		self.setupWindow()
		self.setupBinds()
		
	def setupBinds(self):
		"""
		Sets up keybindings.
		"""
		self.new_frame.exit.bind("<Button-1>", self.closeNewUser)
		self.new_frame.exit.bind("<Return>", self.closeNewUser)
		self.new_frame.newButton.bind("<Button-1>", self.createNewUser)
		self.new_frame.newButton.bind("<Return>", self.createNewUser)
		self.error_frame.error_button.bind("<Button-1>", self.closeError)
		self.error_frame.error_button.bind("<Return>", self.closeError)

		self.new_frame.iuname.bind("<Return>", self.createNewUser)
		self.new_frame.ipw.bind("<Return>", self.createNewUser)
		self.new_frame.ipw_check.bind("<Return>", self.createNewUser)
		self.new_frame.realname.bind("<Return>", self.createNewUser)
		self.new_frame.iquestion.bind("<Return>", self.createNewUser)
		self.new_frame.ianswer.bind("<Return>", self.createNewUser)

	def unBind(self):
		"""
		Unbind keybindings.
		"""
		self.new_frame.exit.unbind("<Button-1>")
		self.new_frame.exit.unbind("<Return>")
		self.new_frame.newButton.unbind("<Return>")
		self.error_frame.error_button.unbind("<Return>")
		self.new_frame.newButton.unbind("<Button-1>")
		self.error_frame.error_button.unbind("<Button-1>")

		self.main_newuser_frame.unbind_all("<Return>")
		self.new_frame.iuname.unbind("<Return>")
		self.new_frame.ipw.unbind("<Return>")
		self.new_frame.ipw_check.unbind("<Return>")
		self.new_frame.realname.unbind("<Return>")
		self.new_frame.iquestion.unbind("<Return>")
		self.new_frame.ianswer.unbind("<Return>")

	def setupWindow(self):
		"""
		sets up the window.
		"""
		self.main_newuser_frame = NewUserFrame.NewUserFrame(self.uiCoordinator)
		self.new_frame = self.main_newuser_frame._nf
		self.error_frame = self.main_newuser_frame._ef
		self.new_frame.iuname.focus_set()

	def createNewUser(self, e):
		"""
		Fetch the inputed parameters from the entry widgets (username, password,
		password check, real name, question, answer). \n
		If any are left empy, error window is opened with an approriate message 
		(Empty ** Field). \n
		If the passwords don't match, error window is opened with the appropriate 
		message. \n
		If the user already exists, error window is opened with the appropriate 
		message. \n
		If everything is good, create a new user (through db connection), 
		go to login menu, destroy new user window/menu, remove keybinds.
		@param e: Passed by keybinding, not actually used.
		"""
		username = self.new_frame.iuname.get()
		password = self.new_frame.ipw.get()
		password_check = self.new_frame.ipw_check.get()
		realname = self.new_frame.realname.get()
		question = self.new_frame.iquestion.get()
		answer = self.new_frame.ianswer.get()

		if (not self.open_window):
			if (username == ""):
				self.error("Empty Name Field")
			elif (password == ""):
				self.error("Empty Password Field")
			elif (realname == ""):
				self.error("Empty Real Name Field")
			elif (question == ""):
				self.error("Empty Question Field")
			elif (answer == ""):
				self.error("Empty Answer Field")
			elif (self.menu_manager.con.checkUser(username)):
				self.error("Username is already taken")
			elif (password == password_check):
				self.menu_manager.con.createUser(username, password, realname,
						question, answer)
				self.closeNewUser("a")
			else:
				self.error("Passwords do not match")

	def closeError(self, e):
		"""
		Close the error window, refocus on username entry.
		@param e: Passed by keybinding, not actually used.
		"""
		self.error_frame.error_button.unbind("<Return>")
		self.new_frame.iuname.focus_set()
		self.main_newuser_frame.lowerFrame(self.error_frame.error_frame)
		self.open_window = False

	def error(self, message):
		"""
		Open the error window and open error message.
		@param message: The message to display on the error window.
		"""
		self.error_frame.error_button.focus_set()
		self.error_frame.error_button.bind("<Return>", self.closeError)
		self.error_frame.error_message.configure(text = message)
		self.main_newuser_frame.liftFrame(self.error_frame.error_frame)
		self.open_window = True

	def closeNewUser(self, e):
		"""
		Closes to the login menu, destroy new user window, remove keybinds.
		@param e: Passed by keybinding, not actually used.
		"""
		self.unBind()
		self.menu_manager.runLogin()
		self.main_newuser_frame.root.destroy()
