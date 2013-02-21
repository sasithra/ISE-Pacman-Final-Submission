"""
This Module contains the frame classes that deal with the Forgot password menu.
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""

from display import ForgotFrame

## Forgot Password functionality
class ForgotMenu():

	"""
	This class deals with the Forgot (password) Menu components.
	"""

	def __init__(self, menu_manager):

		"""
		Class contructor for the Forgot Menu Class. \n
		Initializes the window and menu components. \n
		Sets up keybindings.
		@param menu_manager: The game object (from org/Pacman.py)
		"""

		self.menu_manager = menu_manager
		self.uiCoordinator = menu_manager.uiCoordinator
		self.open_window = False
		self.username = ""
		self.frame_opened = ""

		self.setupWindow()
		self.setupBinds()

## Setup window
	def setupWindow(self):

		"""
		sets up the window.
		"""

		self.main_forgot_frame = ForgotFrame.ForgotPassFrame(self.uiCoordinator)
		self.forgot_frame = self.main_forgot_frame._ff
		self.error_frame = self.main_forgot_frame._ef
		self.forgot_frame.iuname.focus_set()
		self.change_frame = self.main_forgot_frame._cf

## setup keybinds
	def setupBinds(self):

		"""
		Sets up keybindings.
		"""

		self.forgot_frame.exit.bind("<Button-1>", self.closeForgotPass)
		self.forgot_frame.exit.bind("<Return>", self.closeForgotPass)

		self.forgot_frame.iuname.bind("<Return>", self.getQuestion)
		self.forgot_frame.name_button.bind("<Button-1>", self.getQuestion)
		self.forgot_frame.name_button.bind("<Return>", self.getQuestion)

		self.error_frame.error_button.bind("<Button-1>", self.closeError)
		self.error_frame.error_button.bind("<Return>", self.closeError)

## Unbind keys
	def unBind(self):

		"""
		Unbind keys.
		"""

		self.forgot_frame.exit.unbind("<Button-1>")
		self.forgot_frame.iuname.unbind("<Return>")
		self.forgot_frame.name_button.unbind("<Button-1>")
		self.forgot_frame.name_button.unbind("<Return>")
		self.forgot_frame.ianswer.unbind("<Return>")
		self.forgot_frame.newButton.unbind("<Button-1>")
		self.forgot_frame.newButton.unbind("<Return>")
		self.error_frame.error_button.unbind("<Button-1>")
		self.error_frame.error_button.unbind("<Return>")
		self.forgot_frame.exit.unbind("<Return>")

## Bind Change Frame Keys
	def bindChangeFrame(self):

		"""
		Binds items on the change frame (where new passwords are entered)
		"""

		self.change_frame.ipw1.bind("<Return>", self.changePassword)
		self.change_frame.ipw2.bind("<Return>", self.changePassword)
		self.change_frame.change_button.bind("<Button-1>", self.changePassword)
		self.change_frame.close_button.bind("<Button-1>", self.closeChangePassword)

## Unbind Change Frame Keys
	def unbindChangeFrame(self):

		"""
		Unbinds items on the change frame
		"""

		self.change_frame.ipw1.unbind("<Return>")
		self.change_frame.ipw2.unbind("<Return>")
		self.change_frame.change_button.unbind("<Button-1>")
		self.change_frame.close_button.unbind("<Button-1>")

## Check answer and bring up password change prompt
	def checkAnswer(self, e):

		"""
		Checks if the security answer is correct (though db interaction). \n
		Opens error frame if the answer is wrong.
		@param e: Passed by keybinding, not actually used.
		"""

		answer = self.forgot_frame.ianswer.get()
		if self.menu_manager.con.checkAnswer(self.username, answer):
			self.changePasswordFrame()
		else:
			self.error_frame.error_message.configure(text = "Wrong answer.")
			self.openErrorFrame("CheckAnswer")
			self.open_window = True

## Get and display security question
	def getQuestion(self, e):
		
		"""
		Fetch the security question (db interaction). \n
		Open error frame if the username doesn't exist.
		@param e: Passed by keybinding, not actually used.
		"""

		self.username = self.forgot_frame.iuname.get()
		if self.menu_manager.con.checkUser(self.username):
			question = self.menu_manager.con.getQuestion(self.username)
			self.forgot_frame.iquestion.configure(text = question)

			self.forgot_frame.setNormal()
			self.forgot_frame.ianswer.focus_set()
			self.forgot_frame.ianswer.bind("<Return>", self.checkAnswer)
			self.forgot_frame.newButton.bind("<Button-1>", self.checkAnswer)
			self.forgot_frame.newButton.bind("<Return>", self.checkAnswer)
		else:
			self.error_frame.error_message.configure(text = "Bad Username")
			self.openErrorFrame("Name")
			self.open_window = True

## Close change password window withou changing password
	def closeChangePassword(self, e):

		"""
		Close the change password frame.
		@param e: Passed by keybinding, not actually used.
		"""

		self.unbindChangeFrame()
		self.change_frame.deleteEntry()
		self.forgot_frame.lowerFrame(self.change_frame.change_frame)

## To change password screen
	def changePasswordFrame(self):

		"""
		Open change password frame (and focus on first password field).
		"""

		self.change_frame.username.configure(text = self.username)
		self.change_frame.ipw1.focus_set()
		self.bindChangeFrame()
		self.main_forgot_frame.liftFrame(self.change_frame.change_frame)

## Change password
	def changePassword(self, e):

		"""
		Change password. Checks if the password in the first field matches 
		the password in the second field. \n
		Open error frame if the passwords don't match.
		@param e: Passed by keybinding, not actually used.
		"""

		pw1 = self.change_frame.ipw1.get()
		pw2 = self.change_frame.ipw2.get()

		if (pw1 == pw2):
			self.menu_manager.con.changePassword(self.username, pw1)
			self.unBind()
			self.unbindChangeFrame()
			self.menu_manager.runLogin()
		else:
			self.error_frame.error_message.configure(text = "Passwords do not match")
			self.openErrorFrame("Password")
			
## Return to login
	def closeForgotPass(self, e):

		"""
		Close the Forgot (password) Menu and return to the Login Menu.
		@param e: Passed by keybinding, not actually used.
		"""

		self.menu_manager.runLogin()
		self.unBind()
		self.main_forgot_frame.root.destroy()

## Has error frame remember which window brought it up
	def openErrorFrame(self, frame):

		"""
		Open the error Frame.
		@param frame: The last frame open (to know which screen to focus back on)
		"""

		self.frame_opened = frame
		self.forgot_frame.liftFrame(self.error_frame.error_frame)
		self.error_frame.error_button.focus_set()

## hide Error window
	def closeError(self, e):

		"""
		Close the error frame. \n
		Refocus on the previous frame/field.
		@param e: Passed by keybinding, not actually used.
		"""

		self.main_forgot_frame.lowerFrame(self.error_frame.error_frame)
		self.open_window = False
		if (self.frame_opened == "CheckAnswer"):
			self.forgot_frame.removeEntry(self.forgot_frame.ianswer)
			self.forgot_frame.ianswer.focus_set()
		elif (self.frame_opened == "Name"):
			self.forgot_frame.removeEntry(self.forgot_frame.iuname)
			self.forgot_frame.iuname.focus_set()
		elif (self.frame_opened == "Password"):
			self.change_frame.deleteEntry()
			self.change_frame.ipw1.focus_set()
