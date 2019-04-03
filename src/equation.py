class Equation:
	def __init__(self, left_side, right_side, equation_type):
		self.left_side = left_side
		self.right_side = right_side
		self.type = equation_type

	def __str__(self):
		return "left_side = {}; right_side = {}; type = {}".format(str(self.left_side), str(self.right_side), str(self.type))
