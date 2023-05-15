import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables difusas
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de pertenencia para la variable calidad
calidad['mala'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['regular'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['buena'] = fuzz.trimf(calidad.universe, [5, 10, 10])

# Definir funciones de pertenencia para la variable propina
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(calidad['mala'], propina['baja'])
regla2 = ctrl.Rule(calidad['regular'], propina['media'])
regla3 = ctrl.Rule(calidad['buena'], propina['alta'])

# Crear controlador difuso
controlador_propina = ctrl.ControlSystem([regla1, regla2, regla3])

# Definir simulación
simulacion_propina = ctrl.ControlSystemSimulation(controlador_propina)

# Ejemplo de uso
simulacion_propina.input['calidad'] = 6.5
simulacion_propina.compute()

print(simulacion_propina.output['propina'])
propina.view(sim=simulacion_propina)
