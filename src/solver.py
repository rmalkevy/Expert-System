from .helpers.notifications import display_result


def find_answers_for_all_main_questions(equations_dict, facts_base, queries):

	for query_token in queries:
		if query_token in facts_base:
			display_result(query_token, facts_base[query_token].status)
		elif query_token in equations_dict:
			result = False

			for equation in equations_dict[query_token]:
				is_solved = equation.solve(facts_base, equations_dict)

				if is_solved:
					result = is_solved
					break

			display_result(query_token, result)
		else:
			display_result(query_token, False)

