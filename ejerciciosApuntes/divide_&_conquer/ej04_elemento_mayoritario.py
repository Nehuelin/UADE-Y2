# Dado un vector A de números enteros, calcular elemento mayoritario. Si se tiene 
# un vector A de n enteros, un elemento x se denomina mayoritario de A si x
# aparece en el vector A más de n/2 veces. Considerar que no puede haber más 
# de un elemento mayoritario.

class obj:
    def __init__(self, r: bool, n: int, c: int, x: int):
        self.r = r # es cantidato?
        self.n = n # cantidad de elementos en la lista
        self.c = c # cantidad de elementos x en la lista
        self.x = x # elemento a ser investigado

def pseudo_m(u: list[int], i: int, j: int)-> obj:
    if i == j:
        return obj(True, 1, 1, u[i])
    else:
        o1 = pseudo_m(u, i, (i + j)//2)
        o2 = pseudo_m(u, (i + j)//2 + 1, j)
    if not o1.r and not o2.r:
        return obj(False, o1.n + o2.n, 0, 0)
    elif o1.r and not o2.r:
        return obj(True, o1.n + o2.n, o1.c + o2.n//2, o1.x)
    elif not o1.r and o2.r:
        return obj(True, o1.n + o2.n, o2.c + o1.n//2, o2.x)
    elif o1.r and o2.r:
        if o1.x == o2.x:
            return obj(True, o1.n + o2.n, o1.c + o2.c, o1.x)
        elif o1.c > o2.c:
            return obj(True, o1.n + o2.n, o1.c - o2.c, o1.x)
        elif o1.c < o2.c:
            return obj(True, o1.n + o2.n, o2.c - o1.c, o2.x)
        elif o1.n < o2.n:
            return obj(True, o1.n + o2.n, o1.c + o2.n // 2, o1.x)
        elif o1.n > o2.n:
            return obj(True, o1.n + o2.n, o2.c + o1.n // 2, o2.x)
        else:
            return obj(False, o1.n + o2.n, 0, 0)

def m(u: list[int]):
    o = pseudo_m(u, 0, len(u) - 1)
    if not o.r:
        return -99
    elif majority(u, o.x):
        return o.x
    else:
        return -99

def majority(u: list[int], x: int):
    c = 0
    for i in range(len(u)):
        if x == u[i]:
            c += 1
    return True if c > len(u)//2 else False

a = [5,5,6,6,6,6,6,6,6,1,1,1]
print(m(a))

