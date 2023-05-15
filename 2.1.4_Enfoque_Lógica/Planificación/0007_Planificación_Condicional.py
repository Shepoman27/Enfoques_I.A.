class Condition:
    def __init__(self, pred, args):
        self.pred = pred
        self.args = args

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class Plan:
    def __init__(self, actions):
        self.actions = actions

class State:
    def __init__(self, predicates):
        self.predicates = predicates

    def satisfies(self, condition):
        return any(condition.pred == p.pred and condition.args == p.args for p in self.predicates)

class Problem:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

def get_valid_plans(problem, current_state, plans, visited):
    valid_plans = []
    for plan in plans:
        if all(current_state.satisfies(condition) for condition in plan.preconditions) and plan not in visited:
            visited.add(plan)
            new_state = State(current_state.predicates + plan.effects)
            if all(new_state.satisfies(goal) for goal in problem.goal_state):
                valid_plans.append(Plan([plan]))
            else:
                subplans = get_valid_plans(problem, new_state, plans, visited)
                if subplans:
                    valid_plans.append(Plan([plan] + subplans[0].actions))
    return valid_plans

def get_plans(problem):
    return get_valid_plans(problem, problem.initial_state, problem.actions, set())

# Ejemplo de uso
p1 = Problem(
    State([Condition('At', 'a'), Condition('At', 'b'), Condition('On', 'a', 'table'), Condition('On', 'b', 'table'), Condition('Clear', 'a')]),
    [Condition('At', 'b')],
    [
        Action('Pickup', [Condition('At', '?x'), Condition('Clear', '?x')], [Condition('Holding', '?x'), Condition('Clear', 'table'), ~Condition('At', '?x')]),
        Action('Putdown', [Condition('Holding', '?x')], [Condition('At', '?x'), Condition('Clear', '?x'), ~Condition('Holding', '?x')]),
        Action('Stack', [Condition('Holding', '?x'), Condition('Clear', '?y')], [Condition('On', '?x', '?y'), Condition('Clear', 'table'), ~Condition('Holding', '?x'), ~Condition('Clear', '?y')]),
        Action('Unstack', [Condition('On', '?x', '?y'), Condition('Clear', 'table')], [Condition('Holding', '?x'), Condition('Clear', '?y'), ~Condition('On', '?x', '?y')])
    ])

plans = get_plans(p1)
for plan in plans:
    print([action.name for action in plan.actions])
