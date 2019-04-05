
def display_error_with_exit(error):
	display_error(error)
	exit()


def display_error(error):
	print("\033[4m\033[41mERROR: {}\033[0m".format(error))


def display_result(query_token, result):
	print("\033[1m\033[32m{} -> {}\033[0m".format(query_token, result))
