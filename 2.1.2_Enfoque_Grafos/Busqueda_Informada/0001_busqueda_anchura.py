from collections import deque

def bfs(graph, start):
    visited = set()   # conjunto para llevar un registro de los nodos visitados
    queue = deque([start])   # cola de nodos por visitar, empezando con el nodo inicial
    visited.add(start)   # marca el nodo inicial como visitado
    while queue:   # mientras la cola no esté vacía
        vertex = queue.popleft()   # extrae el primer nodo de la cola
        print(vertex)   # imprime el nodo actual
        for neighbor in graph[vertex]:   # para cada vecino del nodo actual
            if neighbor not in visited:   # si no ha sido visitado
                visited.add(neighbor)   # marca el vecino como visitado
                queue.append(neighbor)   # añade el vecino a la cola para visitarlo después

# Ejemplo de grafo representado como lista de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Llamada a la función bfs con el nodo 'A' como punto de partida
bfs(graph, 'A')
