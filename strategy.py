import random

Probabilities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.8, 0.9]

# Function to enerate strategies
def generate_strategies(number_of_strategies, number_of_actions):
    strategies = []
    if (number_of_actions <= len(Probabilities)):
        for i in range(number_of_strategies):
            stra1 = random.sample(Probabilities, number_of_actions)
            strategies.append(stra1)
    else:
        for j in range(number_of_strategies):
            s = []
            for k in range(number_of_actions):
                val = random.choice(Probabilities)
                s.append(val)
            strategies.append(s)
    return strategies

def get_reward(pi_a, pi_d, a, d):
    i1 = pi_a.index(a)
    i2 = pi_d.index(d)
    if(i1==i2):
        return 2
    return 0
