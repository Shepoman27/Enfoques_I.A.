import numpy as np

class Perceptron:
    
    def __init__(self, n_inputs):
        self.weights = np.random.randn(n_inputs)
        self.bias = np.random.randn()
        
    def predict(self, inputs):
        net = np.dot(self.weights, inputs) + self.bias
        output = 1 if net > 0 else 0
        return output
    
    def train(self, inputs, targets, learning_rate, n_epochs):
        for epoch in range(n_epochs):
            for x, y in zip(inputs, targets):
                y_pred = self.predict(x)
                error = y - y_pred
                self.weights += learning_rate * error * x
                self.bias += learning_rate * error
