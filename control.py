import pyxel

class control:
	def __init__(self, row, col, map):
		self.row = row
		self.col = col
		self.map = map
		
	# coordinate control
	def rowPlus(self):
		self.row = self.row + 1
	def rowMinus(self):
		self.row = self.row - 1
	def colPlus(self):
		self.col = self.col + 1
	def colMinus(self):
		self.col = self.col - 1
		
	def run(self):
		
		self.setBeforeCoord()
		
		if pyxel.btnp(pyxel.KEY_LEFT,4,4):
			self.rowMinus()
		elif pyxel.btnp(pyxel.KEY_RIGHT,4,4):
			self.rowPlus()
		elif pyxel.btnp(pyxel.KEY_UP,4,4):
			self.colMinus()
		elif pyxel.btnp(pyxel.KEY_DOWN,4,4):
			self.colPlus()
			
		self.wallJudgment()
		
		return self.row, self.col
	
	def setBeforeCoord(self):
		self.beforeRow = self.row
		self.beforeCol = self.col

	def wallJudgment(self):
		if self.map[self.row][self.col] == 0:
			self.row = self.beforeRow
			self.col = self.beforeCol


