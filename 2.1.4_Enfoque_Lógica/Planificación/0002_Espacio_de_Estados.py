import heapq

class Estado:
    
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.mapa = mapa
class Accion:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def ejecutar(self, estado):
        nuevo_x = estado.x + self.dx
        nuevo_y = estado.y + self.dy

        # Verificar si la nueva posición es válida
        if nuevo_x >= 0 and nuevo_x < len(estado.mapa) and nuevo_y >= 0 and nuevo_y < len(estado.mapa[0]) and estado.mapa[nuevo_x][nuevo_y] == 0:
            nuevo_mapa = [fila[:] for fila in estado.mapa] # copiar el mapa
            nuevo_mapa[estado.x][estado.y] = 0 # dejar libre la posición anterior
            nuevo_mapa[nuevo_x][nuevo_y] = 1 # ocupar la nueva posición
            return Estado(nuevo_x, nuevo_y, nuevo_mapa)
        else:
            return None

def distancia(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def buscar_camino(inicial, final):
    visitados = set()
    cola = [(0, inicial)]
    while len(cola) > 0:
        _, actual = heapq.heappop(cola)
        if actual in visitados:
            continue
        visitados.add(actual)
        if actual.x == final.x and actual.y == final.y:
            # se llegó al destino
            camino = []
            while actual != inicial:
                camino.append(actual)
                actual = actual.padre
            camino.reverse()
            return camino
        # expandir nodos vecinos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            accion = Accion(dx, dy)
            nuevo_estado = accion.ejecutar(actual)
            if nuevo_estado is not None and nuevo_estado not in visitados:
                nuevo_costo
