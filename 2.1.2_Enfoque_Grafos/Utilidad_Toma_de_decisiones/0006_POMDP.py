import networkx as nx
import numpy as np

# Crear el grafo
G = nx.DiGraph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edge('A', 'B', weight=0.2)
G.add_edge('A', 'C', weight=0.8)
G.add_edge('B', 'D', weight=0.5)
G.add_edge('C', 'D', weight=0.6)

# Definir las recompensas
rewards = {'B': 5, 'C': -2, 'D': 10}

# Definir el descuento
discount = 0.9

# Función para calcular el valor de un estado dado una política
def state_value(policy, state, values, G, O):
    """
    Calcula el valor de un estado dado una política y los valores actuales.
    """
    obs_prob = O[state]
    value = 0
    for action, prob in policy[state].items():
        trans_prob = 0
        for next_state in G.successors(state):
            trans_prob += G[state][next_state]['weight'] * O[next_state][obs_prob]
        value += prob * trans_prob * (rewards[action] + discount * values[action])
    return value

# Función para obtener la mejor política
def get_policy(G, values, O):
    """
    Obtiene la mejor política para un conjunto de valores actuales.
    """
    policy = {}
    for state in G.nodes:
        if state in rewards:
            # Si es un estado terminal, la política es vacía
            policy[state] = {}
        else:
            # Seleccionar la acción que maximiza el valor esperado
            max_action = None
            max_value = float('-inf')
            for action in G.successors(state):
                action_value = state_value(policy, action, values, G, O)
                if action_value > max_value:
                    max_value = action_value
                    max_action = action
            # Asignar probabilidad 1 a la mejor acción
            policy[state] = {max_action: 1}
    return policy

# Función para realizar la iteración de políticas
def pomdp_policy_iteration(G, O, threshold=1e-6):
    """
    Realiza la iteración de políticas para el MDP parcialmente observable.
    """
    # Inicializar los valores
    values = {state: 0 for state in G.nodes if state not in rewards}
    # Inicializar la política
    policy = {state: {action: 1/len(G.successors(state)) for action in G.successors(state)} 
              for state in G.nodes if state not in rewards}
    
    while True:
        # Calcular los valores para la política actual
        while True:
            delta = 0
            for state in G.nodes:
                if state not in rewards:
                    old_value = values[state]
                    new_value = state_value(policy, state, values, G, O)
                    values[state] = new_value
                    delta = max(delta, abs(new_value - old_value))
            if delta < threshold:
                break
        
        # Calcular la nueva política
        new_policy = get_policy(G, values, O)
        
        # Verificar si la política actual es óptima
        if new_policy == policy:
            break
        
        policy = new_policy
    
    return
