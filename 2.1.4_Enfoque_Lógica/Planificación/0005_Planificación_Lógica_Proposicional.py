from pysat.solvers import Glucose3
from pysat.formula import CNF

# Definimos la planificación en lógica proposicional
# P = Preparar comida, C = Cocinar, L = Lavar platos
# Los números indican los pasos
planning = ['P1', '-C1', '-L1', 'P2', 'C2', '-L2', 'P3', '-C3']

# Convertimos la planificación a su forma clausal CNF
cnf = CNF()
for clause in planning:
    cnf.append(list(map(int, clause.replace('-', '-').replace('P', '1').replace('C', '2').replace('L', '3'))))

# Creamos un objeto de la clase Glucose3
solver = Glucose3()

# Agregamos la CNF al solver
for clause in cnf.clauses:
    solver.add_clause(clause)

# Ejecutamos el SAT solver
if solver.solve():
    # Si hay solución, obtenemos los valores de verdad de las variables
    solution = [solver.model[i] > 0 for i in range(1, len(cnf.varmap) + 1)]
    # Imprimimos la solución
    print('La planificación encontrada es:')
    for i, var in enumerate(cnf.varmap):
        if var.startswith('-'):
            continue
        if solution[i]:
            print(var)
else:
    print('No se encontró solución para la planificación.')
