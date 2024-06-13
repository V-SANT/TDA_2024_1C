
def p_opt_tribu_agua_gd2(maestros, habilidades, k):
    suma_habilidades = sum(habilidades)
    habilidades_optimo = suma_habilidades / k
    tuplas_maestros = list(zip(maestros, habilidades)) 
    maestros_ordenados = sorted(tuplas_maestros, key=lambda x: x[1], reverse=True)

    grupos = [[] for _ in range(k)]
    suma_grupos = [0] * k
    indice_grupo = 0

    for maestro in maestros_ordenados:
        indice_grupo = indice_grupo % k
        if suma_grupos[indice_grupo] > habilidades_optimo:
            indice_grupo += 1
        grupos[indice_grupo].append(maestro[0])
        suma_grupos[indice_grupo] += maestro[1]
        indice_grupo += 1

    coeficiente = sum(x**2 for x in suma_grupos)

    return grupos, coeficiente
