try:
    from tkinter import *
except:
    from Tkinter import *

import sys
sys.path.append('../src/org')
from gameplay import BonusItem as bi
from maps import Map1
from display import DrawingGenerics

import unittest

class test_BonusItem(unittest.TestCase):
    
    def setUp(self):
        root = Tk()
        gameCanvas = Canvas(root, width = 200, height = 200)
        gameCanvas.grid(row = 0, column = 0)    
        
	_bonusItemSpec = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
			'yCenter': (20 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.BONUS_RADIUS,
			'color': DrawingGenerics.BONUS_COLOR,
			'tag': DrawingGenerics.TAG_BONUS,
			'points': 100}        
        
        self.BI = bi.BonusItem(gameCanvas,_bonusItemSpec)
        
    def test_process(self):
        #CYCLES_PER_SECOND is 125, so DISAPPEAR_CYCLES is 1125
	#If test_activate works, the next line works fine
	self.BI.activate()
	self.BI.activeCycles = 1123
	#The following should not reset activeCycles and deactivate the item
	self.BI.process()
	self.assertEqual(self.BI.activeCycles,1124)
	self.assertTrue(self.BI.active)
	#The following should reset activeCycles and deactivate the item
	self.BI.process()
	self.assertEqual(self.BI.activeCycles,0)
	self.assertFalse(self.BI.active)	
    
    #If the two following functions work, than so does isActive()
    def test_activate(self):
        self.BI.activate()
	self.assertTrue(self.BI.active)
	self.assertTrue(self.BI.isActive())
    
    def test_deactivate(self):
        self.BI.deactivate()
	self.assertFalse(self.BI.active)
	self.assertFalse(self.BI.isActive())
    