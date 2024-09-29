# Analice si es posible extender el algoritmo de Dijkstra para que muestre los caminos de costo mínimo
# (además de los costos mínimos) utilizado una estrategia similar a la del problema de la subsecuencia creciente más larga.

def dijkstra(n, G, s):
    D = [1000 for i in range(n)]
    P = [-1 for i in range(n)]
    D[s] = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] != 1000:
                if D[j] > D[i] + G[i][j]:
                    D[j] = D[i] + G[i][j]
                    P[j] = i
    return D, P

def dijkstra_path(n, G, s):
    D = [1000 for i in range(n)]
    P = [-1 for i in range(n)]
    D[s] = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] != 1000:
                if D[j] > D[i] + G[i][j]:
                    D[j] = D[i] + G[i][j]
                    P[j] = i
    return D, P

def path(P, s, t):
    if t == s:
        return [s]
    else:
        return path(P, s, P[t]) + [t]
    
# 1000 es el valor infinito
G = [[0, 1, 1000, 1], 
     [1, 0, 1, 1000], 
     [1000, 1, 0, 1], 
     [1, 1000, 1, 0]]

D, P = dijkstra(4, G, 0)
print(D)  # [0, 1, 2, 1]
print(P)  # [-1, 0, 1, 0]

print(path(P, 0, 3))  # [0, 1, 2, 3]
print(path(P, 0, 2))  # [0, 1, 2]
print(path(P, 0, 1))  # [0, 1]
print(path(P, 0, 0))  # [0]