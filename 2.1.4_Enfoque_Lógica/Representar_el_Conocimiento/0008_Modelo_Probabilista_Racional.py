from pomegranate import *

# Creamos las distribuciones de probabilidad para las variables aleatorias
D = DiscreteDistribution({'A': 0.5, 'B': 0.5})
A = ConditionalProbabilityTable(
    [[True, 'A', 0.2],
     [True, 'B', 0.8],
     [False, 'A', 0.6],
     [False, 'B', 0.4]],
    [D]
)
B = ConditionalProbabilityTable(
    [[True, True, 0.1],
     [True, False, 0.9],
     [False, True, 0.8],
     [False, False, 0.2]],
    [A]
)

# Creamos las variables aleatorias
d = Node(D, name="D")
a = Node(A, name="A")
b = Node(B, name="B")

# Creamos la red bayesiana
model = BayesianNetwork("Modelo probabilista racional")
model.add_states(d, a, b)
model.add_edge(d, a)
model.add_edge(a, b)
model.bake()

# Hacemos una predicción
print(model.predict_proba({'A': True}))
