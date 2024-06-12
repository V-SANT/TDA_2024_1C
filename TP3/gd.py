def insertar_ordenado(grupos, grupo_minimo):
    grupos_aux = []
    encontrado = False

    for grupo in grupos:
        if grupo_minimo[1]**2 <= grupo[1]**2 and not encontrado:
            grupos_aux.append(grupo_minimo)
            encontrado = True
        grupos_aux.append(grupo)
    
    if not encontrado:
        grupos_aux.append(grupo_minimo)

    return grupos_aux

def p_opt_tribu_agua_gd(maestros, habilidades, k):
    tuplas_maestros = list(zip(maestros, habilidades))
    maestros_ordenados = sorted(tuplas_maestros, key=lambda x: x[1], reverse=True)

    grupos = [([], 0) for _ in range(k)]

    for maestro in maestros_ordenados:
        grupo_minimo = grupos.pop(0)
        nuevo_valor = grupo_minimo[1] + maestro[1]
        maestros_grupo = grupo_minimo[0] + [maestro[0]]
        grupo_minimo = (maestros_grupo, nuevo_valor)

        grupos = insertar_ordenado(grupos, grupo_minimo)
        
    grupos_finales = [x[0] for x in grupos]
    coeficiente = sum(x[1]**2 for x in grupos)

    print("grupos finales:", grupos_finales)

    return grupos_finales, coeficiente


