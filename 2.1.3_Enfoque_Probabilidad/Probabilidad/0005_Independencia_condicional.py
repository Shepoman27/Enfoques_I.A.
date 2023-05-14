from pgmpy.factors.discrete import TabularCPD
from pgmpy.independencies import IndependenceAssertion, Independencies

# Definir la distribución conjunta P(X,Y)
cpd_X = TabularCPD('X', 2, [[0.2], [0.8]])
cpd_Y = TabularCPD('Y', 2, [[0.3], [0.7]])
cpd_XY = TabularCPD('XY', 2, [[0.05, 0.15], [0.25, 0.55]], evidence=['X', 'Y'], evidence_card=[2, 2])

# Imprimir las distribuciones marginales P(X) y P(Y)
print("Distribución marginal P(X):")
print(cpd_X)
print("Distribución marginal P(Y):")
print(cpd_Y)

# Imprimir la distribución conjunta P(X,Y)
print("Distribución conjunta P(X,Y):")
print(cpd_XY)

# Definir la independencia condicional que queremos verificar: X es independiente de Y dado XY
indep_assumption = IndependenceAssertion('X', 'Y', ['XY'])

# Verificar si la independencia condicional se cumple en la distribución P(X,Y)
ind = Independencies([indep_assumption])
print("¿X es independiente de Y dado XY en la distribución P(X,Y)?")
print(ind.check_independence(cpd_X, cpd_Y, [cpd_XY]))
