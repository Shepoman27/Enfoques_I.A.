from queue import PriorityQueue

def best_first_search(graph, start_node, goal_node, heuristic):
    # Inicializa la cola de prioridad con el nodo de inicio y su valor heurístico
    queue = PriorityQueue()
    queue.put((heuristic(start_node), start_node))

    # Inicializa el conjunto de nodos visitados
    visited = set()

    # Inicializa el diccionario de nodos padres
    parents = {start_node: None}

    # Implementa el algoritmo
    while not queue.empty():
        current_node = queue.get()[1]
        visited.add(current_node)
        if current_node == goal_node:
            # Se ha encontrado el camino, lo devuelve
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]
        for neighbor, cost in graph[current_node].items():
            if neighbor not in visited:
                # Calcula el valor heurístico del vecino y lo agrega a la cola de prioridad
                value = heuristic(neighbor)
                queue.put((value, neighbor))
                parents[neighbor] = current_node

    # Si no se encuentra un camino, devuelve None
    return None

graph = {
    'A': {'B': 5, 'C': 6},
    'B': {'D': 8, 'E': 9},
    'C': {'F': 7},
    'D': {},
    'E': {'G': 10},
    'F': {},
    'G': {}
}

start_node = 'A'
goal_node = 'G'

def heuristic(node):
    # En este ejemplo, el valor del nodo es la heurística
    return node[0]

path = best_first_search(graph, start_node, goal_node, heuristic)
print(path)