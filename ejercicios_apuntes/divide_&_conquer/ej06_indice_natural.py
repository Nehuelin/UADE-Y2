# Sea A[1..n], n ≥ 1, un vector de enteros diferentes y ordenados crecientemente, tal 
# que algunos de los valores pueden ser negativos. Diseñar un algoritmo que 
# devuelva un índice natural k, 1 ≤ k ≤ n, tal que A[k] = k, siempre que tal índice 
# exista. 

def encontrar_indice_natural(A: list[int], ini: int, fin: int):
    if ini == fin:
        if A[ini] == ini:
            return A[ini]
        else:
            return -1
    
    if ini > fin:
        return -1

    mid = (ini + fin) // 2

    if A[mid] == mid:
        return mid
    elif A[mid] > mid:
        return encontrar_indice_natural(A, ini, mid - 1)
    else:
        return encontrar_indice_natural(A, mid + 1, fin)

A = [0, 2, 3, 4, 5, 6, 7, 8, 18, 25, 34]

print(encontrar_indice_natural(A, 0, len(A) - 1))
# vos sabes que si A[k] > k, entonces no vas a encontrar A[k] = k en k > mid