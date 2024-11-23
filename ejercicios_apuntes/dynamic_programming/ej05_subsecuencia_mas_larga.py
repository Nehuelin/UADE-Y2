# Dada una secuencia X={x1 x2 ... xm}, 
# decimos que Z={z1 z2 ... zk} es una subsecuencia de X (siendo k  m) si existe 
# una secuencia creciente {i1 i2 ... ik} de índices de X tales que para todo j = 1, 2, ..., 
# k tenemos xij = zj. 
# Por ejemplo, Z={BCDB} es una subsecuencia de X={ABCBDAB} con la 
# correspondiente secuencia de índices {2,3,5,7}. 
# Dadas dos secuencias X e Y, decimos que Z es una subsecuencia común de X 
# e Y si es subsecuencia de X y subsecuencia de Y.  
# Se desea encontrar la longitud de la subsecuencia de longitud máxima común a 
# dos secuencias dadas. Y si además se quisiera encontrar la subsecuencia 
# propiamente dicha?

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

    print(M)
    return M[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y)) 
