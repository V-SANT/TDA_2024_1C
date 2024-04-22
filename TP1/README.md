# TP1: Algoritmos Greedy en la Nación del Fuego

## Instrucciones para ejecutar

Para ejecutar el codigo hay que pasarle un archivo txt que contengan el tiempo de las batallas y el peso de la misma de la siguiente forma: 

| $t_i$ | $b_i$ |
|-------|-------|
|  53   |  100  |
|  61   |  152  |
|  68   |  120  |
|  68   |  245  |

Y luego ejecutar lo siguiente

```
python main.py <<path>>
```

Para mejor entendimiento, el orden en el que se ejecutan las batallas es guardado en un archivo llamado `orden_batallas.txt` el cual se puede consultar una vez ejecutado el programa

## Tests
Para correr los tests es necesario contar con `pytest` y luego ejecutar sobre el directorio del proyecto: 

```
pytest -v
```