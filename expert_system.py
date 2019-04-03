import sys
from src.helpers.errors import *
from src.parsing.parse_file import parse_and_validate_file
from src.extraction.extract import extract_equations_and_facts


if __name__ == "__main__":

	if len(sys.argv) < 2 or len(sys.argv) > 2:
		display_error_with_exit("You must add only one file to arguments")

	lines = parse_and_validate_file(sys.argv[1])
	queries = lines.pop().replace('?', '')
	initialized_facts = lines.pop().replace('=', '')
	equations, facts = extract_equations_and_facts(lines, initialized_facts)
