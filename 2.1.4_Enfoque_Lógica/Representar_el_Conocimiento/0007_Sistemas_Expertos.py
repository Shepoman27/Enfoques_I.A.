from pyknow import *

class Enfermedad(Fact):
    """
    Definición de la clase Fact para la enfermedad
    """
    pass

class SistemaExperto(KnowledgeEngine):
    """
    Definición de la clase del sistema experto
    """
    @Rule(Enfermedad(sintoma1='si', sintoma2='si'))
    def enfermedad1(self):
        """
        Regla de la enfermedad 1
        """
        self.declare(Enfermedad(nombre='enfermedad1', probabilidad=0.8))

    @Rule(Enfermedad(sintoma1='si', sintoma2='no'))
    def enfermedad2(self):
        """
        Regla de la enfermedad 2
        """
        self.declare(Enfermedad(nombre='enfermedad2', probabilidad=0.6))

    @Rule(Enfermedad(sintoma1='no', sintoma2='si'))
    def enfermedad3(self):
        """
        Regla de la enfermedad 3
        """
        self.declare(Enfermedad(nombre='enfermedad3', probabilidad=0.4))

    @Rule(Enfermedad(sintoma1='no', sintoma2='no'))
    def enfermedad4(self):
        """
        Regla de la enfermedad 4
        """
        self.declare(Enfermedad(nombre='enfermedad4', probabilidad=0.2))
        
sistema_experto = SistemaExperto()
sistema_experto.reset()
sistema_experto.declare(Enfermedad(sintoma1='si', sintoma2='no'))
sistema_experto.run()
resultado = sistema_experto.facts[-1]
print(f"La enfermedad más probable es {resultado['nombre']} con una probabilidad del {resultado['probabilidad']*100}%")
