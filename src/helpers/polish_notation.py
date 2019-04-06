from src.helpers.constants import *
from src.classes.stack import Stack


def to_polish_notation(tokens):
	operators = dict()
	operators[NOT] = 4
	operators[AND] = 3
	operators[OR] = 2
	operators[XOR] = 2
	operators[LB] = 1
	operators[RB] = 1
	operators_stack = Stack()
	postfix_polish_notation_list = []

	for token in tokens:
		if token not in operators and token != LB and token != RB:
			postfix_polish_notation_list.append(token)
		elif token == LB:
			operators_stack.push(token)
		elif token == RB:
			first_token = operators_stack.pop()
			while first_token != LB:
				postfix_polish_notation_list.append(first_token)
				first_token = operators_stack.pop()
		else:
			while not operators_stack.is_blank() != 0 and operators[operators_stack.look_top()] >= operators[token]:
				postfix_polish_notation_list.append(operators_stack.pop())
			operators_stack.push(token)

	while not operators_stack.is_blank():
		postfix_polish_notation_list.append(operators_stack.pop())
	return postfix_polish_notation_list
