
import numpy as np
from hmmlearn import hmm

# Definir el modelo oculto de Markov
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Definir los parámetros del modelo
model.startprob_ = np.array([0.6, 0.4]) # Probabilidad inicial
model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]]) # Matriz de transición
model.means_ = np.array([[0.0], [3.0]]) # Media
model.covars_ = np.array([[1.0], [1.5]]) # Varianza

# Definir la secuencia de observaciones
obs = np.array([[0.5], [2.0], [-0.3], [4.1]])

# Calcular las probabilidades hacia adelante
logprob, fwdlattice = model.score_samples(obs)
fwdlattice = np.exp(fwdlattice)

# Calcular las probabilidades hacia atrás
bwdlattice = model.decode(obs)[0]

# Calcular la distribución posterior
posterior = fwdlattice * bwdlattice / np.sum(fwdlattice * bwdlattice, axis=1, keepdims=True)

# Imprimir la distribución posterior
print("La distribución posterior es:")
print(posterior)
