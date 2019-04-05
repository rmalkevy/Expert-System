from .clean_lines import get_lines_from_file
from .validation import validate_lines
from src.helpers.notifications import display_error_with_exit


def parse_and_validate_file(file_name):
	try:
		open(file_name)
	except IOError:
		display_error_with_exit("Could not read {}!".format(file_name))

	lines = get_lines_from_file(file_name)
	return validate_lines(lines)

