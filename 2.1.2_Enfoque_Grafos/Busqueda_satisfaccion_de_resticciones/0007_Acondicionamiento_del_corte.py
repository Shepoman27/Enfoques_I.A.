import networkx as nx

def cut_conditioning(G, S):
    H = G.copy() # Copiamos el grafo original
    for node in S:
        # Eliminamos los nodos adyacentes a S
        for neighbor in H.neighbors(node):
            H.remove_node(neighbor)
        # Eliminamos el nodo S
        H.remove_node(node)
    return H

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
nx.draw(G, with_labels=True)

S = {3, 4}
H = cut_conditioning(G, S)
nx.draw(H, with_labels=True)
