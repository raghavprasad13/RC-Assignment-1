from valid_symbols_dictionary import symbols_dict

def check_balanced_parantheses(formula):
	bracket = ['(', ')', '{', '}', '[', ']']
	for x in formula:
		if x not in bracket:
			formula = formula.replace(x, '')


	brackets = ['()', '{}', '[]']

	while any(x in formula for x in brackets):
		for br in brackets:
			formula = formula.replace(br, '')

	return not formula

def check_formula_validity(subformula):
	global formula
	if not check_balanced_parantheses(formula):
		return False

	if subformula.find('(') == -1:
		for x in subformula:
			if x in symbols_dict.keys():
				index_of_operator = subformula.find(x)
				if x is '!':
					# if index_of_operator+1 < len(subformula):
						
					return (index_of_operator+1 < len(subformula))
				else:
					return (((index_of_operator-1) >= 0) and ((index_of_operator+1)<len(formula)))

	while '(' in formula:
		innermost_open_bracket_index = len(formula) - formula[::-1].find('(') - 1 
		# print("innermost_open_bracket_index: ", innermost_open_bracket_index)
		innermost_close_bracket_index = formula.find(')', innermost_open_bracket_index)
		return check_formula_validity(formula[innermost_open_bracket_index+1:innermost_close_bracket_index])


formula = "(r&(p+q))"
print(check_formula_validity(formula))











