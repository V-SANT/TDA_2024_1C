import os
import csv
import time
from tp1_greedy import *
from constantes import *

def obtener_datos(ruta):
    datos = []
    with open(ruta) as archivo:
        lineas = csv.reader(archivo)
        header = True
        for linea in lineas:
            if header:
                header = False
            else:
                dato = (int(linea[0]), int(linea[1]))
                datos.append(dato)
    return datos 

def main():
    # Obtener la ruta de los datos de las batallas
    ruta_directorio = os.getcwd()

    for archivo in ARCHIVOS_DE_PRUEBA:
        ruta_datos = ruta_directorio + archivo

        datos_batallas = obtener_datos(ruta_datos)
        
        print("---------------------------------------------------------------")
        print(f"Iniciando cálculo de la suma ponderada para el archivo {archivo}")

        inicio_tiempo = time.time()  # Iniciar medición de tiempo

        suma_ponderada = obtener_suma_ponderada(datos_batallas)

        fin_tiempo = time.time()  # Finalizar medición de tiempo
        tiempo_total = fin_tiempo - inicio_tiempo  # Calcular tiempo total

        print(f"La suma ponderada de las batallas es: {suma_ponderada}")
        print(f"Tiempo de ejecución: {tiempo_total} segundos")


if __name__ == "__main__":
    main()
