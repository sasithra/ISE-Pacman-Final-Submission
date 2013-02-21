import sys
sys.path.append('../src/org')

from display import DrawingGenerics

import testMapCoordinator as mc
from maps import Map1 as map1
from maps import Map2 as map2
from maps import Map3 as map3

import unittest

class test_maps(unittest.TestCase):
    
    def setUp(self):
	#This test class uses testMapCoordinator, which is the exact same thing as MapCoordinator in maps, except the path is different, because the test files and the files that open pacman are in different locations
	map1 = mc.getMap(1)
	map2 = mc.getMap(2)
	map3 = mc.getMap(3)
	
	#Get specifications for dots, energizers, ghosts, walls and pacman for each map file
        self.dots1 = map1.getDotSpecifications()
        self.energizers1 = map1.getEnergizerSpecifications()
        self.ghosts1 = map1.getGhostSpecifications()
        self.walls1 = map1.getWallSpecifications()
        self.pacman1 = map1.getPacmanSpecifications()
	self.bonus1 = map1.getBonusItemSpecifications()
        self.dots2 = map2.getDotSpecifications()
        self.energizers2 = map2.getEnergizerSpecifications()
        self.ghosts2 = map2.getGhostSpecifications()
        self.walls2 = map2.getWallSpecifications()
        self.pacman2 = map2.getPacmanSpecifications()
        self.dots3 = map3.getDotSpecifications()
        self.energizers3 = map3.getEnergizerSpecifications()
        self.ghosts3 = map3.getGhostSpecifications()
        self.walls3 = map3.getWallSpecifications()
        self.pacman3 = map3.getPacmanSpecifications()

    
    def test_getDotSpecifications(self):
	_dotSpecs = []
	#Create dot list to compare to getDotSpecifications()
        for i in range(4, DrawingGenerics.MAP_HEIGHT_UNITS - 3):
		for j in range(1, DrawingGenerics.MAP_WIDTH_UNITS - 1):
			# Do not put a dot in a wall locations
			# All wall ranges are defined below
			
			# Top middle vertical wall
			if (4 <= i < 8 and 13 <= j < 15):
				continue
			
			# 4 top horizontal walls
			if (5 <= i < 8 and 2 <= j < 6):
				continue
			if (5 <= i < 8 and 7 <= j < 12):
				continue
			if (5 <= i < 8 and 16 <= j < 21):
				continue
			if (5 <= i < 8 and 22 <= j < 26):
				continue
			
			# 2 horizontal short walls near the top left / top right corners
			if (9 <= i < 11 and 2 <= j < 6):
				continue
			if (9 <= i < 11 and 22 <= j < 26):
				continue
			
			# 3 T-shaped walls near the top middle
			# Left T wall
			if (9 <= i < 17 and 7 <= j < 9):
				continue
			if (12 <= i < 14 and 9 <= j < 12):
				continue
			# Middle T wall
			if (9 <= i < 11 and 10 <= j < 18):
				continue
			if (11 <= i < 14 and 13 <= j < 15):
				continue
			# Right T wall
			if (9 <= i < 17 and 19 <= j < 21):
				continue
			if (12 <= i < 14 and 16 <= j < 19):
				continue
			
			# 2 tunnel regions near middle left / middle right
			if (12 <= i < 23 and 1 <= j < 6):
				continue
			if (12 <= i < 23 and 22 <= j < 27):
				continue
			
			# Ghost enclosure and middle clearance region
			if (12 <= i < 23 and 7 <= j < 21):
				continue
			
			# 2 verticle walls near middle left / middle right
			if (18 <= i < 23 and 7 <= j < 9):
				continue
			if (18 <= i < 23 and 19 <= j < 21):
				continue
			
			# 2 T walls below the ghost enclosure
			# Upper T wall
			if (21 <= i < 23 and 10 <= j < 18):
				continue
			if (23 <= i < 26 and 13 <= j < 15):
				continue
			# Lower T wall
			if (27 <= i < 29 and 10 <= j < 18):
				continue
			if (29 <= i < 32 and 13 <= j < 15):
				continue
			
			# 2 horizontal short walls below the ghost enclosure
			if (24 <= i < 26 and 7 <= j < 12):
				continue
			if (24 <= i < 26 and 16 <= j < 21):
				continue
			
			# 2 upside-down L walls near the bottom left / bottom right corners
			# Left one
			if (24 <= i < 26 and 2 <= j < 6):
				continue
			if (26 <= i < 29 and 4 <= j < 6):
				continue
			# Right one
			if (24 <= i < 26 and 22 <= j < 26):
				continue
			if (26 <= i < 29 and 22 <= j < 24):
				continue
			
			# 2 little nudges out of the left / right outer wall near the bottom corners
			if (27 <= i < 29 and 1 <= j < 3):
				continue
			if (27 <= i < 29 and 25 <= j < 27):
				continue
			
			# 2 upside-down T walls at the bottom of the map
			if (30 <= i < 32 and 2 <= j < 12):
				continue
			if (27 <= i < 30 and 7 <= j < 9):
				continue
			if (30 <= i < 32 and 16 <= j < 26):
				continue
			if (27 <= i < 30 and 19 <= j < 21):
				continue
			
			# Pacman staring position
			if (26 <= i < 27 and 13 <= j < 15):
				continue
			
			# Energizer locations
			if ((i == 6 and j == 1) or (i == 6 and j == 26) or
					(i == 26 and j == 1) or (i == 26 and j == 26)):
				continue

			# No wall or other interference, a dot should be drawn there
			_dotSpecs.append({'xCenter': (j * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'yCenter': (i * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.DOT_RADIUS,
					'color': DrawingGenerics.DOT_COLOR,
					'tag': DrawingGenerics.TAG_DOT,
					'points': 10})

	#The dots are the same for each file, so make sure they all return the same thing
        self.assertEqual(self.dots1, _dotSpecs)
        self.assertEqual(self.dots2, _dotSpecs)
        self.assertEqual(self.dots3, _dotSpecs)

    
    def test_getEnergizerSpecifications(self):
	#Create energizer list to compare getEnergizerSpecifications() to
        _energizerSpecs = []

	j = 1 # x
	i = 6 # y
	# No wall or other interference, a dot should be drawn there
	_energizerSpecs.append({'xCenter': (j * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'yCenter': (i * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.ENERGIZER_RADIUS,
			'color': DrawingGenerics.ENERGIZER_COLOR[1],
			'tag': DrawingGenerics.TAG_ENERGIZER,
			'points': 50})
	i = 26 # y
	# No wall or other interference, a dot should be drawn there
	_energizerSpecs.append({'xCenter': (j * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'yCenter': (i * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.ENERGIZER_RADIUS,
			'color': DrawingGenerics.ENERGIZER_COLOR[1],
			'tag': DrawingGenerics.TAG_ENERGIZER,
			'points': 50})
	j = 26 # x
	i = 6 # y
	# No wall or other interference, a dot should be drawn there
	_energizerSpecs.append({'xCenter': (j * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'yCenter': (i * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.ENERGIZER_RADIUS,
			'color': DrawingGenerics.ENERGIZER_COLOR[1],
			'tag': DrawingGenerics.TAG_ENERGIZER,
			'points': 50})
	i = 26 # y
	# No wall or other interference, a dot should be drawn there
	_energizerSpecs.append({'xCenter': (j * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'yCenter': (i * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.ENERGIZER_RADIUS,
			'color': DrawingGenerics.ENERGIZER_COLOR[1],
			'tag': DrawingGenerics.TAG_ENERGIZER,
			'points': 50})
	#Energizers are same for each file, check that they are, in fact, the same
        self.assertEqual(self.energizers1, _energizerSpecs)
        self.assertEqual(self.energizers2, _energizerSpecs)
        self.assertEqual(self.energizers3, _energizerSpecs)

    
    def test_getPacmanSpecifications(self):
	#Check that each pacman specification is what it is supposed to be
        self.assertEqual(self.pacman1['xCenter'], 14 * DrawingGenerics.TILE_SIZE)
        self.assertEqual(self.pacman1['yCenter'], 26 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING)
        self.assertEqual(self.pacman1['radius'], DrawingGenerics.PACMAN_RADIUS)
        self.assertEqual(self.pacman1['speed'], 1.0 * DrawingGenerics.PIXEL)
        self.assertEqual(self.pacman1['speed_fright'], 1.14 * DrawingGenerics.PIXEL)
        self.assertEqual(self.pacman1['color'], DrawingGenerics.PACMAN_COLOR)
        self.assertEqual(self.pacman1['tag'], DrawingGenerics.TAG_PACMAN)
	#Check for the values in Map2 and Map3 that differ from Map1 (i.e. speed values)
        self.assertEqual(self.pacman2['speed'], 1.14 * DrawingGenerics.PIXEL)
        self.assertEqual(self.pacman2['speed_fright'], 1.33 * DrawingGenerics.PIXEL)
        self.assertEqual(self.pacman3['speed'], 1.14 * DrawingGenerics.PIXEL)
        self.assertEqual(self.pacman3['speed_fright'], 1.33 * DrawingGenerics.PIXEL)

    
    def test_getGhostSpecifications(self):
	#Create ghost tuple to compare getGhostSpecifications() to
	_ghost1 = {'xCenter': (12 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.GHOST_RADIUS,
				'speed': 1.0*DrawingGenerics.PIXEL,
				'speed_fright' : 0.62*DrawingGenerics.PIXEL,
	                        'speed_tunnel' : 0.5*DrawingGenerics.PIXEL,
	                        'speed_eaten' : 2.0*DrawingGenerics.PIXEL,
				'color': DrawingGenerics.GHOST_COLOR[1],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost2 = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.GHOST_RADIUS,
	                        'speed': 1.0*DrawingGenerics.PIXEL,
	                        'speed_fright' : 0.62*DrawingGenerics.PIXEL,
	                        'speed_tunnel' : 0.5*DrawingGenerics.PIXEL,
	                        'speed_eaten' : 2.0*DrawingGenerics.PIXEL,
				'color': DrawingGenerics.GHOST_COLOR[2],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost3 = {'xCenter': (16 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.GHOST_RADIUS,
	                        'speed': 1.0*DrawingGenerics.PIXEL,
	                        'speed_fright' : 0.62*DrawingGenerics.PIXEL,
	                        'speed_tunnel' : 0.5*DrawingGenerics.PIXEL,
	                        'speed_eaten' : 2.0*DrawingGenerics.PIXEL,
				'color': DrawingGenerics.GHOST_COLOR[3],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost4 = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
				'yCenter': (14 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.GHOST_RADIUS,
	                        'speed': 1.0*DrawingGenerics.PIXEL,
	                        'speed_fright' : 0.62*DrawingGenerics.PIXEL,
	                        'speed_tunnel' : 0.5*DrawingGenerics.PIXEL,
	                        'speed_eaten' : 2.0*DrawingGenerics.PIXEL,
				'color': DrawingGenerics.GHOST_COLOR[4],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghostSpecs = {0 : _ghost1, 1 : _ghost2, 2 : _ghost3, 3 : _ghost4}
	#Check that it is equivalent
        self.assertEqual(self.ghosts1, _ghostSpecs)

    def test_getBonusItemSpecifications(self):
	_bonusItemSpec = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
			'yCenter': (20 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.BONUS_RADIUS,
			'color': DrawingGenerics.BONUS_COLOR,
			'tag': DrawingGenerics.TAG_BONUS,
			'points': 100}	
	self.assertEqual(self.bonus1, _bonusItemSpec)

    
    def test_getWallSpecifications(self):
	#Create wall list to compare getWallSpecifications() to
        _wallSpecs = []
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 3 * DrawingGenerics.TILE_SIZE,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 4 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 33 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 34 * DrawingGenerics.TILE_SIZE,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 3 * DrawingGenerics.TILE_SIZE,
            'xRight': DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 34 * DrawingGenerics.TILE_SIZE,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': (DrawingGenerics.MAP_WIDTH - DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
            'yTop': 3 * DrawingGenerics.TILE_SIZE,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': (DrawingGenerics.MAP_WIDTH - DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 34 * DrawingGenerics.TILE_SIZE,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 0,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': DrawingGenerics.MAP_WIDTH,
            'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 11 * DrawingGenerics.TILE_SIZE,
            'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 17 * DrawingGenerics.TILE_SIZE,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 19 * DrawingGenerics.TILE_SIZE,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 13 * DrawingGenerics.TILE_SIZE,
            'yBottom': 16 * DrawingGenerics.TILE_SIZE,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 15 * DrawingGenerics.TILE_SIZE,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 16 * DrawingGenerics.TILE_SIZE,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 15 * DrawingGenerics.TILE_SIZE,
            'yBottom': 16 * DrawingGenerics.TILE_SIZE,
            'color': None,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE,
            'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING + DrawingGenerics.PIXEL,
            'xRight': 15 * DrawingGenerics.TILE_SIZE,
            'yBottom': 16 * DrawingGenerics.TILE_SIZE - DrawingGenerics.PIXEL,
            'color': DrawingGenerics.DOOR_COLOR,
            'tag': DrawingGenerics.TAG_DOOR })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 3 * DrawingGenerics.TILE_SIZE,
            'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 21 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 4 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'xRight': 24 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 1 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 3 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 25 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
        _wallSpecs.append({
            'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
            'yBottom': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
            'color': DrawingGenerics.WALL_OUTLINE,
            'tag': DrawingGenerics.TAG_WALL })
	#The wall objects are the same in each file, check that they are the same
        self.assertEqual(self.walls1, _wallSpecs)
        self.assertEqual(self.walls2, _wallSpecs)
        self.assertEqual(self.walls3, _wallSpecs)


