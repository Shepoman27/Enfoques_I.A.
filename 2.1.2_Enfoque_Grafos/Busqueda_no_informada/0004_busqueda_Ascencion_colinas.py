# Definir el grafo
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 4},
    'C': {'A': 2, 'D': 7},
    'D': {'B': 4, 'C': 7, 'E': 3},
    'E': {'D': 3, 'F': 2},
    'F': {'E': 2, 'G': 1},
    'G': {'F': 1}
}

# Definir la función heurística
def heuristic(node):
    # Se define una función heurística simple que devuelve la distancia al nodo G
    distances = {'A': 11, 'B': 8, 'C': 9, 'D': 6, 'E': 4, 'F': 2, 'G': 0}
    return distances[node]

def hill_climbing_search(graph, start_node, heuristic):
    current_node = start_node
    while True:
        neighbors = graph[current_node]
        best_neighbor = max(neighbors, key=lambda n: heuristic(n))
        if heuristic(best_neighbor) <= heuristic(current_node):
            # Se ha alcanzado un máximo local, se devuelve el nodo actual
            return current_node
        current_node = best_neighbor

# Definir el nodo de inicio y el nodo objetivo
start_node = 'A'
goal_node = 'G'

# Ejecutar la Búsqueda de Ascenso de Colinas
result_node = hill_climbing_search(graph, start_node, heuristic)

# Imprimir el resultado
print(f'El nodo objetivo encontrado es: {result_node}')