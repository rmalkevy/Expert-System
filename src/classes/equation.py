import re


class Equation:
	def __init__(self, left_side_tokens, right_side_tokens, equation_type):
		self.left_side = [token for token in left_side_tokens]
		self.right_side = [token for token in right_side_tokens]
		self.type = equation_type
		self.ls_unique_chars = list(set(re.compile('[^A-Z]').sub('', left_side_tokens)))
		self.rs_unique_chars = list(set(re.compile('[^A-Z]').sub('', right_side_tokens)))

	def __str__(self):
		return "left_side = {}; right_side = {}; type = {}".format(str(self.left_side), str(self.right_side), str(self.type))
