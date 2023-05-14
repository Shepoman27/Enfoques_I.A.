import random

# Función de inicialización del agente Q-learning
def init_q_learning(num_states, num_actions, learning_rate, discount_factor, exploration_rate):
    q_table = [[0] * num_actions for _ in range(num_states)]
    alpha = learning_rate  # tasa de aprendizaje
    gamma = discount_factor  # factor de descuento
    epsilon = exploration_rate  # tasa de exploración
    return q_table, alpha, gamma, epsilon

# Función de selección de acción
def select_action(q_table, state, epsilon):
    if random.uniform(0, 1) < epsilon:
        # Acción aleatoria
        return random.randint(0, len(q_table[state]) - 1)
    else:
        # Acción con mejor valor Q
        return q_table[state].index(max(q_table[state]))

# Función de actualización de la tabla Q
def update_q_table(q_table, state, action, reward, next_state, alpha, gamma):
    old_value = q_table[state][action]
    next_max = max(q_table[next_state])
    new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
    q_table[state][action] = new_value
    return q_table

# Función de entrenamiento del agente Q-learning
def train_q_learning(env, q_table, alpha, gamma, epsilon, num_episodes, max_steps):
    for episode in range(num_episodes):
        state = env.reset()
        for step in range(max_steps):
            action = select_action(q_table, state, epsilon)
            next_state, reward, done = env.step(action)
            q_table = update_q_table(q_table, state, action, reward, next_state, alpha, gamma)
            state = next_state
            if done:
                break
        # Imprimir el progreso
        print(f"Episode {episode+1}/{num_episodes} complete")
    return q_table
