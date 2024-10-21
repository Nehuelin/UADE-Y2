# Determinar si una secuencia de numeros esta ordenada

def estaOrdenada(v: list[int]) -> bool:
    if len(v) == 1:
        return True
    else:
        return v[0] <= v[1] and estaOrdenada(v[1:])

# Test
v = [1, 2, 3, 4, 5]
print(estaOrdenada(v)) # True
