import random
import math

# Función para la búsqueda de temple simulado
def simulated_annealing(graph, start_node, heuristic, temperature, cooling_rate, max_iterations):
    current_node = start_node  # Nodo actual de la búsqueda
    best_node = current_node  # Mejor nodo encontrado
    best_score = heuristic(current_node)  # Calcular la puntuación del mejor nodo encontrado
    iterations = 0  # Contador de iteraciones
    while iterations < max_iterations and temperature > 0.1:  # Bucle principal de la búsqueda
        neighbors = graph[current_node]  # Obtener los nodos vecinos del nodo actual
        next_node = random.choice(list(neighbors.keys()))  # Seleccionar un nodo vecino al azar
        next_score = heuristic(next_node)  # Calcular la puntuación del nodo vecino seleccionado
        delta = next_score - best_score  # Calcular la diferencia de puntuación entre el nodo vecino y el mejor nodo encontrado
        if delta > 0 or math.exp(delta / temperature) > random.random():  # Verificar si se debe seleccionar el nodo vecino
            current_node = next_node  # Actualizar el nodo actual
            if next_score > best_score:  # Verificar si el nodo vecino seleccionado es mejor que el mejor nodo encontrado
                best_node = next_node  # Actualizar el mejor nodo encontrado
                best_score = next_score  # Actualizar la puntuación del mejor nodo encontrado
        temperature *= cooling_rate  # Reducir la temperatura de la búsqueda
        iterations += 1  # Incrementar el contador de iteraciones
    return best_node  # Devolver el mejor nodo encontrado

# Definir el grafo
graph = {
    'A': {'B': 1, 'C': 4, 'D': 5},
    'B': {'A': 1, 'E': 2},
    'C': {'A': 4, 'E': 6, 'F': 3},
    'D': {'A': 5, 'F': 2},
    'E': {'B': 2, 'C': 6, 'G': 2},
    'F': {'C': 3, 'D': 2, 'G': 3},
    'G': {'E': 2, 'F': 3}
}

# Función heurística para el costo de un nodo
def heuristic(node):
    # Devuelve la distancia manhattan del nodo al nodo objetivo 'G'
    distances = {'A': 9, 'B': 7, 'C': 5, 'D': 5, 'E': 3, 'F': 1, 'G': 0}
    return distances[node]

# Iniciar la búsqueda de temple simulado desde el nodo 'A'
start_node = 'A'
temperature = 1000
cooling_rate = 0.95
max_iterations = 1000
result = simulated_annealing(graph, start_node, heuristic, temperature, cooling_rate, max_iterations)

# Imprimir el nodo objetivo encontrado
print('Nodo objetivo:', result)