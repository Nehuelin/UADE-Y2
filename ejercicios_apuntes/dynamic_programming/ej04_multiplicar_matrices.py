# Multiplicación de matrices: Sea M = M1 x M2 x … x Mn una multiplicación encadenada 
# de matrices de dimensiones conocidas. Como la multiplicación es asociativa, hay 
# varias maneras de resolver secuencias de productos matriciales. Se desea conocer 
# la menor cantidad posible de multiplicaciones necesarias para resolver el problema. 
# Dadas dos matrices M1 y M2 de dimensiones m1xm2 y m2xm3 respectivamente, la 
# cantidad necesaria de multiplicaciones es m1xm2xn3. Y si además quisiéramos 
# determinar las asociaciones necesarias? 

def minimizar_multiplicaciones(V: list[int]):
    n = len(V) - 1
    M = [[None] * (n) for _ in range(n)]
    for i in range(n, 0, -1):
        for j in range(i, n):
            M[i][j] = 0
            for k in range(j-1):
                if M[i][j] > 0:
                    if M[i][k] + M[k+1][j] + (V[i-1]*V[k]*V[j]) < M[i][j]:
                        M[i][j] = M[i][k] + M[k+1][j] + (V[i-1]*V[k]*V[j])
                else:
                    M[i][j] = M[i][k] + M[k+1][j] + (V[i-1]*V[k]*V[j])
    print(M)
    return M[0][n-1]

print(minimizar_multiplicaciones([4, 1, 5, 3, 6]))