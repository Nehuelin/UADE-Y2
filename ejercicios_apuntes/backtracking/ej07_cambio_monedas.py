# Dado un conjunto C de N tipos de monedas con un número 
# ilimitado de ejemplares de cada tipo, se requiere formar, si se puede, una 
# cantidad M empleando el mínimo número de ellas. 

def cambio_minimo(C: list, m):
    solucion = [0 for _ in range(len(C))]
    mejor_solucion = []
    minimo_monedas = backtrack(C, m, solucion, 0, mejor_solucion, None, 0)
    return minimo_monedas, mejor_solucion


def backtrack(C, m, solucion_actual, suma, mejor_solucion, minimo, e):
    for i in range(len(C)):
        solucion_actual[e] = C[i]
        suma += C[i]
        if e == len(C) - 1 or suma == m:  
            if suma == m:
                if minimo is None or e + 1 < minimo:
                    minimo = e + 1  
                    mejor_solucion[:] = solucion_actual[:e + 1]  
        elif suma < m:  
            minimo = backtrack(C, m, solucion_actual, suma, mejor_solucion, minimo, e + 1)  
    
        suma -= C[i]

    return minimo


C = [6, 4, 2, 1]
M = 8
minimo_monedas, mejor_solucion = cambio_minimo(C, M)

print(f"Mínimo número de monedas: {minimo_monedas}")
print(f"Combinación óptima: {mejor_solucion}")


