class Creencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.valores = {}

    def agregar_valor(self, valor, probabilidad):
        self.valores[valor] = probabilidad


class GrafoCreencias:
    def __init__(self):
        self.creencias = {}

    def agregar_creencia(self, nombre):
        if nombre not in self.creencias:
            self.creencias[nombre] = Creencia(nombre)

    def agregar_valor(self, creencia, valor, probabilidad):
        if creencia not in self.creencias:
            self.agregar_creencia(creencia)
        self.creencias[creencia].agregar_valor(valor, probabilidad)

    def obtener_probabilidad(self, creencia, valor):
        if creencia in self.creencias:
            if valor in self.creencias[creencia].valores:
                return self.creencias[creencia].valores[valor]
        return 0.0

    def obtener_probabilidad_conjunta(self, creencias):
        probabilidad_conjunta = 1.0
        for creencia, valor in creencias.items():
            probabilidad_conjunta *= self.obtener_probabilidad(creencia, valor)
        return probabilidad_conjunta
