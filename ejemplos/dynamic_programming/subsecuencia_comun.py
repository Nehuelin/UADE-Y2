# Algoritmo para encontrar la subsecuencia común más larga entre dos secuencias de caracteres

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    M = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                M[i][j] = 0
            else:
                if X[i-1] == Y[j-1]:
                    M[i][j] = M[i-1][j-1] + 1
                else:
                    M[i][j] = max(M[i-1][j], M[i][j-1])
    return M[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))  # 4