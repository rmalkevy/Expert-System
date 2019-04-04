from src.helpers.errors import display_error_with_exit
import re


def validate_lines(lines):
	if len(lines) < 3:
		display_error_with_exit("File must contain at least 3 lines with equation, initialized facts and queries")

	queries = lines[-1].replace(' ', '')
	validate_queries(queries)

	initialized_facts = lines[-2]
	validate_initialized_facts(initialized_facts)

	equations = lines[0:-2]
	validate_equations(equations)


def validate_queries(queries):
	pattern = re.compile("^\?[A-Z]+$")
	if not pattern.match(queries):
		display_error_with_exit("Queries must contain at least 2 symbols. Sign '?' and facts. Example: '?ADF'")


def validate_initialized_facts(initialized_facts):
	pattern = re.compile("^=[A-Z]+$")
	if not pattern.match(initialized_facts):
		display_error_with_exit("Initialized facts must contain at least 2 symbols. Sign '=' and facts. Example: '=ADF'")


def validate_equations(equations):
	[validate_equation(equation.replace(' ', '')) for equation in equations]


def validate_equation(equation):
	parties = equation.split("=>")
	if len(parties) < 2:
		parties = equation.split("<=>")
	if len(parties) != 2:
		display_error_with_exit("An equation must contain between left and right side implies sign '=>' or '<=>'")

	if len(parties[0]) == 0 or len(parties[1]):
		display_error_with_exit("Each side of equation must contain fact or condition with facts")

	validate_side_of_equation(parties[0])
	validate_side_of_equation(parties[1])


def validate_side_of_equation(side):
	pass
