from main import *
from ataques_optimos import *
from constantes_tp2 import *

def test_ejemplo_catedra_1():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[0]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[0]][0])

def test_ejemplo_catedra_2():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[1]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[1]][0])

def test_ejemplo_catedra_3():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[2]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[2]][0])

def test_ejemplo_catedra_4():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[3]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[3]][0])

def test_ejemplo_catedra_5():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[4]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[4]][0])

def test_ejemplo_catedra_6():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[5]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[5]][0])

def test_ejemplo_catedra_7():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[6]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[6]][0])

def test_ejemplo_catedra_8():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[7]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[7]][0])

def test_ejemplo_catedra_9():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[8]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[8]][0])

def test_ejemplo_catedra_10():
    ruta_archivo = './archivos_pruebas/'+ARCHIVOS_DE_PRUEBA[9]
    ruta_resultados = './archivos_pruebas/'+RESULTADOS_ESPERADOS
    n, arribos, valores_recarga = leer_archivo_prueba(ruta_archivo)
    resultado = ataques_optimos(n, arribos, valores_recarga)
    assert (resultado[0] == leer_resultados_esperados(ruta_resultados)[ARCHIVOS_DE_PRUEBA[9]][0])

    
