from constantes_tp2 import *

def obtener_valores_optimos_ataque(x, e):

    if len(x) != len(e):
        raise ListasIncompatiblesError()
    
    n = len(x)
    
    opt = [0] * (n+1)
    x = [0] + x
    e = [0] + e

    for i in range(1,n+1):
        opt_i = 0
        for k in range(0,i):
            opt_parcial = opt[k] + min((e[(i-k)],x[(i)]))
            if opt_parcial > opt_i:
                opt_i = opt_parcial
                opt[i] = opt_i

    return opt

def obtener_estrategia_optima_ataque(opt, x, e):

    if len(x) != len(e):
        raise ListasIncompatiblesError()
    
    n = len(x)

    if n == 0:
        return []

    x = [0] + x
    e = [0] + e
    s = [ATACAR]
    tope = n

    for i in range(n,0,-1):
        if i > tope:
            continue
        opt_i = opt[i]
        for k in range(i-1,-1,-1):
            opt_candidato = opt[k] + min((e[(i-k)],x[(i)]))
            if opt_candidato == opt_i:
                if k > 0:
                    s = [ATACAR] + s
                tope = k
                break
            s = [CARGAR] + s

    if opt[-1] != calcular_cantidad_enemigos_eliminados(x[1:], e[1:], s):
        raise EstrategiaInoptimaError()

    return s
 
# def _calcular_cantidad_enemigos_eliminados(x, e, s):
#     enemigos_acumulados = 0
#     energia_acumulada = 0

#     for accion, arribo in zip(s, x):
#         if accion == CARGAR:
#             energia_acumulada += 1
#         elif accion == ATACAR:
#             enemigos_eliminados = min(arribo, e[energia_acumulada])
#             enemigos_acumulados += enemigos_eliminados
#             energia_acumulada = 0

#     return enemigos_acumulados

def g(s):
    return 1 if s == ATACAR else 0

def calcular_cantidad_enemigos_eliminados(x, e, s):

    if len(x) != len(e) or len(x) != len(s) or len(e) != len(s):
        raise ListasIncompatiblesError()

    n = len(x)
    cantidad_total_enemigos_eliminados = 0
    j = 0
    g_s = list(map(g, s))

    for i in range(n):

        cantidad_total_enemigos_eliminados += g_s[i] * min(x[i], e[j])

        if g_s[i] < 1:
            j += 1
        else:
            j = 0

    return cantidad_total_enemigos_eliminados 