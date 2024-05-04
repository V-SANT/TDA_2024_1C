from main import *
from ataques_optimos import *
from constantes_tp2 import *
import time

def test_ejemplo_catedra_1():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[0]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    inicio_tiempo = time.time()  # Iniciar medición de tiempo
    optimo = ataques_optimos(n, arribos, valores_recarga)
    fin_tiempo = time.time()  # Finalizar medición de tiempo
    print(fin_tiempo - inicio_tiempo)  # Calcular tiempo total
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[0]][0])

def test_ejemplo_catedra_2():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[1]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[1]][0])

def test_ejemplo_catedra_3():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[2]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[2]][0])

def test_ejemplo_catedra_4():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[3]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[3]][0])

def test_ejemplo_catedra_5():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[4]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[4]][0])

def test_ejemplo_catedra_6():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[5]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[5]][0])

def test_ejemplo_catedra_7():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[6]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[6]][0])

def test_ejemplo_catedra_8():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[7]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[7]][0])

def test_ejemplo_catedra_9():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[8]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[8]][0])

def test_ejemplo_catedra_10():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[9]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[9]][0])

def test_ejemplo_catedra_10():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[9]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[9]][0])

def test_grupo_1_agrasiva():
    n = 2
    arribos = [5,10]
    valores_recarga = [3,4]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 6)

def test_grupo_2_conservadora():
    n = 2
    arribos = [5,10]
    valores_recarga = [3,10]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 10)
    
def test_grupo_3_valores_recarga_bajos():
    # En este caso tenemos varios escenarios para llegar al optimal:
    # 1) Podriamos atacar siempre con 1
    # 2.a) Podriamos atacar, cargar y atacar
    # 2.b) Podriamos cargar, atcar y atacar
    # 3) Podriamos cargar,cargar y atacar
    n = 3
    arribos = [10, 20, 30]
    valores_recarga = [1, 2, 3]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 3)  

def test_grupo_4_llegadas_constantes():
    # En este caso ocurre lo mismo de tener varios casos posibles de ejecución
    n = 5
    arribos = [10, 10, 10, 10, 10]
    valores_recarga = [5, 10, 15, 20, 25]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 25)  

def test_grupo_5_llegadas_fluctuantes():
    n = 5
    arribos = [5, 20, 5, 20, 5]
    valores_recarga = [10, 15, 20, 25, 30]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 35)  

def test_grupo_6_llegadas_decrecientes():
    n = 5
    arribos = [25, 20, 15, 10, 5]
    valores_recarga = [5, 10, 15, 20, 25]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 25)  

def test_grupo_7_llegadas_y_recargas_iguales():
    n = 5
    arribos = [5, 10, 15, 20, 25]
    valores_recarga = [5, 10, 15, 20, 25]
    optimo = ataques_optimos(n, arribos, valores_recarga)
    assert (optimo[-1] == 25)  

