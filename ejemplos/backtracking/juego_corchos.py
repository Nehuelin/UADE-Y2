def Escabio(e: int, n: int): # e -> estado, # n es 1 (MAX) o -1 (MIN)
    if e == 0:
        return n # si no hay mas turnos, el jugador de turno gana
    else:
        sig = 1 # siguiente jugadas
        val = -1 * n
        poda = False
        while sig <= 3 and sig <= e and not poda:
            e -= sig
            if n == 1:
                val = max(val, Escabio(e, -1 * n))
            else:
                val = min(val, Escabio(e, -1 * n))
            if n * val == 1: # es decir, si n = 1 y val = 1 o n = -1 y val = -1
                poda = True
            else:
                e += sig
            sig += 1
    
    return val

jugador_ganador = Escabio(11, 1)
if jugador_ganador == 1:
    print("MAX ganó la partida")
else:
    print("MIN ganó la partida")