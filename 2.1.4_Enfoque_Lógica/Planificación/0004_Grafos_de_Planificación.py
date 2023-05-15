# Definición del problema de planificación
problem = {
    'init': {'limpiar_a': False, 'limpiar_b': False, 'mover_a_b': False, 'mover_b_a': False},
    'goal': {'limpiar_a': True, 'limpiar_b': True}
}

# Definición de las acciones disponibles
actions = {
    'limpiar_a': {
        'precond': {'limpiar_a': False},
        'effect': {'limpiar_a': True}
    },
    'limpiar_b': {
        'precond': {'limpiar_b': False},
        'effect': {'limpiar_b': True}
    },
    'mover_a_b': {
        'precond': {'mover_a_b': False},
        'effect': {'mover_a_b': True, 'limpiar_a': True}
    },
    'mover_b_a': {
        'precond': {'mover_b_a': False},
        'effect': {'mover_b_a': True, 'limpiar_b': True}
    }
}

# Función para comprobar si un estado cumple con las precondiciones de una acción
def satisfies(state, precond):
    for condition, value in precond.items():
        if state.get(condition) != value:
            return False
    return True

# Función para aplicar los efectos de una acción a un estado
def apply_effects(state, effect):
    new_state = state.copy()
    new_state.update(effect)
    return new_state

# Función que genera el grafo de planificación para el problema dado
def build_graph(problem, actions):
    graph = {
        'nodes': {
            0: { 'state': problem['init'], 'actions': set() }
        },
        'edges': {}
    }
    level = 0
    while True:
        new_nodes = {}
        for node_id, node_data in graph['nodes'].items():
            node_state = node_data['state']
            for action_name, action_data in actions.items():
                if satisfies(node_state, action_data['precond']):
                    new_state = apply_effects(node_state, action_data['effect'])
                    new_node = { 'state': new_state, 'actions': node_data['actions'].union(set([action_name])) }
                    new_node_id = len(new_nodes)
                    new_nodes[new_node_id] = new_node
                    graph['edges'][(node_id, new_node_id)] = action_name
        if len(new_nodes) == 0:
            return None
        if problem['goal'] in [node_data['state'] for node_data in new_nodes.values()]:
            return [node_data['actions'] for node_data in new_nodes.values() if node_data['state'] == problem['goal']]
        graph['nodes'].update(new_nodes)
        level += 1

# Ejecución de la planificación del problema
plan = build_graph(problem, actions)

# Impresión del resultado
if plan is None:
    print("No se encontró una solución para el problema de planificación.")
else:
    print("Plan encontrado: {}".format(plan))
