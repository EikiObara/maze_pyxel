import pyxel

import maze as mz

WINDOW_WIDTH = 230
WINDOW_HEIGHT = 230
WALL_SIZE = 10
OFFSET = 2

class MazeDrawer:
	def __init__(self, width, height, blockSize):
		pyxel.init(width, height)
		self.maze = mz.Maze(int(width / blockSize), int(height / blockSize))
		self.maze.Run()
		self.maze.Display()
		self.blockSize = blockSize
		
		pyxel.run(self.update, self.draw)
		
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		
	def draw(self):
		pyxel.cls(0)
		for row in range(len(self.maze.map)):
			for col in range(len(self.maze.map[row])):
				if self.maze.map[row][col] == 0:
					pyxel.rect(row * self.blockSize, \
					col * self.blockSize, \
					row * self.blockSize + self.blockSize - OFFSET, \
					col * self.blockSize + self.blockSize - OFFSET, 9)
		# pyxel.rect(0,0,WALL_SIZE,WALL_SIZE,10)


drawer = MazeDrawer(WINDOW_WIDTH, WINDOW_HEIGHT, WALL_SIZE)