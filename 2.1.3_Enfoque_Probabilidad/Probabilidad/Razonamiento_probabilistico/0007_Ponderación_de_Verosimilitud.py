import numpy as np

# Definir los datos
x = np.array([1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 1])
z = np.array([0, 1, 0, 0, 1])

# Calcular las probabilidades
p_y_given_xz = {}
for i in range(len(x)):
    for j in range(2):
        for k in range(2):
            if z[i] == k:
                y_col = y[x == i]
                p_y_given_xz[(i, j, k)] = np.mean(y_col[y_col == j])
            else:
                p_y_given_xz[(i, j, k)] = 0

# Calcular la ponderación de verosimilitud
p_x_given_z = {}
p_x = {}
for i in range(len(x)):
    p_x[i] = np.mean(y[x == i])
    p_x_given_z[i] = {}
    for j in range(2):
        p_x_given_z[i][j] = sum([p_y_given_xz[(i, j, k)] for k in range(2)])
    p_x_given_z[i] = p_x_given_z[i][1] / (p_x_given_z[i][0] + p_x_given_z[i][1])

# Imprimir los resultados
print("Probabilidades condicionadas:")
print("P(y=1|x=1,z=1) =", p_y_given_xz[(0, 1, 1)])
print("P(y=1|x=2,z=0) =", p_y_given_xz[(1, 1, 0)])
print("P(y=1|x=3,z=1) =", p_y_given_xz[(2, 1, 1)])
print("P(y=1|x=4,z=0) =", p_y_given_xz[(3, 1, 0)])
print("P(y=1|x=5,z=1) =", p_y_given_xz[(4, 1, 1)])
print("\nPonderación de verosimilitud:")
print("P(x=1|z=1) =", p_x_given_z[0])
print("P(x=2|z=1) =", p_x_given_z[1])
print("P(x=3|z=1) =", p_x_given_z[2])
print("P(x=4|z=1) =", p_x_given_z[3])
print("P(x=5|z=1) =", p_x_given_z[4])
