import sys
from src.helpers.notifications import display_error_with_exit
from src.parsing.parse_file import parse_and_validate_file
from src.extraction.extract import extract_equations_and_facts
from src.solver import find_answers_for_all_main_questions


if __name__ == "__main__":

	if len(sys.argv) < 2 or len(sys.argv) > 2:
		display_error_with_exit("You must add only one file to arguments")

	equations, initialized_facts, queries = parse_and_validate_file(sys.argv[1])
	equations_dict, facts = extract_equations_and_facts(equations, initialized_facts)

	find_answers_for_all_main_questions(equations_dict, facts, queries)
