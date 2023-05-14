from typing import List, Dict

def forward_checking(csp: Dict[str, List[str]]) -> Dict[str, str]:
    def reduce_domains(var: str, value: str, domains: Dict[str, List[str]]) -> Dict[str, List[str]]:
        domains = domains.copy()
        domains[var] = [value]
        affected_vars = csp_with_constraints[var]
        for neighbor in affected_vars:
            if neighbor not in domains:
                continue
            for neighbor_value in domains[neighbor]:
                if (var, value, neighbor, neighbor_value) not in constraints:
                    domains[neighbor].remove(neighbor_value)
                    if len(domains[neighbor]) == 0:
                        return None
        return domains

    def backtrack(assignment: Dict[str, str], domains: Dict[str, List[str]]) -> Dict[str, str]:
        if len(assignment) == len(csp):
            return assignment

        var = select_unassigned_variable(domains)
        for value in domains[var]:
            new_domains = reduce_domains(var, value, domains)
            if new_domains is not None:
                assignment[var] = value
                result = backtrack(assignment, new_domains)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(domains: Dict[str, List[str]]) -> str:
        return min(domains, key=lambda var: len(domains[var]))


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

    # Creamos un diccionario con los dominios de todas las variables
    domains = {}
    for var in csp:
        domains[var] = csp[var][:]

    # Buscamos la solución
    return backtrack({}, domains)

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

solution = forward_checking(csp)
print(solution)
