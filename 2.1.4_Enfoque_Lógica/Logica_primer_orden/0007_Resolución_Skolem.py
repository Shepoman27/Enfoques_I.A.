# Función para convertir una fórmula lógica en la forma clausal
def clausal_form(formula):
    clauses = []
    # Convertir a la forma normal conjuntiva
    cnf = to_cnf(formula)
    # Obtener cláusulas individuales
    for clause in cnf:
        # Convertir cláusula en conjunto de literales
        literals = set()
        for literal in clause:
            # Convertir literal a forma clausal
            if literal.negated:
                literals.add("~" + str(literal))
            else:
                literals.add(str(literal))
        # Agregar cláusula a lista de cláusulas
        clauses.append(literals)
    return clauses

# Función para encontrar el conjunto de resolución de dos cláusulas
def resolve(clause1, clause2):
    resolvents = set()
    # Encontrar todos los literales que aparecen en ambas cláusulas
    for literal in clause1:
        if literal.startswith("~"):
            pos_literal = literal[1:]
        else:
            pos_literal = "~" + literal
        if pos_literal in clause2:
            # Crear nuevo conjunto sin los literales resolventes
            resolvent = set(clause1).union(set(clause2))
            resolvent.remove(literal)
            resolvent.remove(pos_literal)
            resolvents.add(frozenset(resolvent))
    return resolvents

# Función para verificar si dos cláusulas son resolventes
def is_resolvent(clause1, clause2):
    resolvents = resolve(clause1, clause2)
    if resolvents:
        return True
    return False

# Función para verificar si una fórmula es satisfacible mediante resolución Skolem
def skolem(clauses):
    # Agregar cláusula vacía para empezar
    clauses.append(set())
    while True:
        # Hacer todas las combinaciones posibles de cláusulas
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i+1, len(clauses))]
        new_clauses = set()
        for (clause1, clause2) in pairs:
            # Verificar si las cláusulas son resolventes
            if is_resolvent(clause1, clause2):
                resolvents = resolve(clause1, clause2)
                # Verificar si se encontró la cláusula vacía
                if set() in resolvents:
                    return True
                # Agregar nuevos resolventes a conjunto de nuevas cláusulas
                for resolvent in resolvents:
                    new_clauses.add(resolvent)
        # Verificar si no se encontraron nuevas cláusulas
        if not new_clauses:
            return False
        # Verificar si el conjunto de nuevas cláusulas es igual al conjunto de cláusulas existentes
        if new_clauses.issubset(set(clauses)):
            return False
        # Agregar nuevas cláusulas al conjunto de cláusulas existentes
        for clause in new_clauses:
            clauses.append(clause)
