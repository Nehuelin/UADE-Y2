# Dada una matriz cilindrica donde cada celda tiene un costo en forma de entero, diseñar un algoritmo que permita recorrerla de izquierda a derecha con el menor costo posible.
# Se pueden realizar uno de tres movimientos: 
# --> Derecha-Arriba
# --> Derecha
# --> Derecha-Abajo
# CONCEPTO: La matriz cilindrica es una matriz de n x m donde la primera columna y la última columna están unidas. 
# Por ejemplo, si la celda actual es (0, j) entonces la celda a la derecha arriba es (n-1, j+1).


def minimize_traverse_costs(M):
    acum = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    minimo2 = 9999
    coordenadas_minimo = []
    for j in range(len(M[0])):
        for i in range(len(M)):
            if j == 0:
                acum[i][j] = M[i][j]
            else:
                acum[i][j] = min(
                    acum[(i - 1) % len(M)][j - 1], # arriba
                    acum[(i) % len(M)][j - 1], # medio
                    acum[(i + 1) % len(M)][j - 1] # abajo
                    ) + M[i][j]
            if j == len(M[0]) - 1 and acum[i][j] < minimo2:
                minimo2 = acum[i][j]
                coordenadas = [i, j]
    
    i, j = coordenadas[0], coordenadas[1]
    camino = []
    index = [i, j]
    minimo = 9999
    
    while j >= 0:
        camino.append(index)
        if i == 0:
            if acum[i][j-1] < acum[i+1][j-1]:
              index = [i, j-1] 
            else:
              index = [i+1, j-1]
        elif i == len(M)-1:
            if acum[i-1][j-1] < acum[i][j-1]:
              index = [i-1, j-1]
            else:
              index = [i, j-1]
        else:
            if acum[i-1][j-1] < acum[i][j-1] and acum[i-1][j-1] < acum[i+1][j-1]:
              index = [i-1, j-1]
            elif acum[i][j-1] < acum[i-1][j-1] and acum[i][j-1] < acum[i+1][j-1]:
              index = [i, j-1]
            else:
              index = [i+1, j-1]
        j -= 1
    
    return minimo2, camino

M = [[1, 7, 3, 4, 5, 6],
     [4, 3, 6, 5, 1, 2],
     [2, 3, 3, 7, 4, 1],
     [6, 1, 3, 2, 1, 4]]
