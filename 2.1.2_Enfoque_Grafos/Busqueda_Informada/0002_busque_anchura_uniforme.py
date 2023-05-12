import heapq

def uniform_cost_search(graph, start, goal):
    frontier = [(0, start)]   # cola de prioridad de nodos a visitar, ordenados por el costo acumulado
    visited = set()   # conjunto para llevar un registro de los nodos visitados
    costs = {start: 0}   # diccionario para llevar un registro de los costos acumulados de los nodos
    while frontier:   # mientras la cola de prioridad no esté vacía
        cost, node = heapq.heappop(frontier)   # extrae el nodo de menor costo de la cola
        if node == goal:   # si se llega al nodo objetivo, termina la búsqueda
            return cost
        if node in visited:   # si el nodo ya ha sido visitado, se salta al siguiente nodo
            continue
        visited.add(node)   # marca el nodo como visitado
        for neighbor, neighbor_cost in graph[node]:   # para cada vecino del nodo actual
            new_cost = costs[node] + neighbor_cost   # calcula el nuevo costo acumulado del vecino
            if neighbor not in costs or new_cost < costs[neighbor]:   # si el vecino aún no ha sido visitado o el nuevo costo es menor que el anterior
                costs[neighbor] = new_cost   # actualiza el costo acumulado del vecino
                priority = new_cost   # el nuevo costo se convierte en la prioridad del nodo en la cola
                heapq.heappush(frontier, (priority, neighbor))   # añade el vecino a la cola de prioridad para visitarlo después

    return float('inf')   # si no se encuentra un camino al nodo objetivo, retorna infinito

# Ejemplo de grafo con costo uniforme representado como lista de adyacencia
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 7)],
    'D': [('G', 1)],
    'E': [('H', 2)],
    'F': [('I', 4)],
    'G': [('H', 3)],
    'H': [('I', 2)],
    'I': []
}

# Llamada a la función uniform_cost_search con el nodo 'A' como punto de partida y 'I' como objetivo
cost = uniform_cost_search(graph, 'A', 'I')
print(cost)
