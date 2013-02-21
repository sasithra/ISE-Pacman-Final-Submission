"""
Gameplay module
@author: Jason Cohen
@author: Shaun Hamelin-Owens
@author: Sasithra Thanabalan
@author: Andrew Walker
"""
# Imports
from maps import MapCoordinator
from display import GameFrame, DrawingGenerics

from time import *
import sys
import Pacman
import GameItem
import Wall
import Dot
import Ghost
import Energizer
import BonusItem

class GamePlay():
	"""
	GamePlay class.
	This class takes care of all the game interactions and logic.
	It initializes all the game object instances and manages the different levels of play.
	"""
	def __init__(self, gameManager, user, level):
		"""
		Initialization.
		This method creates a Ghost instance, initializes it and draws it.
		
		@param gameManager: The calling class that manages execution and closing of the game
		@param user: User account that is playing, can be a logged in user or a guest account
		@param level: Requested starting level
		"""
		self.gameManager = gameManager
		self.uiCoordinator = gameManager.uiCoordinator
		self.highscore = user.highscore
		self.username = user.username
		self.level = level
		
		# List items
		self.ghosts = []
		self.dots = []
		self.energizers = []
		self.walls = []
		
		self.pause_ = False
		self.window_open = False
		self.game_done = False

		# Game settings
		self.eatGhostMult = 1
		self.gameScore = 0
		self.lives = 3
		self.lifeAdded = {1:False, 2:False}
		self.bonusAdded = {1:False, 2:False}
		
		self.setupWindow()
		self.setupScore()
		self.bindKeys()
		
		self.loadMapSpecs(level)
		
		self.prepareGameItems()
		
		self.createStartText()
		
	def createStartText(self):
		"""
		Create Starting Text.
		Takes care of displaying the starting READY! text under the ghost enclosure.
		The text only stays for a maximum of 5 seconds.
		
		"""
		self.readyTextID = self.gameCanvas.create_text(DrawingGenerics.TILE_SIZE * 14,
				DrawingGenerics.TILE_SIZE * 20 + DrawingGenerics.TILE_CENTERING,
				fill = "yellow", text = "READY!",
				font = ("Times", "22", "bold"))
		self.uiCoordinator.after(5000, self.removeText)
	
	def removeText(self):
		"""
		Remove Text.
		This method removes the starting text READY!.
		
		"""
		if not self.readyTextID is None:
			self.gameCanvas.delete(self.readyTextID)
	
	def bindKeys(self):
		"""
		Bind Keys.
		Takes care of binding keyboard keys to the different frame buttons.
		
		"""
		self.mainGameWindow.bind_all("q", self.exitKey)
		self.mainGameWindow.bind_all("p", self.pauseKey)
		self.mainGameWindow.bind_all("h", self.helpKey)
		self.mainGameWindow.bind_all("m", self.mainKey)
		
		self.infoFrame.options.bind("<Button-1>", self.mainKey)
		self.infoFrame.pause.bind("<Button-1>", self.pauseKey)
		self.infoFrame.hhelp.bind("<Button-1>", self.helpKey)
		self.infoFrame.exit.bind("<Button-1>", self.exitKey)
		
		self.help_frame.close.bind("<Button-1>", self.closeHelpFrame)
		self.help_frame.close.bind("<Return>", self.closeHelpFrame)
		
		self.close_frame.no.bind("<Button-1>", self.closeCloseFrame)
		self.close_frame.no.bind("<Return>", self.closeCloseFrame)
		self.close_frame.yes.bind("<Button-1>", self.closeGame)
		self.close_frame.yes.bind("<Return>", self.closeGame)
		
		self.main_frame.no.bind("<Button-1>", self.closeMain)
		self.main_frame.yes.bind("<Button-1>", self.returnMenu)
		self.main_frame.no.bind("<Return>", self.closeMain)
		self.main_frame.yes.bind("<Return>", self.returnMenu)

	def unBind(self):
		"""
		Unbind Keys.
		Takes care of unbinding keyboard keys from the different frame buttons.
		
		"""
		self.mainGameWindow.unbind_all("q")
		self.mainGameWindow.unbind_all("p")
		self.mainGameWindow.unbind_all("h")
		self.mainGameWindow.unbind_all("m")
		
		self.infoFrame.options.unbind("<Button-1>")
		self.infoFrame.pause.unbind("<Button-1>")
		self.infoFrame.hhelp.unbind("<Button-1>")
		self.infoFrame.exit.unbind("<Button-1>")
		
		self.help_frame.close.unbind("<Button-1>")
		self.help_frame.close.unbind("<Return>")
		
		self.close_frame.no.unbind("<Button-1>")
		self.close_frame.yes.unbind("<Button-1>")
		self.close_frame.no.unbind("<Return>")
		self.close_frame.yes.unbind("<Return>")
		
		self.main_frame.no.unbind("<Button-1>")
		self.main_frame.yes.unbind("<Button-1>")
		self.main_frame.no.unbind("<Return>")
		self.main_frame.yes.unbind("<Return>")
	
	def setupWindow(self):
		"""
		Setup Window.
		Sets up the game window and all enclosed frames.
		
		"""
		self.mainGameWindow = GameFrame.MGameFrame(self.uiCoordinator)
		self.gameFrame = self.mainGameWindow._gf
		self.gameCanvas = self.gameFrame.gf
		self.scoreFrame = self.mainGameWindow._sf
		self.infoFrame = self.mainGameWindow._if
		self.help_frame = self.mainGameWindow._hf
		self.close_frame = self.mainGameWindow._cf 
		self.main_frame = self.mainGameWindow._mf
		self.lives_frame = self.mainGameWindow._lf

	def setupScore(self):
		"""
		Setup Score.
		Prepares the score frame with a score and highscore.
		
		"""
		self.scoreFrame.name.configure(text = self.username)
		self.scoreFrame.highscoreText.set(self.highscore)
		
	def loadMapSpecs(self, level):
		"""
		Load Map Specs.
		Load the desired map into the game with all the level specifications
		
		@param level: The desired map level to load.
		"""
		# Attempt to load the map
		self.map = MapCoordinator.getMap(level)
		
		if (self.map is not None):
			self.dotSpecifications = self.map.getDotSpecifications()
			self.energizerSpecifications = self.map.getEnergizerSpecifications()
			self.bonusItemSpecifications = self.map.getBonusItemSpecifications()
			self.ghostSpecifications = self.map.getGhostSpecifications()
			self.wallSpecifications = self.map.getWallSpecifications()
			self.pacmanSpecifications = self.map.getPacmanSpecifications()
			
		else:
			print "Fatal error: Map could not be loaded."
			raise SystemExit
	
	def prepareGameItems(self):
		"""
		Prepare Game Items.
		Setup all the game items from the map level specifications.
		
		"""
		
		for i in range(len(self.wallSpecifications)):
			self.walls.append(Wall.Wall(self.gameCanvas, self.wallSpecifications[i]))
		
		for i in range(len(self.dotSpecifications)):
			self.dots.append(Dot.Dot(self.gameCanvas, self.dotSpecifications[i]))
		
		for i in range(len(self.energizerSpecifications)):
			self.energizers.append(Energizer.Energizer(self.gameCanvas, self.energizerSpecifications[i]))
		
		self.bonusItem = BonusItem.BonusItem(self.gameCanvas, self.bonusItemSpecifications)
		
		self.pacman = Pacman.Pacman(self, self.gameCanvas, self.pacmanSpecifications)
		
		for i in range(len(self.ghostSpecifications)):
			self.ghosts.append(Ghost.Ghost(self, self.gameCanvas, i + 1, self.ghostSpecifications[i]))
	
	def start(self):
		"""
		Start.
		Runs the game for one iteration. Manages pausing, game over,
		object processing and interaction.
		
		"""
		if (not self.pause_) and (not self.game_done):
			# Check level ending condition
			if len(self.dots) == 0 and len(self.energizers) == 0:
				# Reset the game for the next level
				self.levelWon()
				return
			else:
				# Process all the game items
				self.pacman.process()
				
				for ghost in self.ghosts:
					ghost.process()
					
				for energizer in self.energizers:
					energizer.process()
				self.bonusItem.process()
				
				# Check for overlaps between all game items
				for energizer in self.energizers:
					if self.pacman.inTile() == energizer.inTile():
						energizerPoints = energizer.eat()
						self.addToScore(energizerPoints)
						self.energizers.remove(energizer)
						
						self.eatGhostMult = 1;
						
						for ghost in self.ghosts:
							if ghost.state != DrawingGenerics.GHOST_STATE['Eaten']:
								ghost.fright(self.map.GHOST_FRIGHT_CYCLES)
						self.pacman.energized(self.map.GHOST_FRIGHT_CYCLES)
						break
						
				for dot in self.dots:
					if self.pacman.inTile() == dot.inTile():
						dotPoints = dot.eat()
						self.addToScore(dotPoints)
						self.dots.remove(dot)
						self.pacman.setHaltIterations(1)
						if self.getDotsEaten() >= 70 and self.bonusAdded[1] == False:
							self.bonusItem.activate()
							self.bonusAdded[1] = True
						elif self.getDotsEaten() >= 170 and self.bonusAdded[2] == False:
							self.bonusItem.activate()
							self.bonusAdded[2] = True
						break
				
				if self.pacman.inTile() == self.bonusItem.inTile() and self.bonusItem.isActive():
					bonusPoints = self.bonusItem.eat()
					self.bonusItem.deactivate()
					self.addToScore(bonusPoints)
					
				for ghost in self.ghosts:
					if self.pacman.inTile() == ghost.inTile():
						if ghost.state == DrawingGenerics.GHOST_STATE['Fright']:
							ghostPoints = ghost.eat()
							self.addToScore(ghostPoints * self.eatGhostMult)
							self.eatGhostMult *= 2
						elif ghost.state == DrawingGenerics.GHOST_STATE['Eaten']:
							pass
						else:
							if self.loseLife():
								self.pacman.restart()
								for ghost in self.ghosts:
									ghost.restart()
								for energizer in self.energizers:
									energizer.resetColor()
								self.uiCoordinator.after(5000, self.start)
								return
							else:
								# Game over
								self.returnMenu('e')
								return
				self.uiCoordinator.after(DrawingGenerics.REFRESH_RATE, self.start)
		else:
			self.uiCoordinator.after(DrawingGenerics.REFRESH_RATE, self.start)
		
	def loseLife(self):
		"""
		Lose Life.
		Takes care of removing a pacman life.
		
		"""
		self.lives -= 1
		self.lives_frame.removeLife()
		# Check game over condition
		if self.lives == 0:
			return False
		else:
			return True
	
	def levelWon(self):
		"""
		Level Won.
		This method takes care of moving on to the next level, reloading the
		new map specs and restarting the game.
		
		"""
		if self.level != 3:
			self.level = self.level + 1
			
		# Delete all game canvas drawings for reload
		self.pacman.deleteDrawing()
		self.bonusItem.deactivate()
		self.bonusAdded = {1:False, 2:False}
		for i in range(0,4):
			self.ghosts.pop().deleteDrawing()
		
		for wall in self.walls:
			wall.deleteDrawing()
			self.walls.remove(wall)
			
		# Reload all game specs for the new level
		self.loadMapSpecs(self.level)
		self.prepareGameItems()
		self.createStartText()
		self.uiCoordinator.after(5000, self.start)
	
	def addToScore(self, scoreUpdate):
		"""
		Add To Score.
		Updates the game score with the addition as well as displaying it to the score frame.
		
		@param scoreUpdate: Amount of points to be added to the score.
		"""
		self.gameScore += scoreUpdate
		self.scoreFrame.updateScore(self.gameScore)
		
		# Pacman gains a life if his score exceeds 10000 and 100000
		if self.gameScore >= 10000 and self.lifeAdded[1] == False:
			self.addLife()
			self.lifeAdded[1] = True
		elif self.gameScore >= 100000 and self.lifeAdded[2] == False:
			self.addLife()
			self.lifeAdded[2] = True

	def addLife(self):
		"""
		Add Life.
		Add a life to the game and update the lives frame with this change
		
		"""
		self.lives += 1
		self.lives_frame.addLife()
	
	def getWalls(self):
		"""
		Get Walls.
		Getter method for the game walls.
		
		@return: walls: The game walls.
		"""
		return self.walls
	
	def getDots(self):
		"""
		Get Dots.
		Getter method for the game Dots still in play.
		
		@return: dots: The game dots still in play.
		"""
		return self.dots
	
	def getDotsEaten(self):
		"""
		Get Dots Eaten.
		Getter method for the number of dots eaten so far in the game.
		
		@return: dotsEaten: The number of game dots eaten so far.
		"""
		return 240 - len(self.dots)
	
	def getGhosts(self):
		"""
		Get Ghosts.
		Getter method for the ghost objects in the game.
		
		@return: ghosts: The ghosts instances.
		"""
		return self.ghosts
	
	def getPacman(self):
		"""
		Get Pacman.
		Getter method for the pacman instance in the game.
		
		@return: pacman: The pacman instance in the game.
		"""
		return self.pacman
		
	def exitKey(self, e):
		"""
		Exit Key.
		Open exit dialog.
		
		@param e: Input from keyboard
		"""
		if (not self.pause_):
			self.pause_ = True
			self.window_open = True
			self.infoFrame.pausePress()
			self.close_frame.no.focus_set()
			self.mainGameWindow.liftFrame(self.close_frame.close_frame)
			self.infoFrame.exitPress()
		elif (self.pause_):
			if (not self.window_open):
				self.window_open = True
				self.close_frame.no.focus_set()
				self.mainGameWindow.liftFrame(self.close_frame.close_frame)
				self.infoFrame.exitPress()
			elif (self.window_open and self.infoFrame.exit_red):
				self.window_open = False
				self.gameCanvas.focus_set()
				self.mainGameWindow.lowerFrame(self.close_frame.close_frame)
				self.infoFrame.exitPress()

	def closeCloseFrame(self, e):
		"""
		Close Close Frame.
		Close the close dialog frame.
		
		@param e: Input from keyboard
		"""
		self.gameCanvas.focus_set()
		self.mainGameWindow.lowerFrame(self.close_frame.close_frame)
		self.exitKey("a")

	def closeGame(self, e):
		"""
		Close Game.
		Exit the game.
		
		@param e: Input from keyboard
		"""
		if (self.gameScore > self.highscore):
			self.gameManager.user.highscore = self.gameScore
		self.gameManager.updateHighscores()
		self.mainGameWindow.quit()

	def helpKey(self, e):
		"""
		Help Key.
		Open help menu dialog.
		
		@param e: Input from keyboard
		"""
		if (not self.pause_):
			self.pause_ = True
			self.window_open = True
			self.help_frame.close.focus_set()
			self.infoFrame.pausePress()
			self.mainGameWindow.liftFrame(self.help_frame.help_frame)
			self.infoFrame.helpPress()
		elif (self.pause_):
			if (not self.window_open):
				self.window_open = True
				self.help_frame.close.focus_set()
				self.mainGameWindow.liftFrame(self.help_frame.help_frame)
				self.infoFrame.helpPress()
			elif (self.window_open and self.infoFrame.help_red):
				self.window_open = False
				self.gameCanvas.focus_set()
				self.mainGameWindow.lowerFrame(self.help_frame.help_frame)
				self.infoFrame.helpPress()
				
	def mainKey(self, e):
		"""
		Main Key.
		Open main menu dialog.
		
		@param e: Input from keyboard
		"""
		if (not self.pause_):
			self.pause_ = True
			self.window_open = True
			self.main_frame.no.focus_set()
			self.infoFrame.pausePress()
			self.mainGameWindow.liftFrame(self.main_frame.main_frame)
			self.infoFrame.mainPress()
		elif (self.pause_):
			if (not self.window_open):
				self.window_open = True
				self.main_frame.no.focus_set()
				self.mainGameWindow.liftFrame(self.main_frame.main_frame)
				self.infoFrame.mainPress()
			elif (self.window_open and self.infoFrame.main_red):
				self.window_open = False
				self.gameCanvas.focus_set()
				self.mainGameWindow.lowerFrame(self.main_frame.main_frame)
				self.infoFrame.mainPress()

	def closeHelpFrame(self, e):
		"""
		Close Help Frame.
		Close help frame dialog.
		
		@param e: Input from keyboard
		"""
		self.mainGameWindow.lowerFrame(self.help_frame.help_frame)
		self.gameCanvas.focus_set()
		self.helpKey("a")

	def closeMain(self, e):
		"""
		Close Main.
		Close main menu dialog.
		
		@param e: Input from keyboard
		"""
		self.mainGameWindow.lowerFrame(self.main_frame.main_frame)
		self.gameCanvas.focus_set()
		self.mainKey("a")

	def returnMenu(self, e):
		"""
		Return Menu.
		Return to main menu.
		
		@param e: Input from keyboard
		"""
		self.game_done = True
		self.readyTextID = None
		if (self.gameScore > self.highscore):
			self.gameManager.user.highscore = self.gameScore
		self.gameManager.user.score = self.gameScore
		self.gameManager.updateHighscores()
		self.gameManager.runMenu()
		self.unBind()
		self.mainGameWindow.root.destroy()

	def pauseKey(self, e):
		"""
		Pause Key.
		Pause the gameplay.
		
		@param e: Input from keyboard
		"""
		if not self.pause_:
			self.pause_ = True
			self.infoFrame.pausePress()
		elif (self.pause_ and (not self.window_open)):
			self.pause_ = False
			self.infoFrame.pausePress()
