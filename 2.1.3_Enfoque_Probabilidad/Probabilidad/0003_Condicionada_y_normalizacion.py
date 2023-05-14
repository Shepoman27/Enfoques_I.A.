import numpy as np

# Definir los datos de entrenamiento
x_train = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 1, 1], [0, 0, 0]])
y_train = np.array([1, 0, 1, 0, 1, 0, 1, 0])

# Calcular las probabilidades condicionadas
p_y_given_x = {}
p_x_given_y = {}
for i in range(len(x_train[0])):
    x_col = x_train[:, i]
    for j in range(2):
        y_col = y_train[x_train[:, i] == j]
        p_y_given_x[(i, j)] = np.mean(y_col)
        p_x_given_y[(i, j)] = np.mean(x_col[y_train == j])

# Normalizar las probabilidades
p_x = {}
p_y = {}
for i in range(len(x_train[0])):
    p_x[i] = sum([p_x_given_y[(i, j)] * p_y[j] for j in range(2)])
    for j in range(2):
        p_y[j] = sum([p_y_given_x[(i, j)] * p_x_given_y[(i, j)] * p_y[j] for i in range(len(x_train[0]))])

# Imprimir los resultados
print("Probabilidades condicionadas:")
print("P(y=1|x) =", p_y_given_x[(0, 1)], ", P(y=0|x) =", p_y_given_x[(0, 0)])
print("P(y=1|x) =", p_y_given_x[(1, 1)], ", P(y=0|x) =", p_y_given_x[(1, 0)])
print("P(y=1|x) =", p_y_given_x[(2, 1)], ", P(y=0|x) =", p_y_given_x[(2, 0)])
print("P(x=1|y) =", p_x_given_y[(0, 1)], ", P(x=0|y) =", p_x_given_y[(0, 0)])
print("P(x=1|y) =", p_x_given_y[(1, 1)], ", P(x=0|y) =", p_x_given_y[(1, 0)])
print("P(x=1|y) =", p_x_given_y[(2, 1)], ", P(x=0|y) =", p_x_given_y[(2, 0)])
print("\nProbabilidades normalizadas:")
print("P(x=1) =", p_x[0], ", P(x=0) =", 1 - p_x[0])
print("P(y=1) =", p_y[1], ", P(y=0) =", 1 - p_y[1])
