import math
import heapq

# Función heurística que devuelve una estimación del costo restante del camino más corto desde un nodo hasta el objetivo
def heuristica(nodo, objetivo):
    x1, y1 = nodo
    x2, y2 = objetivo
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Función de búsqueda A*
def buscar_astar(inicio, objetivo, graf):
    # Inicializamos la cola de prioridad con el nodo inicial y su costo cero
    cola_prioridad = [(0, inicio)]
    # Creamos un diccionario para almacenar el costo actual del camino más corto a cada nodo
    costo_camino_corto = {inicio: 0}
    # Creamos un diccionario para almacenar el nodo padre de cada nodo
    nodo_padre = {inicio: None}
    # Mientras la cola de prioridad no esté vacía
    while cola_prioridad:
        # Extraemos el nodo con el menor costo estimado del camino más corto al objetivo
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        # Si llegamos al objetivo, devolvemos el camino desde el nodo inicial hasta el objetivo
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = nodo_padre[nodo_actual]
            camino.reverse()
            return camino
        # Recorremos todos los vecinos del nodo actual
        for vecino, costo in graf[nodo_actual].items():
            # Calculamos el costo del camino más corto desde el nodo inicial al vecino a través del nodo actual
            costo_corto_vecino = costo_camino_corto[nodo_actual] + costo
            # Si el vecino no ha sido visitado o el nuevo costo del camino más corto es menor que el costo anterior
            if vecino not in costo_camino_corto or costo_corto_vecino < costo_camino_corto[vecino]:
                # Actualizamos el costo del camino más corto al vecino
                costo_camino_corto[vecino] = costo_corto_vecino
                # Estimamos el costo restante del camino más corto desde el vecino hasta el objetivo utilizando una función heurística
                estimacion_resto = costo_corto_vecino + heuristica(vecino, objetivo)
                # Agregamos el vecino a la cola de prioridad con su costo estimado del camino más corto al objetivo
                heapq.heappush(cola_prioridad, (estimacion_resto, vecino))
                # Actualizamos el nodo padre del vecino al nodo actual
                nodo_padre[vecino] = nodo_actual
    # Si no se encuentra un camino al objetivo, devolvemos None
    return None


# Ejemplo de uso
# Definimos un grafo no dirigido con pesos que representa un mapa de ci
# Definimos un grafo no dirigido con pesos que representa un mapa de ciudades
grafo_ciudades = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


# Ejemplo de búsqueda A* en el grafo de ciudades
inicio = 'Arad'
objetivo = 'Bucharest'
camino = buscar_astar(inicio, objetivo, grafo_ciudades)
if camino:
    print(f'El camino más corto desde {inicio} hasta {objetivo} es: {camino}')
else:
    print(f'No se encontró un camino desde {inicio} hasta {objetivo}')