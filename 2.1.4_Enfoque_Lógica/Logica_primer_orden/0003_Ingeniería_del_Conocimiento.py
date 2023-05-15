import pyke

# Creamos la base de conocimiento
engine = pyke.KnowledgeEngine('mi_conocimiento')

# Definimos las reglas de inferencia
@engine.rule
def regla1():
    # Si se cumple esta condición...
    pyke.ask('enfermedad', 'tiene_fiebre = True')
    # ...entonces inferimos que...
    pyke.declare('enfermedad', 'gripe')

@engine.rule
def regla2():
    # Si se cumple esta condición...
    pyke.ask('enfermedad', 'tiene_tos = True')
    # ...entonces inferimos que...
    pyke.declare('enfermedad', 'bronquitis')

# Ejecutamos la inferencia
engine.prove_1_goal('enfermedad($enfermedad)', 'enfermo($enfermo)')
print(engine.get_value('enfermedad'))
