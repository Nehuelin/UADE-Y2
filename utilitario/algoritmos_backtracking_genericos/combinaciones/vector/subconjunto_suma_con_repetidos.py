# Dado un conjunto C de N tipos de monedas con un número 
# ilimitado de ejemplares de cada tipo, se requiere formar, si se puede, una 
# cantidad M empleando el mínimo número de ellas. 

def cambio_minimo(C: list, m):
    solucion = [0 for _ in range(100)]
    backtrack(C, m, solucion, 0, 0)


def backtrack(C, m, solucion, suma, e):
    for i in range(len(C)):
        solucion[e] = C[i]
        suma += C[i]
        if suma == m:  
            if suma == m:
                mostrar(solucion)
        elif suma < m:  
            backtrack(C, m, solucion, suma, e + 1)  
    
        suma -= C[i]

def mostrar(solucion):
    lista = solucion[:]
    for i in range(solucion.count(0)):
        lista.remove(0)
    print(lista)

C = [6, 4, 2, 1]
M = 8
cambio_minimo(C, M)

