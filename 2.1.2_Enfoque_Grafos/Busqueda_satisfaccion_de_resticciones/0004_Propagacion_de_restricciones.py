from typing import List, Dict, Tuple

def ac3(csp: Dict[str, List[str]], constraints: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    queue = list(constraints)
    while queue:
        (xi, xj) = queue.pop(0)
        if revise(csp, xi, xj):
            if not csp[xi]:
                return None
            for xk in csp_with_constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return csp

def revise(csp: Dict[str, List[str]], xi: str, xj: str) -> bool:
    revised = False
    for x in csp[xi]:
        if not any([constraint_satisfied(x, y) for y in csp[xj]]):
            csp[xi].remove(x)
            revised = True
    return revised

def constraint_satisfied(x: str, y: str) -> bool:
    # Implementa aquí tus restricciones
    return x != y

# Ejemplo de uso
csp = {
    'A': ['1', '2', '3'],
    'B': ['1', '2', '3'],
    'C': ['1', '2', '3']
}

constraints = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C')
]

ac3(csp, constraints)
print(csp)