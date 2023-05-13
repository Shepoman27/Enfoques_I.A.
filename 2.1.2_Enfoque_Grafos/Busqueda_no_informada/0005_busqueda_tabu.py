def tabu_search(graph, start_node, heuristic, tabu_size, max_iterations):
    current_node = start_node
    tabu_list = []
    best_node = current_node
    best_score = heuristic(current_node)
    iterations = 0
    while iterations < max_iterations:
        neighbors = graph[current_node]
        candidate_moves = [(n, heuristic(n)) for n in neighbors if n not in tabu_list]
        if not candidate_moves:
            # Si no hay movimientos candidatos, se regresa el mejor nodo encontrado hasta ahora
            return best_node
        # Se selecciona el movimiento con la puntuación más alta
        next_node, next_score = max(candidate_moves, key=lambda x: x[1])
        # Se actualiza el mejor nodo encontrado hasta ahora
        if next_score > best_score:
            best_node = next_node
            best_score = next_score
        # Se agrega el movimiento actual a la lista tabú
        tabu_list.append(current_node)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        current_node = next_node
        iterations += 1
    # Se regresa el mejor nodo encontrado hasta ahora
    return best_node

# Definir el grafo
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 3},
    'C': {'D': 2, 'E': 5},
    'D': {'E': 3},
    'E': {}
}

# Función heurística para el costo de un nodo
def heuristic(node):
    return ord(node) - ord('A')

# Iniciar la búsqueda tabú desde el nodo A
start_node = 'A'
tabu_size = 2
max_iterations = 10
result = tabu_search(graph, start_node, heuristic, tabu_size, max_iterations)

# Imprimir el nodo objetivo encontrado
print('Nodo objetivo encontrado:', result)