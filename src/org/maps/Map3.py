
"""
Map3
@author: Jason Cohen
"""
# Import map general specifications
from display import DrawingGenerics

# Level specific features
PACMAN_SPEED = 1.14 * DrawingGenerics.PIXEL
PACMAN_SPEED_FRIGHT = 1.33 * DrawingGenerics.PIXEL

GHOST_SPEED = 1.14 * DrawingGenerics.PIXEL
GHOST_SPEED_TUNNEL = 0.5 * DrawingGenerics.PIXEL
GHOST_SPEED_FRIGHT = 0.89 * DrawingGenerics.PIXEL
GHOST_SPEED_EATEN = 2 * DrawingGenerics.PIXEL # 160% max speed

GHOST_START = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
				'yCenter': (14 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING}

# Time in iteration cycles for ghosts to be in fright mode
GHOST_FRIGHT_CYCLES = DrawingGenerics.CYCLES_PER_SECOND * 4


def getDotSpecifications():
	"""
	Return dot item drawing specifications
	@return: Dot specs
	"""
	_dotSpecs = []
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

	return _dotSpecs

def getEnergizerSpecifications():
	"""
	Return energizer item drawing specifications
	@return: energizer specs
	"""
	_energizerSpecs = []
	
	# Energizer locations
	
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
	
	return _energizerSpecs
			
def getPacmanSpecifications():
	"""
	Return pacman item drawing specifications
	@return: pacman specs
	"""
	_pacmanSpecs = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
					'yCenter': (26 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
					'radius': DrawingGenerics.PACMAN_RADIUS,
					'speed': PACMAN_SPEED,
					'speed_fright' : PACMAN_SPEED_FRIGHT,
					'color': DrawingGenerics.PACMAN_COLOR,
					'tag': DrawingGenerics.TAG_PACMAN}
	
	return _pacmanSpecs


