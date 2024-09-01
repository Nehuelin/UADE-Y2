# Una variante del ejercicio 2. 
# Se le da un arreglo infinito A en el que las primeras n posiciones contienen números enteros en cualquier orden 
# y el resto de las posiciones contienen ∞. 
# Encuentre el número n en tiempo O(log n)

def generar_lista_infinita(A: list):
    for i in range(10000):
        A.append("∞")


def encontrar_ultima_posicion(A: list):
    def definir_rango(A: list, i: int):
        if A[i] == "∞":
            return i
        else: 
            return definir_rango(A, i*2)
    
    def encontrar_ultima_posicion_r(A: list, ini: int, fin: int) -> int:
        if ini == fin:
            return ini
        
        mid = (fin + ini) // 2

        if A[mid] != "∞" and A[mid + 1] == "∞":
            return mid
        elif A[mid] != "∞" and A[mid + 1] != "∞":
            return encontrar_ultima_posicion_r(A, mid + 1, fin)
        else: 
            return encontrar_ultima_posicion_r(A, ini, mid - 1)
        
    fin = definir_rango(A, 1)
    return encontrar_ultima_posicion_r(A, 0, fin)

lista = [1, 5, 8, 9]
generar_lista_infinita(lista)
print(f"La posicion n en la lista es {encontrar_ultima_posicion(lista)}")