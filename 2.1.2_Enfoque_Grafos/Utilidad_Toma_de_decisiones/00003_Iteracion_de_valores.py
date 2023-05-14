import networkx as nx

# Creamos el grafo
G = nx.DiGraph()
G.add_node('A', value=0)
G.add_node('B', value=0)
G.add_node('C', value=0)
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=1)

# Iteración de Valores
while True:
    delta = 0
    for node in G.nodes():
        if G.out_degree(node) > 0:
            new_value = max([sum([d['weight'] * G.nodes[child]['value'] for _, child, d in G.out_edges(node, data=True)])])
            delta = max(delta, abs(G.nodes[node]['value'] - new_value))
            G.nodes[node]['value'] = new_value
    if delta < 1e-6:
        break

# Imprimimos los valores de los nodos
print("Valores de los nodos:")
for node in G.nodes():
    print(node, ": ", G.nodes[node]['value'])
