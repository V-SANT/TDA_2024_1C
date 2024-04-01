

def obtener_suma_ponderada(batallas):
    
    #Ordeno las batallas según relación entre su valor y el tiempo que tardan
    batallas_ordenadas =  sorted(batallas, key=lambda x: x[1]/x[0],reverse=True)
    
    suma_ponderada = 0
    suma_parcial = 0
    
    for batalla in batallas_ordenadas:
        suma_parcial += batalla[0]
        suma_ponderada += suma_parcial*batalla[1]

    return suma_ponderada

