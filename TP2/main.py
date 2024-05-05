import sys
from constantes_tp2 import *
from ataques_optimos import obtener_valores_optimos_ataque, obtener_estrategia_optima_ataque
from funciones_lectura import leer_archivo_prueba

def main():
    ruta_archivo = sys.argv[1]
    arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimos = obtener_valores_optimos_ataque(arribos, valores_recarga)
    solucion = obtener_estrategia_optima_ataque(optimos, arribos, valores_recarga)
    print(f"Cantidad de enemigos eliminados: {optimos[-1]}")
    print(f"Estrategia seguida: {solucion}")

if __name__ == "__main__":
    main()
