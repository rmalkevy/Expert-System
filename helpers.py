
def display_error_with_exit(error):
	display_error(error)
	exit()


def display_error(error):
	print("\033[1m\033[41mERROR: ", error, '\033[0m')
