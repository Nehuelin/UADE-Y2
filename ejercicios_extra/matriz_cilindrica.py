# Dada una matriz cilindrica donde cada celda tiene un costo en forma de entero, diseñar un algoritmo que permita recorrerla de izquierda a derecha con el menor costo posible.
# Se pueden realizar uno de tres movimientos: 
# --> Derecha-Arriba
# --> Derecha
# --> Derecha-Abajo
# CONCEPTO: La matriz cilindrica es una matriz de n x m donde la primera columna y la última columna están unidas. 
# Por ejemplo, si la celda actual es (0, j) entonces la celda a la derecha arriba es (n-1, j+1).


def minimize_traverse_costs(M):
    
    ...

M = [[1, 7, 3, 4, 5, 6],
     [4, 3, 6, 5, 1, 2],
     [2, 3, 3, 7, 4, 1],
     [6, 1, 3, 2, 1, 4]]