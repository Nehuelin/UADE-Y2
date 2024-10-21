
# Una operación de merge múltiple. 
# Suponga que tiene k arreglos ordenados, cada uno con n elementos, y que usted quiere combinarlos en un único arreglo ordenado de kn elementos.
# --> 1) He aquí una estrategia: usando el procedimiento de merge que ya conocemos, combine los dos primeros arreglos, combine el resultado con el tercero, luego con el cuarto y así sucesivamente. 
# ¿Cuál es la complejidad temporal de este algoritmo en términos de k y n?
# --> 2) Dé un algoritmo más eficiente usando la técnica divide & conquer.
def merge_sort(u: list[int]):
    def merge_sort_r(u: list[int], ini: int, fin: int):
        def merge(u: list[int], ini: int, mid: int, fin: int):
            w = [0] * (fin - ini + 1)  
            i = ini
            j = mid + 1
            k = 0
            while i <= mid and j <= fin:
                if u[i] <= u[j]:
                    w[k] = u[i]
                    i += 1
                else:
                    w[k] = u[j]
                    j += 1
                k += 1
            while i <= mid:
                w[k] = u[i]
                i += 1
                k += 1
            while j <= fin:
                w[k] = u[j]
                j += 1
                k += 1
            for k in range(len(w)):
                u[ini + k] = w[k]
        
        if ini < fin:
            mid = (ini + fin) // 2
            merge_sort_r(u, ini, mid)
            merge_sort_r(u, mid + 1, fin)
            merge(u, ini, mid, fin)
    if len(u) > 1:
        merge_sort_r(u, 0, len(u) - 1)

def merge_k_arrays(k: list[list], ini: int, fin: int):
    def merge(u: list[int], ini: int, mid: int, fin: int):
        w = [0] * (fin - ini + 1)  
        i = ini
        j = mid + 1
        k = 0
        while i <= mid and j <= fin:
            if u[i] <= u[j]:
                w[k] = u[i]
                i += 1
            else:
                w[k] = u[j]
                j += 1
            k += 1
        while i <= mid:
            w[k] = u[i]
            i += 1
            k += 1
        while j <= fin:
            w[k] = u[j]
            j += 1
            k += 1
        for k in range(len(w)):
            u[ini + k] = w[k]

    if ini == fin:
        return k[ini]
    mid = (ini + fin) // 2
    mitad_izquierda = merge_k_arrays(k, ini, mid)
    mitad_derercha = merge_k_arrays(k, mid + 1, fin)
    return merge(mitad_izquierda, mitad_derercha)

k1 = [1, 6, 8, 9, 11]
k2 = [2, 3, 7, 10, 12]

k3 = k1 + k2

print(merge_sort(k3))
