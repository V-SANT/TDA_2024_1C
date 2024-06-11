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

# TEST

# Caso 1: El conjunto A no cubre todos los elementos

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
print(validar_multiway_partition_problem(A, k, subconjuntos))

# Caso 2: Un elemento no pertenece al conjunto A
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
print(validar_multiway_partition_problem(A, k, subconjuntos))

# Caso 3: Un elemento se encuentra en más conjuntos de los que debería
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10]]
print(validar_multiway_partition_problem(A, k, subconjuntos))

# Caso 4: La suma de los elementos de los subconjuntos no es igual
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
print(validar_multiway_partition_problem(A, k, subconjuntos))

# Caso 5: Caso correcto
A = [1, 2, 3, 4, 5]
k = 3
subconjuntos = [[2, 3], [1,4], [5]]
print(validar_multiway_partition_problem(A, k, subconjuntos))