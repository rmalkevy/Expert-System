
def parse_file(file_name):
	lines = get_lines_from_file(file_name)
	print(lines)


"""
Methods for get clean lines from file

"""


def get_lines_from_file(file_name):
	lines = [clean_comment_and_white_spaces(line) for line in open(file_name)]
	return delete_empty_lines(lines)


def clean_comment_and_white_spaces(line):
	return line.partition('#')[0].strip()


def delete_empty_lines(lines):
	return list(filter(None, lines))
