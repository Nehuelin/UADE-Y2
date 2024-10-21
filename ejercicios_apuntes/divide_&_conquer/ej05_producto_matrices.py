# Dadas dos matrices cuadradas M1 y M2 de NxN, calcular el producto de ambas, donde N es una potencia de 2. 

class Matriz:
    def __init__(self, m: list[list[int]]):
        self.m = m
        self.n = len(m)
    
    def __str__(self):
        s = ''
        for i in range(self.n):
            s += str(self.m[i]) + '\n'
        return s

def productoMatrices(m1: Matriz, m2: Matriz) -> Matriz:
    if m1.n == 1:
        return Matriz([[m1.m[0][0] * m2.m[0][0]]])
    else:
        m1a, m1b, m1c, m1d = dividirMatriz(m1)
        m2a, m2b, m2c, m2d = dividirMatriz(m2)
        p1 = productoMatrices(Matriz(sumaMatrices(m1a, m1d)), Matriz(sumaMatrices(m2a, m2d)))
        p2 = productoMatrices(Matriz(sumaMatrices(m1c, m1d)), m2a)
        p3 = productoMatrices(m1a, Matriz(restaMatrices(m2b, m2d)))
        p4 = productoMatrices(m1d, Matriz(restaMatrices(m2c, m2a)))
        p5 = productoMatrices(Matriz(sumaMatrices(m1a, m1b)), m2d)
        p6 = productoMatrices(Matriz(restaMatrices(m1c, m1a)), Matriz(sumaMatrices(m2a, m2b)))
        p7 = productoMatrices(Matriz(restaMatrices(m1b, m1d)), Matriz(sumaMatrices(m2c, m2d)))
        c1 = Matriz(sumaMatrices(restaMatrices(sumaMatrices(p1.m, p4.m), p5.m), p7.m))
        c2 = Matriz(sumaMatrices(p3.m, p5.m))
        c3 = Matriz(sumaMatrices(p2.m, p4.m))
        c4 = Matriz(sumaMatrices(sumaMatrices(restaMatrices(p1.m, p2.m), p3.m), p6.m))
        return unirMatriz(c1, c2, c3, c4)

def dividirMatriz(m: Matriz) -> tuple[list[list[int]]]:
    n = m.n
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    for i in range(n//2):
        m1.append(m.m[i][:n//2])
        m2.append(m.m[i][n//2:])
        m3.append(m.m[i + n//2][:n//2])
        m4.append(m.m[i + n//2][n//2:])
    return m1, m2, m3, m4

def sumaMatrices(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    n = len(m1)
    suma = []
    for i in range(n):
        suma.append([m1[i][j] + m2[i][j] for j in range(n)])
    return suma

def restaMatrices(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    n = len(m1)
    resta = []
    for i in range(n):
        resta.append([m1[i][j] - m2[i][j] for j in range(n)])
    return resta

def unirMatriz(m1: Matriz, m2: Matriz, m3: Matriz, m4: Matriz) -> Matriz:
    n = m1.n
    m = []
    for i in range(n):
        m.append(m1.m[i] + m2.m[i])
    for i in range(n):
        m.append(m3.m[i] + m4.m[i])
    return Matriz(m)

# Test
m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
print(productoMatrices(m1, m2)) # [[19, 22], [43, 50]]