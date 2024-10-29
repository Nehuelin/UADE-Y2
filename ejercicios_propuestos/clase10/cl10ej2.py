# Suponga que lo desafían a un partido del juego de los corchos pero con un número arbitrario de corchos (conocido de antemano) 
# y que le ofrecen la opción de comenzar el juego o hacer la segunda movida. 
# Diseñe una estrategia ganadora greedy.

def escabio_greedy(c: int, k: int):
    kplusone = k + 1
    if c % kplusone == 0:
        print("El jugador debe ir segundo")
        empezar = False
    else:
        print("El jugador debe empezar primero")
        empezar = True
    
    turnos_jugador = empezar
    corchos_restantes = c

    while corchos_restantes > 0:
        if turnos_jugador:
            quitar = corchos_restantes % kplusone
            if quitar == 0:
                quitar = 1
            corchos_restantes -= quitar
        else:
            quitar = min(1, corchos_restantes)
            corchos_restantes -= quitar
            
        turnos_jugador = not turnos_jugador
    
    if turnos_jugador:
        print("Min gano el juego")
    else:
        print("Max gano el juego")

jugador_ganador = escabio_greedy(11, 3)


# Estrategia :
# Divide el número de corchos N entre k+1 (donde k es el número máximo de corchos que se pueden tomar en cada turno).

# Decide si deseas ser el primer jugador o el segundo jugador:
# -> Si N es múltiplo de k+1 (es decir, N % (k+1) = 0), estás en una posición perdedora si empiezas. En este caso, debes elegir ser el segundo jugador para asegurar que tu oponente comience en la posición perdedora.
# -> Si N no es múltiplo de k+1, estás en una posición ganadora si empiezas. En este caso, debes elegir ser el primer jugador.

# Para mantener al oponente en una posicion perdedora:
# --> Si inicia el juego, quita una cantidad de corchos de tal manera que el número de corchos restantes sea un múltiplo de k+1. Esto garantiza que después de tu turno, el oponente siempre esté en una posición perdedora.
# --> En cada turno posterior, responde tomando la cantidad de corchos necesaria para devolver al oponente a una posición que sea un múltiplo de k+1 después de cada una de tus jugadas.