"""
Pacman, the game.
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
from display import GameFrame, LoginFrame, MenuFrame
from menu import GameMenu, OptionsMenu, LoginMenu, NewUser, ForgotMenu
from gameplay import Gameplay
from db import DbInt as db
from time import *
try:
	from tkinter import *
except:
	from Tkinter import *


class Game():
	"""
	This controls the flow of the menus into each other and the game.
	"""
	def __init__(self, uiCoordinator, user, level, high_scores):
		"""
		Inits the game. Creates db connections, updates it's user variables.
		@param uiCoordinator: The root tk.
		@param user: The user of the game.
		@param level: The first level to be played.
		@param high_scores: The high scores.
		"""
		self.con = db.Connection('Pacman.db')
		self.uiCoordinator = uiCoordinator
		self.user = user
		self.current_score = user.highscore
		self.high_scores = self.con.getHighscores("DESC")
		self.level = level
		self.runLogin()

## Update user
	def updateUser(self):
		"""
		Updates the user.
		"""
		self.user = Guest()

## Update Highscores
	def updateHighscores(self):
		"""
		Updates the high score.
		"""
		if (self.user.username != "Guest"):
			if (self.current_score < self.user.highscore):
				self.current_score = self.user.highscore
				self.con.updatePersonalHighscore(user)
			self.con.updateHighscore(user)

## Login
	def runLogin(self):
		"""
		Runs the login menu.
		"""
		self.newGame = LoginMenu.LoginMenu(self)

## Forgot password
	def runForgot(self):
		"""
		Runts the forgot menu.
		"""
		self.newGame = ForgotMenu.ForgotMenu(self)

## Menu
	def runMenu(self):
		"""
		Runs the main menu.
		"""
		self.newGame = GameMenu.GameMenu(self)

## Options
	def runOptions(self):
		"""
		Runs the options menu.
		"""
		self.newGame = OptionsMenu.OptionMenu(self)
		
## New User
	def runNewUser(self):
		"""
		Runs the new user menu.
		"""
		self.newGame = NewUser.NewUserMenu(self)

## Game
	def runGame(self):
		"""
		Runts the game.
		"""
		self.newGame = Gameplay.GamePlay(self, user, level)
		self.uiCoordinator.after(5000, self.newGame.start)


class Account(object):
	"""
	This class is an account class for users.
	"""
	def __init__(self, username, highscore, score):
		"""
		Inits the account object.
		@param username: The name of the account user.
		@param highscore: The high score of the account user.
		@param score: The current score of the account user.
		"""
		self.username = username
		self.score = score
		self.highscore = highscore
	
	def getUsername(self):
		"""
		Returns username.
		@return: Username.
		"""
		return self.username
	
	def getScore(self):
		"""
		Returns the score
		@return: Score
		"""
		return self.score
	
	def getHighScore(self):
		"""
		Returns the high score
		@return: High score.
		"""
		return self.highscore
	
	def setScore(self, newScore):
		"""
		Sets the score.
		@param newScore: The new score to be set.
		"""
		self.score = newScore
	
	def setHighScore(self, newHighScore):
		"""
		Sets the high score.
		@param newHighScore: The high score to be set.
		"""
		self.highscore = newHighScore


class HighScores():
	def __init__(self):
		self.highscores = []

		for i in range(0,10):
			self.highscores.append(0)



class User(Account):
	def __init__(self):
		super(User, self).__init__("", 0, 0)
		
class Guest(Account):
	def __init__(self):
		super(Guest, self).__init__("Guest", 0, 0)

class RootConfigure(Frame):
	"""Configures the game window"""
	def __init__(self, root):
		"""
		Configures the game window
		@param root: The root tk frame
		"""
		Frame.__init__(self,root)
		root.geometry("800x600")
		root.title("Pacman v0.1")

		root.columnconfigure(0, weight = 1)
		root.rowconfigure(0, weight = 1)
		root.grid_propagate(False)

		
high_scores = HighScores()
user = User()
level = 1

root = Tk()
RootConfigure(root)
game = Game(root, user, level, high_scores)
root.mainloop()
