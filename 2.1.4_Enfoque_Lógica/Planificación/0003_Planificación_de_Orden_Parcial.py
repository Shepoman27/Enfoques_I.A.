import pycopl
import networkx as nx

class PartialOrderPlanning:

    def __init__(self, init_state, goal_state, actions, constraints):
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = actions
        self.constraints = constraints

    def plan(self):
        # Construir el grafo de planificación
        G = self._build_graph()

        # Resolver el CSP
        vars = list(G.nodes)
        domains = [G.nodes[v]['domain'] for v in vars]
        constraints = []
        for u, v in G.edges:
            constraints.append((u, v, lambda x, y: x < y))
        solution = pycopl.solve(constraints, vars, domains)

        # Construir el plan a partir de la solución
        if solution is None:
            return None
        plan = []
        for var, value in solution.items():
            node = G.nodes[var]
            if node['type'] == 'action':
                plan.append(node['action'])
        return plan

    def _build_graph(self):
        # Crear el grafo de planificación
        G = nx.DiGraph()

        # Agregar los nodos de estado iniciales
        for state in self.init_state:
            G.add_node(state, type='state', domain=[state])

        # Agregar los nodos de estado objetivo
        for state in self.goal_state:
            G.add_node(state, type='state', domain=[state])

        # Agregar los nodos de acción y sus precondiciones y efectos
        for action in self.actions:
            G.add_node(action.name, type='action', domain=[True, False])
            for precond in action.preconds:
                G.add_node(precond, type='state', domain=[True, False])
                G.add_edge(precond, action.name)
            for effect in action.effects:
                G.add_node(effect, type='state', domain=[True, False])
                G.add_edge(action.name, effect)

        # Agregar las restricciones de orden parcial
        for constraint in self.constraints:
            G.add_edge(constraint[0], constraint[1])

        return G
