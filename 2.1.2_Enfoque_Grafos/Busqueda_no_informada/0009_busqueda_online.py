import random

# Definir el grafo como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# Definir las celdas que contienen objetos
object_cells = {
    'D': 'key',
    'G': 'treasure'
}

# Función de búsqueda en profundidad
def dfs(graph, start, visited, objective):
    visited.append(start)
    if start in object_cells.keys() and object_cells[start] == objective:
        return visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, visited, objective)
            if path is not None:
                return path
    return None

# Función de búsqueda online
def online_search(graph, start, objective):
    visited = []
    current_cell = start
    while True:
        # Verificar si la celda actual contiene el objetivo
        if current_cell in object_cells.keys() and object_cells[current_cell] == objective:
            visited.append(current_cell)
            return visited
        # Si no hay objetos en la celda actual, elegir una celda adyacente al azar
        neighbors = graph[current_cell]
        if len(neighbors) == 0:
            return None
        next_cell = random.choice(neighbors)
        # Realizar una búsqueda en profundidad desde la celda adyacente elegida
        path = dfs(graph, next_cell, visited.copy(), objective)
        if path is not None:
            visited = path
        current_cell = next_cell

# Ejemplo de búsqueda online desde la celda A en busca del objeto 'treasure'
start_cell = 'A'
objective = 'treasure'
path = online_search(graph, start_cell, objective)
print('Camino encontrado:', path)