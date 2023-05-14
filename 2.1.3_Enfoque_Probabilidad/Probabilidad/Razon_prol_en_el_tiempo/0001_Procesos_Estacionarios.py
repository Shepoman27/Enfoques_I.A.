import numpy as np
import matplotlib.pyplot as plt

# Configuración de la simulación
n = 1000    # Número de puntos de datos
mu = 0      # Media
sigma = 1   # Desviación estándar

# Generar proceso estacionario de ruido blanco
x = np.random.normal(mu, sigma, size=n)

# Graficar los datos
plt.plot(x)
plt.title("Proceso estacionario de ruido blanco")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()
