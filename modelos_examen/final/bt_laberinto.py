def puede_salir(M):
    m = len(M)
    n = len(M[0])
    
    visitado = [[False] * n for _ in range(m)]

    if M[0][0] == 0:  
        return backtrack(M, m, n, 0, 0, visitado)
    
    return False

def backtrack(M, m, n, i, j, visitado):
    if i == m - 1 and j == n - 1:
        return True
    
    visitado[i][j] = True

    if j + 1 < n and not visitado[i][j + 1] and M[i][j + 1] == 0:
        if backtrack(M, m, n, i, j + 1, visitado):
            return True

    if i + 1 < m and not visitado[i + 1][j] and M[i + 1][j] == 0:
        if backtrack(M, m, n, i + 1, j, visitado):
            return True
    
    visitado[i][j] = False
    return False


M = [[0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]

print(puede_salir(M))
