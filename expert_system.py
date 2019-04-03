import sys
from src.helpers import *
from src.parsing.parse_file import parse_and_validate_file
from src.extraction.extract import extract_equations_and_tokens


if __name__ == "__main__":

	if len(sys.argv) < 2 or len(sys.argv) > 2:
		display_error_with_exit("You must add only one file to arguments")

	lines = parse_and_validate_file(sys.argv[1])
	print(lines)
	extract_equations_and_tokens(lines)
