import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Definimos los datos de ejemplo
x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float)

# Definimos la arquitectura de la red neuronal
class RedNeuronal(nn.Module):
    def __init__(self):
        super(RedNeuronal, self).__init__()
        self.capa_oculta = nn.Linear(2, 3)
        self.capa_salida = nn.Linear(3, 1)
        
    def forward(self, x):
        h = torch.sigmoid(self.capa_oculta(x))
        y_pred = torch.sigmoid(self.capa_salida(h))
        return y_pred

# Definimos el modelo
modelo = RedNeuronal()

# Definimos la función de pérdida y el optimizador
funcion_perdida = nn.BCELoss()
optimizador = optim.SGD(modelo.parameters(), lr=0.1)

# Entrenamos la red neuronal
for epoch in range(1000):
    y_pred = modelo(x)
    perdida = funcion_perdida(y_pred, y)
    
    optimizador.zero_grad()
    perdida.backward()
    optimizador.step()

# Probamos la red neuronal
with torch.no_grad():
    y_pred = modelo(x)
    y_pred_bin = np.round(y_pred.numpy())
    print("Predicciones: ", y_pred_bin)
