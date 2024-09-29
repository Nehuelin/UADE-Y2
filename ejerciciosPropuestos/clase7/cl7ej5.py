# La permutación de n elementos tomados de a k se refiere al proceso de acomodar k elementos de un conjunto de n para formar una secuencia. 
# El coeficiente de permutaciones P(n,k) nos da el número de secuencias que podemos obtener tomando k elementos de un conjunto de n.
# Este coeficiente está dado por la fórmula P(n, k) = n!/(n − k)!

# EJEMPLO: Si n = 4 y k = 2 entonces P(4, 2) = 24/2 = 12, pues tenemos doce maneras de formar pares en un conjunto de cuatro elementos.
# Si A = {a, b, c, d}, podemos formar los pares (a, b), (b, a), (a, c), (c, a), (a, d), (d, a), (b, c), (c, b), (b, d), (d, b), (c, d) y (d, c).

# El coeficiente P(n, k) se puede computar a partir de resultados ya obtenidos para números menores: P(n, k) = P(n − 1, k) + k·P(n − 1, k − 1)
# Además tenemos los casos base: 
# --> Si k > n entonces P(n, k) = 0, 
# --> Si k = n entonces P(n, k) = P(n, n) = n!
# --> Si k = 0 entonces P(n, k) = P(0, 0) = 1

# Con esta información, se pide definir una estrategia de programación dinámica para encontrar P(n, k) dados n y k.

import numpy as np
import math

def permutaciones(n, k):
    P = np.zeros((n+1, k+1), int)
    for i in range(n+1):
        for j in range(k+1):
            if j > i:
                P[i][j] = 0
            elif j == i:
                P[i][j] = math.factorial(i)
            elif j == 0:
                P[i][j] = 1
            else:
                P[i][j] = P[i-1][j] + j * P[i-1][j-1]
    return P[n][k]

n = 4
k = 2
print(f"El numero de permutaciones de {n} elementos tomados de a {k} es: {permutaciones(n, k)}")