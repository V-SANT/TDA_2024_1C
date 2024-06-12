def validar_multiway_partition_problem(A, k, subconjuntos):

    def contar(conjunto):
        contador = {}
        for elemento in conjunto:
            contador[elemento] = contador.get(elemento, 0) + 1
        return contador

    if len(subconjuntos) != k:
        return False

    elementos_cubiertos = []
    
    suma_objetivo = sum(subconjuntos[0])

    for subconjunto in subconjuntos:
        suma = 0
        for elemento in subconjunto:
            if elemento not in A:
                return False
            elementos_cubiertos.append(elemento)
            suma += elemento

        if suma != suma_objetivo:
            return False

    return contar(A) == contar(elementos_cubiertos)
