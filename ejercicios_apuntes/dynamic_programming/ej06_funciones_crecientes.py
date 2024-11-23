# Dadas n funciones f1, f2, ..., fn y un entero positivo M, deseamos maximizar la 
# función f1(x1) + f2(x2) + ... + fn(xn) sujeta a la restricción x1 +x2 + ... + xn 
# = M, donde fi(0) = 0 (i=1,..,n), xi son números naturales, y todas las 
# funciones son monótonas crecientes, es decir, x  
# y implica que fi(x) > fi(y). 
# Supóngase que los valores de cada función se almacenan en un vector.

import math

# Definición de funciones monótonamente crecientes
def f1(n):
    return n

def f2(n):
    return n**2

def f3(n):
    return n**3

def f4(n):
    return 2**n

def f5(n):
    return math.log2(n) if n > 0 else None 

def f6(n):
    return 3**n

def f7(n):
    return 5*n**4 + 3*n**2

def f8(n):
    return math.sqrt(n) if n >= 0 else None  

def f9(n):
    return math.floor(n)

def f10(n):
    return math.log(n) if n > 0 else None  

def maximizar_funciones_monotonamente_crecientes(funciones, M):
    n = len(funciones)
    valores = [[funciones[i](j) for j in range(M+1)] for i in range(n)]
    print(valores)
    dp = [[0 for _ in range(M+1)] for _ in range(n)]
    for i in range(n):
        for j in range(1, M+1):
            dp[i][j] = max(dp[i][j-1], valores[i][j])
    for i in range(1, n):
        for j in range(1, M+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
    print(dp)
    return dp[n-1][M]

funciones_monotonamente_crecientes = [f1, f2, f3]

M = 5
print(maximizar_funciones_monotonamente_crecientes(funciones_monotonamente_crecientes, M))  # Output: 55
