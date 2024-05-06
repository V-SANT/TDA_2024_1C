from main import *
from ataques_optimos import *
from constantes_tp2 import *
from funciones_lectura import *
import time
import random

def test_ejemplo_catedra_1():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[0]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[0]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_2():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[1]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[1]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_3():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[2]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[2]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_4():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[3]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    s = obtener_estrategia_optima_ataque(valores_optimos, x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[3]][0])

def test_ejemplo_catedra_5():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[4]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[4]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_6():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[5]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[5]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_7():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[6]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[6]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_8():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[7]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[7]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_9():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[8]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[8]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_10():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[9]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[9]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_ejemplo_catedra_10():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[9]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    x, e = leer_archivo_prueba(ruta_archivo)
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[9]][0])
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_1_agresiva():
    x = [5,10]
    e = [3,4]
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    s = obtener_estrategia_optima_ataque(valores_optimos, x, e)
    assert (valores_optimos[-1] == 6)
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_2_conservadora():
    x = [5,10]
    e = [3,10]
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    s = obtener_estrategia_optima_ataque(valores_optimos, x, e)
    assert (valores_optimos[-1] == 10)
    assert (s == [CARGAR, ATACAR])

    
def test_grupo_3_e_bajos():
    # En este caso tenemos varios escenarios para llegar al optimal:
    # 1) Podriamos atacar siempre con 1
    # 2.a) Podriamos atacar, cargar y atacar
    # 2.b) Podriamos cargar, atcar y atacar
    # 3) Podriamos cargar,cargar y atacar
    x = [10, 20, 30]
    e = [1, 2, 3]
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == 3)  
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_4_llegadas_constantes():
    # En este caso ocurre lo mismo de tener varios casos posibles de ejecución
    x = [10, 10, 10, 10, 10]
    e = [5, 10, 15, 20, 25]
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    s = obtener_estrategia_optima_ataque(valores_optimos, x, e)
    assert (valores_optimos[-1] == 25)  
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_5_llegadas_fluctuantes():
    x = [5, 20, 5, 20, 5]
    e = [10, 15, 20, 25, 30]
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == 35)  
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_6_llegadas_decrecientes():
    x = [25, 20, 15, 10, 5]
    e = [5, 10, 15, 20, 25]
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == 25)  
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_7_llegadas_y_recargas_iguales():
    x = [5, 10, 15, 20, 25]
    e = [5, 10, 15, 20, 25]
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == 25) 
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s)) 

def test_grupo_8_ataque_nulo():
    x = []
    e = []
    s = obtener_estrategia_optima_ataque(obtener_valores_optimos_ataque(x, e), x, e)
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    assert (valores_optimos[-1] == 0)
    assert (valores_optimos[-1] == calcular_cantidad_enemigos_eliminados(x, e, s))

def test_grupo_11_calcular_cantidad_enemigos_eliminados():
    x = [5, 10, 15, 20, 25]
    e = [5, 10, 15, 20, 25]
    s = [CARGAR, ATACAR, ATACAR, ATACAR, ATACAR]
    assert (calcular_cantidad_enemigos_eliminados(x, e, s) == 25)

def test_grupo_9_excepcion_listas_incompatibles():
    x = [5, 10, 15, 20, 25]
    e = [5, 10, 15, 20]
    try:
        obtener_valores_optimos_ataque(x, e)
        assert False
    except ListasIncompatiblesError:
        assert True

def test_grupo_10_excepcion_estrategia_inoptima():
    x = [5, 10, 15, 20, 25]
    e = [5, 10, 15, 20, 25]
    valores_optimos = obtener_valores_optimos_ataque(x, e)
    valores_optimos[-1] -= 1
    try:
        obtener_estrategia_optima_ataque(valores_optimos, x, e)
        assert False
    except EstrategiaInoptimaError:
        assert True


        

