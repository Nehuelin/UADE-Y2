# ¿Qué cambiaría en el juego de los 11 corchos si el ganador fuera quien retira el último corcho?

# RESPUESTA:
# Si el ganador fuera el que retira el ultimo corcho, entonces la estrategia ganadora seria NO iniciar el primer turno.

def Escabio(e: int, n: int): # e -> estado, # n es 1 (MAX) o -1 (MIN)
    if e == 0:
        return n 
    else:
        sig = 1 
        val = -1 * n
        poda = False
        while sig <= 3 and sig <= e and not poda:
            e -= sig
            if n == 1:
                val = min(val, Escabio(e, -1 * n))
            else:
                val = max(val, Escabio(e, -1 * n))
            if n * val == 1:
                poda = True
            else:
                e += sig
            sig += 1
    
    return val

jugador_ganador = Escabio(11, -1)
if jugador_ganador == 1:
    print("MAX ganó la partida")
else:
    print("MIN ganó la partida")