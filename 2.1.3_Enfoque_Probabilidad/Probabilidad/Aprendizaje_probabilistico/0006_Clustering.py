import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generamos los datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# Creamos el modelo de clustering utilizando Gaussian Mixture Models (GMM)
modelo = GaussianMixture(n_components=4, random_state=42)
modelo.fit(X)

# Obtenemos las etiquetas de los clusters
etiquetas = modelo.predict(X)

# Visualizamos los resultados
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=40, cmap='viridis')
plt.show()
