import numpy as np

# Función de activación sigmoide
def sigmoid(x, derivative=False):
    if derivative:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))

# Definir datos de entrada y salida
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# Definir hiperparámetros
num_epocas = 60000
learning_rate = 0.1
num_entradas = X.shape[1]
num_ocultas = 4
num_salidas = 1

# Inicializar pesos aleatorios
np.random.seed(1)
w1 = 2 * np.random.random((num_entradas, num_ocultas)) - 1
w2 = 2 * np.random.random((num_ocultas, num_salidas)) - 1

# Entrenamiento de la red neuronal
for i in range(num_epocas):
    # Forward propagation
    capa_oculta = sigmoid(np.dot(X, w1))
    y_pred = sigmoid(np.dot(capa_oculta, w2))
    
    # Cálculo del error
    error = y - y_pred
    
    # Backpropagation
    delta_y = error * sigmoid(y_pred, derivative=True)
    delta_oculta = delta_y.dot(w2.T) * sigmoid(capa_oculta, derivative=True)
    
    # Actualización de pesos
    w2 += capa_oculta.T.dot(delta_y) * learning_rate
    w1 += X.T.dot(delta_oculta) * learning_rate

print("Salida de la red neuronal después del entrenamiento:")
print(y_pred)
