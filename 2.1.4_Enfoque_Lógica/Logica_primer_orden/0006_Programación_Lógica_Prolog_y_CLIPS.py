from pyDatalog import pyDatalog

# Definimos las reglas de nuestra base de conocimiento
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

padre('juan', 'pedro')
padre('pedro', 'maria')
padre('pedro', 'jorge')

# Regla para inferir la relación de abuelo
abuelo(X, Z) <= padre(X, Y) & padre(Y, Z)

# Consultas a nuestra base de conocimiento
print(abuelo('juan', Z))  # Salida: [('maria',), ('jorge',)]
print(abuelo('pedro', Z)) # Salida: []
