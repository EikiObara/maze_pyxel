# This maze generator is defined
# 0 is wall, 1 is way

import random as rd

DIRECTION = 4	# 2D(Plane)
WALL = 0
ROAD = 1
STEP_WIDTH = 2

D_MAT = [[0,1],[1,0],[0,-1],[-1,0]]  # direction matrix

class Maze:
	def __init__(self, width, height):
		if self.Even(width):
			self.width = width - 1
		else:
			self.width = width

		if self.Even(height):
			self.height = height - 1
		else:
			self.height = height
		
		self.map = [[WALL for i in range(self.width)] for j in range(self.height)]
		
		self.Run()
		
	def Even(self, num):
		if num % 2 == 0:
			return True
		else:
			return False
		
	def RandomDirection(self):
		return rd.randrange(DIRECTION)
		
	def DecideStart(self):
		self.start_x = rd.randrange(1, self.width - 1, STEP_WIDTH)
		self.start_y = rd.randrange(1, self.height - 1, STEP_WIDTH)
		# self.Display()

		self.map[self.start_y][self.start_x] = ROAD
		
		# self.Display()
		
	def Generate(self, start_x, start_y):
		first_dict = self.RandomDirection()
		dict = first_dict
		
		while True:
			buf_x = start_x + D_MAT[dict][0] * 2
			buf_y = start_y + D_MAT[dict][1] * 2
			
			if buf_x < 0 or buf_x >= self.width \
				or buf_y < 0 or buf_y >= self.height \
				or self.map[buf_y][buf_x] != WALL:
				dict = dict + 1
				if dict == 4:
					dict = 0
				if dict == first_dict:
					return
				continue
			
			self.map[buf_y][buf_x] = ROAD
			self.map[start_y + D_MAT[dict][1]][start_x + D_MAT[dict][0]] = ROAD
			
			# self.Display()
			
			# 再帰で計算する
			self.Generate(buf_x, buf_y)
			
			first_dict = self.RandomDirection()
			dict = first_dict
	
	def Run(self):
		self.DecideStart()
		self.Generate(self.start_x, self.start_y)
	
	def Display(self):
		print("width = " + str(self.width))
		print("height = " + str(self.height))

		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if self.map[i][j] == ROAD:
					print(" ", end='')
				else:
					print("#", end='')
			print("")
