from main import obtener_datos
from tp1_greedy import *

def test_ejemplo_catedra_1():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/10.txt')) == 309600

def test_ejemplo_catedra_2():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/50.txt')) == 5218700

def test_ejemplo_catedra_3():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/100.txt')) == 780025365

def test_ejemplo_catedra_4():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/1000.txt')) == 74329021942

def test_ejemplo_catedra_5():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/5000.txt')) == 1830026958236

def test_ejemplo_catedra_6():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/10000.txt')) == 7245315862869

def test_ejemplo_catedra_7():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/100000.txt')) == 728684685661017

def test_grupo_1():
    # Todos con el mismo peso deberia ejecutarse las de menor duracion al principio
    batallas = [(3, 1), (2, 1), (4, 1)]
    assert obtener_batallas_ordenadas(batallas) == [(2, 1), (3, 1), (4, 1)]
    assert obtener_suma_ponderada(batallas) == 16

def test_grupo_2():
    # Al tener distintos pesos ahora usamos la relacion de peso/tiempo. En caso de igualdad da lo mismo cual se ejecuta
    batallas = [(3, 3), (2, 1), (4, 2)] 
    assert obtener_batallas_ordenadas(batallas) == [(3, 3), (2, 1), (4, 2)]
    assert obtener_suma_ponderada(batallas) == 32

def test_grupo_3():
    # En este caso el orden de las batallas seran: b2,b3,b1
    batallas = [(5, 1), (3, 5), (4, 3)]
    assert obtener_batallas_ordenadas(batallas) == [(3, 5), (4, 3), (5, 1)]
    assert obtener_suma_ponderada(batallas) == 48

def test_grupo_4():
    batallas = [(2, 5), (3, 9), (4, 11)] 
    assert obtener_batallas_ordenadas(batallas) == [(3, 9), (4, 11), (2, 5)]
    assert obtener_suma_ponderada(batallas) == 149

    assert obtener_batallas_ordenadas_por_peso(batallas) == [(4, 11), (3, 9), (2, 5)]
    assert obtener_suma_ponderada_por_peso(batallas) == 152
    
    assert obtener_batallas_ordenadas_por_tiempo(batallas) == [(2, 5), (3, 9), (4, 11)]
    assert obtener_suma_ponderada_por_tiempo(batallas) == 154

def test_grupo_5():
    batallas = [(5, 2), (9, 3), (11, 4)]  
    assert obtener_suma_ponderada(batallas) == 149
    assert obtener_batallas_ordenadas(batallas) == [(5, 2), (11, 4), (9, 3)]

    assert obtener_suma_ponderada_por_peso(batallas) == 154
    assert obtener_batallas_ordenadas_por_peso(batallas) == [(11, 4), (9, 3), (5, 2)]
    
    assert obtener_suma_ponderada_por_tiempo(batallas) == 152
    assert obtener_batallas_ordenadas_por_tiempo(batallas) == [(5, 2), (9, 3), (11, 4)]
    

