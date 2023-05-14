import numpy as np
import matplotlib.pyplot as plt

# Generar 1000 muestras de una distribución uniforme en [0, 1]
samples = np.random.rand(1000)

# Transformar las muestras a una distribución normal estándar
samples = np.sqrt(-2 * np.log(samples)) * np.cos(2 * np.pi * samples)

# Imprimir los primeros 10 valores generados
print(samples[:10])





# Definir la PDF objetivo (distribución normal estándar)
def target_pdf(x):
    return np.exp(-0.5 * x ** 2) / np.sqrt(2 * np.pi)

# Definir la PDF acotadora (distribución uniforme en [-5, 5])
def bounding_pdf(x):
    return np.where((x > -5) & (x < 5), 0.2, 0)

# Generar 1000 muestras de la PDF acotadora
bounding_samples = np.random.uniform(low=-5, high=5, size=1000)

# Generar muestras de la PDF objetivo utilizando el método de rechazo
target_samples = []
for i in range(1000):
    # Generar una muestra de la PDF acotadora
    x = bounding_samples[i]
    
    # Generar una muestra de la PDF objetivo utilizando la PDF acotadora
    y = np.random.uniform(low=0, high=0.4)
    while y > target_pdf(x) / bounding_pdf(x):
        x = np.random.uniform(low=-5, high=5)
        y = np.random.uniform(low=0, high=0.4)
        
    target_samples.append(x)

# Imprimir los primeros 10 valores generados
print(target_samples[:10])

# Graficar las PDFs objetivo y acotadora y las muestras generadas
x = np.linspace(-5, 5, 1000)
plt.plot(x, target_pdf(x), label='PDF Objetivo')
plt.plot(x, bounding_pdf(x), label='PDF Acotadora')
plt.hist(target_samples, density=True, bins=30, alpha=0.5, label='Muestras')
plt.legend()
plt.show()