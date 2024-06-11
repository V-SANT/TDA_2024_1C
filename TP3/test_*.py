from main import *
from constantes import *
from bt import *
from pl import *
from lectura_escritura import *
from validador_problema_mw import *
from validador_problema_ta import *

def calcular_suma_total(maestros, habilidades, grupos):
    dic_maestros = dict(zip(maestros, habilidades))

    suma_total = 0
    for grupo in grupos:
        suma_grupo = 0
        for maestro in grupo:
            suma_grupo += dic_maestros[maestro]
        suma_total += suma_grupo**2
    
    return suma_total

def test1_1_bt():
    maestros, habilidades, k =  leer_archivo(PRUEBA_1, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_bt(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1894340

def test2_1_pl():
    maestros, habilidades, k =  leer_archivo(PRUEBA_1, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_pl(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1894340

def test3_2_bt():
    maestros, habilidades, k =  leer_archivo(PRUEBA_2, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_bt(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1640690

def test4_2_pl():
    maestros, habilidades, k =  leer_archivo(PRUEBA_2, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_pl(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 1640690

def test5_3_bt():
    maestros, habilidades, k =  leer_archivo(PRUEBA_3, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_bt(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 807418

def test6_3_pl():
    maestros, habilidades, k =  leer_archivo(PRUEBA_3, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_pl(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 807418

def test7_4_bt():
    maestros, habilidades, k =  leer_archivo(PRUEBA_4, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_bt(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 4298131

def test8_4_pl():
    maestros, habilidades, k =  leer_archivo(PRUEBA_4, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_pl(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 4298131

def test9_5_bt():
    maestros, habilidades, k =  leer_archivo(PRUEBA_5, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_bt(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 385249

def test10_5_pl():
    maestros, habilidades, k =  leer_archivo(PRUEBA_5, CARPETA)
    grupos, coeficiente = p_opt_tribu_agua_pl(maestros, habilidades, k)
    suma_total = calcular_suma_total(maestros, habilidades, grupos)
    assert coeficiente == suma_total == 385249

def test11_validador_mw_no_se_cubren_todos_los_elementos():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
    assert not validar_multiway_partition_problem(A, k, subconjuntos)

def test12_validador_mw_elemento_no_pertenece_a_A():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
    assert not validar_multiway_partition_problem(A, k, subconjuntos)

def test13_validador_mw_elemento_se_encuentra_en_mas_conjuntos_de_los_que_deberia():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10]]
    assert not validar_multiway_partition_problem(A, k, subconjuntos)

def test14_validador_mw_suma_de_los_elementos_de_los_subconjuntos_no_es_igual():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    subconjuntos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
    assert not validar_multiway_partition_problem(A, k, subconjuntos)

def test15_validador_mw_caso_correcto():
    A = [1, 2, 3, 4, 5]
    k = 3
    subconjuntos = [[2, 3], [1,4], [5]]
    assert validar_multiway_partition_problem(A, k, subconjuntos)
    
def test_validar_problema_de_la_tribu_agua_no_se_cubren_todos_los_elementos():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 58
    S = [[1, 2], [3, 4]]
    assert not validar_problema_de_la_tribu_agua(X, k, B, S)

def test_validar_problema_de_la_tribu_agua_elemento_no_pertenece_a_X():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 178
    S = [[1, 2], [3, 4, 6]]
    assert not validar_problema_de_la_tribu_agua(X, k, B, S)

def test_validar_problema_de_la_tribu_agua_elemento_se_encuentra_en_mas_conjuntos_de_los_que_deberia():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 180
    S = [[1, 2, 3], [3, 4, 5]]
    assert not validar_problema_de_la_tribu_agua(X, k, B, S)

def test_validar_problema_de_la_tribu_agua_suma_de_los_elementos_de_los_subconjuntos_es_mayor_a_B():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 150
    S = [[1, 2], [3, 4, 5]]
    assert not validar_problema_de_la_tribu_agua(X, k, B, S)

def test_validar_problema_de_la_tribu_agua_suma_de_los_elementos_de_los_subconjuntos_es_igual_a_B():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 153
    S = [[1, 2], [3, 4, 5]]
    assert validar_problema_de_la_tribu_agua(X, k, B, S)

def test_validar_problema_de_la_tribu_agua_suma_de_los_elementos_de_los_subconjuntos_es_menor_a_B():
    X = [1, 2, 3, 4, 5]
    k = 2
    B = 155
    S = [[1, 2], [3, 4, 5]]
    assert validar_problema_de_la_tribu_agua(X, k, B, S)


