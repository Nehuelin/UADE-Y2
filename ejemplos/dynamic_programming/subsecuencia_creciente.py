# Algoritmo para encontrar la subsecuencia creciente más larga en una secuencia de números
def lis(X):
    n = len(X)
    D = [[0 for i in range(n)] for j in range(2)]
    for i in range(n):
        D[0][i] = 1
        D[1][i] = -1
    for i in range(1, n):
        for j in range(i):
            if X[j] <= X[i] and D[0][j] + 1 >= D[0][i]:
                D[0][i] = D[0][j] + 1
                D[1][i] = j
    inx = D[0].index(max(D[0]))
    L = D[0][inx]
    Z = [0 for i in range(L)]
    Z[L-1] = X[inx]
    for i in range(L-2, -1, -1):
        Z[i] = X[D[1][inx]]
        inx = D[1][inx]
    return L, Z

X = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(X))  # (6, [10, 22, 33, 50, 60, 80])
