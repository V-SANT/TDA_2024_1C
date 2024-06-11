def problema_decision_subset_sum(S,t):
    
    z_1 = sum(S)
    z_2 = 2*t
    S_prima = S + z_1 - z_2

    return problema_decision_multiway_number_partition(S_prima,2) 

def problema_decision_multiway_number_partition(A,k):
    return True