from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Definir los nodos y las estructuras de tiempo para el DBN
time_slice = ["t_0", "t_1", "t_2"]
nodes = ["A", "B", "C"]
edges = [("A", "B"), ("B", "C")]

# Crear el modelo de la red bayesiana dinámica
model = DBN(edges, nodes, time_slice)

# Definir las distribuciones de probabilidad condicional (CPDs) para cada variable en cada paso de tiempo
cpd_a = TabularCPD(variable="A", variable_card=2, values=[[0.7], [0.3]])
cpd_b = TabularCPD(variable="B", variable_card=2, 
                   values=[[0.9, 0.6], [0.1, 0.4]],
                   evidence=["A"], evidence_card=[2])
cpd_c = TabularCPD(variable="C", variable_card=2, 
                   values=[[0.8, 0.2], [0.2, 0.8]],
                   evidence=["B"], evidence_card=[2])

# Añadir las CPDs al modelo
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Inferir la probabilidad de la variable C en el tiempo t_2 dado la evidencia de las variables A y B en los tiempos t_0 y t_1
infer = DBNInference(model)
query = {"C": 1}
evidence = {"A": 0, "B": 1}
result = infer.query(variables=query, evidence=evidence, joint=False, elimination_order="MinFill")
print(result)
