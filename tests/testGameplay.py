##################
## Run the game ##
##################

import sys
sys.path.append('../src/org')

import testMapCoordinator as MapCoordinator
from display import GameFrame, DrawingGenerics


from time import *
import sys
from gameplay import Pacman
from gameplay import GameItem
from gameplay import Wall
from gameplay import Dot
from gameplay import Ghost
from gameplay import Energizer
from gameplay import BonusItem

#The test class test_Gameplay can't access map files using mapcoordinator from the tests folder, so testGameplay, which is identical to Gameplay, was created so that the maps could be accessed
class GamePlay():
	def __init__(self, gameManager, user, level):
		self.gameManager = gameManager
		self.uiCoordinator = gameManager.uiCoordinator
		self.highscore = user.highscore
		self.username = user.username
		self.level = level
		
		self.ghosts = []
		self.dots = []
		self.energizers = []
		self.walls = []
		
		self.pause_ = False
		self.window_open = False
		self.game_done = False

		self.eatGhostMult = 1
		self.gameScore = 0
		self.lives = 3
		self.lifeAdded = {1:False, 2:False}
		self.bonusAdded = {1:False, 2:False}
		# self.toggleChaseScatterCycles = 6 * DrawingGenerics.CYCLES_PER_SECOND # CHANGED SINCE DEMO
		# self.toggleChaseScatter = self.toggleChaseScatterCycles # CHANGED SINCE DEMO
		
		self.setupWindow()
		self.setupScore()
		self.bindKeys()
		
		self.loadMapSpecs(level)
		
		self.prepareGameItems()
		
		self.createStartText()
		
		
	def createStartText(self):
		self.readyTextID = self.gameCanvas.create_text(DrawingGenerics.TILE_SIZE * 14,
				DrawingGenerics.TILE_SIZE * 20 + DrawingGenerics.TILE_CENTERING,
				fill = "yellow", text = "READY!",
				font = ("Times", "22", "bold"))
		self.uiCoordinator.after(5000, self.removeText)
	
	def removeText(self):
		if not self.readyTextID is None:
			self.gameCanvas.delete(self.readyTextID)
	
	def bindKeys(self):
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

## Remove keybindings
	def unBind(self):
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
		self.scoreFrame.name.configure(text = self.username)
		self.scoreFrame.highscoreText.set(self.highscore)
		
	
	def loadMapSpecs(self, level):
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
		
		
		# self.pacman.draw()
		# for i in range(len(self.walls)):
			# self.walls[i].draw()
		# for i in range(len(self.dots)):
			# self.dots[i].draw()
		# for i in range(len(self.ghosts)):
			# self.ghosts[i].draw()
	
	def start(self):
		if (not self.pause_) and (not self.game_done):
			# Check level ending condition
			if len(self.dots) == 0 and len(self.energizers) == 0:
				self.levelWon()
				self.pacman.deleteDrawing()
				self.bonusItem.deactivate()
				self.bonusAdded = {1:False, 2:False}
				for i in range(0,4):
					self.ghosts.pop().deleteDrawing()
				
				for wall in self.walls:
					wall.deleteDrawing()
					self.walls.remove(wall)
					
				self.loadMapSpecs(self.level)
				self.prepareGameItems()
				self.createStartText()
				self.uiCoordinator.after(5000, self.start)
				return
			else:
				# Process all the game items
				self.pacman.process()
				
				for ghost in self.ghosts:
					ghost.process()
					
				for energizer in self.energizers:
					energizer.process()
				self.bonusItem.process()
				
				for energizer in self.energizers:
					if self.pacman.inTile() == energizer.inTile():
					# if self.pacman.findCurrentOverlappingWith(energizer):
						energizerPoints = energizer.eat()
						self.addToScore(energizerPoints)
						self.energizers.remove(energizer)
						#self.pacman.setHaltIterations(3)
						
						self.eatGhostMult = 1;
						
						for ghost in self.ghosts:
							if ghost.state != DrawingGenerics.GHOST_STATE['Eaten']:
								ghost.fright(self.map.GHOST_FRIGHT_CYCLES)
						self.pacman.energized(self.map.GHOST_FRIGHT_CYCLES)
						break
						
				for dot in self.dots:
					if self.pacman.inTile() == dot.inTile():
					# if self.pacman.findCurrentOverlappingWith(dot):
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
								self.returnMenu('e')
								return
				self.uiCoordinator.after(DrawingGenerics.REFRESH_RATE, self.start)
				# self.uiCoordinator.after(5000, self.start)
		else:
			self.uiCoordinator.after(DrawingGenerics.REFRESH_RATE, self.start)
		
	def loseLife(self):
		self.lives -= 1
		self.lives_frame.removeLife()
		if self.lives == 0:
			return False
		else:
			return True
	
	
	def levelWon(self):
		if self.level != 3:
			self.level = self.level + 1
		#Plus one life
		self.pacman.restart()
	
	def addToScore(self, scoreUpdate):
		self.gameScore += scoreUpdate
		self.scoreFrame.updateScore(self.gameScore)
		
		if self.gameScore >= 10000 and self.lifeAdded[1] == False:
			self.addLife()
			self.lifeAdded[1] = True
		elif self.gameScore >= 100000 and self.lifeAdded[2] == False:
			self.addLife()
			self.lifeAdded[2] = True

	def addLife(self):
		self.lives += 1
		self.lives_frame.addLife()
	
	def getWalls(self):
		return self.walls
	
	def getDots(self):
		return self.dots
	
	def getDotsEaten(self):
		return 240 - len(self.dots)
	
	def getGhosts(self):
		return self.ghosts
	
	def getPacman(self):
		return self.pacman
		
## Open exit dialog
	def exitKey(self, e):
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

## Close close dialog
	def closeCloseFrame(self, e):
		self.gameCanvas.focus_set()
		self.mainGameWindow.lowerFrame(self.close_frame.close_frame)
		self.exitKey("a")

## Exit the game
	def closeGame(self, e):
		if (self.gameScore > self.highscore):
			self.gameManager.user.highscore = self.gameScore
		self.gameManager.updateHighscores()
		self.mainGameWindow.quit()

## Open help menu dialog
	def helpKey(self, e):
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
				
## Open main menu dialog
	def mainKey(self, e):
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

## Close help frame dialog
	def closeHelpFrame(self, e):
		self.mainGameWindow.lowerFrame(self.help_frame.help_frame)
		self.gameCanvas.focus_set()
		self.helpKey("a")

## Close main menu dialog
	def closeMain(self, e):
		self.mainGameWindow.lowerFrame(self.main_frame.main_frame)
		self.gameCanvas.focus_set()
		self.mainKey("a")

## Return to main menu
	def returnMenu(self, e):
		self.game_done = True
		self.readyTextID = None
		if (self.gameScore > self.highscore):
			self.gameManager.user.highscore = self.gameScore
		self.gameManager.user.score = self.gameScore
		self.gameManager.updateHighscores()
		self.gameManager.runMenu()
		self.unBind()
		self.mainGameWindow.root.destroy()

## Pause
	def pauseKey(self, e):
		if not self.pause_:
			self.pause_ = True
			self.infoFrame.pausePress()
		elif (self.pause_ and (not self.window_open)):
			self.pause_ = False
			self.infoFrame.pausePress()


