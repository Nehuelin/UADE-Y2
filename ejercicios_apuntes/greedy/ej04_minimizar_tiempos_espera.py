# Minimizar tiempo de espera: Un procesador debe atender n procesos. Se conoce 
# de antemano el tiempo que necesita cada uno de ellos. Determinar en qué orden 
# el procesador debe atender dichos procesos para minimizar la suma del tiempo que 
# los procesos están en el sistema.

def minimizar_tiempos(P: list[tuple]):
    procesos_ordenados = sorted(P, key=lambda proceso: proceso[1])
    total = 0
    suma_anteriores = 0
    for i in range(len(P)):
        total += suma_anteriores + procesos_ordenados[i][1]
        suma_anteriores += procesos_ordenados[i][1]
    
    return total, procesos_ordenados


P = [(1, 5), (2, 10), (3, 3)]
print(minimizar_tiempos(P))