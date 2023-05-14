import networkx as nx

def policy_iteration(G, discount_factor=1.0):
    """
    Realiza la iteración de políticas en un grafo dirigido con nodos de decisión y nodos de azar.
    """
    # Inicializar la política
    policy = {node: list(G.successors(node))[0] for node in G.nodes() if G.out_degree(node) > 0}
    
    while True:
        # Evaluar la política actual
        values = value_iteration(G, policy, discount_factor)
        
        # Mejorar la política
        policy_stable = True
        for node in G.nodes():
            if G.nodes[node]['type'] == 'decision':
                successors = G.successors(node)
                max_value = float('-inf')
                best_action = None
                for action in successors:
                    child = next(G.successors(action))
                    child_value = sum(d['weight'] * values[child] for _, _, d in G.out_edges(action, data=True))
                    if child_value > max_value:
                        max_value = child_value
                        best_action = action
                if policy[node] != best_action:
                    policy_stable = False
                    policy[node] = best_action
        
        if policy_stable:
            break
    
    return values, policy
