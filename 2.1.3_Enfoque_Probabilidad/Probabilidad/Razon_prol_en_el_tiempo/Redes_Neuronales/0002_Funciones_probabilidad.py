import numpy as np

# Función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función tangente hiperbólica
def tanh(x):
    return np.tanh(x)

# Función ReLU (Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

# Función softmax
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

# Ejemplo de uso
x = np.array([0.5, -0.5, 1.0, -1.0])
print("Sigmoid:", sigmoid(x))
print("Tanh:", tanh(x))
print("ReLU:", relu(x))
print("Softmax:", softmax(x))
