def depth_limited_search(graph, start, goal, limit):
    stack = [(start, [start], 0)]  # pila de nodos a visitar, junto con el camino recorrido hasta ese punto y la profundidad actual
    visited = set()   # conjunto para llevar un registro de los nodos visitados
    while stack:   # mientras la pila no esté vacía
        node, path, depth = stack.pop()   # extrae el último nodo, su camino y la profundidad desde la pila
        if node == goal:   # si se llega al nodo objetivo, termina la búsqueda y devuelve el camino
            return path
        if depth == limit or node in visited:   # si se alcanza el límite de profundidad o el nodo ya ha sido visitado, se salta al siguiente nodo
            continue
        visited.add(node)   # marca el nodo como visitado
        for neighbor in graph[node]:   # para cada vecino del nodo actual
            stack.append((neighbor, path + [neighbor], depth + 1))   # añade el vecino a la pila para visitarlo después, junto con el camino recorrido hasta ese punto y la profundidad actual

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

# Llamada a la función depth_limited_search con el nodo 'A' como punto de partida, 'I' como objetivo y límite de profundidad de 3
path = depth_limited_search(graph, 'A', 'I', 3)
print(path)
