# Cambio de monedas: Dado un conjunto C de N tipos de monedas con un número 
# ilimitado de ejemplares de cada tipo, se requiere formar, si se puede, una 
# cantidad M empleando el mínimo número de ellas. Por ejemplo, un cajero 
# automático dispone de billetes de distintos valores: $100, $25, $10, $5 y $1, si 
# se tiene que pagar $289, la mejor solución consiste en dar 10 billetes: 2 de 
# $100, 3 de $25, 1 de $10 y 4 de $1. 

def cambio(C: list[int], M: int):
    solucion = []
    i = 0
    while i < len(C) and M != 0:
        if C[i] > M:
            i += 1
        elif M - C[i] >= 0:
            solucion.append(C[i])
            M -= C[i]

    return solucion



C = [100, 25, 10, 5, 1]

solucion = cambio(C, 0)
print(len(solucion), solucion)