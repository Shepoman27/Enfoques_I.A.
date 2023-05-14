from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Crear modelo
model = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('G', 'S')])

# Crear Tabular Conditional Probability Distributions (CPDs)
cpd_d = TabularCPD('D', 2, [[0.6], [0.4]])
cpd_i = TabularCPD('I', 2, [[0.7], [0.3]])
cpd_g = TabularCPD('G', 3, [[0.3, 0.05, 0.9, 0.5],
                           [0.4, 0.25, 0.08, 0.3],
                           [0.3, 0.7, 0.02, 0.2]],
                   evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD('L', 2, [[0.1, 0.4, 0.99], [0.9, 0.6, 0.01]], evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD('S', 2, [[0.5, 0.9], [0.5, 0.1]], evidence=['G'], evidence_card=[3])

# Agregar CPDs al modelo
model.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Comprobar si el modelo es válido
model.check_model()
