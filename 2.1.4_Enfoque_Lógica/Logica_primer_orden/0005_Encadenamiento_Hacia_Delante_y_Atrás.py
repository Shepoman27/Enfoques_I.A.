class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chain(self):
        while True:
            new_facts = []
            for rule in self.rules:
                if all(fact in self.facts for fact in rule.if_conditions):
                    new_facts.extend(rule.then_conclusions)
            if not new_facts:
                break
            for fact in new_facts:
                if fact not in self.facts:
                    self.facts.append(fact)
        return self.facts

    def backward_chain(self, goal):
        if goal in self.facts:
            return True
        for rule in self.rules:
            if goal in rule.then_conclusions:
                if all(self.backward_chain(if_cond) for if_cond in rule.if_conditions):
                    return True
        return False


class Rule:
    def __init__(self, if_conditions, then_conclusions):
        self.if_conditions = if_conditions
        self.then_conclusions = then_conclusions


kb = KnowledgeBase()

# Agregar hechos a la base de conocimiento
kb.add_fact("Tiene pelo")
kb.add_fact("Tiene alas")
kb.add_fact("Es un pájaro")

# Agregar reglas a la base de conocimiento
kb.add_rule(Rule(["Tiene pelo"], ["No es un pájaro"]))
kb.add_rule(Rule(["Tiene alas"], ["Es un ave"]))
kb.add_rule(Rule(["Es un ave", "No vuela"], ["Es un pingüino"]))
kb.add_rule(Rule(["Es un ave", "Tiene pico"], ["Es un ave con pico"]))

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
print(kb.forward_chain())

# Encadenamiento hacia atrás
print("Encadenamiento hacia atrás:")
print("¿Es un pingüino?", kb.backward_chain("Es un pingüino"))
print("¿Es un ave con pico?", kb.backward_chain("Es un ave con pico"))
