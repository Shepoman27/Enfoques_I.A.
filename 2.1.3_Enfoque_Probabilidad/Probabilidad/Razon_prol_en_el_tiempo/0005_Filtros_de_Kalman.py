import numpy as np

# Definir las matrices del modelo
A = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[1, 0], [0, 1]])  # Covarianza del ruido del proceso
R = np.array([[1]])  # Covarianza del ruido de la observación

# Definir las matrices de estado inicial y covarianza
x0 = np.array([[0], [0]])  # Vector de estado inicial
P0 = np.array([[1, 0], [0, 1]])  # Covarianza del estado inicial

# Generar la secuencia de observaciones
obs = np.array([[0.5], [2.0], [-0.3], [4.1]])

# Crear las listas para guardar las estimaciones del estado y la covarianza
estados = [x0]
covarianzas = [P0]

# Aplicar el filtro de Kalman
for i in range(len(obs)):
    # Predicción del estado y la covarianza
    x_pred = A @ estados[i]
    P_pred = A @ covarianzas[i] @ A.T + Q

    # Actualización del estado y la covarianza
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_est = x_pred + K @ (obs[i] - H @ x_pred)
    P_est = (np.eye(2) - K @ H) @ P_pred

    estados.append(x_est)
    covarianzas.append(P_est)

# Imprimir las estimaciones del estado y la covarianza
print("Estimaciones del estado:")
print(estados)

print("Estimaciones de la covarianza:")
print(covarianzas)
