import os
from constantes_tp2 import *
from ataques_optimos import ataques_optimos

def main():
    
    directorio_actual = os.getcwd()

    directorio_datos = directorio_actual + DIRECTORIO_DATOS

    for archivo in ARCHIVOS_DE_PRUEBA:
        with open(directorio_datos + archivo) as file:
            file.readline()
            n = int(file.readline())
            
            arrivos = []
            for i in range(n):
                arrivos.append(int(file.readline()))
            
            valores_recarga = []
            for i in range(n):
                valores_recarga.append(int(file.readline()))


            print(f"Maximo enemigos atacados en {archivo}: {ataques_optimos(n, arrivos, valores_recarga)}")

if __name__ == "__main__":
    main()