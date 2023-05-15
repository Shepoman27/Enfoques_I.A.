from collections import Counter
from math import log2

class FOIL:

    def __init__(self, X, Y, attributes):
        self.X = X
        self.Y = Y
        self.attributes = attributes
        self.target_attr = attributes[-1]

    def entropy(self, X):
        Y = self.Y[X]
        counter = Counter(Y)
        probs = [v / len(Y) for v in counter.values()]
        entropy = -sum([p * log2(p) for p in probs])
        return entropy

    def gain(self, X, attr):
        Y = self.Y[X]
        attr_values = set(self.X[attr])
        total_entropy = self.entropy(X)
        weighted_entropy = 0
        for val in attr_values:
            X_val = [x for x in X if x[attr] == val]
            weighted_entropy += len(X_val) / len(X) * self.entropy(X_val)
        return total_entropy - weighted_entropy

    def best_attribute(self, X):
        gain_list = [(self.gain(X, attr), attr) for attr in self.attributes[:-1]]
        return max(gain_list)[1]

    def build_tree(self, X):
        Y = self.Y[X]
        if len(set(Y)) == 1:
            return Y[0]
        elif len(X[0]) == 1:
            counter = Counter(Y)
            return max(counter.items(), key=lambda x: x[1])[0]
        else:
            best_attr = self.best_attribute(X)
            tree = {best_attr: {}}
            for val in set(self.X[best_attr]):
                X_val = [x for x in X if x[best_attr] == val]
                Y_val = self.Y[X_val]
                if not X_val:
                    counter = Counter(Y)
                    tree[best_attr][val] = max(counter.items(), key=lambda x: x[1])[0]
                else:
                    self.attributes.remove(best_attr)
                    tree[best_attr][val] = self.build_tree(X_val)
                    self.attributes.append(best_attr)
            return tree

    def train(self):
        X = [tuple(row) for row in self.X]
        self.tree = self.build_tree(X)

    def predict(self, x):
        node = self.tree
        while isinstance(node, dict):
            attr = next(iter(node))
            node = node[attr][x[self.attributes.index(attr)]]
        return node
