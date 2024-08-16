import random
from itertools import permutations
import copy
import json
import ast
import data
import time
from strategy import generate_strategies, get_reward

data_sets = []
t = 5, data.data5
data_sets.append(t)
t = 8, data.data8
data_sets.append(t)
t = 10, data.data10
data_sets.append(t)
t = 12, data.data12
data_sets.append(t)
t = 15, data.data15
data_sets.append(t)
t = 17, data.data17
data_sets.append(t)
t = 18, data.data18
data_sets.append(t)

S = data.data5
#S = data.data8
# S = data.data10
# S = data.data12
#S = data.data15
#S = data.data17
# S = data.data18
packet_size = 18

print(generate_strategies(100, 20))
def get_immediate_reward(state):
    return Reward_per_state[state]

def get_pi_a(liste):
    liste.sort(reverse=True)
    return liste[0]
    
def get_successor(current_state, S):
    return list(S.get(current_state))

def belief_update(current_state, b_s, pi_a, pi_d, T_o_s, S):
    som1 = som2 = 0
    print("\n********************* Belief update pour l'état ", current_state, "***********************\n")
    #print("Calcul de la somme des Pb,πa,πd[s, µa, µd, o, s′]\n")
    for m_d_s in pi_d:
        som1 = som1 + b_s*get_pi_a(pi_a)*m_d_s*T_o_s 
    #print("\nCalcul de la somme des Pb,π1,π2[a1, o] \n")
    state_Successor_list = get_successor(current_state, S)
    for successor in state_Successor_list:
        for mu_a in pi_a:
            for mu_d_s in pi_d:
                som2 = som2 + b_s*mu_a*mu_d_s*T_o_s
    #print("Somme des Pb,π1,π2[a1, o] = ", som2)
    val = (som1/som2)
    print("Valeur du belief pour :", current_state, "valeur:", val)
    return val
        
def E(pi_a, pi_d, S):
    som = 0
    b_s = 1
    alpha = 1
    T_o_s = 0.7
    for current_state in S.keys():
        for mu_a in pi_a:
            for mu_d_s in pi_d:
                reward = get_reward(pi_a, pi_d, mu_a, mu_d_s)
                som = som + alpha*b_s*mu_a*mu_d_s*reward
        b_s = belief_update(current_state, b_s, pi_a, pi_d, T_o_s, S)
        alpha = alpha - (1/1000000000)
    return som

def sup_inf(PI_a, PI_d, S):
    liste_min = []
    print("\n************************** Optimal value calculation *********************************\n")
    for pi_d in PI_d:
        liste_max = []
        for pi_a in PI_a:
            val = E(pi_a, pi_d, S)
            liste_max.append(val)
        liste_max.sort()
        item = liste_max[-1]
        liste_min.append(item)
    liste_min.sort()
    return liste_min[0]

def sup_inf_random(PI_a, PI_d, S):
    liste_min = []
    print("\n************************** Optimal value calculation *********************************\n")
    for pi_d in PI_d:
        liste_max = []
        for pi_a in PI_a:
            val = E(pi_a, pi_d, S)
            liste_max.append(val)
        liste_max.sort()
        item = liste_max[-1]
        #item = random.choice(liste_max)
        liste_min.append(item)
    #liste_min.sort()
    #return liste_min[0]
    return random.choice(liste_min)
    
def generate_time_value_over_packets(state_sets, PI_a, PI_d):
    fichier = open('output_value.txt', 'a')
    for packetSize, state_set in state_sets:
        title = "\n************** Optimal value function with "+str(packetSize)+" packets ***************"
        fichier.write(title)
        now = time.time()
        opt_value = sup_inf(PI_a, PI_d, state_set)
        print("La valeur du sup_inf est= ", opt_value)
        later = time.time()
        difference = int(later - now)
        print("Duration to compute the optimal value :", difference, "seconds")
        string = "\nTaille de paquet: "+ str(packetSize) +" time: " + str(difference)+" Value: "+ str(opt_value)
        fichier.write(string)
    fichier.close()

def optimal_value_over_packets(state_set, PI_a, PI_d):
    fichier = open('output_value.txt', 'a')
    now = time.time()
    opt_value = sup_inf(PI_a, PI_d, state_set)
    print("La valeur du sup_inf est= ", opt_value)
    later = time.time()
    difference = int(later - now)
    #print("Duration to compute the optimal value :", difference, "seconds")
    string = "\n "+ str(opt_value)
    fichier.write(string)
    fichier.close()

