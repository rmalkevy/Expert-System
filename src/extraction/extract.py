from src.helpers import constants
from src.classes.equation import Equation
from src.classes.token import Token


def extract_equations_and_facts(equations, initialized_facts):
	facts = create_facts(initialized_facts)
	equations = [create_equation(equation) for equation in equations]
	equations_dict = create_equations_dict(equations)
	return equations_dict, facts


def create_equation(equation):
	equation_type = constants.TWO_WAY
	parts = equation.split('<=>')
	if len(parts) != 2:
		parts = equation.split('=>')
		equation_type = constants.ONE_WAY

	equation = Equation(parts[0], parts[1], equation_type)
	return equation


def create_facts(initialized_facts):
	facts = {}
	for char in list(set(initialized_facts)):
		facts[char] = Token(constants.OPERATOR, char)
	return initialize_facts(facts, initialized_facts)


def initialize_facts(facts, initialized_facts):
	for char in initialized_facts:
		facts[char].status = True
	return facts


def create_equations_dict(equations):
	equations_dict = dict()
	for eq in equations:
		if constants.AND in eq.right_side:
			facts = [fact for fact in eq.right_side if fact != constants.AND]
		else:
			facts = eq.right_side

		for fact in facts:
			if fact in equations_dict:
				equations_dict[fact].append(eq)
			else:
				equations_dict[fact] = [eq]
	return equations_dict
