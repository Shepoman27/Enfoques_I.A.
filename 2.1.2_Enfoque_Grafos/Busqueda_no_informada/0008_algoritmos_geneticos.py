import random

# Función para generar una población inicial aleatoria
def generate_population(size, gene_pool):
    population = []
    for i in range(size):
        individual = []
        for j in range(len(gene_pool)):
            gene = random.choice(gene_pool)
            individual.append(gene)
        population.append(individual)
    return population

# Función para calcular el fitness de un individuo
def calculate_fitness(individual, target):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
            fitness += 1
    return fitness

# Función para seleccionar los padres para la reproducción
def selection(population, fitness_fn):
    fitnesses = [fitness_fn(individual) for individual in population]
    max_fitness = max(fitnesses)
    return random.choice([individual for individual, fitness in zip(population, fitnesses) if fitness == max_fitness])

# Función para realizar el cruce entre dos padres para producir un nuevo individuo
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Función para mutar un gen de un individuo
def mutate(individual, gene_pool, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(gene_pool)
    return individual

# Función principal de algoritmos genéticos
def genetic_algorithm(gene_pool, target, size=100, max_generations=100, crossover_rate=0.8, mutation_rate=0.1):
    population = generate_population(size, gene_pool)
    for i in range(max_generations):
        new_population = []
        for j in range(size):
            parent1 = selection(population, lambda individual: calculate_fitness(individual, target))
            parent2 = selection(population, lambda individual: calculate_fitness(individual, target))
            child = crossover(parent1, parent2)
            child = mutate(child, gene_pool, mutation_rate)
            new_population.append(child)
        population = new_population
        fitnesses = [calculate_fitness(individual, target) for individual in population]
        if max(fitnesses) == len(target):
            return population[fitnesses.index(max(fitnesses))]
    return None

# Ejemplo de uso
gene_pool = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
target = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
solution = genetic_algorithm(gene_pool, target, size=100, max_generations=1000, crossover_rate=0.8, mutation_rate=0.1)
print(solution)
