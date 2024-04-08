import sys
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
    path = sys.argv[1]
    
    # Obtener las batallas del archivo
    datos_batallas = obtener_datos(path)
    
    print("---------------------------------------------------------------")
    print(f"Iniciando cálculo de la suma ponderada para el archivo {path}")

    inicio_tiempo = time.time()  # Iniciar medición de tiempo

    suma_ponderada = obtener_suma_ponderada(datos_batallas)

    fin_tiempo = time.time()  # Finalizar medición de tiempo
    tiempo_total = fin_tiempo - inicio_tiempo  # Calcular tiempo total

    print(f"La suma ponderada de las batallas es: {suma_ponderada}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

    # Escribir el orden de las batallas en un archivo
    with open("orden_batallas.txt", "w") as archivo:
        for batalla in obtener_batallas_ordenadas(datos_batallas):
            archivo.write(f"{batalla}\n")

if __name__ == "__main__":
    main()
