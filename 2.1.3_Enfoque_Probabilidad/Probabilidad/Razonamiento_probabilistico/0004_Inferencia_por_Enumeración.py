import numpy as np

# Definir la red bayesiana
variables = ['D', 'S', 'C', 'R']
parents = {'D': [], 'S': ['D'], 'C': ['D'], 'R': ['S', 'C']}
probabilities = {'D': [0.6, 0.4],
                 'S': [[0.3, 0.7], [0.8, 0.2]],
                 'C': [[0.2, 0.8], [0.7, 0.3]],
                 'R': [[0.9, 0.1, 0.3, 0.7], [0.4, 0.6, 0.1, 0.9], [0.2, 0.8, 0.6, 0.4], [0.1, 0.9, 0.5, 0.5]]}

# Definir la evidencia
evidence = {'R': 0}

# Función de inferencia por enumeración
def enumeration_inference(X, e, bn):
    if len(X) == 0:
        return 1
    Y = X[0]
    y_values = bn[Y]
    if Y in e:
        result = y_values[e[Y]] * enumeration_inference(X[1:], e, bn)
    else:
        result = sum([y_values[y] * enumeration_inference(X[1:], {**e, **{Y: y}}, bn) for y in range(len(y_values))])
    return result

# Calcular la probabilidad deseada
probability = enumeration_inference(['D'], evidence, probabilities)

# Imprimir el resultado
print("La probabilidad de D dado R = 0 es:", probability)
