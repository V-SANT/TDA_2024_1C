from main import obtener_datos
from tp1_greedy import obtener_suma_ponderada

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

def ejemplo_grupo_tp_1():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/100000.txt')) == 728684685661017

def ejemplo_grupo_tp_2():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/100000.txt')) == 728684685661017

def ejemplo_grupo_tp_3():
    assert obtener_suma_ponderada(obtener_datos('./archivos_pruebas_tp1/100000.txt')) == 728684685661017

