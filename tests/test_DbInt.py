import sqlite3 as lite
import sys
sys.path.append('../src/org')
import os

from db import DbInt as db

import unittest

class Account(object):
	def __init__(self, username, score, highscore):
		self.username = username
		self.score = score
		self.highscore = highscore
	
	def getUsername(self):
		return self.username
	
	def getScore(self):
		return self.score
	
	def getHighScore(self):
		return self.highscore
	
	def setScore(self, newScore):
		self.score = newScore
	
	def setHighScore(self, newHighScore):
		self.highscore = newHighScore


class HighScores():
	def __init__(self):
		self.highscores = []

		for i in range(0,10):
			self.highscores.append(0)

class User(Account):
	def __init__(self,user,score,highscore):
		super(User, self).__init__(user, score, highscore)

class test_DbInt(unittest.TestCase):
	def setUp(self) :
		#If all tests pass, than iniTable and createTable work properly (they are called when Connection is made)
		self.dbTest = db.Connection('Test_Pacman.db')

		#If Player and JohnDoe are not created, create them
		if not self.dbTest.checkUser("Player"):
			self.dbTest.createUser("Player","pass","Gary","Q1?","A1")
		if not self.dbTest.checkUser("JohnDoe"):
			self.dbTest.createUser("JohnDoe","swordfish", "John", "Q2?","A2")
        
	def test_checkUser(self):
		#If this passes than createUser,createTables and iniTables function properly
		#Check for existing player
		self.assertTrue(self.dbTest.checkUser("Player"))
		self.assertTrue(self.dbTest.checkUser("JohnDoe")) 		 	      
		#Check for non-existing player
		self.assertFalse(self.dbTest.checkUser("NotAPlayer"))

	def test_checkAnswer(self):
		#Check if answers match
		self.assertTrue(self.dbTest.checkAnswer("JohnDoe","A2"))
		#Check for non-matching, existing username and answer
		self.assertFalse(self.dbTest.checkAnswer("Player","A2"))
		self.assertFalse(self.dbTest.checkAnswer("JohnDoe","A1"))
		#Check for existing user with non-existant answer
		self.assertFalse(self.dbTest.checkAnswer("Player","NotAnAnswer"))
		self.assertFalse(self.dbTest.checkAnswer("JohnDoe","NotAnAnswer"))
		#Check for non-existant user with existing answer
		self.assertFalse(self.dbTest.checkAnswer("NotAPlayer","A1"))
		self.assertFalse(self.dbTest.checkAnswer("NotAPlayer","A2"))
		#Check for non-existant user with non-existant answer
		self.assertFalse(self.dbTest.checkAnswer("NotAPlayer","NotAnAnswer"))

	def test_checkPassword(self):
		#Check for existing player and password
		self.assertTrue(self.dbTest.checkPassword("Player","pass"))
		self.assertTrue(self.dbTest.checkPassword("JohnDoe","swordfish"))
		#Check for existing player and non-existing password
		self.assertFalse(self.dbTest.checkPassword("Player","notapassword"))
		self.assertFalse(self.dbTest.checkPassword("JohnDoe","notapassword"))
		#Check for existing player with another player's password 
		self.assertFalse(self.dbTest.checkPassword("Player","swordfish"))
		self.assertFalse(self.dbTest.checkPassword("JohnDoe","pass"))
		#Check for non-existing player with existing password
		self.assertFalse(self.dbTest.checkPassword("NotAPlayer","pass"))
		self.assertFalse(self.dbTest.checkPassword("NotAPlayer","swordfish"))
		#Check for non-existing player and non-existing password
		self.assertFalse(self.dbTest.checkPassword("NotAPlayer","notapassword"))

	def test_getQuestion(self):
		#Get existing player's question
		self.assertEqual(self.dbTest.getQuestion("JohnDoe"),"Q2?")
		#Get non-existing player's question
		self.assertEqual(self.dbTest.getQuestion("NotAPlayer"),None)

	def test_getScore(self):
		#Check existing scores		
		user1 = User("Player", "0", "1000")
		user2 = User("JohnDoe", "10", "2000")	
		self.dbTest.updatePersonalHighscore(user1)
		self.dbTest.updatePersonalHighscore(user2)
		self.assertEqual(self.dbTest.getScore(user1.username),1000)
		self.assertEqual(self.dbTest.getScore(user2.username),2000)
		user1.highscore = 2000
		user2.highscore = 4000
		self.dbTest.updatePersonalHighscore(user1)
		self.dbTest.updatePersonalHighscore(user2)
		#Check for updated scores
		self.assertEqual(self.dbTest.getScore(user1.username),2000)
		self.assertEqual(self.dbTest.getScore(user2.username),4000)	
       
	def test_getHighscores(self):
		#This function will only work if updatePersonalHighscore works
		#Populate highscore list with dummy values
		highscores = ["10000","9001","9000","8500","8000","7500","7000","6500","6000","5000"]
		user1 = User("Player","0","0")
		for i in range(0,10):
			user1.score=highscores[i]
			self.dbTest.updateHighscore(user1)
		#Check that the values have been changed
		j=1
		for i in self.dbTest.getHighscores("DESC"):
			self.assertEqual(str(i),"("+str(j)+", u'Player', "+highscores[j-1]+")")
			j=j+1

	def test_changePassword(self):
		#Ensure Player and JohnDoe have their default passwords
		self.assertTrue(self.dbTest.checkPassword("Player","pass"))
		self.assertTrue(self.dbTest.checkPassword("JohnDoe","swordfish"))
		#Change passwords
		self.dbTest.changePassword("Player","newpass")
		self.dbTest.changePassword("JohnDoe","catfish")
		#Check if passwords have changed
		self.assertFalse(self.dbTest.checkPassword("Player","pass"))
		self.assertFalse(self.dbTest.checkPassword("JohnDoe","swordfish"))
		#Check if passwords are what they were supposed to be set to
		self.assertTrue(self.dbTest.checkPassword("Player","newpass"))
		self.assertTrue(self.dbTest.checkPassword("JohnDoe","catfish"))
		#Change passwords back for use in other tests and check to make sure
		self.dbTest.changePassword("Player","pass")
		self.dbTest.changePassword("JohnDoe","swordfish")
		self.assertTrue(self.dbTest.checkPassword("Player","pass"))
		self.assertTrue(self.dbTest.checkPassword("JohnDoe","swordfish"))		

	def test_changeName(self):
		#This also checks that getName works properly
		#Check that name is equivalent to initial value
		self.assertEqual(self.dbTest.getName("Player"), "Gary")
		#Change name and check that it has been changed
		self.dbTest.changeName("Player", "Amy")
		self.assertEqual(self.dbTest.getName("Player"), "Amy")

	def test_changeSecurity(self):
		#Check that question and answer are equivalent to initial values
		self.assertEqual(self.dbTest.getQuestion("Player"), "Q1?")
		self.assertTrue(self.dbTest.checkAnswer("Player", "A1"))
		#Change question and answer
		self.dbTest.changeSecurity("Player", "How do you love?", "...")
		#Check that they have been changed
		self.assertEqual(self.dbTest.getQuestion("Player"), "How do you love?")
		self.assertTrue(self.dbTest.checkAnswer("Player", "..."))
		
	def test_getHighscoreRecords(self):
		#Populate highscore list with dummy values
		highscores = ["10000","9001","9000","8500","8000","7500","7000","6500","6000","5000"]
		user1 = User("Player","0","0")
		for i in range(0,10):
			user1.score=highscores[i]
			self.dbTest.updateHighscore(user1)

		#Check that the values have been changed
		j=1
		for i in self.dbTest.getHighscores("DESC"):
			self.assertEqual(str(i),"("+str(j)+", u'Player', "+highscores[j-1]+")")
			j=j+1
		
	def tearDown(self):
		self.dbTest.con.close()
		os.remove('Test_Pacman.db')
            
if __name__ == '__main__':
	unittest.main()            
