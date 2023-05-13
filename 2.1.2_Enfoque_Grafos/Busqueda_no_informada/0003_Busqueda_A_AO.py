from queue import PriorityQueue

def a_star_search(graph, start_node, goal_node, heuristic, cost):
    # Inicializa la cola de prioridad con el nodo de inicio y su valor heurístico
    queue = PriorityQueue()
    queue.put((heuristic(start_node), start_node, 0))

    # Inicializa el conjunto de nodos visitados
    visited = set()

    # Inicializa el diccionario de nodos padres y los costos del camino
    parents = {start_node: None}
    g = {start_node: 0}

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
        for neighbor, cost_to_neighbor in graph[current_node].items():
            if neighbor not in visited:
                # Calcula el costo del camino desde el inicio hasta el vecino a través del nodo actual
                tentative_g = g[current_node] + cost_to_neighbor
                if neighbor not in g or tentative_g < g[neighbor]:
                    # Actualiza el costo del camino y el nodo padre del vecino
                    g[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor)
                    queue.put((f, neighbor, tentative_g))
                    parents[neighbor] = current_node

    # Si no se encuentra un camino, devuelve None
    return None
