def cambio(d, v):
    M = [[float('inf')] * (v + 1) for _ in range(len(d))]
    for i in range(len(d)):
        M[i][0] = 0

    for i in range(len(d)):
        for j in range(1, v + 1):
            if i == 0:
                if d[i] > j:
                    M[i][j] = float('inf') 
                else:
                    M[i][j] = M[i][j - d[i]] + 1
            else:
                if d[i] > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = min(M[i - 1][j], M[i][j - d[i]] + 1)

    return M[len(d) - 1][v]

d = [1, 3, 4]  
v = 6  
resultado = cambio(d, v)
print(f"El número mínimo de monedas para pagar ${v} es: {resultado}")