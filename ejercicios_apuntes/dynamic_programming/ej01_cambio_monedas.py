# Cambio de monedas: Dado un conjunto C de N tipos de monedas, cada una con 
# una denominación ci (1<=i<=n), con un número ilimitado de ejemplares de cada 
# tipo, se requiere determinar, si se puede, la cantidad mínima de ellas necesarias 
# para formar una cantidad M. Por ejemplo, un expendedor de boletos electrónico 
# dispone de monedas de distintos valores: $100, $25, $10, $5 y $1, si se tiene 
# que pagar $289, la mejor solución consiste en dar 10 monedas (2 de $100, 3
# de $25, 1 de $10 y 4 de $1). Otro ejemplo sería si se disponen de monedas 
# de $5, $4 y $1, y se quieren entregar $8, la mejor solución sería entregar 2 
# monedas de $4. Y si además de saber cuántas monedas se requieren en total, 
# se quisiera averiguar cuántas de cada denominación? 

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

d = [5, 4, 1]  
v = 8  
print(cambio(d, v))