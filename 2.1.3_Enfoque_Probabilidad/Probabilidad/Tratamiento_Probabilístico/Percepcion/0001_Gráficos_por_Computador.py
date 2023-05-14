import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear gráfico
fig, ax = plt.subplots()
ax.plot(x, y)

# Personalizar gráfico
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de ejemplo')

# Mostrar gráfico
plt.show()
