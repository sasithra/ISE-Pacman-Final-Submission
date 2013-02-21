try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
import testGameplay as gp
import testMapCoordinator as tmc
from gameplay import Ghost as gh
from gameplay import Pacman as pm
from gameplay import Dot as dot
from gameplay import Energizer as en
from gameplay import BonusItem as bi
from display import DrawingGenerics

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

class test_Gameplay(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        self.gameCanvas = Canvas(root, width = 200, height = 200)
        self.gameCanvas.grid(row = 0, column = 0)        
        
	self.uiCoordinator = root
        
	self.user = User("Player","0","10")
	self.level = 1
        
        self.GP = gp.GamePlay(self,self.user,1)
	
	self.createSpecs()
	
    def createSpecs(self):
	Map1 = tmc.getMap(1)
	self.dotSpecs = Map1.getDotSpecifications()
	self.energizerSpecs = Map1.getEnergizerSpecifications()
	self.pacmanSpecs = Map1.getPacmanSpecifications()
	self.ghostSpecs = Map1.getGhostSpecifications()
	self.wallSpecs = Map1.getWallSpecifications()
	self.bonusSpecs = Map1.getBonusItemSpecifications()
	
    def test_loadMapSpecs(self):
	self.GP.loadMapSpecs(1)
	self.assertEqual(self.GP.dotSpecifications,self.dotSpecs)
	self.assertEqual(self.GP.energizerSpecifications,self.energizerSpecs)
	self.assertEqual(self.GP.bonusItemSpecifications,self.bonusSpecs)
	self.assertEqual(self.GP.ghostSpecifications,self.ghostSpecs)
	self.assertEqual(self.GP.wallSpecifications,self.wallSpecs)
	self.assertEqual(self.GP.pacmanSpecifications,self.pacmanSpecs)

    def test_start(self):
	self.GP.pause_ = False
	self.GP.game_done = False
	self.GP.level = 1
	self.GP.lives = 3
	#Move a ghost object, so pacman can be eaten
	xDest = (13*DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
	yDest = (26*DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
	self.GP.ghosts[0].move(xDest-self.GP.ghosts[0].xCenter,yDest-self.GP.ghosts[0].yCenter)
	
	self.GP.start()
	#Ghost is worth 200 points
	self.assertEqual(self.GP.gameScore,0)	
	self.assertEqual(self.GP.lives,2)
	
	#Win game
	self.GP.dots = []
	self.GP.energizers = []
	self.GP.start()
	#Make sure level increments and dots and energizers reset
	self.assertEqual(self.GP.level,2)
	self.assertEqual(len(self.GP.dots),240)
	self.assertEqual(len(self.GP.energizers),4)
	self.assertEqual(self.GP.gameScore,0)
	
	#Create a dot object that Pacman can eat
	dot1 = ({'xCenter': (13.4 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'yCenter': (26 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': DrawingGenerics.DOT_COLOR,
					'tag': DrawingGenerics.TAG_DOT,
					'points': 10})
	self.GP.dots.append(dot.Dot(self.gameCanvas,dot1))
	self.assertEqual(len(self.GP.dots),241)
	self.GP.start()
	#Pacman will be in the tile in which the dot object was created
	#There should be one less dot (240)
	self.assertEqual(len(self.GP.dots),240)
	self.assertEqual(self.GP.gameScore,10)
	
	#Create an energizer object that Pacman can eat
	energizer1 = ({'xCenter': (13.4 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'yCenter': (26 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': DrawingGenerics.DOT_COLOR,
					'tag': DrawingGenerics.TAG_DOT,
					'points': 10})
	
	self.GP.energizers.append(en.Energizer(self.gameCanvas,energizer1))
	self.assertEqual(len(self.GP.energizers),5)
	self.GP.start()
	#Pacman will be in the tile in which the energizer object was created
	#There should be one less energizer (240)
	self.assertEqual(len(self.GP.energizers),4)
	self.assertEqual(self.GP.gameScore,20)
	
	#Move a ghost object, so pacman can eat it
	xDest = (13*DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
	yDest = (26*DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING
	self.GP.ghosts[0].move(xDest-self.GP.ghosts[0].xCenter,yDest-self.GP.ghosts[0].yCenter)
	
	self.GP.start()
	#Ghost is worth 200 points
	self.assertEqual(self.GP.gameScore,220)
	
	#Create bonus item in the same tiles as pacman so he can eat it
	bonus = {'xCenter': xDest,
		                'yCenter': yDest,
		                'radius': DrawingGenerics.BONUS_RADIUS,
		                'color': DrawingGenerics.BONUS_COLOR,
		                'tag': DrawingGenerics.TAG_BONUS,
		                'points': 100}
	self.GP.bonusItem = bi.BonusItem(self.gameCanvas, bonus)
	self.GP.bonusItem.active = True
	
	self.GP.start()
	#Bonus item is worth 100 points
	self.assertFalse(self.GP.bonusItem.active)
	self.assertEqual(self.GP.gameScore,320)
	
	
    def test_loseLife(self):
	self.assertEqual(self.GP.lives,3)
	self.assertTrue(self.GP.loseLife())
	self.assertEqual(self.GP.lives,2)
	self.assertTrue(self.GP.loseLife())
	self.assertEqual(self.GP.lives,1)
	self.assertFalse(self.GP.loseLife())	
	self.assertEqual(self.GP.lives,0)
    
    def test_levelWon(self):
	self.GP.level=1
	self.GP.levelWon()
	self.assertEqual(self.GP.level,2)
	self.GP.levelWon()
	self.assertEqual(self.GP.level,3)	
	#Can only increase your lives to three from beating a round, and can only reach level 3, at the moment
	self.GP.levelWon()
	self.assertEqual(self.GP.level,3)	
    
    def test_addToScore(self):
	self.GP.gameScore = 0
	self.GP.lives = 2
	self.GP.addToScore(100)
	self.assertEqual(self.GP.gameScore,100)
	self.assertEqual(self.GP.lives,2)
	self.GP.addToScore(9900)
	self.assertEqual(self.GP.gameScore,10000)
	self.assertEqual(self.GP.lives,3)
	self.GP.addToScore(10000)
	self.assertEqual(self.GP.gameScore,20000)
	self.assertEqual(self.GP.lives,3)
	self.GP.addToScore(80000)
	self.assertEqual(self.GP.gameScore,100000)
	self.assertEqual(self.GP.lives,4)
	self.GP.addToScore(99900000)
	self.assertEqual(self.GP.gameScore,100000000)
	self.assertEqual(self.GP.lives,4)	
	#This method should only increase your lives when you get 10000 points and when you get 100000 points
    
    def test_addLife(self):
	self.GP.lives=1
	self.GP.addLife()
	self.assertEqual(self.GP.lives,2)
	self.GP.addLife()
	self.assertEqual(self.GP.lives,3)
	#Can't have more than three lives
	self.GP.addLife()
	self.assertEqual(self.GP.lives,4)
    
    def test_getDotsEaten(self):
	#No dots eaten
	self.assertEqual(self.GP.getDotsEaten(),0)
	self.GP.dots.pop()
	self.GP.dots.pop()
	self.GP.dots.pop()
	self.GP.dots.pop()
	self.GP.dots.pop()
	#Five dots "eaten"
	self.assertEqual(self.GP.getDotsEaten(),5)