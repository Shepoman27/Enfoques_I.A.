from constraint import Problem

def backtrack_with_conflict_set(csp):
    problem = Problem()
    for var in csp:
        problem.addVariable(var, csp[var])
    for constraint in constraints:
        problem.addConstraint(constraint)

    def conflict_set(variable):
        conflict_set = []
        for value in csp[variable]:
            if problem.getSolution({variable: value}) is None:
                conflict_set.append(value)
        return conflict_set

    def select_variable(variables):
        return max(variables, key=lambda var: len(conflict_set(var)))

    def ordered_values(variable):
        return sorted(csp[variable], key=lambda value: len(conflict_set(variable)))

    return problem.getSolutions()

# Ejemplo de uso
csp = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3],
    'D': [1, 2, 3]
}

constraints = [('A', '!=', 'B'), ('A', '!=', 'C'), ('B', '!=', 'C'), ('C', '!=', 'D')]

solutions = backtrack_with_conflict_set(csp)
print(solutions)
