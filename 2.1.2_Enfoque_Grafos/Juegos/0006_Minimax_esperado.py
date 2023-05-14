import networkx as nx
import random

def minimax_expected(graph, start, depth, max_player=True):
    if depth == 0 or not graph[start]:
        return 0

    if max_player:
        best_score = float('-inf')
        for neighbor in graph[start]:
            score = minimax_expected(graph, neighbor, depth - 1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        total_score = 0
        for neighbor in graph[start]:
            score = minimax_expected(graph, neighbor, depth - 1, True)
            total_score += score
        return total_score / len(graph[start])

# Ejemplo de uso
graph = nx.DiGraph()
graph.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)])
print(minimax_expected(graph, 0, 2))
