from typing import List, Dict

def backtracking_search(csp: Dict[str, List[str]]) -> Dict[str, str]:
    def backtrack(assignment: Dict[str, str]) -> Dict[str, str]:
        if len(assignment) == len(csp):
            return assignment

        var = select_unassigned_variable(assignment)
        for value in order_domain_values(var, assignment):
            if is_consistent(var, value, assignment):
                assignment[var] = value
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(assignment: Dict[str, str]) -> str:
        for var in csp:
            if var not in assignment:
                return var

    def order_domain_values(var: str, assignment: Dict[str, str]) -> List[str]:
        values = csp[var]
        return sorted(values, key=lambda value: num_conflicts(var, value, assignment))

    def num_conflicts(var: str, value: str, assignment: Dict[str, str]) -> int:
        conflicts = 0
        for neighbor in csp_with_constraints[var]:
            if neighbor not in assignment:
                for neighbor_value in csp[neighbor]:
                    if value == neighbor_value:
                        conflicts += 1
        return conflicts

    def is_consistent(var: str, value: str, assignment: Dict[str, str]) -> bool:
        for neighbor in csp_with_constraints[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    # Convertimos el CSP a un grafo de restricciones, en el que cada variable
    # es un nodo y cada restricción es una arista que conecta los nodos afectados
    # por la restricción
    csp_with_constraints = {}
    for var in csp:
        csp_with_constraints[var] = []
    for var1 in csp:
        for var2 in csp:
            if var1 != var2:
                for value1 in csp[var1]:
                    for value2 in csp[var2]:
                        if (var1, value1, var2, value2) in constraints:
                            csp_with_constraints[var1].append(var2)
                            csp_with_constraints[var2].append(var1)

    # Buscamos la solución
    return backtrack({})

# Ejemplo de uso
csp = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3],
    'D': [1, 2, 3]
}

constraints = {
    ('A', 1, 'B', 1),
    ('A', 1, 'C', 1),
    ('B', 1, 'C', 1),
    ('C', 1, 'D', 1)
}

solution = backtracking_search(csp)
print(solution)
