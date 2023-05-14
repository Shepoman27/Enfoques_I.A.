from typing import List, Dict

def backtracking_search(csp: Dict[str, List[str]]) -> Dict[str, str]:
    # Función principal que ejecuta el algoritmo de búsqueda de vuelta atrás

    def backtrack(assignment: Dict[str, str]) -> Dict[str, str]:
        # Función recursiva que asigna valores a las variables y verifica la consistencia del CSP

        if len(assignment) == len(csp):  # Si todas las variables tienen un valor asignado, se devuelve la asignación
            return assignment

        var = select_unassigned_variable(assignment)  # Selecciona la variable sin asignar con el grado heurístico más alto
        for value in order_domain_values(var, assignment):  # Itera sobre los valores del dominio de la variable seleccionada, ordenados por conflicto
            if is_consistent(var, value, assignment):  # Verifica la consistencia del CSP
                assignment[var] = value  # Asigna el valor a la variable seleccionada
                result = backtrack(assignment)  # Recursivamente, intenta asignar valores a las variables restantes
                if result is not None:  # Si se encuentra una solución, se devuelve la asignación
                    return result
                del assignment[var]  # Si no se encontró solución, se deshace la asignación
        return None  # Si no se encontró solución para ninguna de las variables, se devuelve None

    def select_unassigned_variable(assignment: Dict[str, str]) -> str:
        # Selecciona la variable sin asignar con el grado heurístico más alto

        for var in csp:
            if var not in assignment:
                return var

    def order_domain_values(var: str, assignment: Dict[str, str]) -> List[str]:
        # Retorna los valores del dominio de la variable seleccionada, ordenados por conflicto

        values = csp[var]
        return sorted(values, key=lambda value: num_conflicts(var, value, assignment))

    def num_conflicts(var: str, value: str, assignment: Dict[str, str]) -> int:
        # Retorna el número de conflictos para la asignación de la variable seleccionada

        conflicts = 0
        for neighbor in csp_with_constraints[var]:  # Itera sobre las variables conectadas por restricciones con la variable seleccionada
            if neighbor not in assignment:  # Si la variable vecina no ha sido asignada aún
                for neighbor_value in csp[neighbor]:  # Itera sobre los valores del dominio de la variable vecina
                    if value == neighbor_value:  # Si el valor asignado a la variable seleccionada es igual a alguno de los valores del dominio de la variable vecina
                        conflicts += 1  # Se incrementa el contador de conflictos
        return conflicts

    def is_consistent(var: str, value: str, assignment: Dict[str, str]) -> bool:
        # Verifica la consistencia del CSP

        for neighbor in csp_with_constraints[var]:  # Itera sobre las variables conectadas por restricciones con la variable seleccionada
            if neighbor in assignment and assignment[neighbor] == value:  # Si la variable vecina ya tiene un valor asignado que es igual al valor seleccionado
                return False  # Se retorna False, indicando que la asignación es inconsistente
        return True  # Si no se encontró ninguna inconsistencia, se retorna True

    # Convertimos el

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
