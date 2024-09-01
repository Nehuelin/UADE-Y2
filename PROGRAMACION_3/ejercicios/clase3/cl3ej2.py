# Se le da un arreglo infinito A en el que las primeras n posiciones contienen enteros ordenados y el resto de las posiciones contienen ∞.
# Usted no conoce el valor de n. 
# Describa un algoritmo que recibe como entrada un entero x y encuentra la posición del arreglo que contiene a x, si tal posición existe, en tiempo O(log n).
# Si la idea de un arreglo infinito no es de su agrado, puede asumir como opción que el arreglo tiene longitud n, 
# pero usted no conoce este valor (ni cuenta, por supuesto, con un método que se lo devuelva) y que la 
# implementación del arreglo en su lenguaje de programación devuelve el mensaje de error ∞ siempre que se trata de acceder a un elemento A[i] con i > n.
# Ayuda: puede buscar inspiración en la estrategia del ejercicio anterior.

def generar_lista_infinita(A: list):
    for i in range(10000):
        A.append("∞")

def encontrar_entero(A: list, x: int):
    def definir_rango(A: list, i: int) -> int:
        if A[i + 1] == "∞":
            return i
        else:
            if A[i] == "∞":
                definir_rango(A, i - 1)

            else:
                return definir_rango(A, i*2)

    def encontrar_entero_r(A: list, x: int, ini: int, fin: int):
        if ini == fin:
            if A[ini] == x:
                return ini
            else: 
                return None
        
        mid = (fin + ini) // 2

        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return encontrar_entero_r(A, x, ini, mid - 1)
        else:
            return encontrar_entero_r(A, x, mid + 1, fin)
        
    fin = definir_rango(A, 1)
    return encontrar_entero_r(A, x, 0, fin)




lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
generar_lista_infinita(lista)
print(encontrar_entero(lista, 0))

