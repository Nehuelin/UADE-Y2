# Un mecánico necesita llevar a cabo n reparaciones urgentes conociendo el tiempo 
# que le va a llevar cada una de ellas, es decir, en la tarea i-ésima tardará ti 
# minutos.  Debido a que el pago que recibe el mecánico depende del nivel de 
# satisfacción del cliente, necesita decidir el orden en el que atenderá cada 
# reparación para minimizar el tiempo medio de espera de los clientes. 


def minimizar_tiempo_medio(T: list[tuple]):
    tiempos_ordenados = sorted(T, key=lambda t: t[1])

    tiempo_acumulado = 0
    tiempo_total = 0

    for tiempo in tiempos_ordenados:
        tiempo_acumulado += tiempo[1]
        tiempo_total += tiempo_acumulado

    tiempo_medio_espera = tiempo_total // len(tiempos_ordenados)

    return tiempo_medio_espera, tiempos_ordenados 

T = [(1, 4), (2, 5), (3, 2), (4, 7)]
print(minimizar_tiempo_medio(T))

