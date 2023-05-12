def iterative_deepening_search(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):   # para cada profundidad desde 0 hasta la profundidad máxima
        visited = set()   # conjunto para llevar un registro de los nodos visitados
        stack = [(start, [start])]   # pila de nodos a visitar, junto con el camino recorrido hasta ese punto
        while stack:   # mientras la pila no esté vacía
            node, path = stack.pop()   # extrae el último nodo y su camino desde la pila
            if node == goal:   # si se llega al nodo objetivo, termina la búsqueda y devuelve el camino
                return path
            if node in visited or len(path) > depth + 1:   # si el nodo ya ha sido visitado o el camino es demasiado largo para la profundidad actual, se salta al siguiente nodo
                continue
            visited.add(node)   # marca el nodo como visitado
            for neighbor in graph[node]:   # para cada vecino del nodo actual
                stack.append((neighbor, path + [neighbor]))   # añade el vecino a la pila para visitarlo después, junto con el camino recorrido hasta ese punto

    return None   # si no se encuentra un camino al nodo objetivo, retorna None

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

# Llamada a la función iterative_deepening_search con el nodo 'A' como punto de partida, 'I' como objetivo y límite de profundidad de 3
path = iterative_deepening_search(graph, 'A', 'I', 3)
print(path)
