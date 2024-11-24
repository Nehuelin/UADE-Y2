def mostrar_ternas(A: list[int], q: int):
    backtrack(A, [0 for _ in range(5)], 0, q, 0)

def backtrack(A, solucion: list, suma, q, e):
    for i in range(2):
        solucion[e] = i
        suma += A[e] * i
        if e == 4:
            if solucion.count(1) == 3:
                if suma < q:
                    print(solucion)
        else:
            if suma < q:
                backtrack(A, solucion, suma, q, e + 1)

A = [1, 4, 2, 5, 3]
mostrar_ternas(A, 9)