import pymc3 as pm
import numpy as np

# Definir la red bayesiana
with pm.Model() as model:
    a = pm.Bernoulli('a', 0.5)
    b = pm.Bernoulli('b', 0.3)
    c = pm.Bernoulli('c', pm.math.switch(a, 0.9, pm.math.switch(b, 0.6, 0.2)))

# Eliminar la variable c
with model:
    marginals = pm.sample_prior_predictive(1000, vars=[a, b])
    a_marginal = np.mean(marginals['a'])
    b_marginal = np.mean(marginals['b'])
    
# Imprimir los resultados
print("P(a) =", a_marginal)
print("P(b) =", b_marginal)
