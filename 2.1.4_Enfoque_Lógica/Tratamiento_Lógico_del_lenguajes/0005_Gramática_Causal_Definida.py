class CausalGrammar:
    def __init__(self, rules):
        self.rules = rules
        
    def generate(self, start_symbol):
        self.expansions = []
        self.expand(start_symbol)
        return self.expansions
        
    def expand(self, symbol):
        if symbol in self.rules:
            rule = self.rules[symbol]
            for expansion in rule:
                self.expand(expansion)
        else:
            self.expansions.append(symbol)
