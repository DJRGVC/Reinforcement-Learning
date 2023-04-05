import numpy as np
from collections import defaultdict


class Agent:

    def __init__(self, nA=6, epsilon=.3, alpha=0.3, gamma=1, eps_min=0.0005):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.epCount = 0


        self.nA = nA
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.eps_min = eps_min

        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """

        # conforming to the epsilon-greedy policy
        # if np.random.random() > self.epsilon:
            #return np.random.choice(self.nA)
        # else:
            #return np.argmax(self.Q[state])

        best_action = np.argmax(self.Q[state])
        probs = np.full(self.nA, self.epsilon / self.nA)
        probs[best_action] += 1 - self.epsilon
        return np.random.choice(np.arange(self.nA), p=probs)

    def expected_return(self, state):
        """ Given the state, return the expected return.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - expected_return: the expected return
        """
        return np.sum([self.Q[state][a] * self.epsilon / self.nA for a in range(self.nA)]) + np.max(self.Q[state]) * (1 - self.epsilon)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        # update the epsilon value
        self.epsilon = max(1/(self.epCount + 1), self.eps_min)

        # update the Q table, conforming to the expected SARSA algorithm
        if not done:
            self.Q[state][action] += self.alpha * (reward + self.gamma * self.expected_return(next_state) - self.Q[state][action])
        else:
            self.Q[state][action] += self.alpha * (reward - self.Q[state][action])
            self.epCount += 1


    

