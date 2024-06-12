import os
import time
import argparse
from lectura_escritura import *
import bt
import pl 
import gd
from constantes import *

def main(filename, metodo, guardar):
    print("Archivo:", filename)
    maestros, habilidades, k = leer_archivo(filename,CARPETA)
    
    start_time = time.time()
    
    if metodo == PROGRAMACON_LINEAL:
        grupos, coeficiente = pl.p_opt_tribu_agua_pl(maestros, habilidades, k)
    elif metodo == BACKTRACKING:
        grupos, coeficiente = bt.p_opt_tribu_agua_bt(maestros, habilidades, k)
    elif metodo == GREEDY:
        grupos, coeficiente = gd.p_opt_tribu_agua_gd(maestros, habilidades, k)
    else:
        raise ValueError("Método {metodo} no reconocido. Use 'pl' para programación lineal, 'bt' para backtracking o 'gd' para greedy.")
    
    end_time = time.time()
    execution_time = end_time - start_time

    imprimir_resultado(execution_time, grupos, coeficiente)
    
    if guardar:
        guardar_resultados(filename, execution_time, grupos, coeficiente, metodo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analizar un archivo específico mediante un método indicado.")
    parser.add_argument('filename', type=str, help="El nombre del archivo que se desea analizar.")
    parser.add_argument('metodo', type=str, choices=['pl', 'bt', 'gd'], help="El método a utilizar: 'pl' para programación lineal, 'bt' para backtracking o 'gd' para greedy.")
    parser.add_argument('--guardar', action='store_true', help="Indica si se deben guardar los resultados en un archivo.")
    
    args = parser.parse_args()
    main(args.filename, args.metodo, args.guardar)

