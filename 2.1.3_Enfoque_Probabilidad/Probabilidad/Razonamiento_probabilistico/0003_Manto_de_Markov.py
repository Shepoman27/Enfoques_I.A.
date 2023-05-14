import markovify

# Leer los datos de entrada
with open("datos.txt") as f:
    text = f.read()

# Crear un modelo de Markov de orden 1
model = markovify.Text(text, state_size=1)

# Generar una oración aleatoria basada en el modelo
print(model.make_sentence())
