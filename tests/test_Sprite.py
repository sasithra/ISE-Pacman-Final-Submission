try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import Sprite as sp
from maps import Map1
from display import DrawingGenerics

import unittest

class test_Sprite(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)
        self.wallSpecs = Map1.getWallSpecifications()

        self.specs1 = {'xCenter': 40,
					'yCenter': 24,
					'radius': 10,
                                        'speed': 10,
					'color': "white",
					'tag': "dot"}

        self.specs2 = {'xCenter': 800,
					'yCenter': 40,
					'radius': 10,
                                        'speed': 10,
					'color': "blue",
					'tag': "dot"}    
        
        self.specs3 = {'xCenter': 10,
					'yCenter': -10,
					'radius': 10,
                                        'speed': 10,
					'color': "red",
					'tag': "dot"}               
        
        self.sprite1 = sp.Sprite(gameCanvas,self.specs1)
        self.sprite2 = sp.Sprite(gameCanvas,self.specs2)
        self.sprite3 = sp.Sprite(gameCanvas,self.specs3)      

    def test_stop(self):
        self.sprite1.stop()
        self.assertFalse(self.sprite1.left)
        self.assertFalse(self.sprite1.right)
        self.assertFalse(self.sprite1.up)
        self.assertFalse(self.sprite1.down)
    
    def test_isPastCentreOfTile(self):
        self.sprite1.left=True
        self.sprite2.left=True
        self.sprite3.left=False
        self.sprite3.right=False
        self.sprite3.up=True
        self.assertFalse(self.sprite1.isPastCentreOfTile())
        self.assertTrue(self.sprite2.isPastCentreOfTile())
        self.assertTrue(self.sprite3.isPastCentreOfTile())
            
    def test_inTile(self):
        self.assertEqual(self.sprite1.inTile(),(2,1))
        self.assertEqual(self.sprite2.inTile(),(50,2))
        self.assertEqual(self.sprite3.inTile(),(0,-1))
    
    def test_inCentreOfTile(self):
        #Center of sprite is in centre of tile
        self.assertTrue(self.sprite1.inCentreOfTile())
        #One center is the same as the tile center, but the other is not
        self.assertFalse(self.sprite2.inCentreOfTile())
        #Neither center is in the middle of a tile
        self.assertFalse(self.sprite3.inCentreOfTile())
    
    