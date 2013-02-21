"""
Forgot Frame for forgot menu.
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

class ForgotPassFrame(FrameMaster.FrameMaster):
	"""
	Forgot Pass Frame class.
	This class contains the methods used in the creation and interaction of the popup
	when Forgot Password is selected in Gameplay.
	It is of the tkinter library and inherits an instance of FrameMaster.

	"""
	def __init__(self, game):
		"""
		Initialization.
		This method creates a new Forgot Password frame and initializes the 
		Change Frame and Forgot Frame.
		
		@param game: Game Frame instance that this frame is being used in.
		"""
		
		# Initializing FrameMaster to be used here
		FrameMaster.FrameMaster.__init__(self)
		
		# Initializes the ChageFrame and ForgotFrame classes to be used here
		self._cf = ChangeFrame(self.root)
		self._ff = ForgotFrame(self.root)

class ChangeFrame(ForgotPassFrame):
	"""
	Change Frame class.
	This class contains the methods used in the creation and interaction or the popup
	when Forgot Password is selected in Gameplay.
	It is of the tkinter library and inherits an instance of ForgotPassFrame.
	"""
	def __init__(self, main):
		"""
		Initialization.
		This method creates a new Change Password frame and cofigures its Canvas 
		Buttons and all other related Canvas Labels related to the Frame.
		
		@param main: Instance of the ForgotFrame class that this class is used in.
		"""
		
		#------------------------------------------------------------------------------
		# Drawing the frame, configuring its rows and columns and creating the text
		# labels required in this frame. 
		# NOTE: Passwords entered are masked and only "*" characters are shown for 
		# added privacy.
		#------------------------------------------------------------------------------
		self.change_frame = Frame(main, bg = "black", borderwidth = 3, relief = RIDGE)
		self.change_frame.grid(row = 1, rowspan = 6,  column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.change_frame.grid_propagate(False)
		
		for i in range(0, 7):
			self.change_frame.rowconfigure(i, weight = 1)
		self.change_frame.columnconfigure(0, weight = 1)

		self.change_frame.lower()

		self.username = Label(self.change_frame, bg = "black", fg = "yellow")
		self.username.grid(row = 0, sticky = E+W)

		#------------------------------------------------------------------------------
		# Configuring Enter new password field entry.
		#------------------------------------------------------------------------------
		h1 = Label(self.change_frame, text = "Enter new password:", fg = "yellow",
				bg = "black")
		h1.grid(row = 1, sticky = E+W)

		self.ipw1 = Entry(self.change_frame, show = "*")
		self.ipw1.grid(row = 2, sticky = E+W)

		#------------------------------------------------------------------------------
		# Configuring Reenter new password field entry.
		#------------------------------------------------------------------------------
		h2 = Label(self.change_frame, text = "Re-enter new password:", bg = "black",
				fg = "yellow")
		h2.grid(row = 3, sticky = E+W)

		self.ipw2 = Entry(self.change_frame, show = "*")
		self.ipw2.grid(row = 4, sticky = E+W)

		#------------------------------------------------------------------------------
		# Configuring Change password entry.
		#------------------------------------------------------------------------------
		self.change_button = Button(self.change_frame, text = "Change Password", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.change_button.grid(row = 5, sticky = E+W)

		#------------------------------------------------------------------------------
		# Configuring close entry.
		#------------------------------------------------------------------------------
		self.close_button = Button(self.change_frame, text = "Close", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.close_button.grid(row = 6, sticky = E+W)

	#------------------------------------------------------------------------------
	# Helper method: Deletes the text that is entered in the available fields.
	#------------------------------------------------------------------------------
	def deleteEntry(self):
		self.ipw1.delete(0, END)
		self.ipw2.delete(0, END)

class ForgotFrame(ForgotPassFrame):
	"""
	ForgotFrame class.
	This class contains the methods used in the creation and interaction of the frame when the
	User has to reset their password when they forgot their password.
	It is of the tkinter library and inherits an instance of ForgotPassFrame.
	"""
	def __init__(self, main):
		"""
		Initialization.
		This method creates a new Change Password frame and cofigures its Canvas 
		Buttons and all other related Canvas Labels related to the Frame.
		
		@param main: Instance of the ForgotFrame class that this class is used in.
		"""
		
		#------------------------------------------------------------------------------
		# Drawing the frame, configuring its rows and columns.
		#------------------------------------------------------------------------------
		self.forgot_frame = Frame(main, bg = "black", borderwidth = 3, relief = 
				RIDGE)
		self.forgot_frame.grid(row = 1, rowspan = 6, column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.forgot_frame.grid_propagate(False)

		root = self.forgot_frame

		for i in range(0,5):
			root.rowconfigure(i, weight = 1)
		for j in range(0,2):
			root.columnconfigure(j, weight = 1)

		#------------------------------------------------------------------------------
		# Configuring the welcome window
		#------------------------------------------------------------------------------
		welcomeFrame = Frame(root, height = 100, width = 200)
		welcome = Label(welcomeFrame, text = "New User", bg = "black",
				fg = "yellow")
		welcome.pack(fill = BOTH, side = TOP)
		welcomeFrame.grid(row = 0, column = 0, columnspan = 2,
				sticky = N)
		welcomeFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring User Name entry.
		#------------------------------------------------------------------------------
		unameFrame = Frame(root, height = 100, width = 200, bg = "black")
		uname = Label(unameFrame, text = "User Name:", bg = "black",
				fg = "yellow")
		uname.pack(fill = BOTH, side = TOP)
		self.iuname = Entry(unameFrame)
		self.iuname.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Configuring entry that Gets the Security Question associated with user.
		#------------------------------------------------------------------------------
		self.name_button = Button(unameFrame, text = "Get Question", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red")
		self.name_button.pack(fill = BOTH, side = TOP, pady = 5)

		unameFrame.grid(row = 1, column = 0, columnspan = 2,
				sticky = N)
		unameFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring Security Question entry.
		#------------------------------------------------------------------------------
		questionFrame = Frame(root, height = 100, width = 200)
		question = Label(questionFrame, text = "Security Question:", bg = "black",
				fg = "yellow")
		question.pack(fill = BOTH, side = TOP)
		self.iquestion = Label(questionFrame, bg = "black", fg = "yellow")
		self.iquestion.pack(fill = BOTH, side = TOP)
		questionFrame.grid(row = 2, column = 0, columnspan = 2,
				sticky = N)
		questionFrame.grid_propagate(False)

		#------------------------------------------------------------------------------
		# Configuring the Security Answer entry.
		#------------------------------------------------------------------------------
		answer = Label(questionFrame, text = "Answer:", bg = "black", fg = "yellow")
		answer.pack(fill = BOTH, side = TOP)
		self.ianswer = Entry(questionFrame, state = DISABLED)
		self.ianswer.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Configuring Change Password entry.
		#------------------------------------------------------------------------------
		buttonFrame = Frame(root, bg = "black", height = 100, width = 200)
		buttonFrame.grid(row = 3, column = 0, columnspan = 2, sticky = N+S+E+W)
		self.newButton = Button(buttonFrame, text = "Change Password", bg = "black",
				fg = "yellow",highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red", state = DISABLED)
		self.newButton.pack(fill = BOTH, side = TOP)

		#------------------------------------------------------------------------------
		# Configuring Exit entry.
		#------------------------------------------------------------------------------
		exitFrame = Frame(root, height = 100, width = 200, bg = "black")
		self.exit = Button(exitFrame, text = "Exit", bg = "black", fg = "yellow", 
				highlightcolor = "red", highlightbackground = "yellow",
				activebackground = "black", activeforeground = "red",
				width = 10)
		self.exit.pack(fill = BOTH)
		exitFrame.grid(row = 4, column = 0, rowspan = 1, columnspan = 2,
				sticky = N+S+E+W)
		exitFrame.grid_propagate(False)

	#------------------------------------------------------------------------------
	# Helper Method: Allow writing and button pressing.
	#------------------------------------------------------------------------------
	def setNormal(self):
		"""
		Allows the user to write in the answer field and press the new password
		button.
		"""
		self.ianswer.configure(state = NORMAL)
		self.newButton.configure(state = NORMAL)

	#------------------------------------------------------------------------------
	# Helper Method: Remove text from entry widget
	#------------------------------------------------------------------------------
	def removeEntry(self, widget):
		"""
		Remove the text in an entry field.
		"""
		widget.delete(0, END)
