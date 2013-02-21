try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import PointItem as pi
from maps import Map1
from display import DrawingGenerics

import unittest

class test_PointItem(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)
        self.specs1 = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
					'yCenter': (14 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': "white",
					'tag': "dot"}
        
        self.specs2 = {'xCenter': (14.5 * DrawingGenerics.TILE_SIZE),
					'yCenter': (15 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': "black",
					'tag': "dot"}
        
        self.specs3 = {'xCenter': (13.99 * DrawingGenerics.TILE_SIZE),
					'yCenter': (15.49 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': "red",
					'tag': "cherry"}
        
        self.ptItem1 = pi.PointItem(gameCanvas,self.specs1,50)
        self.ptItem2 = pi.PointItem(gameCanvas,self.specs2,100)
        self.ptItem3 = pi.PointItem(gameCanvas,self.specs3,200)
        
    def test_setPoints(self):
        #We also test getPoints
        #Check initial values of points
        self.assertEqual(self.ptItem1.getPoints(),50)
        self.assertEqual(self.ptItem2.getPoints(),100)
        self.assertEqual(self.ptItem3.getPoints(),200)
        
        self.ptItem1.setPoints(500)
        self.ptItem2.setPoints(5000)
        self.ptItem3.setPoints(9001)
        
        self.assertEqual(self.ptItem1.getPoints(),500)
        self.assertEqual(self.ptItem2.getPoints(),5000)
        self.assertEqual(self.ptItem3.getPoints(),9001)
        
    def test_inTile(self):
        #The inTile method rounds down the coordinates xCenter and yCenter to get the tile
        self.assertEqual(self.ptItem1.inTile(),(14,14))
        self.assertEqual(self.ptItem2.inTile(),(14,15))
        self.assertEqual(self.ptItem3.inTile(),(13,15))
        
        
        