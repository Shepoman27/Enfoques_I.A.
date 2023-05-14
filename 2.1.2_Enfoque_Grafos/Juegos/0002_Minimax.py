import networkx as nx

def minimax(graph, start, depth, max_player=True):
    if depth == 0 or not graph[start]:
        return 0

    if max_player:
        best_score = float('-inf')
        for neighbor in graph[start]:
            score = minimax(graph, neighbor, depth - 1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for neighbor in graph[start]:
            score = minimax(graph, neighbor, depth - 1, True)
            best_score = min(best_score, score)
        return best_score

# Creamos el grafo
graph = nx.Graph()
graph.add_nodes_from([0, 1, 2, 3])
graph.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])

# Ejecutamos el algoritmo Minimax
minimax_score = minimax(graph, 0, 3)
print("Puntuación Minimax: ", minimax_score)
