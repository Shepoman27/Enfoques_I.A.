import networkx as nx
import numpy as np

# Crear el grafo
G = nx.DiGraph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edge('A', 'B', weight=0.2)
G.add_edge('A', 'C', weight=0.8)
G.add_edge('B', 'D', weight=0.5)
G.add_edge('C', 'D', weight=0.6)

# Definir las recompensas
rewards = {'B': 5, 'C': -2, 'D': 10}

# Definir el descuento
discount = 0.9

# Obtener la matriz de transición y las recompensas como arreglos NumPy
P = nx.to_numpy_matrix(G, nodelist=G.nodes)
R = np.array([rewards.get(node, 0) for node in G.nodes])

# Calcular el valor óptimo de cada estado utilizando programación lineal
values = np.linalg.solve(np.eye(len(G.nodes)) - discount * P, R)

# Calcular la política óptima
policy = {}
for i, node in enumerate(G.nodes):
    if node in rewards:
        # Si es un estado terminal, la política es vacía
        policy[node] = {}
    else:
        # Seleccionar la acción que maximiza el valor esperado
        max_action = None
        max_value = float('-inf')
        for j, successor in enumerate(G.successors(node)):
            action_value = R[j] + discount * values[j]
            if action_value > max_value:
                max_value = action_value
                max_action = successor
        # Asignar probabilidad 1 a la mejor acción
        policy[node] = {max_action: 1}

# Imprimir los resultados
print("Valores:")
print(values)
print("Política:")
print(policy)

