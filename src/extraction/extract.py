
def extract_equations_and_tokens(lines):
	operand_tokens = {}
	symbol_tokens = {}

	queries = lines.pop()
	initialized_facts = lines.pop()
	equations = lines

	for equation in equations:
		create_equation(equation)


def create_equation(equation):
	parts = equation.split('<=>')
	if len(parts) != 2:
		parts = equation.split('=>')

