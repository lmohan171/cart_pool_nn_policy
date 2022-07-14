import gym
import numpy as np
import time
from tqdm import tqdm


#Creating environment
env=gym.make('CartPole-v1')

#def basic_policy(PoleAngle):
#    if PoleAngle <0: #move to left
#        return 0 
#    else:
#        return 1

def basic_policy(PoleAngle):
    if PoleAngle < 0: #falling left
        return 0 #move left
    return 1
 
total_rewards=list()

N_episodes=200
N_steps=200

for episodes in range(N_episodes):
    rewards=0
    #Cart position, cartvelocity, pole angle, pole angular velocity
    observtions=env.reset()
    PoleAngle=observtions[2]
    for steps in tqdm(range(N_steps)):
        env.render()
        action=basic_policy(PoleAngle)
        observations, reward, done, info=env.step(action)
        time.sleep(0.001) #sleep
        rewards+=reward

        if done: #fallen
            break
    total_rewards.append(rewards)

stats={
    'mean':np.mean(total_rewards),
    'std_dev':np.std(total_rewards),
    'min':np.min(total_rewards),
    'max':np.max(total_rewards),
    
}

print(stats)