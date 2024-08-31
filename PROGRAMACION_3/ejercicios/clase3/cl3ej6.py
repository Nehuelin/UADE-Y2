# Dado un arreglo ordenado con números todos diferentes A[0..n − 1], usted quiere encontrar si existe un índice i tal que A[i] = i. 
# Dé un algoritmo divide & conquer que resuelva este problema en tiempo O(log n).

def encontrar_coincidencia(A: list[int]):
    def encontrar_coincidencia_r(A: list[int], ini: int, fin: int):
        if ini == fin:
            return ini
        
        mid = (ini + fin) // 2

        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            return encontrar_coincidencia_r(A, ini, mid - 1)
        else:
            return encontrar_coincidencia_r(A, mid + 1, fin)

    return encontrar_coincidencia_r(A, 0, len(A) - 1)

lista = [0, 2, 4, 6, 8, 9, 10]
print(encontrar_coincidencia(lista))