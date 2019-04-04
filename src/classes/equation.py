import re
from src.helpers.polish_notation import to_polish_notation
from src.helpers.constants import *


class Equation:
	def __init__(self, left_side_tokens, right_side_tokens, equation_type):
		self.left_side = to_polish_notation(left_side_tokens)
		self.right_side = to_polish_notation(right_side_tokens)
		self.type = equation_type
		self.ls_unique_chars = list(set(re.compile('[^A-Z]').sub('', left_side_tokens)))
		self.rs_unique_chars = list(set(re.compile('[^A-Z]').sub('', right_side_tokens)))

	def __str__(self):
		return "left_side = {}; right_side = {}; type = {}".format(str(self.left_side), str(self.right_side), str(self.type))

	def solve(self, facts_base, equations_dict):
		stack = []

		for token in self.left_side:
			if token not in [NOT, AND, XOR, OR]:
				if token in facts_base and facts_base[token].status:
					stack.append(True)
				elif token in equations_dict:
					if token in self.right_side:
						stack.append(False)
						continue

					result = False

					for eq in equations_dict[token]:
						solve = eq.solve(facts_base, equations_dict)


						if solve:
							result = solve
							break

					stack.append(result)

				else:
					stack.append(False)
			else:
				if token == NOT:
					stack[-1] = not stack[-1]
				else:
					if len(stack) < 2:
						print('Warning! Redundant operator \'', token, '\'. Ignored!')
					else:
						if token == AND:
							stack[-2] = stack[-2] and stack[-1]
							stack.pop()
						elif token == OR:
							stack[-2] = stack[-2] or stack[-1]
							stack.pop()
						elif token == XOR:
							stack[-2] = stack[-2] ^ stack[-1]
							stack.pop()
		return stack[-1]
