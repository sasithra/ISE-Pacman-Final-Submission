"""
Frame for the option menu.
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from display import FrameMaster
try:
	from tkinter import *
except:
	from Tkinter import *

class MainOptionFrame(FrameMaster.FrameMaster):
	"""
	MainOptionFrame class.
	This class contains the main options frame and initializes all the other Frames in this
	Frame.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, game):
		"""
		Initialization.
		This method creates a Main Option Frame and initializes all the other 
		frames related to it.
		
		@param game: Instance of the current Pacman game.
		"""
		
		#Initializes the FrameMaster
		FrameMaster.FrameMaster.__init__(self)

		# Initializes the options frame within this frame.
		self._of = OptionFrame(self.root)

class OptionFrame(Frame):
	"""
	OptionFrame class.
	This class contains the options frame and initializes all the other frames related to
	this options frame.
	It is of the tkinter library and inherits an instance of FrameMaster.
	"""
	def __init__(self, root):
		"""
		Initialization.
		This method creates a new Options Frame and initializes all the other 
		frames related to it, configures its size and its components.
		
		@param root: Root is the tkinter root of an instance of this class.
		"""
		
		#------------------------------------------------------------------------------
		# Creates this main frame and configures its rows and columns as well as 
		# its components.
		#------------------------------------------------------------------------------
		self.option_frame = Frame(root, bg = "black", borderwidth = 3, relief = 
				RIDGE)
		self.option_frame.grid(row = 1, rowspan = 6, column = 3, columnspan = 2,
				sticky = N+S+E+W)
		self.option_frame.grid_propagate(False)

		option_frame = self.option_frame
		
		for i in range(0,5):
			option_frame.rowconfigure(i, weight = 1)
			i = i + 1
		option_frame.columnconfigure(0, weight = 1)

		#------------------------------------------------------------------------------
		# Create and configure the options label at the top.
		#------------------------------------------------------------------------------
		Label(option_frame, text = "Options", fg = "yellow", bg = "black"
				).grid(column = 0, row = 0)

		#------------------------------------------------------------------------------
		# Create and configure the Change password button.
		#------------------------------------------------------------------------------
		self.option_password_button = Button(option_frame, bg = "black",
				text = "Change Password",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.option_password_button.grid(row = 1, sticky = E+W)

		#------------------------------------------------------------------------------
		# Create and configure the change real name button.
		#------------------------------------------------------------------------------
		self.option_realname_button = Button(option_frame, bg = "black",
				text = "Change Real Name",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.option_realname_button.grid(row = 2, sticky = E+W)

		#------------------------------------------------------------------------------
		# Create and configure the change security question/answer button.
		#------------------------------------------------------------------------------
		self.option_sec_button = Button(option_frame, bg = "black",
				text = "Change Question/Answer",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.option_sec_button.grid(row = 3, sticky = E+W)

		#------------------------------------------------------------------------------
		# Create and configure the close button.
		#------------------------------------------------------------------------------
		self.close = Button(option_frame, text = "Return to menu", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.close.grid(column = 0, row = 4, sticky = E+W)

		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the ask for current password entry field.
		#------------------------------------------------------------------------------
		self.current_password_frame = Frame(root, bg = "black", bd = 5,
				relief = RIDGE)
		self.current_password_frame.grid(column = 3, row = 3, rowspan = 2,
				columnspan = 2, sticky = N+S+E+W)
		self.current_password_frame.grid_propagate(False)
		self.current_password_frame.lower()

		for i in range(0,4):
			self.current_password_frame.rowconfigure(i, weight = 1)
		self.current_password_frame.columnconfigure(0, weight = 1)

		cp = self.current_password_frame
		
		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the enter current password field.
		#------------------------------------------------------------------------------
		Label(cp, bg = "black", fg = "yellow",
				text = "Please enter \n your current Password").grid(row = 0, 
						sticky = N+S+E+W)

		self.icpw = Entry(cp, show = "*")
		self.icpw.grid(row = 1)

		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the Change password confirmation button.
		#------------------------------------------------------------------------------
		self.cpw_button = Button(cp, bg = "black", text = "Change",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.cpw_button.grid(row = 2, sticky = E+W)

		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the Cancel button.
		#------------------------------------------------------------------------------
		self.cancel_button = Button(cp, bg = "black", text = "Cancel",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.cancel_button.grid(row = 3, sticky = E+W)

		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the new password entry field.
		#------------------------------------------------------------------------------
		self.change_password_frame = Frame(root, bg = "black", bd = 5, 
				relief = RIDGE)
		self.change_password_frame.grid(column = 3, row = 2, rowspan = 3,
				columnspan = 2, sticky = N+S+E+W)
		self.change_password_frame.grid_propagate(False)
		self.change_password_frame.lower()

		for i in range(0,6):
			self.change_password_frame.rowconfigure(i, weight = 1)

		self.change_password_frame.columnconfigure(0, weight = 1)

		change_password_frame = self.change_password_frame

		#------------------------------------------------------------------------------
		# CHANGE PASSWORD:
		# Create and configure the new password re entry field.
		#------------------------------------------------------------------------------
		Label(change_password_frame, text = "Change Password to", bg = "black",
				fg = "yellow").grid(row = 0, column = 0, sticky = N+S+E+W)

		self.change_password = Entry(change_password_frame, show = "*")
		self.change_password.grid(row = 1, column = 0)

		Label(change_password_frame, text = "Retype new Password", bg = "black",
				fg = "yellow").grid(row = 2, column = 0, sticky = N+S+E+W)

		self.change_password_re = Entry(change_password_frame, show = "*")
		self.change_password_re.grid(row = 3, column = 0)

		self.password_button = Button(change_password_frame,
				text = "Change Password", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.password_button.grid(row = 4, column = 0, sticky = E+W, pady = 10)

		self.close_password = Button(change_password_frame,
				text = "Close", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.close_password.grid(row = 5, column = 0, sticky = E+W, pady = 10)

		#------------------------------------------------------------------------------
		# CHANGE REAL NAME:
		# Create and configure the Change real name option button.
		#------------------------------------------------------------------------------
		self.change_realname_frame = Frame(root, bg = "black", bd = 5, 
				relief = RIDGE)
		self.change_realname_frame.grid(column = 3, row = 3, columnspan = 2,
				rowspan = 2, sticky = N+S+E+W)
		self.change_realname_frame.grid_propagate(False)
		self.change_realname_frame.lower()

		for i in range(0,4):
			self.change_realname_frame.rowconfigure(i, weight = 1)
		self.change_realname_frame.columnconfigure(0, weight = 1)

		change_realname_frame = self.change_realname_frame

		Label(change_realname_frame, text = "Change Real Name", bg = "black",
				fg = "yellow").grid(row = 0, sticky = N+E+W)

		self.change_realname = Entry(change_realname_frame)
		self.change_realname.grid(row = 1)

		#------------------------------------------------------------------------------
		# CHANGE REAL NAME:
		# Create and configure the Change real name option button button.
		#------------------------------------------------------------------------------
		self.realname_button = Button(change_realname_frame,
				text = "Change Real Name", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.realname_button.grid(row = 2, stick = N+S+E+W, pady = 10)

		#------------------------------------------------------------------------------
		# CHANGE REAL NAME:
		# Create and configure the close button.
		#------------------------------------------------------------------------------
		self.realname_close = Button(change_realname_frame,
				text = "Close", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.realname_close.grid(row = 3, stick = N+S+E+W, pady = 10)
		
		#------------------------------------------------------------------------------
		# CHANGE SECURITY QUESTION AND ANSWER:
		# Create and configure the Change Security question and answer entry field field.
		#------------------------------------------------------------------------------
		self.question_and_answer = Frame(root, bg = "black", bd = 5, 
				relief = RIDGE)
		self.question_and_answer.grid(column = 3, row = 2, columnspan = 2,
				rowspan = 3, sticky = N+S+E+W)
		self.question_and_answer.grid_propagate(False)
		self.question_and_answer.lower()

		for i in range(0,7):
			self.question_and_answer.rowconfigure(i, weight = 1)
		self.question_and_answer.columnconfigure(0, weight = 1)

		question_and_answer = self.question_and_answer

		Label(question_and_answer, text = "Change Question and Answer",
				bg = "black", fg = "yellow").grid(row = 0, sticky = N+S+E+W)

		#------------------------------------------------------------------------------
		# CHANGE SECURITY QUESTION AND ANSWER:
		# Create and configure the insert new question and answer entry field.
		#------------------------------------------------------------------------------
		Label(question_and_answer, text = "New Question", bg = "black",
				fg = "yellow").grid(row = 1, sticky = N+S+E+W)

		self.change_question = Entry(question_and_answer)
		self.change_question.grid(row = 2)

		Label(question_and_answer, text = "New Answer", bg = "black",
				fg = "yellow").grid(row = 3, sticky = N+S+E+W)

		self.change_answer = Entry(question_and_answer)
		self.change_answer.grid(row = 4)

		#------------------------------------------------------------------------------
		# CHANGE SECURITY QUESTION AND ANSWER:
		# Create and configure the Cnage security question/answer button.
		#------------------------------------------------------------------------------
		self.qa_button = Button(question_and_answer,
				text = "Change Question and Answer", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.qa_button.grid(row = 5, sticky = N+S+E+W, pady = 10)

		#------------------------------------------------------------------------------
		# CHANGE SECURITY QUESTION AND ANSWER:
		# Create and configure the Close button.
		#------------------------------------------------------------------------------
		self.qa_close = Button(question_and_answer,
				text = "Close", bg = "black",
				fg = "yellow", highlightcolor = "red", highlightbackground
				= "yellow", activebackground = "black", activeforeground
				= "red")
		self.qa_close.grid(row = 6, sticky = N+S+E+W, pady = 10)

	#------------------------------------------------------------------------------
	# Helper method: Deleted the text entered in the fields.
	#------------------------------------------------------------------------------
	def deleteEntry(self, window):
		"""
		Delete the text in an entry field.
		@param window: The entry field in which the text will be deleted.
		"""
		if (window == "ChangePassword"):
			self.change_password.delete(0, END)
			self.change_password_re.delete(0, END)
		elif (window == "CurrentPassword"):
			self.icpw.delete(0, END)
