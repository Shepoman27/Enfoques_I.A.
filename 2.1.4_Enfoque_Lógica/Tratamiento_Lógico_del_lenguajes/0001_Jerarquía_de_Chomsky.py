import re

# Función para determinar el tipo de gramática según la jerarquía de Chomsky
def chomsky(gramatica):
    # Eliminar espacios y saltos de línea
    gramatica = re.sub(r'\s+', '', gramatica)
    # Determinar el tipo de gramática
    if '->' not in gramatica:
        return 'Gramática no válida'
    lados = gramatica.split('->')
    if len(lados) != 2:
        return 'Gramática no válida'
    if lados[1].islower():
        return 'Tipo 3: Gramática regular'
    if lados[1].isupper():
        if lados[0].isupper():
            return 'Tipo 0: Gramática sensible al contexto'
        else:
            return 'Tipo 1: Gramática sensible al contexto libre'
    if lados[1].find('|') != -1:
        return 'Tipo 2: Gramática independiente del contexto'
    return 'Gramática no válida'

# Ejemplo de uso
gramatica = '''
S -> AB
A -> a | b
B -> Aa | Ba | c
'''
print(chomsky(gramatica))
