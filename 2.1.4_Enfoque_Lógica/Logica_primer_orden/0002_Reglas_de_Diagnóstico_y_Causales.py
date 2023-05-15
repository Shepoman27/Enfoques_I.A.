from pyke import knowledge_engine

# Crear un motor de conocimiento
engine = knowledge_engine.engine(__file__)

# Definir reglas
engine.add_rules("""
    rule symptom_check:
        (diagnosis ?x)
        <=
        (symptom fever)
        (symptom headache)
        =>
        (diagnosis "Malaria")

    rule symptom_check:
        (diagnosis ?x)
        <=
        (symptom cough)
        (symptom fever)
        =>
        (diagnosis "Tuberculosis")

    rule symptom_check:
        (diagnosis ?x)
        <=
        (symptom fatigue)
        (symptom headache)
        =>
        (diagnosis "Typhoid Fever")
""")

# Cargar hechos
engine.assert_('symptom', 'fever')
engine.assert_('symptom', 'headache')

# Ejecutar el motor de conocimiento
engine.activate('symptom_check')

# Obtener resultado
for diagnosis, in engine.ask('diagnosis ?x'):
    print(diagnosis)
