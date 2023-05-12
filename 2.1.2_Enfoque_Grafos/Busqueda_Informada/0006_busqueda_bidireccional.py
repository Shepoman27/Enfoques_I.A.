def bidirectional_search(graph, start, goal):
    # Inicializa las dos búsquedas en profundidad, una desde el nodo inicial y otra desde el nodo objetivo
    start_visited = set()
    start_stack = [(start, [start])]
    goal_visited = set()
    goal_stack = [(goal, [goal])]

    while start_stack and goal_stack:
        # Primero se busca desde el nodo inicial
        node, path = start_stack.pop()
        if node == goal or node in goal_visited:
            # Si se llega al nodo objetivo o si se encuentra en la lista de nodos visitados de la búsqueda desde el objetivo, se ha encontrado el camino
            return path + goal_visited[node][::-1]   # Concatena el camino recorrido desde el nodo inicial con el camino recorrido desde el objetivo en orden inverso

        if node not in start_visited:
            # Marca el nodo como visitado
            start_visited.add(node)
            for neighbor in graph[node]:
                start_stack.append((neighbor, path + [neighbor]))

        # Ahora se busca desde el nodo objetivo
        node, path = goal_stack.pop()
        if node == start or node in start_visited:
            # Si se llega al nodo inicial o si se encuentra en la lista de nodos visitados de la búsqueda desde el inicial, se ha encontrado el camino
            return path + start_visited[node][::-1]   # Concatena el camino recorrido desde el objetivo con el camino recorrido desde el inicial en orden inverso

        if node not in goal_visited:
            # Marca el nodo como visitado
            goal_visited.add(node)
            for neighbor in graph[node]:
                goal_stack.append((neighbor, path + [neighbor]))

    # Si no se encuentra un camino entre el nodo inicial y el objetivo, retorna None
    return None

# Ejemplo de grafo representado como lista de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

# Llamada a la función bidirectional_search con el nodo 'A' como punto de partida y 'I' como objetivo
path = bidirectional_search(graph, 'A', 'I')
print(path)
