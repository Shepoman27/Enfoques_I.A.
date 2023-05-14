import networkx as nx

def expected_value_node(G, node):
    """
    Calcula el valor esperado de un nodo en un grafo utilizando la regla de decisión de Wald.
    """
    if G.out_degree(node) == 0:  # Nodo hoja
        return G.nodes[node]['value']
    
    successors = G.successors(node)
    expected_value = 0
    
    for action in successors:
        child = next(G.successors(action))
        child_values = [d['weight'] for _, _, d in G.out_edges(child, data=True)]
        expected_value += (1 / len(successors)) * sum(child_values)
            
    return expected_value

def information_value(G, info_node):
    """
    Calcula el valor de información de un nodo de información en un grafo.
    """
    before_value = expected_value_node(G, info_node)
    
    G_copy = G.copy()
    for action in G_copy.predecessors(info_node):
        G_copy.remove_edge(action, info_node)
        
    after_value = expected_value_node(G_copy, info_node)
    
    return before_value - after_value

# Ejemplo de uso
G = nx.DiGraph()
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(2, 5, weight=4)
G.add_edge(3, 6, weight=5)
G.add_node(4, value=10)
G.add_node(5, value=20)
G.add_node(6, value=30)
G.add_node(7, value=40, type='information')

iv = information_value(G, 7)
print(f"El valor de información del nodo 7 es {iv}")

