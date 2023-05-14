import networkx as nx

# Creamos el grafo
G = nx.DiGraph()

# Añadimos los nodos y sus valores
G.add_node('A', value=10)
G.add_node('B', value=5)
G.add_node('C', value=3)
G.add_node('D', value=8)

# Añadimos las conexiones entre los nodos y sus valores
G.add_edge('A', 'B', weight=0.4)
G.add_edge('A', 'C', weight=0.6)
G.add_edge('B', 'D', weight=0.7)
G.add_edge('C', 'D', weight=0.3)

# Función para calcular el valor esperado de un nodo dado
def expected_value(node, G):
    children = list(G.successors(node))
    if not children:
        return G.nodes[node]['value']
    else:
        value = 0
        for child in children:
            edge_weight = G.edges[(node, child)]['weight']
            value += edge_weight * expected_value(child, G)
        return value

# Calculamos el valor esperado para cada nodo
for node in G.nodes:
    value = expected_value(node, G)
    print(f"El valor esperado del nodo {node} es {value}")
