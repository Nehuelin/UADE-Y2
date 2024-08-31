# Encuentre un esquema de prueba para el algoritmo greedy del problema del cambio en el caso de las frutillas

def cambio(v: int):
    n = 0 
    accum = 0 
    i = 0
    coins = [500, 200, 100, 50, 20, 10, 5, 1]
    while accum < v and i < len(coins):
        if accum + coins[i] <= v:
            accum += coins[i]
            n += 1 
        else:
            i += 1 
    if (i < len(coins)):
        return n 
    else:
        return -1 
    
print(cambio(878)) 