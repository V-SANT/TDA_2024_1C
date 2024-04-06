def obtener_ratio_batalla(batalla):
    tiempo_batalla, peso_batalla = batalla
    return peso_batalla / tiempo_batalla

def obtener_suma_ponderada(batallas):
    regla = lambda batalla: obtener_ratio_batalla(batalla)
    batallas_ordenadas = sorted(batallas, key=regla, reverse=True)
    
    suma_ponderada = 0
    suma_parcial = 0
    
    for batalla in batallas_ordenadas:
        tiempo_batalla,peso_batalla = batalla
        suma_parcial += tiempo_batalla
        suma_ponderada += suma_parcial*peso_batalla

    return suma_ponderada

def obtener_batallas_ordenadas(batallas):
    regla = lambda batalla: obtener_ratio_batalla(batalla)
    return sorted(batallas, key=regla, reverse=True)

#------------------------------------------------------------
def obtener_peso_batalla(batalla):
    _, peso_batalla = batalla
    return peso_batalla

def obtener_suma_ponderada_por_peso(batallas):
    regla = lambda batalla: obtener_peso_batalla(batalla)
    batallas_ordenadas = sorted(batallas, key=regla, reverse=True)
    
    suma_ponderada = 0
    suma_parcial = 0
    
    for batalla in batallas_ordenadas:
        tiempo_batalla,peso_batalla = batalla
        suma_parcial += tiempo_batalla
        suma_ponderada += suma_parcial*peso_batalla

    return suma_ponderada

def obtener_batallas_ordenadas_por_peso(batallas):
    regla = lambda batalla: obtener_peso_batalla(batalla)
    return sorted(batallas, key=regla, reverse=True)

#-------------------------------------------------------------
def obtener_tiempo_batalla(batalla):
    tiempo_batalla, _ = batalla
    return tiempo_batalla

def obtener_suma_ponderada_por_tiempo(batallas):
    regla = lambda batalla: obtener_tiempo_batalla(batalla)
    batallas_ordenadas = sorted(batallas, key=regla)
    
    suma_ponderada = 0
    suma_parcial = 0
    
    for batalla in batallas_ordenadas:
        tiempo_batalla,peso_batalla = batalla
        suma_parcial += tiempo_batalla
        suma_ponderada += suma_parcial*peso_batalla

    return suma_ponderada

def obtener_batallas_ordenadas_por_tiempo(batallas):
    regla = lambda batalla: obtener_tiempo_batalla(batalla)
    return sorted(batallas, key=regla)



