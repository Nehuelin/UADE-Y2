# Considere 5 objetos con pesos (w1,w2,...,w5) = (10,3,5,7,2) y una mochila de tamaño m = 15. 
# Use una estrategia de backtracking para encontrar todas las combinaciones de objetos que caben exactamente en la mochila. 
# Calcule la complejidad de este método.

def mostrar(lista, combinacion):
    resultado = []
    for i in range(len(lista)):
        if combinacion[i] != 0:
            resultado.append(combinacion[i])
    print(resultado)

def encontrar_combinaciones(objetos: list[int], tamaño: int):
    combinacion = [0 for _ in range(len(objetos))]
    encontrar_combinaciones_rec(objetos, tamaño, 0, 0, combinacion)

def encontrar_combinaciones_rec(objetos, tamaño, e, suma, combinacion_actual):
    for i in range(2):
        combinacion_actual[e] = i
        suma += objetos[e]*i
        if e == len(objetos) - 1 or suma == tamaño:
            if suma == tamaño:
                mostrar(objetos, combinacion_actual)
        else:
            if suma <= tamaño:
                encontrar_combinaciones_rec(objetos, tamaño, e + 1, suma, combinacion_actual)

                
def mostrar(v, solucion):
    combinacion = [v[i] for i in range(len(v)) if solucion[i] == 1]
    print("Combinación:", combinacion)

objetos = [10, 3, 5, 7, 2]

tamaño = 15

lista = encontrar_combinaciones(objetos, tamaño)