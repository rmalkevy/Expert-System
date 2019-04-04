

def find_answers_for_all_main_questions(equations_dict, facts_base, queries):

	for query in queries:
		if query in facts_base and facts_base[query].status != None:
			print("\033[1m\033[32m", query, " - ", facts_base[query].status, "\033[0m")
		elif query in equations_dict:
			res = False

			for eq in equations_dict[query]:
				solve = eq.solve(facts_base, equations_dict)

				if solve:
					res = solve
					break

			print("\033[1m\033[32m", query, ' - ', res, "\033[0m")
		else:
			print("\033[1m\033[32m", query, ' - ', False, "\033[0m")

