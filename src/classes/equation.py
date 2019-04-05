from src.helpers.polish_notation import to_polish_notation
from src.helpers.constants import *
from src.helpers.notifications import display_error_with_exit


class Equation:
	def __init__(self, left_side_tokens, right_side_tokens, equation_type):
		self.left_side = to_polish_notation(left_side_tokens)
		self.right_side = to_polish_notation(right_side_tokens)
		self.type = equation_type

	def __str__(self):
		return "left_side = {}; right_side = {}; type = {}".format(str(self.left_side), str(self.right_side), str(self.type))

	def solve(self, facts_base, equations_dict):
		results_list = []

		for token in self.left_side:
			if token.isalpha():
				if token in facts_base:
					results_list.append(True)
				elif token in equations_dict:
					if token in self.right_side:
						results_list.append(False)
						continue

					result = False

					for equation in equations_dict[token]:
						is_solved = equation.solve(facts_base, equations_dict)

						if is_solved:
							result = is_solved
							break

					results_list.append(result)
				else:
					results_list.append(False)
			else:
				if token == NOT:
					results_list[LAST_ELEM] = not results_list[LAST_ELEM]
				elif len(results_list) < 2:
					display_error_with_exit("Something wrong with Polish notation. Interrupting...")
				elif token == AND:
					results_list[PREV_ELEM] = results_list[PREV_ELEM] and results_list[LAST_ELEM]
					results_list.pop()
				elif token == OR:
					results_list[PREV_ELEM] = results_list[PREV_ELEM] or results_list[LAST_ELEM]
					results_list.pop()
				elif token == XOR:
					results_list[PREV_ELEM] = results_list[PREV_ELEM] ^ results_list[LAST_ELEM]
					results_list.pop()
		return results_list[LAST_ELEM]
