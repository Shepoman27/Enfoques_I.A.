import numpy as np

# Definir los valores posibles de la variable aleatoria
valores = np.array([0, 1, 2, 3, 4])

# Definir las probabilidades de cada valor
probabilidades = np.array([0.2, 0.3, 0.1, 0.2, 0.2])

# Calcular la media y la varianza de la distribución
media = np.sum(valores * probabilidades)
varianza = np.sum(probabilidades * (valores - media)**2)

# Imprimir los resultados
print("Valores:", valores)
print("Probabilidades:", probabilidades)
print("Media:", media)
print("Varianza:", varianza)
