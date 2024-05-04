import re
from constantes_tp2 import *

def leer_archivo_prueba(ruta):
    with open(ruta) as file:
        file.readline()
        n = int(file.readline())
        arribos = [int(file.readline()) for _ in range(n)]
        valores_recarga = [int(file.readline()) for _ in range(n)]
        return arribos, valores_recarga

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