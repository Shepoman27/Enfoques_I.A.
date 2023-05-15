from collections import deque

# Definición del problema
# Estructura: (nombre_estado, (precondiciones), (efectos))
problema = [
    ("at(b, c)", (), ("holding(b)", "clear(c)")),
    ("at(c, a)", (), ("holding(c)", "clear(a)")),
    ("on(b, a)", ("clear(a)", "holding(b)"), ("clear(b)",)),
    ("on(c, b)", ("clear(b)", "holding(c)"), ("clear(c)",)),
    ("on(a, table)", ("clear(a)"), ("clear(table)", "holding(a)")),
    ("clear(c)", ("on(c, b)"), ("on(c, table)", "clear(b)")),
    ("clear(b)", ("on(b, a)"), ("on(b, table)", "clear(a)")),
    ("clear(a)", ("on(a, table)"), ("on(a, b)", "clear(table)")),
    ("holding(b)", ("on(b, x)"), ("clear(x)", "hand-empty")),
    ("holding(c)", ("on(c, x)"), ("clear(x)", "hand-empty")),
    ("hand-empty", (), ("holding(a)",))
]

# Estado objetivo
estado_objetivo = set(["on(a, b)", "on(b, c)", "on(c, table)", "clear(a)"])

# Función de expansión
def expandir(estado):
    sucesores = []
    for e in problema:
        if all(p in estado for p in e[1]):
            nuevo_estado = estado.difference(e[1]).union(e[2])
            sucesores.append((e[0], nuevo_estado))
    return sucesores

# Algoritmo STRIPS
def strips(start, goal):
    # Inicialización
    visitados = set()
    cola = deque([(None, start)])
    plan = []
    
    # Búsqueda en anchura
    while cola:
        padre, estado = cola.popleft()
        if estado == goal:
            # Objetivo alcanzado
            plan.append((padre, estado))
            while padre:
                padre, estado = [n for n in plan if n[0] == padre][0]
                plan.append((padre, estado))
            return list(reversed(plan))
        visitados.add(estado)
        for accion, sucesor in expandir(estado):
            if sucesor not in visitados:
                cola.append((accion, sucesor))
                plan.append((accion, sucesor))
    return None

# Ejemplo de uso
estado_inicial = set(["at(b, c)", "at(c, a)", "on(b, a)", "on(c, b)", "on(a, table)", "clear(c)", "clear(b)", "clear(table)", "holding(a)", "hand-empty"])
plan = strips(estado_inicial, estado_objetivo)
if plan is None:
    print("No se encontró solución")
else:
    print("Plan:")
    for accion, estado in plan:
        if accion is not None:
            print(accion)
    print("Objetivo alcanzado")
