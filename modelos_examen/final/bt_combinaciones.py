# q = cantidad de elementos
# n = rango de 0 a n

def combinaciones(n, q):
    lista = [0 for _ in range(q)]
    combinaciones_rec(lista, n, 0)

def combinaciones_rec(lista, n, e):
    if e == len(lista):
        if not repetidos(lista):
            print(lista)
    else:
        for i in range(n + 1):
            lista[e] = i
            combinaciones_rec(lista, n, e + 1)

def repetidos(lista: list[int]):
    return len(lista) != len(set(lista))

combinaciones(4, 3)