import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

# Generamos los datos de ejemplo
np.random.seed(42)
datos = np.random.binomial(n=1, p=0.6, size=100)

# Definimos el modelo de Aprendizaje Bayesiano
with pm.Model() as modelo:
    p = pm.Beta('p', alpha=1, beta=1) # Definimos la distribución a priori
    y = pm.Bernoulli('y', p=p, observed=datos) # Definimos la distribución a posteriori

    traza = pm.sample(5000, tune=1000) # Ejecutamos el muestreador de Gibbs

# Visualizamos los resultados
pm.plot_posterior(traza, var_names='p', credible_interval=0.95)
plt.show()
