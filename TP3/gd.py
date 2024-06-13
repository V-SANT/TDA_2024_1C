
def insertar_ordenado(grupos, grupo_minimo):
    def valor_cuadrado(grupo):
        return grupo[1]**2
    
    def busqueda_binaria(grupos, grupo_minimo):
        valor_minimo = valor_cuadrado(grupo_minimo)
        izquierda, derecha = 0, len(grupos)
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            if valor_cuadrado(grupos[medio]) < valor_minimo:
                izquierda = medio + 1
            else:
                derecha = medio
        return izquierda
    
    posicion = busqueda_binaria(grupos, grupo_minimo)
    grupos.insert(posicion, grupo_minimo)
    
    return grupos



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

    return grupos_finales, coeficiente
