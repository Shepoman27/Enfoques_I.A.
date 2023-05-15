import pyke

# Definir la base de conocimiento del agente
engine = pyke.KnowledgeEngine()
engine.prove_1_goal('load.knowledge_base()')

# Definir la función de inferencia lógica
@engine.provable
def inferencia_lógica(fact):
    engine.activate('forward_chain') # Encadenamiento hacia adelante
    engine.activate('backward_chain') # Encadenamiento hacia atrás
    return engine.prove_1_goal(fact)

# Definir la función de búsqueda
def buscar_solución(problema):
    solución = None
    engine.reset() # Resetear la base de conocimiento
    engine.prove_1_goal('assert({})'.format(problema)) # Añadir el problema a la base de conocimiento
    for solution in engine.prove_all_goals('solve()'):
        solución = solution
        break
    return solución

# Definir la función de ejecución
def ejecutar_acción(acción):
    print('Ejecutando acción:', acción)

# Ejemplo de uso
if __name__ == '__main__':
    # Definir la base de conocimiento
    engine.defrule('rule1',
        (('animal', '?x'),
         ('come', '?x', 'carne')),
        ('carnivoro', '?x'))
    engine.defrule('rule2',
        (('animal', '?x'),
         ('come', '?x', 'hierba')),
        ('herbivoro', '?x'))

    # Inferir nuevos hechos
    inferencia_lógica('carnivoro(gato)') # True
    inferencia_lógica('herbivoro(cabra)') # True
    inferencia_lógica('carnivoro(cabra)') # False

    # Buscar solución a un problema
    problema = ('animal', 'gato')
    solución = buscar_solución(problema)
    if solución:
        ejecutar_acción(solución['accion'])
    else:
        print('No se encontró solución')
