import random

def satisfaccion_restricciones(formula_proposicional, max_iteraciones):
    # Se inicializan las variables aleatoriamente
    variables = {}
    for literal in formula_proposicional.variables:
        variables[literal] = random.choice([True, False])

    # Se define la función de evaluación
    def evaluacion(asignacion):
        return formula_proposicional.evaluar(asignacion)

    # Se inicia la búsqueda local iterativa
    iteracion = 0
    while iteracion < max_iteraciones:
        # Se selecciona la variable más prometedora para cambiar su valor
        mejor_variable = None
        mejor_evaluacion = evaluacion(variables)
        for literal in formula_proposicional.variables:
            if literal not in variables:
                for valor in [True, False]:
                    nueva_asignacion = variables.copy()
                    nueva_asignacion[literal] = valor
                    nueva_evaluacion = evaluacion(nueva_asignacion)
                    if nueva_evaluacion > mejor_evaluacion:
                        mejor_variable = literal
                        mejor_evaluacion = nueva_evaluacion

        # Si no se encuentra una variable prometedora, se termina la búsqueda
        if mejor_variable is None:
            break

        # Se cambia el valor de la variable más prometedora
        variables[mejor_variable] = not variables[mejor_variable]

        # Se incrementa el número de iteraciones
        iteracion += 1

    # Se retorna la asignación encontrada
    return variables
