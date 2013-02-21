try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import GameItem as gi
import unittest

class test_GameItem(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)
	#Create variety of GameItem objects
        self.PxL = 0
        self.PxR = 16
        self.PyT = 32
        self.PyB = 48
        self.Pcolor = 'yellow'
        self.Ptag = 'Pacman'

        self.GIxL = 8
        self.GIxR = 24
        self.GIyT = 24
        self.GIyB = 40
        self.GIcolor = 'light blue'
        self.GItag = 'Inky'

        self.GCxL = 0
        self.GCxR = 16
        self.GCyT = 16
        self.GCyB = 32
        self.GCcolor = 'orange'
        self.GCtag = 'Clyde'

        self.GPxL = 16
        self.GPxR = 32
        self.GPyT = 16
        self.GPyB = 32
        self.GPcolor = 'pink'
        self.GPtag = 'Pinky'

        self.GBxL = 16
        self.GBxR = 32
        self.GByT = 32
        self.GByB = 48
        self.GBcolor = 'red'
        self.GBtag = 'Blinky'

        self.G5xL = 32
        self.G5xR = 48
        self.G5yT = 16
        self.G5yB = 32
        self.G5color = 'black'
        self.G5tag = 'G5'

        self.itemP = gi.GameItem(gameCanvas, self.PxL, self.PyT, self.PxR, self.PyB, self.Pcolor, self.Ptag)
        self.itemGI = gi.GameItem(gameCanvas, self.GIxL, self.GIyT, self.GIxR, self.GIyB, self.GIcolor, self.GItag)
        self.itemGC = gi.GameItem(gameCanvas, self.GCxL, self.GCyT, self.GCxR, self.GCyB, self.GCcolor, self.GCtag)
        self.itemGP = gi.GameItem(gameCanvas, self.GPxL, self.GPyT, self.GPxR, self.GPyB, self.GPcolor, self.GPtag)
        self.itemGB = gi.GameItem(gameCanvas, self.GBxL, self.GByT, self.GBxR, self.GByB, self.GBcolor, self.GBtag)
        self.itemG5 = gi.GameItem(gameCanvas, self.G5xL, self.G5yT, self.G5xR, self.G5yB, self.G5color, self.G5tag)
	
    def test_changeColor(self):
	#The following should not change color
	self.itemP.changeColor("white")
	self.assertNotEqual(self.itemP.color,"white")
	#The following should change color
	self.itemP.canvasID = 1
	self.itemP.changeColor("white")
	self.assertEqual(self.itemP.color,"white")
	self.itemP.changeColor("yellow")
	self.assertEqual(self.itemP.color,"yellow")
    
    def test_findCurrentOverlappingWith(self):
	#Check for target that touches corner of item
        self.assertTrue(self.itemP.findCurrentOverlappingWith(self.itemGP))
	#Check for target that touches top edge of item
        self.assertTrue(self.itemP.findCurrentOverlappingWith(self.itemGC))
	#Check for target that touchesright edge of item
        self.assertTrue(self.itemP.findCurrentOverlappingWith(self.itemGB))
	#Check for target that is partially contained by item
        self.assertTrue(self.itemP.findCurrentOverlappingWith(self.itemGI))
	#Check for target that doesn't touch item at all
        self.assertFalse(self.itemP.findCurrentOverlappingWith(self.itemG5))

    
    def test_findOverlappingWith(self):
	#Check for target that touches corner of item
        self.assertTrue(self.itemP.findOverlappingWith(0, 32, 16, 48, self.itemGP))
	#Check for target that touches top edge of item
        self.assertTrue(self.itemP.findOverlappingWith(0, 32, 16, 48, self.itemGC))
	#Check for target that touchesright edge of item
        self.assertTrue(self.itemP.findOverlappingWith(0, 32, 16, 48, self.itemGB))
	#Check for target that is partially contained by item
        self.assertTrue(self.itemP.findOverlappingWith(0, 32, 16, 48, self.itemGI))
	#Check for target that doesn't touch item at all
        self.assertFalse(self.itemP.findOverlappingWith(0, 32, 16, 48, self.itemG5))

    
    def test_getCoord(self):
	#Create lists to compare lists from getCoord() to
        coordsP = (0, 32, 16, 48)
        coordsGP = (16, 16, 32, 32)
        coordsGB = (16, 32, 32, 48)
        coordsGI = (8, 24, 24, 40)
        coordsGC = (0, 16, 16, 32)
        coordsG5 = (32, 16, 48, 32)
	#Compare lists with their associated items
        self.assertEqual(self.itemP.getCoord(), coordsP)
        self.assertEqual(self.itemGP.getCoord(), coordsGP)
        self.assertEqual(self.itemGB.getCoord(), coordsGB)
        self.assertEqual(self.itemGI.getCoord(), coordsGI)
        self.assertEqual(self.itemGC.getCoord(), coordsGC)
        self.assertEqual(self.itemG5.getCoord(), coordsG5)


