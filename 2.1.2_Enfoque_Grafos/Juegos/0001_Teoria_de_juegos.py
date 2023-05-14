import networkx as nx

# Crea el grafo
G = nx.Graph()
G.add_nodes_from([1,2,3,4])

# Define las estrategias de los jugadores
strategy_1 = {1: 0, 2: 1, 3: 1, 4: 0} # Jugador 1
strategy_2 = {1: 1, 2: 0, 3: 0, 4: 1} # Jugador 2

# Define las recompensas de los jugadores
rewards_1 = {1: 3, 2: 0, 3: 1, 4: 1} # Jugador 1
rewards_2 = {1: 0, 2: 3, 3: 1, 4: 1} # Jugador 2

# Calcula el pago de cada jugador
payoff_1 = sum([rewards_1[n]*strategy_2[n] for n in G])
payoff_2 = sum([rewards_2[n]*strategy_1[n] for n in G])

# Imprime los pagos de cada jugador
print("El jugador 1 tiene un pago de: ", payoff_1)
print("El jugador 2 tiene un pago de: ", payoff_2)
