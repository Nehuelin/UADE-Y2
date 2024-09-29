# Este algoritmo calcula la ruta más corta entre todos los pares de nodos en un grafo dirigido o no dirigido con pesos positivos o negativos, pero sin ciclos negativos.
def floyd_marshall(n, G):
    A = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k == 0:
                    A[k][i][j] = min(G[i][j], G[i][k]+G[k][j])
                else:
                    A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k]+A[k-1][k][j])
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = A[n-1][i][j]
    return M

# 1000 es el valor infinito
G = [[0, 1, 1000, 1], 
     [1, 0, 1, 1000], 
     [1000, 1, 0, 1], 
     [1, 1000, 1, 0]]

print(floyd_marshall(4, G))  # [[0, 1, 2, 1], [1, 0, 1, 2], [2, 1, 0, 1], [1, 2, 1, 0]]

