"""
This Module contains the database connection class "Connection"
@author: Shaun Hamelin-Owens
@author: Jason Cohen
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
import sqlite3 as lite
import sys


class Connection:
	def __init__(self, db_name):

		"""
		Class Contructor for the database connection. \n
		Initializes connection to the database, and creates/initializes tables if
		there is need. \n
		The game produces/reads from a database located in the same folder as 
		the Pacman.py file \n

		@param db_name: The name of the database we are connecting to.
		"""

		self.con = lite.connect(db_name)
		with self.con:
			self.cur = self.con.cursor()
			self.createTables()
			self.iniTables()

# Create tables
	def createTables(self):

		"""
		Creates tables if they do not exist.
		"""

		self.cur.execute("CREATE TABLE IF NOT EXISTS Users("
				"name STRING, "
				"password STRING, "
				"realname STRING, "
				"question STRING, "
				"answer STRING, "
				"highscore INT)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS Highscores("
				"id INT,"
				"name STRING,"
				"score INT)")

# Create User
	def createUser(self, username, password, realname, question, answer):

		"""
		Creates a new user from the values obtained on screen.\n
		@param username: The unsername of the new user.
		@param password: The password of the new user.
		@param realname: The real name of the new user.
		@param question: The security question for the new user.
		@param answer: The security answer for the new user.
		"""

		with self.con:
			self.cur.execute("INSERT INTO Users VALUES('"
					+str(username)+"','"
					+password+"','"
					+realname+"','"
					+question+"','"
					+answer+"',"
					"0000);")

# Init highscore if empty
	def iniTables(self):

		"""
		Initializes Highscores to populate with username Empty, highscore 0000.
		"""

		with self.con:
			self.cur.execute("SELECT * FROM Highscores;")
			i = len(self.cur.fetchall())
			if (i == 0):
				for j in range(0, 10):
					self.cur.execute("INSERT INTO Highscores VALUES("
							""+str(j+1)+","
							"'Empty',"
							"0000);")

# Check if user exists
	def checkUser(self, username):

		"""
		Checks if user already exists.
		@param username: Username to be checked.
		@return: Returns true of user exists, false if it doesn't
		"""

		with self.con:
			self.cur.execute("SELECT name FROM Users WHERE name='"+username+"';")
			i = len(self.cur.fetchall())
			if i == 1:
				return True
			else:
				return False

# Check if answe is correct
	def checkAnswer(self, username, answer):

		"""
		Checks if the answer is the correct answer for the username.
		@param username: username to check answer to.
		@param answer: answer to be checked.
		@return: Returns true if the answer is correct, false if incorrect
		"""

		with self.con:
			self.cur.execute("SELECT name FROM Users WHERE name='"+username+"'"
					" AND answer='"+answer+"';")
			i = len(self.cur.fetchall())
			if i == 1:
				return True
			else:
				return False

# Check if user is associated with password
	def checkPassword(self,username, password):

		"""
		Checks the password of the username.
		@param username: username to check password to.
		@param password: password to be checked.
		"""

		with self.con:
			self.cur.execute("SELECT name FROM Users WHERE name='"+username+"' AND"
					" password='"+password+"';")
			i = len(self.cur.fetchall())
			if i == 1:
				return True
			else:
				return False

# Get the user's security question
	def getQuestion(self, username):

		"""
		Fetch the security question associated to the username.
		@param username: username to get question for
		@return: Returns the security question associated to the username
		"""

		with self.con:
			self.cur.execute("SELECT question FROM Users WHERE name='"
					+username+"';")
			question = self.cur.fetchall()
			for qst in question:
				for q in qst:
					return q

# Get the user's personal best
	def getScore(self, username):

		"""
		Fetch the user's high score.
		@param username: the username to get the highscore for.
		@return: Returns the highscore associated to the username.
		"""

		with self.con:
			self.cur.execute("SELECT highscore FROM Users WHERE name='"
					+username+"';")
			score = self.cur.fetchall()
			for sc in score:
				for s in sc:
					return s

# Update High scores
	# def updateHighscores(self, user):
		# self.updatePersonalHighscore(user)
		# self.updateHighscore(user)

## Update User's high score
	def updatePersonalHighscore(self, user):

		"""
		Update the high score associated to a user.
		@param user: user object containing the parameters for which the highscore
		will be updated. (user.highscore, user.username) Note: should probably be 
		changed to take username and highscore separately
		"""

		with self.con:
			score = user.highscore
			name = user.username
			self.cur.execute("UPDATE Users "
					"SET highscore="+str(score)+" "
					"WHERE name='"+str(name)+"';")

## Update High Score list
	def updateHighscore(self, user):

		"""
		Updates the high scores list with a new username/highscore entry
		@param user: user object containing the parameters for which the highscore
		will be updated. (user.highscore, user.username) Note: should probably be 
		changed to take username and highscore separately
		"""

		with self.con:
			ID = True
			name = user.username
			userscore = user.score
			scores = self.getHighscoreRecords("ASC")
			for score in scores:
				for field in score:
					# print field
					try:
						if (ID):
							id_ = int(field)
							# print id_
							ID = False
						elif (not ID) and (int(userscore) > int(field)):
							# print field
							self.cur.execute("UPDATE Highscores "
									"SET name='"+str(name)+"', score="+str(userscore)+" "
									"WHERE id="+str(id_)+"")
							return
						elif (not ID) and (int(userscore) < int(field)):
							ID = True
					except:
						print "error updateHighscore"
						ID = False

# Change Password
	def changePassword(self, name, password):

		"""
		Change password for the user.
		@param name: Username for which the password will be changed.
		@param password: New password for the user.
		"""

		with self.con:
			self.cur.execute("UPDATE Users "
					"SET password='"+password+"' "
					"WHERE name='"+name+"';")

# Return Real Name
	def getName(self, username):

		"""
		Fetches the real name of the user.
		@param username: Username for which the real name will be returned.
		@return: Returns the real name for the user.
		"""

		with self.con:
			self.cur.execute("SELECT realname FROM Users WHERE name='"
					+username+"';")
			name = self.cur.fetchall()
			for na in name:
				for n in na:
					return n

# Change Real Name
	def changeName(self, name, realname):

		"""
		Change the real name of the user.
		@param name: The username for which the real name will be changed.
		@param realname: The real name that will be changed too.
		"""

		with self.con:
			self.cur.execute("UPDATE Users "
					"SET realname='"+realname+"'"
					"WHERE name='"+name+"'")

# Change Security
	def changeSecurity(self, name, question, answer):

		"""
		Change the security question/answer for the user.
		@param name: The username for which security will be changed.
		@param question: The new question for the username.
		@param answer: The new answer for the username
		"""

		with self.con:
			self.cur.execute("UPDATE Users "
					"SET question='"+question+"',"
					" answer='"+answer+"' "
					"WHERE name='"+name+"';")


# Get a list of high scores
	def getHighscores(self, direction):

		"""
		Fetch the list of high scores
		@param direction: The direction to sort (ascending, descending)
		@return: Returns an array of 10 entries, 3 entries long (id, username, highscore).
		"""

		with self.con:
			self.cur.execute("SELECT * FROM Highscores ORDER BY score "
					""+str(direction)+" LIMIT 10;")
			return self.cur.fetchall()

	def getHighscoreRecords(self, direction):
		
		"""
		Fetch the list of high scores
		@param direction: The direction to sort (ascending, descending)
		@return: Returns an array of 10 entries, 2 entries long. (id, highscore)
		"""

		with self.con:
			self.cur.execute("SELECT id, score FROM Highscores ORDER BY score "
					""+str(direction)+" LIMIT 10;")
			return self.cur.fetchall()
