import sys
from helpers import *
from parse_file import parse_file

if __name__ == "__main__":

	if len(sys.argv) < 2 or len(sys.argv) > 2:
		display_error_with_exit("You must add only one file to arguments")

	parse_file(sys.argv[1])
