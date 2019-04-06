from src.helpers.notifications import display_error_with_exit
from src.helpers.constants import *
import re


def validate_lines(lines):
	if len(lines) < 3:
		display_error_with_exit("File must contain at least 3 lines with equation, initialized facts and queries")

	initialized_facts = ''
	queries = ''
	equations = []
	for line in lines:
		if line[0] == QUERY_TOKEN and validate_queries(line):
			queries += line.replace('?', '')
		elif line[0] == INITIALIZED_FACTS_TOKEN and validate_initialized_facts(line):
			initialized_facts += line.replace('=', '')
		elif validate_equation(line):
			equations.append(line)
	return equations, initialized_facts, queries


def validate_queries(queries):
	pattern = re.compile("^\?[A-Z]+$")
	if not pattern.match(queries):
		display_error_with_exit("Queries must contain at least 2 symbols. Sign '?' and facts. Example: '?ADF'")
	return True


def validate_initialized_facts(initialized_facts):
	pattern = re.compile("^=([A-Z]+)?$")
	if not pattern.match(initialized_facts):
		display_error_with_exit("Initialized facts must contain at least 2 symbols. Sign '=' and facts. Example: '=ADF'")
	return True


def validate_equation(equation):
	sides = equation.split("<=>")
	if len(sides) == 2:
		display_error_with_exit("Biconditional rules are not supported: Bonus part")

	sides = equation.split("=>")
	if len(sides) != 2:
		display_error_with_exit("An equation must contain between left and right side implies sign '=>' or '<=>'")

	if len(sides[0]) == 0 or len(sides[1]) == 0:
		display_error_with_exit("Each side of equation must contain fact or condition with facts")

	for token in [OR, XOR, LB, RB]:
		if token in sides[RIGHT]:
			display_error_with_exit("Right side of {} contains unsupported symbols".format(equation))

	validate_side_of_equation(sides[0])
	validate_side_of_equation(sides[1])
	return True

def validate_extra_chars(str):
	new_str = re.sub(r'([A-Z]|!|\||\^|\+)', "", str)
	if len(new_str) > 0:
		display_error_with_exit("The string should not contain only capitalized letters and operators: " + new_str)

def validate_operator_operand_pair(pair, operand_pattern, operator_pattern):
	if len(pair) == 1:
		if not operand_pattern.match(pair[0]):
			display_error_with_exit("The equation contains an invalid operand: " + pair[0])
	else:
		if not operand_pattern.match(pair[0]):
			display_error_with_exit("The equation contains an invalid operand: " + pair[0])
		if not operator_pattern.match(pair[1]):
			display_error_with_exit("The equation contains an invalid operator: " + pair[1])

def validate_side_of_equation(side):
	validate_extra_chars(side)

	operand_pattern = re.compile("([A-Z]|!)") # regex match to validate operand
	operator_pattern = re.compile("(\||\^|\+)") # regex match to validate operator

	for i in range(0, len(side), 2): # go over the side string by 2 and validate character pairs
		validate_operator_operand_pair(side[i:i+2], operand_pattern, operator_pattern)