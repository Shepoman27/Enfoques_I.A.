# Definición de constantes
X = ['x1', 'x2', 'x3']
Y = ['y1', 'y2', 'y3']

# Definición de predicados
P = lambda x: x in ['x1', 'x2']
Q = lambda x, y: x == 'x1' and y == 'y1'

# Ejemplo de uso de cuantificadores
# Para todo x en X, si P(x) entonces existe y en Y tal que Q(x, y)
if all(P(x) for x in X):
    exists = False
    for y in Y:
        if Q(x, y):
            exists = True
            break
    if not exists:
        print('La condición no se cumple')
