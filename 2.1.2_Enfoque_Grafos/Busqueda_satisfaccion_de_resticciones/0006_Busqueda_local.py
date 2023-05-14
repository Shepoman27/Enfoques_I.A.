from typing import List, Dict
import random

def min_conflicts(csp: Dict[str, List[str]], max_steps: int) -> Dict[str, str]:
    # Inicializamos una asignación aleatoria
    current = {var: random.choice(csp[var]) for var in csp}

    for i in range(max_steps):
        # Seleccionamos una variable aleatoria que tenga algún conflicto
        conflicted_vars = [var for var in csp if not is_consistent(var, current[var], current)]
        if not conflicted_vars:
            return current
        var = random.choice(conflicted_vars)

        # Seleccionamos el valor que minimiza el número de conflictos con sus vecinos
        min_conflicts = len(csp)*2
        min_value = None
        for value in csp[var]:
            conflicts = num_conflicts(var, value, current)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_value = value

        current[var] = min_value

    return None

def num_conflicts(var: str, value: str, assignment: Dict[str, str]) -> int:
    conflicts = 0
    for neighbor in csp_with_constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            conflicts += 1
    return conflicts

def is_consistent(var: str, value: str, assignment: Dict[str, str]) -> bool:
    for neighbor in csp_with_constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

# Ejemplo de uso
csp = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul'],
    'E': ['rojo', 'verde', 'azul']
}

constraints = {
    ('A', 'rojo', 'B', 'rojo'),
    ('A', 'rojo', 'C', 'rojo'),
    ('B', 'rojo', 'C', 'rojo'),
    ('C', 'rojo', 'D', 'rojo'),
    ('C', 'rojo', 'E', 'rojo')
}

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

solution = min_conflicts(csp, 100)
print(solution)
