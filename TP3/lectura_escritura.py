import os

def leer_archivo(archivo,ruta):
    maestros = []
    habilidades = []
    file_path = os.path.join(ruta, archivo)
    with open(file_path) as file:
        file.readline()
        k = int(file.readline())
        lines = file.readlines()
        for line in lines:
            nombre, habilidad = line.strip().split(", ")
            maestros.append(nombre)
            habilidades.append(int(habilidad))
    return maestros,habilidades, k


def imprimir_resultado(execution_time, grupos, coeficiente):
    print("Tiempo de ejecucion:", execution_time, "seconds")
    print("Grupos óptimos")
    for index, grupo in enumerate(grupos):
        print("Grupo", index+1, ":", grupo)
    print("Coeficiente:", coeficiente)


def guardar_resultados(archivo, execution_time, grupos, coeficiente, metodo):
    with open(f'resultados_{metodo}.txt', 'a') as f:
        f.write(f"Archivo: {archivo}\n")
        f.write(f"Execution time: {execution_time} seconds\n")
        f.write("Grupos óptimos\n")
        for index, grupo in enumerate(grupos):
            f.write(f"Grupo {index+1}: {grupo}\n")
        f.write(f"Coeficiente: {coeficiente}\n\n")