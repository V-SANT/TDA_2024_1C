DIRECTORIO_DATOS = '/archivos_pruebas/'
RESULTADOS_ESPERADOS = 'Resultados Esperados.txt'

ARCHIVOS_DE_PRUEBA = [
    '5.txt',
    '10.txt',
    '10_bis.txt',
    '20.txt',
    '50.txt',
    '100.txt',
    '200.txt',
    '500.txt',
    '1000.txt',
    '5000.txt',
]

ARCHIVOS_5 = ['5.txt']

CARGAR = 'Cargar'
ATACAR = 'Atacar'

PATRON = r"(\d+_?\w*\.txt)\nEstrategia: (.+)\nCantidad de tropas eliminadas: (\d+)"


MENSAJE_ERROR_LISTAS_INCOMPATIBLES = "Las listas de arribos y valores de recarga deben tener el mismo tamaño"
class ListasIncompatiblesError(Exception):
    def __init__(self):
        self.mensaje = MENSAJE_ERROR_LISTAS_INCOMPATIBLES
        super().__init__(MENSAJE_ERROR_LISTAS_INCOMPATIBLES)



MENSAJE_ERROR_ESTRATEGIA_INOPTIMA= "La estrategia generada no coincide con la cantidad optima de enemigos eliminados"
class EstrategiaInoptimaError(Exception):
    def __init__(self):
        self.mensaje = MENSAJE_ERROR_ESTRATEGIA_INOPTIMA
        super().__init__(MENSAJE_ERROR_ESTRATEGIA_INOPTIMA)