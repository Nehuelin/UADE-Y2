# En el problema del cambio, complete el pseudo-código de manera que se pueda saber cuáles fueron las monedas usadas

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
    
    i = len(d) - 1
    j = v
    monedas = []
    while j > 0 and i >= 0:
        if i == 0:
            monedas.append(d[i])
            j -= d[i]
        elif M[i][j] == M[i - 1][j]:
            i -= 1
        else:
            monedas.append(d[i])
            j -= d[i]

    return M[len(d) - 1][v], monedas

d = [1, 3, 4]
v = 6
resultado, monedas_usadas = cambio(d, v)
print(f"El número mínimo de monedas para pagar ${v} es: {resultado}")
print(f"Las monedas usadas son: {monedas_usadas}")