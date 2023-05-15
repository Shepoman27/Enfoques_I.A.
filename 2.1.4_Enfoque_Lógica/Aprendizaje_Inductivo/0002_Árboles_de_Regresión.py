from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
import numpy as np

boston = load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio: {:.2f}".format(mse))



# Cargamos el conjunto de datos de Boston Housing
boston = load_boston()
X = boston.data
y = boston.target

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un objeto de árbol de regresión y lo ajustamos al conjunto de entrenamiento
tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)

# Realizamos predicciones en el conjunto de prueba y calculamos el error cuadrático medio
y_pred = tree.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("Error cuadrático medio: {:.2f}".format(mse))
