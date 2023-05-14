import numpy as np

class PassiveAgent:
    def __init__(self, num_states, num_actions, gamma, alpha):
        self.num_states = num_states
        self.num_actions = num_actions
        self.gamma = gamma
        self.alpha = alpha
        self.V = np.zeros(num_states)

    def update_V(self, reward, state):
        self.V[state] += self.alpha * (reward - self.V[state])

    def learn(self, env, num_episodes):
        for i in range(num_episodes):
            state = env.reset()
            done = False
            while not done:
                action = np.random.choice(self.num_actions)
                next_state, reward, done, _ = env.step(action)
                self.update_V(reward, state)
                state = next_state

class MyEnvironment:
    def __init__(self):
        self.num_states = 10
        self.num_actions = 2
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 0:
            if self.state < self.num_states - 1:
                self.state += 1
        else:
            if self.state > 0:
                self.state -= 1
        if self.state == self.num_states - 1:
            reward = 1
            done = True
        else:
            reward = 0
            done = False
        return self.state, reward, done, {}
