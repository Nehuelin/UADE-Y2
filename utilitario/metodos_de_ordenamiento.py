# vvvvvvvvvvvvvvvvvvvvvvv ITERATIVOS INEFICIENTES vvvvvvvvvvvvvvvvvvvvvvv
def bubble_sort(u: list[int]):
    for i in range(len(u) - 1, -1, -1):
        for j in range(i):
            if u[i] < u[j]:
                aux = u[i]
                u[i] = u[j]
                u[j] = aux

def insertion(u: list[int]):
    for i in range(1, len(u)):
        for j in range(i, 0, -1):
            if u[j] < u[j - 1]:
                aux = u[j - 1]
                u[j - 1] = u[j]
                u[j] = aux


# vvvvvvvvvvvvvvvvvvvvvv RECURSIVOS EFICIENTES vvvvvvvvvvvvvvvvvvvvvvvv
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

    


def quick_sort(u: list[int]):
    def quick_sort_r(u: list[int], ini: int, fin: int):
        def pivot(u: list[int], ini: int, fin: int):
            p = u[ini]
            i = ini + 1
            j = fin
            while True:
                while i <= j and u[i] <= p:
                    i += 1
                while i <= j and u[j] > p:
                    j -= 1
                if i < j:
                    u[i], u[j] = u[j], u[i]
                else:
                    break
            u[ini], u[j] = u[j], u[ini]
            return j
        
        if ini < fin:
            p = pivot(u, ini, fin)
            quick_sort_r(u, ini, p - 1)
            quick_sort_r(u, p + 1, fin)
    if len(u) > 1:
        quick_sort_r(u, 0, len(u) - 1)




test = [1, 2, 9, 7, 5, 6]

merge_sort(test)
print(test)