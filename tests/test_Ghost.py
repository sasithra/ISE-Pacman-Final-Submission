try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import Ghost as gh
from gameplay import Pacman as pm
from gameplay import Wall as w
from maps import Map1
from display import DrawingGenerics

import math

import unittest

class test_Ghost(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)
        self.ghostSpecs = Map1.getGhostSpecifications()
	self.pacmanSpecs = Map1.getPacmanSpecifications()
	self.pacman = pm.Pacman(self, gameCanvas, self.pacmanSpecs)	
        self.wallSpecs = Map1.getWallSpecifications()
        self.ghost1 = gh.Ghost(self, gameCanvas, 1, self.ghostSpecs[0])
	self.ghost2 = gh.Ghost(self, gameCanvas, 2, self.ghostSpecs[1])
	self.ghost3 = gh.Ghost(self, gameCanvas, 3, self.ghostSpecs[2])
	self.ghost4 = gh.Ghost(self, gameCanvas, 4, self.ghostSpecs[3])
	self.dots = [0,0,0,0,0,0,0,0,0,0]
	self.dotsEaten=100
	self.walls = []
	for i in self.wallSpecs:
	    self.walls.append(w.Wall(gameCanvas,i))

    def getGhosts(self):
	_ghostSpecs = {0 : self.ghost1, 1 : self.ghost2, 2 : self.ghost3, 3 : self.ghost4}
	return _ghostSpecs	

    def getPacman(self):
	return self.pacman

    def getDots(self):
	return self.dots

    def getDotsEaten(self):
	return self.dotsEaten

    def getWalls(self):
	return self.walls

    def test_initGame(self):
	self.ghost1.initGame()
	self.assertFalse(self.ghost1.started)
	self.assertFalse(self.ghost1.left)
	self.assertFalse(self.ghost1.right)
	self.assertFalse(self.ghost1.up)
	self.assertFalse(self.ghost1.down)

    def test_start(self):
	#Move ghost to arbitrary location
	self.ghost1.xCenter=0
	self.ghost1.yCenter=10
	#Ghost should be moved back to start
	self.ghost1.start()
	self.assertEqual(self.ghost1.xCenter,14*DrawingGenerics.TILE_SIZE)
	self.assertEqual(self.ghost1.xCenter,14*DrawingGenerics.TILE_SIZE)

    def test_restart(self):
	self.ghost1.restart()
	self.assertEqual(self.ghost1.dotLimit,230)
	self.assertFalse(self.ghost1.started)
	#Current coordinates check
	self.assertEqual(self.ghost1.toggleChaseScatter,6 * DrawingGenerics.CYCLES_PER_SECOND)

    def test_started_(self):
	self.ghost1.left=False
	self.ghost1.right=False
	self.ghost1.color = 'red'
	self.ghost1.started_()
	self.assertTrue(self.ghost1.left)
	self.assertFalse(self.ghost1.right)

	self.ghost1.left=False
	self.ghost1.right=False
	self.ghost1.color = 'cyan'
	self.ghost1.started_()
	self.assertFalse(self.ghost1.left)
	self.assertTrue(self.ghost1.right)

	self.ghost1.left=False
	self.ghost1.right=False	
	self.ghost1.color = 'pink'
	self.ghost1.started_()
	self.assertFalse(self.ghost1.left)
	self.assertTrue(self.ghost1.right)

	self.ghost1.left=False
	self.ghost1.right=False	
	self.ghost1.color = 'orange'
	self.ghost1.started_()
	self.assertTrue(self.ghost1.left)
	self.assertFalse(self.ghost1.right)

	self.assertTrue(self.ghost1.started)

    def test_eat(self):
	self.assertEqual(self.ghost1.eat(),200)

    def test_chase(self):
	self.ghost1.chase()
	self.assertEqual(self.ghost1.color,DrawingGenerics.GHOST_COLOR[1])
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Chase'])
	self.assertEqual(self.ghost1.speed,1.0 * DrawingGenerics.PIXEL)
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Chase'])

    def test_scatter(self):
	self.ghost1.scatter()
	self.assertEqual(self.ghost1.color,DrawingGenerics.GHOST_COLOR[1])
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Scatter'])
	self.assertEqual(self.ghost1.speed,1.0 * DrawingGenerics.PIXEL)
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Scatter'])

    def test_returnToPen(self):
	self.ghost1.returnToPen()
	self.assertEqual(self.ghost1.color,"grey")
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Eaten'])
	self.assertEqual(self.ghost1.speed,2 * DrawingGenerics.PIXEL)
	self.assertEqual(self.ghost1.destX,14)
	self.assertEqual(self.ghost1.destY,14.5)

    def test_fright(self):
	self.ghost1.fright(10)
	self.assertEqual(self.ghost1.color,DrawingGenerics.GHOST_FRIGHT_COLOR[1])
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Fright'])
	self.assertEqual(self.ghost1.speed,0.62 * DrawingGenerics.PIXEL)
	self.assertEqual(self.ghost1.frightCycles,10)

    def test_isInTunnel(self):
	#Should return True
	self.ghost1.xCenter = 0*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 18*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertTrue(self.ghost1.isInTunnel())
	self.ghost1.xCenter = 24*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 18*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertTrue(self.ghost1.isInTunnel())

	#Should return False
	self.ghost1.xCenter = 0*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 17.9*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertFalse(self.ghost1.isInTunnel())
	self.ghost1.xCenter = 22*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 18*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertFalse(self.ghost1.isInTunnel())
	self.ghost1.xCenter = 6*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 18*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertFalse(self.ghost1.isInTunnel())
	self.ghost1.xCenter = 12*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.ghost1.yCenter = 18*DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING
	self.assertFalse(self.ghost1.isInTunnel())

    def test_reverseDirection(self):
	self.ghost1.left=True
	self.ghost1.right=False
	self.ghost1.up=False
	self.ghost1.down=False
	self.ghost1.reverseDirection()
	self.assertTrue(self.ghost1.right)
	self.assertFalse(self.ghost1.left)
	self.ghost1.reverseDirection()
	self.assertTrue(self.ghost1.left)
	self.assertFalse(self.ghost1.right)

	self.ghost1.left=False
	self.ghost1.right=False
	self.ghost1.up=True
	self.ghost1.down=False
	self.ghost1.reverseDirection()
	self.assertTrue(self.ghost1.down)
	self.assertFalse(self.ghost1.up)
	self.ghost1.reverseDirection()
	self.assertTrue(self.ghost1.up)
	self.assertFalse(self.ghost1.down)

    def test_toggleColor(self):
	self.ghost1.color = DrawingGenerics.GHOST_FRIGHT_COLOR[1]
	self.ghost1.toggleColor()
	self.assertEqual(self.ghost1.color,DrawingGenerics.GHOST_FRIGHT_COLOR[2])
	self.ghost1.toggleColor()
	self.assertEqual(self.ghost1.color,DrawingGenerics.GHOST_FRIGHT_COLOR[1])

    def test_toggleState(self):
	#We will check these values to make sure parts of toggleState have worked
	self.ghost1.left=True
	self.ghost1.right=False
	self.ghost1.up=False
	self.ghost1.down=False

	self.ghost1.stateFlag = DrawingGenerics.GHOST_STATE['Chase']
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Scatter']
	self.ghost1.toggleState()
	#Expected that ghost1.stateFlag is now Scatter
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Scatter'])
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Scatter'])
	self.assertTrue(self.ghost1.left)
	self.assertFalse(self.ghost1.right)
	self.ghost1.toggleState()
	#Expected change in direction
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Chase'])
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Chase'])
	self.assertTrue(self.ghost1.right)
	self.assertFalse(self.ghost1.left)
	
	self.ghost1.left=True
	self.ghost1.right=False
	self.ghost1.up=False
	self.ghost1.down=False

	self.ghost1.stateFlag = DrawingGenerics.GHOST_STATE['Scatter']
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Chase']
	self.ghost1.toggleState()
	#Expected that ghost1.stateFlag is now Scatter
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Chase'])
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Chase'])
	self.assertTrue(self.ghost1.left)
	self.assertFalse(self.ghost1.right)
	self.ghost1.toggleState()
	#Expected change in direction
	self.assertEqual(self.ghost1.state,DrawingGenerics.GHOST_STATE['Scatter'])
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Scatter'])
	self.assertTrue(self.ghost1.right)
	self.assertFalse(self.ghost1.left)		

    def test_process(self):
	#Check for scatter mode
	self.ghost1.toggleChaseScatterCycle = 5
	self.ghost1.toggleChaseScatter = 5
	self.ghost1.frightCycles = 100
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Scatter']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,4)	
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Scatter'])
	
	#Check for chase mode
	self.ghost1.toggleChaseScatterCycle = 5
	self.ghost1.toggleChaseScatter = 5
	self.ghost1.frightCycles = 100
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Chase']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,4)	
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Chase'])    
	
	#Check for toggle, both ways
	self.ghost1.toggleScatterCycle = 7
	self.ghost1.toggleChaseScatter = 0
	self.ghost1.frightCycles = 100
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Chase']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,7)
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Scatter'])
	
	self.ghost1.toggleChaseCycle = 20
	self.ghost1.toggleChaseScatter = 0
	self.ghost1.frightCycles = 100
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Scatter']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,20)
	self.assertEqual(self.ghost1.stateFlag,DrawingGenerics.GHOST_STATE['Chase'])	
	
	#Check for frightened mode, before flashing
	self.ghost1.toggleChaseScatterCycle = 5
	self.ghost1.toggleChaseScatter = 5
	self.ghost1.frightCycles = 100
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Fright']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,4)
	self.assertEqual(self.ghost1.frightCycles,99)
	
	#Check for frightened mode, flashing
	self.ghost1.toggleChaseScatterCycle = 5
	self.ghost1.toggleChaseScatter = 5
	self.ghost1.frightCycles = 40
	self.ghost1.state = DrawingGenerics.GHOST_STATE['Fright']
	
	self.ghost1.process()
	
	self.assertEqual(self.ghost1.toggleChaseScatter,4)
	
	#In tunnel
	self.ghost1.xCenter = 0
	self.ghost1.yCenter = 280
	self.ghost1.process()
	self.assertTrue(self.ghost1.isInTunnel())
	self.assertEqual(self.ghost1.speed,0.5 * DrawingGenerics.PIXEL)

    def test_setNextDirection(self):
	self.ghost1.destX=14*DrawingGenerics.TILE_SIZE
	self.ghost1.destY=14*DrawingGenerics.TILE_SIZE
	self.ghost4.destX=14*DrawingGenerics.TILE_SIZE
	self.ghost4.destY=14*DrawingGenerics.TILE_SIZE
	#Ghost 1 should only be able to move right
	self.ghost1.setNextDirection()
	self.assertTrue(self.ghost1.right)
	#Ghost 4 should only be able to move left or right at the beginning
	self.ghost4.setNextDirection()
	self.assertTrue(self.ghost4.left or self.ghost4.right)
	

	
    def test_shortestDistance(self):
	dirDict = { 'left': 1, 'right': 2, 'up': 3, 'down': 4 }
	#nextDir should be left
	self.assertEqual(self.ghost1.shortestDistance(dirDict,10,16),"left")
	#nextDir should be right
	self.assertEqual(self.ghost2.shortestDistance(dirDict,16,18),"right")
	#nextDir should be up
	self.assertEqual(self.ghost3.shortestDistance(dirDict,17,15),"up")
	#nextDir should be down
	self.assertEqual(self.ghost4.shortestDistance(dirDict,13,16),"down")
	

    def test_distance(self):
	#Check that a distances are calculated correctly
	self.assertEqual(self.ghost1.distance(0,0,3,4),5)
	self.assertEqual(self.ghost1.distance(0,0,1,1),math.sqrt(2))
	
    def test_destinationTile(self):
	#Ghost 1, in chase mode, follows inky's logic
	self.ghost1.state=DrawingGenerics.GHOST_STATE['Chase']
	self.pacman.currDir='left'
	rX,rY = self.ghost4.inTile()
	dX,dY = self.ghost1.destinationTile()
	pX,pY = self.getPacman().inTile()
	pX = pX-2
	g1X,g1Y = (rX+2*(pX-rX),rY+2*(pY-rY))
	self.assertEqual((dX,dY),(g1X,g1Y))	
	
	self.ghost1.state=DrawingGenerics.GHOST_STATE['Chase']
	self.pacman.currDir='up'
	rX,rY = self.ghost4.inTile()
	dX,dY = self.ghost1.destinationTile()
	pX,pY = self.getPacman().inTile()
	pX,pY = (pX-2,pY-2)
	g1X,g1Y = (rX+2*(pX-rX),rY+2*(pY-rY))
	self.assertEqual((dX,dY),(g1X,g1Y))		
	
	#Ghost 2, in chase mode, follows clyde's logic
	self.ghost2.state=DrawingGenerics.GHOST_STATE['Chase']	
	self.pacman.currDir='right'
	dX,dY = self.ghost2.destinationTile()
	pX,pY = self.getPacman().inTile()
	pX = pX+4
	self.assertEqual((dX,dY),(pX,pY))
	
	self.ghost2.state=DrawingGenerics.GHOST_STATE['Chase']	
	self.pacman.currDir='up'
	dX,dY = self.ghost2.destinationTile()
	pX,pY = self.getPacman().inTile()
	pX,pY = (pX-4,pY-4)
	self.assertEqual((dX,dY),(pX,pY))	
	
	#Ghost 3, in chase mode, follows pinky's logic
	self.ghost3.state=DrawingGenerics.GHOST_STATE['Chase']
	#Ghost 3 is far from pacman (arbitrary coordinates for ghost and pacman, and are sufficiently far from one another)
	self.ghost3.xCenter = 0
	self.ghost3.yCenter = 0
	self.pacman.xCenter = 200
	self.pacman.yCenter = 200
	dX,dY = self.ghost3.destinationTile()
	pX,pY = self.getPacman().inTile()
	self.assertEqual((dX,dY),(pX,pY))
	
	#(Ghost 3 targets pacman)
	#Ghost 3 is close to pacman
	self.ghost3.xCenter = 50
	self.ghost3.yCenter = 50
	self.pacman.xCenter = 55
	self.pacman.yCenter = 55	
	dX,dY = self.ghost3.destinationTile()
	self.assertEqual((dX,dY),(0.5,34.5))
	#(Ghost 3 returns to his corner)
	
	#Ghost 4, in chase mode, follows blinky's logic
	self.ghost4.state=DrawingGenerics.GHOST_STATE['Chase']
	dX,dY = self.ghost4.destinationTile()
	pX,pY = self.getPacman().inTile()
	self.assertEqual((dX,dY),(pX,pY))
	


	#Ghost 1, in scatter mode, targets bottom right corner
	self.ghost1.state=DrawingGenerics.GHOST_STATE['Scatter']
	dX,dY = self.ghost1.destinationTile()
	self.assertEqual((dX,dY),(27.5,34.5))
	
	#Ghost 2, in scatter mode, targets bottom left corner
	self.ghost2.state=DrawingGenerics.GHOST_STATE['Scatter']
	dX,dY = self.ghost2.destinationTile()
	self.assertEqual((dX,dY),(2.5,0.5))
	
	#Ghost 3, in scatter mode, targets top left corner
	self.ghost3.state=DrawingGenerics.GHOST_STATE['Scatter']
	dX,dY = self.ghost3.destinationTile()
	self.assertEqual((dX,dY),(0.5,34.5))	
	
	#Ghost 4, in scatter mode, targets top right corner
	self.ghost4.state=DrawingGenerics.GHOST_STATE['Scatter']
	dX,dY = self.ghost4.destinationTile()
	self.assertEqual((dX,dY),(25.5,0.5))
	
	#Ghost(any) is eaten
	self.ghost1.state=DrawingGenerics.GHOST_STATE['Eaten']
	dX,dY = self.ghost1.destinationTile()
	self.assertEqual((dX,dY),(14,14.5))