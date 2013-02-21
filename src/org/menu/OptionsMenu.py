"""
This module contains the Options Menu class "OptionMenu".
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
from display import OptionFrame 

class OptionMenu():
	"""
	This class deals with the Option Menu components.
	"""
	def __init__(self, menu_manager):
		"""
		Class contructor for the Option Menu Class. \n
		Initializes the window and menu components. \n
		Sets up keybindings.
		@param menu_manager: The game object (from org/Pacman.py)
		"""
		self.menu_manager = menu_manager
		self.uiCoordinator = menu_manager.uiCoordinator
		self.highscore = menu_manager.user.highscore
		self.name = menu_manager.user.username
		self.open_window = ""
		self.att_change = ""

		self.windowSetup()
		self.binds()

# Key bindings
	def binds(self):
		"""
		Sets up keybindings.
		"""
		self.option_menu.close.bind("<Button-1>", self.returnToMain)
		self.option_menu.close.bind("<Return>", self.returnToMain)

		self.option_menu.option_password_button.bind("<Button-1>", self.changePassword)
		self.option_menu.option_password_button.bind("<Return>", self.changePassword)

		self.option_menu.option_realname_button.bind("<Button-1>", self.changeName)
		self.option_menu.option_realname_button.bind("<Return>", self.changeName)

		self.option_menu.option_sec_button.bind("<Button-1>", self.changeSec)
		self.option_menu.option_sec_button.bind("<Return>", self.changeSec)

		self.option_menu.change_password.bind("<Return>", self.changePasswordEntry)
		self.option_menu.change_password_re.bind("<Return>", self.changePasswordEntry)
		self.option_menu.password_button.bind("<Return>", self.changePasswordEntry)
		self.option_menu.password_button.bind("<Button-1>", self.changePasswordEntry)
		self.option_menu.close_password.bind("<Return>", self.closeCurrent)
		self.option_menu.close_password.bind("<Button-1>", self.closeCurrent)

		self.option_menu.change_question.bind("<Return>", self.changeSecEntry)
		self.option_menu.change_answer.bind("<Return>", self.changeSecEntry)
		self.option_menu.qa_button.bind("<Return>", self.changeSecEntry)
		self.option_menu.qa_button.bind("<Button-1>", self.changeSecEntry)
		self.option_menu.qa_close.bind("<Return>", self.closeCurrent)
		self.option_menu.qa_close.bind("<Button-1>", self.closeCurrent)

		self.option_menu.change_realname.bind("<Return>", self.changeNameEntry)
		self.option_menu.realname_button.bind("<Return>", self.changeNameEntry)
		self.option_menu.realname_button.bind("<Button-1>", self.changeNameEntry)
		self.option_menu.realname_close.bind("<Return>", self.closeCurrent)
		self.option_menu.realname_close.bind("<Button-1>", self.closeCurrent)

		self.error_frame.error_button.bind("<Return>", self.closeError)
		self.error_frame.error_button.bind("<Button-1>", self.closeError)

		self.option_menu.icpw.bind("<Return>", self.checkPassword)
		self.option_menu.cpw_button.bind("<Return>", self.checkPassword)
		self.option_menu.cpw_button.bind("<Button-1>", self.checkPassword)
		self.option_menu.cancel_button.bind("<Return>", self.closeCurrent)
		self.option_menu.cancel_button.bind("<Button-1>", self.closeCurrent)

# Unbind keys
	def unBind(self):
		"""
		Unbind keybindings.
		"""
		self.option_menu.close.unbind("<Button-1>")
		self.option_menu.close.unbind("<Return>")
		self.option_menu.option_password_button.unbind("<Button-1>")
		self.option_menu.option_password_button.unbind("<Return>")
		self.option_menu.option_realname_button.unbind("<Button-1>")
		self.option_menu.option_realname_button.unbind("<Return>")
		self.option_menu.option_sec_button.unbind("<Button-1>")
		self.option_menu.option_sec_button.unbind("<Return>")
		self.option_menu.change_password.unbind("<Return>")
		self.option_menu.change_password_re.unbind("<Return>")
		self.option_menu.password_button.unbind("<Return>")
		self.option_menu.password_button.unbind("<Button-1>")
		self.error_frame.error_button.unbind("<Return>")
		self.error_frame.error_button.unbind("<Button-1>")
		self.option_menu.icpw.unbind("<Return>")
		self.option_menu.cpw_button.unbind("<Return>")
		self.option_menu.cpw_button.unbind("<Button-1>")
		self.option_menu.cancel_button.unbind("<Return>")
		self.option_menu.cancel_button.unbind("<Button-1>")
		self.option_menu.close_password.unbind("<Return>")
		self.option_menu.close_password.unbind("<Button-1>")
		self.option_menu.change_realname.unbind("<Return>")
		self.option_menu.realname_button.unbind("<Return>")
		self.option_menu.realname_button.unbind("<Button-1>")
		self.option_menu.realname_close.unbind("<Return>")
		self.option_menu.realname_close.unbind("<Button-1>")

# window setups
	def windowSetup(self):
		"""
		sets up the window.
		"""
		self.main_option_menu = OptionFrame.MainOptionFrame(self.uiCoordinator)
		self.option_menu = self.main_option_menu._of
		self.error_frame = self.main_option_menu._ef
		self.option_menu.option_password_button.focus_set()

# Change Name (open dialog)
	def changeName(self, e):
		"""
		Open the change real name window. Save ChangeName string for use in focusing
		after an error message and attribute changing.
		@param e: Passed by keybinding, not actually used.
		"""
		self.open_window = "ChangeName"
		self.att_change = "ChangeName"
		self.main_option_menu.liftFrame(self.option_menu.change_realname_frame)
		self.main_option_menu.lowerFrame(self.option_menu.option_frame)
		self.option_menu.change_realname.focus_set()

# Change Name (after new name entry)
	def changeNameEntry(self, e):
		"""
		Fetches the new real name. \n
		If the field is empty, error window displays appropriate message. \n
		If the field is not empty, the enter current password window is opened and
		CurrentPassword string is saved for use in refocusing after later errors.
		@param e: Passed by keybinding, not actually used.
		"""
		self.realname = self.option_menu.change_realname.get()

		if (self.realname == ""):
			self.Error("Bad Name Entry")
		else:
			self.option_menu.icpw.focus_set()
			self.main_option_menu.lowerFrame(self.option_menu.change_realname_frame)
			self.open_window = "CurrentPassword"
			self.main_option_menu.liftFrame(self.option_menu.current_password_frame)

# Change question/answer (open dialog)
	def changeSec(self, e):
		"""
		Change security window. Save ChangeSec string for user after error message,
		and attribute changing \n
		Focus set on the question field.
		@param e: Passed by keybinding, not actually used.
		"""
		self.open_window = "ChangeSec"
		self.att_change = "ChangeSec"
		self.main_option_menu.liftFrame(self.option_menu.question_and_answer)
		self.main_option_menu.lowerFrame(self.option_menu.option_frame)
		self.option_menu.change_question.focus_set()

# Change sec (after new sec entry)
	def changeSecEntry(self, e):
		"""
		Fetch from question and answer fields. \n
		If empty, an appropriate error message appears. \n
		If correctly formatted, the current password window opens and CurrentPassword
		string is saved.
		@param e: Passed by keybinding, not actually used.
		"""
		self.question = self.option_menu.change_question.get()
		self.answer = self.option_menu.change_answer.get()

		if (self.question == "") or (self.answer == ""):
			self.Error("Bad Question/Answer")
		else:
			self.option_menu.icpw.focus_set()
			self.main_option_menu.lowerFrame(self.option_menu.change_password_frame)
			self.open_window = "CurrentPassword"
			self.main_option_menu.liftFrame(self.option_menu.current_password_frame)

# Change Password (open dialog)
	def changePassword(self, e):
		"""
		Change Password window. Save ChangePassword string for user after error
		message and attribute changing. \n 
		Focus set on the fist password field.
		@param e: Passed by keybinding, not actually used.
		"""
		self.open_window = "ChangePassword"
		self.att_change = "ChangePassword"
		self.main_option_menu.liftFrame(self.option_menu.change_password_frame)
		self.main_option_menu.lowerFrame(self.option_menu.option_frame)
		self.option_menu.change_password.focus_set()

# Change Password (after new password entry)
	def changePasswordEntry(self, e):
		"""
		Fetch from both password fields. \n
		If empty, an appropriate error message appears. \n
		If missmatch, an appropriate error message appreas. \n
		If correctly formatted, the current password window opens and CurrentPassword
		string is saved.
		@param e: Passed by keybinding, not actually used.
		"""
		pw1 = self.option_menu.change_password.get()
		pw2 = self.option_menu.change_password_re.get()
		self.pw = pw1

		if (pw1 == "") or (pw2 == ""):
			self.Error("Bad Password Entry")
		elif (pw1 == pw2):
			self.option_menu.icpw.focus_set()
			self.main_option_menu.lowerFrame(self.option_menu.change_password_frame)
			self.open_window = "CurrentPassword"
			self.main_option_menu.liftFrame(self.option_menu.current_password_frame)
		else:
			self.Error("Passwords do not match")

# Checking if current password is correct
	def checkPassword(self, e):
		"""
		Fetch current password from password entry field. \n
		If password matches the password of the user, change the field (database)
		that is described by the attribute change string. \n
		Return to main menu.
		@param e: Passed by keybinding, not actually used.
		"""
		password = self.option_menu.icpw.get()
		username = self.menu_manager.user.username

		if (self.menu_manager.con.checkPassword(username, password)):
			if (self.att_change == "ChangePassword"):
				self.menu_manager.con.changePassword(username, self.pw)
				self.returnToMain("a")
			elif (self.att_change == "ChangeSec"):
				self.menu_manager.con.changeSecurity(username, self.question,
						self.answer)
				self.returnToMain("a")
			elif (self.att_change == "ChangeName"):
				self.menu_manager.con.changeName(username, self.realname)
				self.returnToMain("a")
		else:
			self.Error("Wrong Password")

# Cancel Password
	def cancelPassword(self, e):
		"""
		Cancel entering new password. \n
		Refocus on change password button.
		@param e: Passed by keybinding, not actually used.
		"""
		self.option_menu.deleteEntry(self.att_change)
		self.main_option_menu.liftFrame(self.option_menu.option_frame)
		self.option_menu.option_password_button.focus_set()

# Close current
	def closeCurrent(self, e):
		"""
		Cancel entering current password. \n
		Refocus on change password button.
		@param e: Passed by keybinding, not actually used.
		"""
		self.option_menu.deleteEntry(self.att_change)
		self.main_option_menu.liftFrame(self.option_menu.option_frame)
		self.option_menu.option_password_button.focus_set()

# error
	def Error(self, message):
		"""
		Open error message with messaged passed from where the error originated. \n
		Focus on close button.
		@param message: The message to be displayed on the error message.
		"""
		self.error_frame.error_button.focus_set()
		self.error_frame.error_message.configure(text = message)
		self.main_option_menu.liftFrame(self.error_frame.error_frame)

# close error
	def closeError(self, e):
		"""
		Close the error window. \n
		Focus on the appropriate field depending on where the error originated.
		@param e: Passed by keybinding, not actually used.
		"""
		self.main_option_menu.lowerFrame(self.error_frame.error_frame)

		if (self.open_window == "CurrentPassword"):
			self.option_menu.deleteEntry(self.open_window)
			self.option_menu.icpw.focus_set()
		elif (self.open_window == "ChangePassword"):
			self.option_menu.deleteEntry(self.open_window)
			self.option_menu.change_password.focus_set()
		elif (self.open_window == "ChangeName"):
			self.option_menu.deleteEntry(self.open_window)
			self.option_menu.change_realname.focus_set()
		elif (self.open_window == "ChangeSec"):
			self.option_menu.deleteEntry(self.open_window)
			self.option_menu.change_question.focus_set()

# Return to main menu
	def returnToMain(self, e):
		"""
		Return to main menu, unbind keys, destroy window.
		@param e: Passed by keybinding, not actually used.
		"""
		self.unBind()
		self.menu_manager.runMenu()
		self.main_option_menu.root.destroy()
