
def number_of_states_per_packet_size(packet_size):
    som = 0
    for j in range(1, packet_size+1):
        tmp = 1
        for k in range(j, packet_size+1):
            tmp = tmp*k
        som = som + tmp
    return som

print("************ Display the number of states over the size of packets ***********")
print("Size of packets  ----  Number of states")
for i in range(1, 21):
    print("   ",i,"                    ",number_of_states_per_packet_size(i))