def random_value_over_packets(state_set, PI_a, PI_d):
    fichier = open('output_value.txt', 'a')
    now = time.time()
    opt_value = sup_inf_random(PI_a, PI_d, state_set)
    #print("La valeur du sup_inf est= ", opt_value)
    later = time.time()
    difference = int(later - now)
    #print("Duration to compute the optimal value :", difference, "seconds")
    string = "\n"+ str(opt_value)
    fichier.write(string)
    fichier.close()

def generate_time_value_over_strategy_size(state_set):
    fichier = open('output_value.txt', 'a')
    for i in range(2, 21):
        # the number of actions is fixed at 10
        PI_a = generate_strategies(i, 10)
        PI_d = generate_strategies(i, 10)
        title = "\n\n************** Optimal value function with "+str(i)+" Strategies ***************"
        fichier.write(title)
        now = time.time()
        # fixed the packet size to 8
        opt_value = sup_inf(PI_a, PI_d, state_set)
        print("La valeur du sup_inf est= ", opt_value)
        later = time.time()
        difference = int(later - now)
        print("Duration to compute the optimal value :", difference, "seconds")
        string = "\n Strategies: "+ str(i) +" time: " + str(difference)+" Value: "+ str(opt_value)
        fichier.write(string)
    fichier.close()

def generate_time_value_over_action_size(state_set):
    fichier = open('output_value.txt', 'a')
    for i in range(2, 21):
        # the number of strategies is fixed at 5
        PI_a = generate_strategies(5, i)
        PI_d = generate_strategies(5, i)
        title = "\n\n************** Optimal value function with "+str(i)+" Actions ***************"
        fichier.write(title)
        now = time.time()
        # fixed the packet size to 10
        opt_value = sup_inf(PI_a, PI_d, state_set)
        print("La valeur du sup_inf est= ", opt_value)
        later = time.time()
        difference = int(later - now)
        print("Duration to compute the optimal value :", difference, "seconds")
        string = "\n Actions: "+ str(i) +" time: " + str(difference)+" Value: "+ str(opt_value)
        fichier.write(string)
    fichier.close()


PI_a = generate_strategies(3, 5)
PI_d = generate_strategies(3, 5)
#generate_time_value_over_packets(data_sets, PI_a, PI_d)
#generate_time_value_over_strategy_size(data.data8)
#generate_time_value_over_action_size(data.data5)
fichier = open('output_value.txt', 'a')
fichier.write("*********************Optimal value evaluation******************************")
fichier.close()
optimal_value_over_packets(data.data3, PI_a, PI_d)
optimal_value_over_packets(data.data5, PI_a, PI_d)
optimal_value_over_packets(data.data8, PI_a, PI_d)
optimal_value_over_packets(data.data10, PI_a, PI_d)
optimal_value_over_packets(data.data12, PI_a, PI_d)
optimal_value_over_packets(data.data15, PI_a, PI_d)
#optimal_value_over_packets(data.data17, PI_a, PI_d)
#optimal_value_over_packets(data.data18, PI_a, PI_d)

fichier = open('output_value.txt', 'a')
fichier.write("*********************Random value evaluation******************************")
fichier.close()

random_value_over_packets(data.data3, PI_a, PI_d)
random_value_over_packets(data.data5, PI_a, PI_d)
random_value_over_packets(data.data8, PI_a, PI_d)
random_value_over_packets(data.data10, PI_a, PI_d)
random_value_over_packets(data.data12, PI_a, PI_d)
random_value_over_packets(data.data15, PI_a, PI_d)
#random_value_over_packets(data.data17, PI_a, PI_d)
#random_value_over_packets(data.data18, PI_a, PI_d)



"""
fichier = open('output_value.txt', 'a') 
now = time.time()
opt_value = sup_inf(PI_a, PI_d, S)
print("La valeur du sup_inf est= ", opt_value)
later = time.time()
difference = int(later - now)
print("Duration to compute the optimal value :", difference, "seconds")
string = "\nTaille de paquet: "+ str(packet_size) +" time: " + str(difference)+" Value: "+ str(opt_value)
fichier.write(string)
fichier.close()
"""








