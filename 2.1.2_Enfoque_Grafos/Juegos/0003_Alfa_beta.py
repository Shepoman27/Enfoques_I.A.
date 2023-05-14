import networkx as nx

def alphabeta(graph, start, depth, alpha, beta, max_player=True):
    if depth == 0 or not graph[start]:
        return 0
    
    if max_player:
        best_score = float('-inf')
        for neighbor in graph[start]:
            score = alphabeta(graph, neighbor, depth - 1, alpha, beta, False)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for neighbor in graph[start]:
            score = alphabeta(graph, neighbor, depth - 1, alpha, beta, True)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score
# Crear grafo
graph = nx.DiGraph()
graph.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])

# Calcular la mejor puntuación para el jugador maximizador
best_score = alphabeta(graph, 0, 3, float('-inf'), float('inf'), True)
print(f"Mejor puntuación: {best_score}")
