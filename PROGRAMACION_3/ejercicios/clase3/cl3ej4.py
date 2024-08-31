from typing import Callable

# Una variante del ejercicio 1. Muestre que si el decrecimiento de la función es estricto, 
# es decir si f (i) > f (i + 1)), entonces el problema se puede resolver más sencillamente.

def encontrar_minimo(f: Callable[[int], int]):
    def encontrar_rango(i: int) -> int:
        if f(i) <= 0 and i == 1:
            return f(i), i
        elif f(i) <= 0 and i != 1:
            return i/2, i
        else:
            return encontrar_rango(i*2)

    def encontrar_minimo_r(f, ini: int, fin: int) -> int:
        if ini == fin:
            return ini
        
        mid = (fin + ini) // 2

        if f(mid) == 0:
            return mid + 1
        elif f(mid) > 0:
            return encontrar_minimo_r(f, mid + 1, fin)
        else:
            return encontrar_minimo_r(f, ini, mid)

    ini, fin = encontrar_rango(1)
    return encontrar_minimo_r(f, ini, fin)
   
    
f = lambda x: -2*x + 5

print(encontrar_minimo(f))


