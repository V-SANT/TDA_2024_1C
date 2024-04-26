from constantes_tp2 import *

def ataques_optimos(n, arribos, valores_recarga):
    
    if n == 0:
        return 0,[]
    
    
    optimos = [0] * (n+1)
    arribos = [0] + arribos
    valores_recarga = [0] + valores_recarga

    for j in range(1,n+1):
        optimo_j = 0
        #print(f"Valor de j:{j}")
        for k in range(0,j):
            #print(f"Valor de k: {k}")
            #print(f"    OPT({k}) + MIN(e_{k-j},x_{j}) = {optimos[k]} + min({valores_recarga[(j-k)]},{arribos[(j)]})")
            optimo_parcial = optimos[k] + min((valores_recarga[(j-k)],arribos[(j)]))
            if optimo_parcial > optimo_j:
                optimo_j = optimo_parcial
                optimos[j] = optimo_j

        #print(f"Optimo_j: {optimo_j}")

    ataques = [ATACAR]
    tope = n

    for j in range(n,0,-1):

        if j > tope:
            continue

        optimo_j = optimos[j]

        for k in range(j-1,-1,-1):

            optimo_candidato = optimos[k] + min((valores_recarga[(j-k)],arribos[(j)]))
            
            if optimo_candidato == optimo_j:
                if k > 0:
                    ataques = [ATACAR] + ataques
                tope = k
                break
            
            ataques = [CARGAR] + ataques

    return optimos[-1],ataques

