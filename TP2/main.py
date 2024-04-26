import os
import csv
import re
from constantes_tp2 import *
from ataques_optimos import ataques_optimos

def obtener_rutas_archivos():
    directorio_actual = os.getcwd()
    directorio_datos = os.path.join(directorio_actual, DIRECTORIO_DATOS)
    resultados_esperados = os.path.join(directorio_datos, RESULTADOS_ESPERADOS)
    return directorio_datos, resultados_esperados

def leer_archivo_prueba(ruta):
    with open(ruta) as file:
        file.readline()
        n = int(file.readline())
        arribos = [int(file.readline()) for _ in range(n)]
        valores_recarga = [int(file.readline()) for _ in range(n)]
        return n, arribos, valores_recarga

def leer_resultados_esperados(ruta):
    resultados_esperados = {}
    with open(ruta) as file:
        contenido = file.read()
        matches = re.findall(PATRON, contenido)
        for match in matches:
            archivo = match[0]
            estrategia = [e.strip() for e in match[1].split(",")]
            cantidad = int(match[2])
            resultados_esperados[archivo] = (cantidad, estrategia)
    return resultados_esperados

def comparar_resultados(resultados_obtenidos, resultados_esperados):
    for archivo, resultado_obtenido in resultados_obtenidos.items():
        resultado_esperado = resultados_esperados.get(archivo)
        if resultado_obtenido != resultado_esperado:
            print(f"Prueba {archivo} fallida")
            print("Posiciones donde los resultados difieren:")
            for i, (esperado, obtenido) in enumerate(zip(resultado_esperado[1], resultado_obtenido[1])):
                if esperado != obtenido:
                    print(f"Posición {i}: Esperado: {esperado}, Obtenido: {obtenido}")
            print("\n")
            print("╔═════════════════════════════════════╗")
            print("║             (X) ¡Falló!              ║")
            print("╚═════════════════════════════════════╝\n")
        else:
            print(f"Prueba {archivo} exitosa")
            print("╔═════════════════════════════════════╗")
            print("║              \o/ ¡Éxito!             ║")
            print("╚═════════════════════════════════════╝\n")


def main():
    directorio_datos, ruta_resultados_esperados = obtener_rutas_archivos()
    resultados_obtenidos = {}

    for archivo in ARCHIVOS_DE_PRUEBA:
        ruta_archivo = os.path.join(directorio_datos, archivo)
        ruta_archivo_completa = os.getcwd() + "/" + ruta_archivo
        n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo_completa)
        resultado = ataques_optimos(n, arribos, valores_recarga)
        resultados_obtenidos[archivo] = resultado

    ruta_resultados_esperados_completa = os.getcwd() + ruta_resultados_esperados
    print(ruta_resultados_esperados_completa)

    resultados_esperados = leer_resultados_esperados(ruta_resultados_esperados_completa)

    comparar_resultados(resultados_obtenidos, resultados_esperados)

if __name__ == "__main__":
    main()
