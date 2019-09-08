from valid_symbols_dictionary import symbols_dict

formula = "(s.(r>(!(p+q))))"

formula_backup = formula

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

def check_subformula_validity(subformula):
	global formula

	if subformula[1:len(subformula)-1].find('(') == -1:
		subformula_wo_parentheses = subformula[1:len(subformula)-1]
		binary_ops = list(symbols_dict.keys())
		binary_ops.remove('!')

		if any(x in subformula for x in binary_ops):
			if (len(subformula_wo_parentheses) == 3) and (not subformula_wo_parentheses[0] in symbols_dict.keys()) and (not subformula_wo_parentheses[2] in symbols_dict.keys()) and (subformula_wo_parentheses[1] in binary_ops):
				formula = formula.replace(subformula, 'X')
				return True
			return False

		elif '!' in subformula:
			if (len(subformula_wo_parentheses) == 2) and (not subformula_wo_parentheses[1] in symbols_dict.keys()) and (subformula_wo_parentheses[0] == '!'):
				formula = formula.replace(subformula, 'X')
				return True
			return False
		
		# print("Formula so far: ", formula)
		return False


def check_formula_validity():
	global formula

	if formula[0] != '(' or formula[-1] != ')':
		return False

	while '(' in formula:
		innermost_open_bracket_index = len(formula) - formula[::-1].find('(') - 1
		innermost_close_bracket_index = formula.find(')', innermost_open_bracket_index)
		if not check_subformula_validity(formula[innermost_open_bracket_index:innermost_close_bracket_index+1]):
			return False

	return True

print(check_balanced_parantheses(formula) and check_formula_validity())










