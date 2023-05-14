import numpy as np
from hmmlearn import hmm

# Definimos el modelo de Markov Oculto
modelo = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Definimos los datos de ejemplo
observaciones = np.array([[0.5, -1.0], [0.0, 1.0], [1.5, 0.5]])

# Ajustamos el modelo a los datos de ejemplo
modelo.fit(observaciones)

# Predecimos la secuencia de estados ocultos
estados, _ = modelo.decode(observaciones)

# Imprimimos los resultados
print("Secuencia de estados ocultos:", estados)
