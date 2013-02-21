try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import Pacman as pm
from gameplay import Wall as w
from maps import Map1
from display import DrawingGenerics

import unittest

class KeyPress(object):
	def __init__(self, keysym):
		self.keysym = keysym
	
	def getKeysym(self):
		return self.keysym
	
	def setKeysym(self, newKey):
		self.keysym = newKey

class test_Pacman(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)
        self.pacmanSpecs = Map1.getPacmanSpecifications()
        self.wallSpecs = Map1.getWallSpecifications()
        self.pacman = pm.Pacman(self, gameCanvas, self.pacmanSpecs)
	self.walls = []
	for i in self.wallSpecs:
	    self.walls.append(w.Wall(gameCanvas,i))
    
    def getWalls(self):
        return self.walls

    
    def test_initGame(self):
	#Check that default values set by initGame have been set
        self.pacman.initGame()
        self.assertEqual(self.pacman.started_, False)
        self.assertEqual(self.pacman.left, True)
        self.assertEqual(self.pacman.right, False)
        self.assertEqual(self.pacman.up, False)
        self.assertEqual(self.pacman.down, False)
        self.assertEqual(self.pacman.currDir, 'left')
        self.assertEqual(self.pacman.inGame, True)

    
    def test_setHaltIterations(self):
	#Check that setHaltIterations has, in fact, set self.pacman.halt
        self.pacman.setHaltIterations(10)
        self.assertEqual(self.pacman.halt, 10)
        self.pacman.setHaltIterations(20)
        self.assertEqual(self.pacman.halt, 20)	
    
    def test_movement(self):
	key = KeyPress("Left")
        self.pacman.movement(key)
	self.assertTrue(self.pacman.started_)
	self.assertEqual(self.pacman.desiredDir,"left")
	key.setKeysym("Right")
	self.pacman.movement(key)
	self.assertTrue(self.pacman.started_)
	self.assertEqual(self.pacman.desiredDir,"right")
	key.setKeysym("Up")
	self.pacman.movement(key)
	self.assertTrue(self.pacman.started_)
	self.assertEqual(self.pacman.desiredDir,"up")
	key.setKeysym("Down")
	self.pacman.movement(key)
	self.assertTrue(self.pacman.started_)
	self.assertEqual(self.pacman.desiredDir,"down")	
    
    def test_energized(self):
	#Check that values that are supposed to change after calling energized() have changed
        self.pacman.energized(10)
        self.assertEqual(self.pacman.halt, 3)
        self.assertEqual(self.pacman.energizeCycles, 10)
        self.assertEqual(self.pacman.state, DrawingGenerics.PACMAN_STATE['Energized'])

    
    def test_checkReversalOfDirection(self):
	#Expected reversal of direction
        self.pacman.desiredDir = 'right'
        self.pacman.left = True
        self.pacman.right = False
        self.pacman.up = False
        self.pacman.down = False
        self.pacman.checkReversalOfDirection()
        self.assertTrue(self.pacman.right)
        self.assertFalse(self.pacman.left)
        self.assertFalse(self.pacman.up)
        self.assertFalse(self.pacman.down)
	#No expected change
        self.pacman.desiredDir = 'left'
        self.pacman.left = True
        self.pacman.right = False
        self.pacman.up = False
        self.pacman.down = False
        self.pacman.checkReversalOfDirection()
        self.assertTrue(self.pacman.left)
        self.assertFalse(self.pacman.right)
        self.assertFalse(self.pacman.up)
        self.assertFalse(self.pacman.down)
	#Expected reversal of directiono
        self.pacman.desiredDir = 'up'
        self.pacman.left = False
        self.pacman.right = False
        self.pacman.up = False
        self.pacman.down = True
        self.pacman.checkReversalOfDirection()
        self.assertTrue(self.pacman.up)
        self.assertFalse(self.pacman.right)
        self.assertFalse(self.pacman.left)
        self.assertFalse(self.pacman.down)
	#No expected change
        self.pacman.desiredDir = 'down'
        self.pacman.left = False
        self.pacman.right = True
        self.pacman.up = False
        self.pacman.down = False
        self.pacman.checkReversalOfDirection()
        self.assertTrue(self.pacman.right)
        self.assertFalse(self.pacman.left)
        self.assertFalse(self.pacman.up)
        self.assertFalse(self.pacman.down)

    
    def test_directionChanged(self):
	#Pacman is in starting position, expected to be able to turn left or right, but not up or down
        self.pacman.left = False
        self.pacman.right = False
        self.pacman.up = False
        self.pacman.down = False	

	#No input/no desired direction
	self.pacman.desiredDir = ""
	self.assertFalse(self.pacman.directionChanged())
	self.assertFalse(self.pacman.left)
	self.assertFalse(self.pacman.right)
	self.assertFalse(self.pacman.up)
	self.assertFalse(self.pacman.down)
	
	#Try to move left
        self.pacman.desiredDir = "left"
	self.assertTrue(self.pacman.directionChanged())
	self.assertTrue(self.pacman.left)
	self.assertFalse(self.pacman.right)
	self.assertFalse(self.pacman.up)
	self.assertFalse(self.pacman.down)
	#Now moving left, so if we check directionChanged again, it should be false
	self.assertFalse(self.pacman.directionChanged())
	
	#Try to move up
        self.pacman.desiredDir = "up"
	self.assertFalse(self.pacman.directionChanged())
	#Direction cannot be changed, so remains left
	self.assertTrue(self.pacman.left)
	self.assertFalse(self.pacman.right)
	self.assertFalse(self.pacman.up)
	self.assertFalse(self.pacman.down)
	
	#Try to move right
        self.pacman.desiredDir = "right"
	self.assertTrue(self.pacman.directionChanged())
	#Direction can be changed, so becomes right
	self.assertFalse(self.pacman.left)
	self.assertTrue(self.pacman.right)
	self.assertFalse(self.pacman.up)
	self.assertFalse(self.pacman.down)
	#Now moving right, so if we check directionChanged again, it should be false
	self.assertFalse(self.pacman.directionChanged())

	#Try to move down
        self.pacman.desiredDir = "down"
	self.assertFalse(self.pacman.directionChanged())
	#Direction cannot be changed, so remains right
	self.assertFalse(self.pacman.left)
	self.assertTrue(self.pacman.right)
	self.assertFalse(self.pacman.up)
	self.assertFalse(self.pacman.down)
	
    
    def test_currCoordinates(self):
	#Check that real current coordinates are being returned
        xL = self.pacman.xLeft = 4
        xR = self.pacman.xRight = 20
        yT = self.pacman.yTop = 10
        yB = self.pacman.yBottom = 26
        xCenter = (xL + xR) / 2
        yCenter = (yT + yB) / 2
        self.assertTrue(self.pacman.currCoordinates(), (xCenter, yCenter))

    
    def test_currDirection(self):
	#Check that currDirection returns correct value
        direction = 'right'
        self.pacman.currDir = 'right'
        self.assertEqual(self.pacman.currDirection(), direction)
        direction = 'left'
        self.pacman.currDir = 'left'
        self.assertEqual(self.pacman.currDirection(), direction)
        direction = 'up'
        self.pacman.currDir = 'up'
        self.assertEqual(self.pacman.currDirection(), direction)
        direction = 'down'
        self.pacman.currDir = 'down'
        self.assertEqual(self.pacman.currDirection(), direction)


    def test_process(self):
	#Check for when Pacman is energized
	self.pacman.energizeCycles = 2
	self.pacman.halt = 0
	self.pacman.process()
	self.assertEqual(self.pacman.energizeCycles,1)
	self.assertEqual(self.pacman.state,DrawingGenerics.PACMAN_STATE['Energized'])
	self.assertEqual(self.pacman.speed,1.14 * DrawingGenerics.PIXEL)
	
	#Check for when Pacman is neither energized nor halted
	self.pacman.energizeCycles = 0
	self.pacman.halt = 0
	self.pacman.process()
	self.assertEqual(self.pacman.energizeCycles,0)
	self.assertEqual(self.pacman.state,DrawingGenerics.PACMAN_STATE['Normal'])
	self.assertEqual(self.pacman.speed,1.0 * DrawingGenerics.PIXEL)
	
	#Check for when Pacman is halted
	self.pacman.energizeCycles = 0
	self.pacman.halt = 4
	self.pacman.process()
	self.assertEqual(self.pacman.halt,3)
	self.assertEqual(self.pacman.state,DrawingGenerics.PACMAN_STATE['Normal'])
	#Halt doesn't change the speed, it just skips one iteration of process, stopping him temporarily
	self.assertEqual(self.pacman.speed,1.0 * DrawingGenerics.PIXEL)
	
	#Check for when Pacman is halted while energized
	self.pacman.energizeCycles = 4
	self.pacman.halt = 4
	self.pacman.process()
	self.assertEqual(self.pacman.energizeCycles,3)
	self.assertEqual(self.pacman.halt,3)
	self.assertEqual(self.pacman.state,DrawingGenerics.PACMAN_STATE['Energized'])
	#Halt doesn't change the speed, it just skips one iteration of process, stopping him temporarily
	self.assertEqual(self.pacman.speed,1.14 * DrawingGenerics.PIXEL)	

    def test_restart(self):
	#This function relies on initGame, which has been tested already
	#Check that other values set have been set to what is expected
	self.pacman.restart()
	self.assertEqual(self.pacman.energizeCycles, 0)
        self.assertEqual(self.pacman.halt, 0)
        self.assertEqual(self.pacman.currCoordinates(), (self.pacman.specs['xCenter'], self.pacman.specs['yCenter']))
	self.assertEqual(self.pacman.desiredDir,"")


