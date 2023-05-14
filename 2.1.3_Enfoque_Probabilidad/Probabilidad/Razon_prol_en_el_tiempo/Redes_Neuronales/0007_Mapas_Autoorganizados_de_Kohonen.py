import numpy as np

# Definir datos de entrada
X = np.array([[0.2, 0.6, 0.5, 0.7], [0.1, 0.3, 0.4, 0.9], [0.4, 0.1, 0.7, 0.2], [0.8, 0.5, 0.9, 0.1]])

# Definir hiperparámetros
num_epocas = 1000
learning_rate_inicial = 0.1
radio_inicial = 1
num_neuronas = 2

# Inicializar pesos aleatorios
np.random.seed(1)
pesos = np.random.rand(num_neuronas, X.shape[1])

# Entrenamiento de los mapas autoorganizados
for epoca in range(num_epocas):
    # Calcular tasa de aprendizaje y radio de vecindad para esta época
    learning_rate = learning_rate_inicial * (1 - epoca/num_epocas)
    radio = radio_inicial * (1 - epoca/num_epocas)
    
    # Seleccionar un patrón aleatorio
    i = np.random.randint(X.shape[0])
    patron = X[i]
    
    # Calcular distancias entre los patrones y los pesos
    distancias = np.linalg.norm(patron - pesos, axis=1)
    
    # Encontrar la neurona ganadora
    neurona_ganadora = np.argmin(distancias)
    
    # Actualizar los pesos de la neurona ganadora y sus vecinas
    for j in range(num_neuronas):
        if np.linalg.norm(j - neurona_ganadora) <= radio:
            pesos[j] += learning_rate * (patron - pesos[j])
            
# Clasificar los patrones según la neurona ganadora más cercana
clases = []
for i in range(X.shape[0]):
    distancias = np.linalg.norm(X[i] - pesos, axis=1)
    clase = np.argmin(distancias)
    clases.append(clase)
    
print(clases)
