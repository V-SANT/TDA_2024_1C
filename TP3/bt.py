import os
from constantes import *
import time

def calcular_coeficiente(sumas):
    return sum(suma**2 for suma in sumas)

def indices_ordenados_por_valor(arreglo):
    tuplas_indice_valor = list(enumerate(arreglo))
    # Ordenar las tuplas por valor 
    tuplas_ordenadas = sorted(tuplas_indice_valor, key=lambda x: x[1])
    # Extraer solo los índices
    indices_ordenados = [tupla[0] for tupla in tuplas_ordenadas]
    return indices_ordenados

def buscar_optimo_tribu_agua_bt(maestros, habilidades, k, grupos, sumas, index, mejor_solucion):
    # Hasta que no hayamos ubicado el último maestro no es una solución final
    if index == len(maestros):
        coeficiente_actual = calcular_coeficiente(sumas)
        if coeficiente_actual < mejor_solucion[0]:
            # Sobreescribo mi mejor solucion con todos los maestros asignados
            mejor_solucion[0] = coeficiente_actual
            # Pongo como quedaría mi mejor solución
            mejor_solucion[1] = [list(grupo) for grupo in grupos]
        # Siempre voy a querer retornear para que se sigan calculando las otras opciones
        return

    # Asignamos al grupo con menor habilidad acumulada
    for i in indices_ordenados_por_valor(sumas):
        if index == 0 and i >= 1:
            break
        
        # Evitar combinaciones redundantes explorando solo un subconjunto si las sumas son iguales
        if index > 0 and any(sumas[i] == sumas[j] for j in range(i)):
            continue

        # Me quedo con un maestro de mi lista de maestros
        maestro = maestros[index]
        habilidad = habilidades[index]

        # Sumo la habilidad del maestro al grupo que estoy analizando
        sumas[i] += habilidad
        
        # Si el coeficiente de mis grupos todavia puede ser una opcion (es menor a mi mejor solución) sigo armando esta solución
        if calcular_coeficiente(sumas) < mejor_solucion[0]:
            # Lo sumo en el grupo que estoy analizando
            grupos[i].append(maestro)
            # Llamo recursivamente
            buscar_optimo_tribu_agua_bt(maestros, habilidades, k, grupos, sumas, index + 1, mejor_solucion)
            # El maestro que acabo de poner en el grupo i lo saco 
            grupos[i].pop()

        # Acá llego en 2 casos:
        # 1. Ya no puedo seguir armando esta solución porque ya no me conviene
        # 2. Ya llegué a una solución final y ahora queda desarmarla de a poco y seguir probando otras opciones
        
        # La suma del grupo i le resto el maestro que acabo de sacar
        sumas[i] -= habilidad
        # En la proxima iteración si hay otro grupo disponible voy a poner el maestro en ese grupo

def p_opt_tribu_agua_bt(maestros, habilidades, k):
    # Emparejar los maestros con sus habilidades y ordenar por habilidad
    pares_ordenados = sorted(zip(maestros, habilidades), key=lambda x: x[1], reverse=True)
    # Desempaquetar los pares ordenados de nuevo en dos listas
    maestros, habilidades = zip(*pares_ordenados)
    # En mi mejor solución almaceno el coeficiente y los grupos
    mejor_solucion = [float('inf'), None]    
    # Almacenamos los nombres de los grupos
    grupos = [[] for _ in range(k)]    
    # Almacenamos la suma de los grupos para no volver a recularlas
    sumas = [0] * k
    buscar_optimo_tribu_agua_bt(maestros, habilidades, k, grupos, sumas, 0, mejor_solucion)
    return mejor_solucion[1], mejor_solucion[0]

