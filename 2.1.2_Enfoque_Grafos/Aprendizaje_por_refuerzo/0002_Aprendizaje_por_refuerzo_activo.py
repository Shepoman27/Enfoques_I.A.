import numpy as np

class MyEnvironment:
    def __init__(self, n_states, n_actions, transitions, rewards):
        self.n_states = n_states
        self.n_actions = n_actions
        self.transitions = transitions
        self.rewards = rewards

    def get_transition_probs(self, state, action):
        return self.transitions[state, action, :]

    def get_reward(self, state, action):
        return self.rewards[state, action]

class MyAgent:
    def __init__(self, n_states, n_actions, alpha, epsilon):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.epsilon = epsilon
        self.Q = np.zeros((n_states, n_actions))

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        else:
            return np.argmax(self.Q[state, :])

    def update_Q(self, state, action, reward, next_state):
        self.Q[state, action] += self.alpha * (reward + np.max(self.Q[next_state, :]) - self.Q[state, action])

def rl_loop(env, agent, n_episodes):
    for i in range(n_episodes):
        state = np.random.randint(env.n_states)
        action = agent.select_action(state)
        while True:
            transition_probs = env.get_transition_probs(state, action)
            next_state = np.random.choice(env.n_states, p=transition_probs)
            reward = env.get_reward(state, action)
            agent.update_Q(state, action, reward, next_state)
            action = agent.select_action(next_state)
            state = next_state
            if np.argmax(agent.Q, axis=1)[0] != 0:  # if Q[0][0] is not the maximum
                break

    return agent.Q
