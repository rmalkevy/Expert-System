from .helpers.notifications import display_result


def find_answers_for_all_main_questions(equations_dict, facts_base, queries):

	for query_token in queries:
		if query_token in facts_base and facts_base[query_token].status:
			display_result(query_token, True)
		elif query_token in equations_dict:
			result = False

			for equation in equations_dict[query_token]:
				is_solved = equation.solve(facts_base, equations_dict)

				if is_solved:
					result = is_solved
					break

			answer = not result if facts_base[query_token].is_negative else result
			display_result(query_token, answer)
		else:
			answer = True if facts_base[query_token].is_negative else False
			display_result(query_token, answer)

