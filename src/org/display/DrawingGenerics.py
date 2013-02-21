
"""
Drawing Generics class.
This class contains the generic variables and units of measurements of all the 
Pacman Canvas items in the game.

@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
#--------------------------------------------------------------------------------
# Generic game specifications for the game frame only
#--------------------------------------------------------------------------------

PIXEL = 2
TILE_SIZE = 8 * PIXEL
TILE_CENTERING = TILE_SIZE / 2
MAP_WIDTH_UNITS = 28
MAP_HEIGHT_UNITS = 36
MAP_WIDTH = TILE_SIZE * MAP_WIDTH_UNITS
MAP_HEIGHT = TILE_SIZE * MAP_HEIGHT_UNITS

#--------------------------------------------------------------------------------
# Screen refresh rate (in milliseconds) ~ 60 frames/second and timing
#--------------------------------------------------------------------------------
REFRESH_RATE = 12
CYCLES_PER_SECOND = int(1000 / REFRESH_RATE)

#--------------------------------------------------------------------------------
# For the drawn wall, not the specification wall used in game logic
#--------------------------------------------------------------------------------
OUTER_WALL_WIDTH = TILE_SIZE / 2

#--------------------------------------------------------------------------------
# Ghost modes of operation (states)
#--------------------------------------------------------------------------------
GHOST_STATE = {'Chase': 1,'Scatter': 2,'Fright': 3, 'Eaten': 4}

#--------------------------------------------------------------------------------
# Pacman modes of operation (states)
#--------------------------------------------------------------------------------
PACMAN_STATE = {'Normal': 1,'Energized': 2}
PACMAN_RADIUS = 6 * TILE_SIZE / 8
GHOST_RADIUS = 6 * TILE_SIZE / 8
DOT_RADIUS = TILE_SIZE / 8
ENERGIZER_RADIUS = TILE_SIZE / 2
BONUS_RADIUS = ENERGIZER_RADIUS

#--------------------------------------------------------------------------------
# Defines the shape of each Game Canvas item.
#--------------------------------------------------------------------------------
WALL_SHAPE = "rectangle"
PACMAN_SHAPE = "oval"
GHOST_SHAPE = "rectangle"
DOT_SHAPE = "oval"
ENERGIZER_SHAPE = "oval"
BONUS_SHAPE = "oval"

#--------------------------------------------------------------------------------
# Defines of all the game items with their respective characteristics 
# (color, key etc.) and states of game characters.
#--------------------------------------------------------------------------------
WALL_OUTLINE = "blue"
DOOR_COLOR = "grey"
PACMAN_COLOR = "yellow" 
GHOST_COLOR = {1: "cyan", 2: "pink", 3: "orange", 4: "red"}
GHOST_FRIGHT_COLOR = {1: "blue", 2: "white"}
DOT_COLOR = "white"
ENERGIZER_COLOR = {1: "white", 2: "black"}
BONUS_COLOR = "red"

#--------------------------------------------------------------------------------
## Defines of all the character and game item tags.
#--------------------------------------------------------------------------------
TAG_GHOST = "Ghost"
TAG_PACMAN = "Pacman"
TAG_WALL = "Wall"
TAG_DOOR = "Door"
TAG_DOT = "Dot"
TAG_ENERGIZER = "Energizer"
TAG_BONUS = "Bonus"
