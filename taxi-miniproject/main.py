from agent import Agent
from monitor import interact
import gymnasium as gym
import numpy as np

env = gym.make('Taxi-v3')
agent = Agent()
avg_rewards, best_avg_reward = interact(env, agent)

print('Best average reward: {}'.format(best_avg_reward))
if (best_avg_reward > 9.1):
    print('The environment was solved in {} episodes.'.format(len(avg_rewards)))
else:
    print('The environment was not solved in {} episodes.'.format(len(avg_rewards)))
