import pyxel
import control as ctrl
import random as rm
import sys

sys.setrecursionlimit(10000)

import maze as mz

SCALE = 3
FPS = 15.0
BORDER = 2

DIFFICULTY = 2

BASE_COLOR = 15


SELL_SIZE	= 38
WINDOW_GAIN_ROW	= int(256 / SELL_SIZE)
WINDOW_GAIN_COL	= int(256 / SELL_SIZE)

WINDOW_WIDTH	= SELL_SIZE * WINDOW_GAIN_ROW
WINDOW_HEIGHT	= SELL_SIZE * WINDOW_GAIN_COL

OFFSET = 1

class App:
	def __init__(self, width, height, blockSize):
		pyxel.init(width, height, caption = "maze runner", \
		scale = SCALE, fps = FPS, \
		border_width = BORDER, border_color = BASE_COLOR)

		self.width = width
		self.height = height
		self.blockSize = blockSize
		
		self.setConstValue()
		self.setMaze()
		
		pyxel.run(self.update, self.draw)

##################################################################
		
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_R):
			self.blockSize = self.blockSize - DIFFICULTY
			self.setConstValue()
			self.setMaze()

		if self.isGoal == False:
			self.row, self.col = self.cl.run()
		
	def draw(self):
		pyxel.cls(0)
		self.mazeDraw()
		
		# destination
		self.drawCircle(self.rowDest, self.colDest, self.destColor)
		# player
		self.drawCircle(self.row, self.col, self.playerColor)
		
		self.goalDetect()
		
	def drawCircle(self, row, col, color):
		pyxel.circ(row * self.blockSize + self.blockSize / 2, \
		col * self.blockSize + self.blockSize / 2, \
		(self.blockSize - OFFSET) / 2, color)
		
	def mazeDraw(self):
		pyxel.cls(0)
		for rowtemp in range(len(self.maze.map)):
			for coltemp in range(len(self.maze.map[rowtemp])):
				if self.maze.map[rowtemp][coltemp] == 0:
					pyxel.rect(rowtemp * self.blockSize, \
					coltemp * self.blockSize, \
					rowtemp * self.blockSize + self.blockSize - OFFSET, \
					coltemp * self.blockSize + self.blockSize - OFFSET, \
					self.stageColor)
					
	def generateNode(self):
		tempRow = rm.randint(0, self.rowMax - 1)
		tempCol = rm.randint(0, self.colMax - 1)
		
		if (self.rowMax - 1) == tempRow or (self.colMax - 1) == tempCol:
			return self.generateNode()

		if self.maze.map[tempRow][tempCol] == 1:
			return tempRow, tempCol
		elif self.maze.map[tempRow][tempCol] == 0:
			return self.generateNode()
			
	def goalDetect(self):
		if self.row == self.rowDest and self.col == self.colDest:
			pyxel.text(self.width / 2.5, \
			self.blockSize / 3, \
			"Congraturation", rm.randint(1,14))
			self.isGoal = True
	
	def setConstValue(self):
		self.rowMax = int(self.width / self.blockSize)
		self.colMax = int(self.height / self.blockSize)
		
		self.playerColor = rm.randint(1, 4)
		self.destColor = rm.randint(5, 8)
		self.stageColor = rm.randint(9, 12)
		self.isGoal = False
	
	def setMaze(self):
		self.maze = mz.Maze(self.rowMax, self.colMax)
		self.maze.Run()
                # self.maze.Display()
		
		while True:
			self.row, self.col = self.generateNode()
			self.rowDest, self.colDest = self.generateNode()

			if self.row != self.rowDest or self.col != self.colDest:
				break
		
		self.cl = ctrl.control(self.row, self.col, self.maze.map)
		self.isGoal = False


App(WINDOW_WIDTH, WINDOW_HEIGHT, SELL_SIZE)
