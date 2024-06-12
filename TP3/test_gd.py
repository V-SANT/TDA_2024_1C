from gd import *
from lectura_escritura import *
from constantes import *

def calcular_suma_total(maestros, habilidades, grupos):
    dic_maestros = dict(zip(maestros, habilidades))

    suma_total = 0
    for grupo in grupos:
        suma_grupo = 0
        for maestro in grupo:
            suma_grupo += dic_maestros[maestro]
        suma_total += suma_grupo**2
    
    return suma_total

def test_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_1, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1894340

def test2_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_2, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1640690

def test3_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_3, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 807418

def test4_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_4, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 4298131

def test5_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_5, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 385249

def test6_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_6, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 172295

def test7_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_7, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 2906564

def test8_gd():
    maestros, habilidades, k =  leer_archivo(PRUEBA_10, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_gd(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 355882