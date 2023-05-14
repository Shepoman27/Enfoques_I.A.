import numpy as np

class LinearSeparabilityChecker:
    
    def __init__(self):
        pass
    
    def is_linearly_separable(self, inputs, targets):
        # Convertimos las etiquetas a 1's y -1's
        targets = np.where(targets == 0, -1, targets)
        
        # Buscamos el hiperplano que separe las clases
        w = np.zeros(inputs.shape[1])
        b = 0
        for i in range(100):
            misclassified = 0
            for x, y in zip(inputs, targets):
                if y * (np.dot(w, x) + b) <= 0:
                    w += y * x
                    b += y
                    misclassified += 1
            if misclassified == 0:
                return True
        
        # Si después de 100 iteraciones no se encuentra un hiperplano que separe las clases, se considera que no son linealmente separables
        return False
