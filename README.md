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

## Tests
Para correr los tests es necesario contar con `pytest` y luego ejecutar sobre el directorio del proyecto: 

```
pytest -v
```