# Dado un conjunto de n cintas con ni registros ordenados en cada una de ellas, 
# se pretende mezclarlas de a pares hasta lograr una  única cinta ordenada. La 
# secuencia en la que se realiza la mezcla determinará la eficiencia del proceso. 
# Diseñar un algoritmo que busque la solución óptima minimizando el número de 
# movimientos. 
# Por ejemplo: 3 cintas: A con 30 registros, B con 20 y C con 10: 
# A. Mezclamos A con B (50 movimientos) y el resultado con C (60 
# movimientos), con lo que realizamos en total 110 movimientos. 
# B. Mezclamos C con B (30 Movimientos) y el resultado con A (60). Total 
# = 90 movimientos 

def minimizar_movimientos(C: list[tuple]):
    cintas_ordenadas = sorted(C, key=lambda c: c[1])
    accum = 0
    total_movimientos = 0
    for cinta in cintas_ordenadas:
        if cintas_ordenadas.index(cinta) == 0:
            accum = cinta[1]
        else:
            total_movimientos += accum + cinta[1]
            accum += cinta[1]

    return total_movimientos, cintas_ordenadas

C = [('A', 30), ('B', 20), ('C', 10)]

print(minimizar_movimientos(C))