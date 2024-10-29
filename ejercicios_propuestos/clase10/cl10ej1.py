# En el juego de Nim dos participantes se turnan para sacar objetos de varios grupos o pilas. 
# En cada movida, un participante debe sacar por lo menos un objeto, aunque puede retirar tantos como quiera siempre que sean todos del mismo grupo.
# El jugador que toma el último objeto gana el juego. 
# Escriba un programa que determine qué jugador gana el juego de Nim game de la figura. 
# Los grupos están dispuestos horizontalmente.

def es_fin_del_juego(pilas):
    return all(pila == 0 for pila in pilas)

def evaluar():
    return -1

def movimientos_posibles(pilas):
    movimientos = []
    for i, cantidad in enumerate(pilas):
        for quitar in range(1, cantidad + 1):
            nuevo_estado = pilas[:]
            nuevo_estado[i] -= quitar
            movimientos.append(nuevo_estado)
    return movimientos

def minmax(pilas, es_max):
    if es_fin_del_juego(pilas):
        return evaluar()

    if es_max:
        mejor_valor = float('-inf')
        for movimiento in movimientos_posibles(pilas):
            valor = minmax(movimiento, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for movimiento in movimientos_posibles(pilas):
            valor = minmax(movimiento, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

if __name__ == "__main__":
    estado_inicial = [1, 3, 5, 7]
    resultado = minmax(estado_inicial, es_max=True)
    if resultado == 1:
        print("El jugador MAX tiene una estrategia ganadora.")
    else:
        print("El jugador MIN puede forzar una derrota de MAX.")