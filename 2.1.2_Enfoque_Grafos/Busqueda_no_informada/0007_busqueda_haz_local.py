import heapq

def beam_search(graph, start_node, goal_node, beam_width):
    # Lista de nodos a explorar
    current_beam = [(0, start_node)]
    while True:
        # Seleccionar los 'beam_width' nodos con menor costo
        next_beam = []
        for _, node in current_beam:
            for next_node, cost in graph[node].items():
                heapq.heappush(next_beam, (_, next_node))
        current_beam = next_beam[:beam_width]
        # Comprobar si alguno de los nodos del haz es el nodo objetivo
        for _, node in current_beam:
            if node == goal_node:
                return node
            
graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2}
}
