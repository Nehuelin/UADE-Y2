# El triángulo de Tartaglia. O de Pascal. O de Yang Hui. 
# El coeficiente binomial C(n,k) da el coeficiente de la potencia k de x en el polinomio (1 + x)^n. 
# Por ejemplo: C(4,3) = 4 porque (1 + x)^4 = 1+4x +6x^2 +4x^3 +x^4.
# Describa una estrategia de programación dinámica para encontrar C(n,k) a partir de dos valores n y k dados. 
# Observe que C(n,k) puede ser computado a partir de resultados previos: C(n,k) = C(n−1,k −1)+C(n−1,k)

import numpy as np

def coeficiente_binomial(n, k):
    M = np.zeros((n+1, k+1), dtype=int)
    for i in range(n+1):
        for j in range(k+1):
            if (j == 0 or i == j):
                M[i][j] = 1
            else:
                M[i][j] = M[i-1][j-1] + M[i-1][j]
    print(M)
    return M[n][k]
    
n = 4
k = 3

print(coeficiente_binomial(n, k))

