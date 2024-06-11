def validar_problema_de_la_tribu_agua(X,k,B,S):
    
    def contar(conjunto):
        contador = {}
        for elemento in conjunto:
            contador[elemento] = contador.get(elemento, 0) + 1
        return contador

    if len(S) != k:
        return False
    
    suma_total = 0
    fuerzas_cubiertas = []

    for s in S:
        suma_s = 0
        for fuerza in s:
            if fuerza not in X:
                return False
            fuerzas_cubiertas.append(fuerza)
            suma_s += fuerza
        suma_total += suma_s**2

    return contar(X) == contar(fuerzas_cubiertas) and suma_total <= B