class Backtracking:
    def __init__(self, clauses):
        self.clauses = clauses
        self.variables = set()
        for clause in clauses:
            for var in clause:
                self.variables.add(abs(var))
        self.assignment = {}

    def solve(self):
        return self.backtrack()

    def backtrack(self):
        if self.is_satisfiable():
            return self.assignment
        unassigned_var = self.pick_unassigned()
        if unassigned_var is None:
            return None
        self.assignment[unassigned_var] = True
        result = self.backtrack()
        if result is not None:
            return result
        self.assignment[unassigned_var] = False
        return self.backtrack()

    def is_satisfiable(self):
        for clause in self.clauses:
            satisfied = False
            for var in clause:
                if var > 0 and self.assignment.get(var) or var < 0 and not self.assignment.get(abs(var)):
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True

    def pick_unassigned(self):
        for var in self.variables:
            if var not in self.assignment:
                return var
        return None
