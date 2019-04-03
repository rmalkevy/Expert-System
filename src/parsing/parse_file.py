from .clean_lines import get_lines_from_file
from .validation import validate_lines


def parse_and_validate_file(file_name):
	lines = get_lines_from_file(file_name)
	validate_lines(lines)
	return [line.replace(' ', '') for line in lines]

