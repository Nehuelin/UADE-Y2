def puede_salir(M):
    m = len(M)
    n = len(M[0])
    
    L = [[False] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                L[i][j] = True
            elif M[i][j] == 0:
                if i == 0:
                    if M[i][j - 1] == 0:
                        L[i][j] = True
                elif j == 0:
                    if M[i - 1][j] == 0:
                        L[i][j] = True
                else:
                    if M[i][j - 1] == 0 or M[i - 1][j] == 0:
                        L[i][j] = True
    
    return L[m - 1][n - 1]
                    
M = [[0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]

print(puede_salir(M))
