import networkx as nx

def horizon_effect(graph, node, horizon):
    """
    Returns True if the horizon effect is in effect at the given node
    in the given graph, and False otherwise.
    """
    neighbors = list(graph.neighbors(node))
    if not neighbors:
        # This is a leaf node, so no horizon effect can occur
        return False
    elif horizon == 0:
        # We've reached the maximum depth, so horizon effect applies
        return True
    else:
        # Recursively check if any child node triggers horizon effect
        for neighbor in neighbors:
            if horizon_effect(graph, neighbor, horizon - 1):
                return True
        return False
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(3, 5)

horizon = 1
node = 2

print(horizon_effect(G, node, horizon))  # True
