class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.add(rule)

    def retract_fact(self, fact):
        self.facts.remove(fact)

    def retract_rule(self, rule):
        self.rules.remove(rule)

    def clear_facts(self):
        self.facts.clear()

    def clear_rules(self):
        self.rules.clear()

class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def apply(self, kb):
        if all(fact in kb.facts for fact in self.antecedent):
            kb.add_fact(self.consequent)

class Fact:
    def __init__(self, name, value=True):
        self.name = name
        self.value = value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((self.name, self.value))

    def __str__(self):
        if self.value:
            return self.name
        else:
            return "not " + self.name
