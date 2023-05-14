import numpy as np

# Definir la matriz de transición
P = np.array([[0.8, 0.2], [0.4, 0.6]])

# Definir los estados
estados = ["soleado", "lluvioso"]

# Definir el estado inicial
estado_actual = np.random.choice(estados)

# Simular el proceso de Markov
for i in range(10):
    print("Estado actual:", estado_actual)
    # Calcular la probabilidad de transición
    p_transicion = P[estados.index(estado_actual), :]
    # Generar el siguiente estado
    estado_siguiente = np.random.choice(estados, p=p_transicion)
    # Actualizar el estado actual
    estado_actual = estado_siguiente
