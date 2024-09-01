# Suponga que nos dan un arreglo A[0..n-1] ordenado de enteros que ha sido desplazado circularmente k posiciones hacia la derecha. 
# Por ejemplo, [35, 42, 5, 15, 27, 29] es un arreglo ordenado desplazado circularmente k = 2 posiciones, 
# mientras que [27, 29, 35, 42, 5, 15] ha sido desplazado k = 4 posiciones; 
# [1, 3, 5, 6, 7, 15] ha sido desplazado k = 0.
# Queremos encontrar el mayor elemento del arreglo en A. 
# Obviamente, podemos encontrarlo en tiempo O(n). 
# Describa un algoritmo que resuelva el problema en tiempo O(log n).

def rotar_derecha(A: list[int], k: int):
    k = k % len(A)
    return A[-k:] + A[:-k]

def encontrar_mayor(A: list[int]):
    def encontrar_mayor_r(A: list[int], ini: int, fin: int):
        if ini == fin:
            return A[ini]
        
        if fin - ini == 1:
            if A[ini] > A[fin]:
                return A[ini]
            else:
                return A[fin]
        
        mid = (fin + ini) // 2

        if A[mid] < A[mid + 1] and A[mid] > A[ini]:
            return encontrar_mayor_r(A, mid + 1, fin)
        else:
            return encontrar_mayor_r(A, ini, mid)
    
    return encontrar_mayor_r(A, 0, len(A) - 1)

lista = [5, 15, 27, 29, 35, 42, 50, 69, 420, 700]
rotada = rotar_derecha(lista, 5)
print(f"El mayor elemento en la lista es {encontrar_mayor(rotada)}")
