def problema_decision_subset_sum(S,t):
    
    z_1 = sum(S)
    z_2 = 2*t
    S_prima = S + z_1 - z_2

    return problema_decision_multiway_number_partition(S_prima,2) 

def problema_decision_multiway_number_partition(A,k):
    
    if sum(A) % k != 0:
        return False

    B = sum(A)**2//k

    return problema_decision_tribu_agua(A,k,B)

def problema_decision_tribu_agua(S,k,B):
    return True