def getGhostSpecifications():
	"""
	Return ghost item drawing specifications
	@return: ghost specs
	"""
	_ghost1 = {'xCenter': (12 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.GHOST_RADIUS,
				'speed': GHOST_SPEED,
				'speed_fright' : GHOST_SPEED_FRIGHT,
				'speed_tunnel' : GHOST_SPEED_TUNNEL,
				'speed_eaten' : GHOST_SPEED_EATEN,
				'color': DrawingGenerics.GHOST_COLOR[1],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost2 = {'xCenter': (14 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.PACMAN_RADIUS,
				'speed': GHOST_SPEED,
				'speed_fright' : GHOST_SPEED_FRIGHT,
				'speed_tunnel' : GHOST_SPEED_TUNNEL,
				'speed_eaten' : GHOST_SPEED_EATEN,
				'color': DrawingGenerics.GHOST_COLOR[2],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost3 = {'xCenter': (16 * DrawingGenerics.TILE_SIZE),
				'yCenter': (17 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
				'radius': DrawingGenerics.PACMAN_RADIUS,
				'speed': GHOST_SPEED,
				'speed_fright' : GHOST_SPEED_FRIGHT,
				'speed_tunnel' : GHOST_SPEED_TUNNEL,
				'speed_eaten' : GHOST_SPEED_EATEN,
				'color': DrawingGenerics.GHOST_COLOR[3],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghost4 = {'xCenter': GHOST_START['xCenter'],
				'yCenter': GHOST_START['yCenter'],
				'radius': DrawingGenerics.PACMAN_RADIUS,
				'speed': GHOST_SPEED,
				'speed_fright' : GHOST_SPEED_FRIGHT,
				'speed_tunnel' : GHOST_SPEED_TUNNEL,
				'speed_eaten' : GHOST_SPEED_EATEN,
				'color': DrawingGenerics.GHOST_COLOR[4],
				'tag': DrawingGenerics.TAG_GHOST}
	_ghostSpecs = {0 : _ghost1, 1 : _ghost2, 2 : _ghost3, 3 : _ghost4}
	return _ghostSpecs

def getWallSpecifications():
	"""
	Return wall item drawing specifications
	@return: wall specs
	"""
	_wallSpecs = []
	
	## Outer boundary walls ##
	# Top horizontal boundary wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 3 * DrawingGenerics.TILE_SIZE,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 4 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Bottom horizontal boundary wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 33 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 34 * DrawingGenerics.TILE_SIZE,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Left-upper vertical boundary wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 3 * DrawingGenerics.TILE_SIZE,
				'xRight': DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Left-lower vertical boundary wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 34 * DrawingGenerics.TILE_SIZE,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right-upper vertical boundary wall
	_wallSpecs.append({'xLeft': DrawingGenerics.MAP_WIDTH - DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 3 * DrawingGenerics.TILE_SIZE,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right-lower vertical boundary wall
	_wallSpecs.append({'xLeft': DrawingGenerics.MAP_WIDTH - DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 34 * DrawingGenerics.TILE_SIZE,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## Tunnel walls ##
	# Upper-left tunnel wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Upper-right tunnel wall
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Lower-left tunnel wall
	_wallSpecs.append({'xLeft': 0,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Lower-right tunnel wall
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': DrawingGenerics.MAP_WIDTH,
				'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## Ghost enclosure walls ##
	# Left wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 11 * DrawingGenerics.TILE_SIZE,
				'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right wall
	_wallSpecs.append({'xLeft': 17 * DrawingGenerics.TILE_SIZE,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Lower wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 19 * DrawingGenerics.TILE_SIZE,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 20 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Upper-left horizontal wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 13 * DrawingGenerics.TILE_SIZE,
				'yBottom': 16 * DrawingGenerics.TILE_SIZE,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Upper-right horizontal wall
	_wallSpecs.append({'xLeft': 15 * DrawingGenerics.TILE_SIZE,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 16 * DrawingGenerics.TILE_SIZE,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Invisible upper horizontal wall
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 15 * DrawingGenerics.TILE_SIZE,
				'yBottom': 16 * DrawingGenerics.TILE_SIZE,
				'color': None,
				'tag': DrawingGenerics.TAG_WALL})
	# Enclosure door
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE,
				'yTop': 15 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING + DrawingGenerics.PIXEL,
				'xRight': 15 * DrawingGenerics.TILE_SIZE,
				'yBottom': 16 * DrawingGenerics.TILE_SIZE - DrawingGenerics.PIXEL,
				'color': DrawingGenerics.DOOR_COLOR,
				'tag': DrawingGenerics.TAG_DOOR})
	
	## Top middle vertical wall ##
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 3 * DrawingGenerics.TILE_SIZE,
				'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 4 top horizontal walls ##
	_wallSpecs.append({'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 5 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 8 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 horizontal short walls near the top left / top right corners ##
	_wallSpecs.append({'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 3 T-shaped walls near the top middle ##
	# Left T wall
	_wallSpecs.append({'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Middle T wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 11 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right T wall
	_wallSpecs.append({'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 9 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 17 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 12 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yBottom': 14 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 verticle walls near middle left / middle right ##
	_wallSpecs.append({'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 18 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 T walls below the ghost enclosure ##
	# Upper T wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 21 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 23 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Lower T wall
	_wallSpecs.append({'xLeft': 10 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 18 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 13 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'xRight': 15 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 horizontal short walls below the ghost enclosure ##
	_wallSpecs.append({'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 upside-down L walls near the bottom left / bottom right corners ##
	# Left one
	_wallSpecs.append({'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 4 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'xRight': 6 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right one
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 24 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 22 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'xRight': 24 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 little nudges out of the left / right outer wall near the bottom corners ##
	_wallSpecs.append({'xLeft': 1 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 3 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 25 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yBottom': 29 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	## 2 upside-down T walls at the bottom of the map ##
	# Left one
	_wallSpecs.append({'xLeft': 2 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 12 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 7 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 9 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	# Right one
	_wallSpecs.append({'xLeft': 16 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 26 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 32 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	_wallSpecs.append({'xLeft': 19 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'yTop': 27 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'xRight': 21 * DrawingGenerics.TILE_SIZE - DrawingGenerics.TILE_CENTERING,
				'yBottom': 30 * DrawingGenerics.TILE_SIZE + DrawingGenerics.TILE_CENTERING,
				'color': DrawingGenerics.WALL_OUTLINE,
				'tag': DrawingGenerics.TAG_WALL})
	
	return _wallSpecs
	
def getBonusItemSpecifications():
	"""
	Return bonus item drawing specifications
	@return: bonus specs
	"""
	_bonusItemSpec = {'xCenter': GHOST_START['xCenter'],
			'yCenter': (20 * DrawingGenerics.TILE_SIZE) + DrawingGenerics.TILE_CENTERING,
			'radius': DrawingGenerics.BONUS_RADIUS,
			'color': DrawingGenerics.BONUS_COLOR,
			'tag': DrawingGenerics.TAG_BONUS,
			'points': 500}
	
	return _bonusItemSpec
