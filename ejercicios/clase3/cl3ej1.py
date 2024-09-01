from typing import Callable

# En este ejercicio consideramos una función monótonamente decreciente f : N → Z.
# Esto es, una función definida sobre los números naturales que devuelve valores enteros, de manera que es f (i) ≥ f (i + 1)). 
# Asumiendo que podemos evaluar f en cualquier punto i en tiempo constante, queremos encontrar n = min{i ∈ N|f (i) ≤ 0}. 
# En otras palabras, queremos encontrar el valor en el que f se vuelve negativa.
# Por supuesto, es posible resolver el problema en tiempo O(n) evaluando f (1), f (2), f (3), . . . f (n). 
# Describa un algoritmo que lo resuelva en O(log n).
# Ayuda: evalúe f en O(log n) valores x ≤ n cuidadosamente elegidos y tal vez en algún valores entre n y 2n — pero tenga en cuenta que usted no conoce el valor n inicialmente.

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
   
    
f = lambda x: -x // 2

print(encontrar_minimo(f))
