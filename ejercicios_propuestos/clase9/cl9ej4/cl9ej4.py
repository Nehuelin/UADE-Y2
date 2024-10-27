# Implemente un algoritmo de backtracking para encontrar todas las permutaciones de los cuatro dígitos (1,2,3,4) 
# de manera que ningún dígito quede repetido y que el valor absoluto de la diferencia entre un dígito cualqueira y su precedente sea a menor o igual a 2. 
# Simule el funcionamiento de su algoritmo mostrando el árbol de las permutaciones hasta encontrar la primera permutación que satisface las restricciones.

def hay_repetidos(lista: list):
    numeros = [n for n in lista if n is not None]
    return len(numeros) != len(set(numeros))

def cumple_diferencia(lista: int):
    numeros = [n for n in lista if n is not None]
    for i in range(1, len(numeros)):
        if abs(numeros[i] - numeros[i - 1]) > 2:
            return False
    return True

def encontrar_permutaciones(numeros: list[int]):
    permutacion = [0 for _ in range(len(numeros))]
    encontrar_permutaciones_rec(numeros, 0, permutacion)

def encontrar_permutaciones_rec(numeros: list[int], e, permutacion):
    if e == len(numeros):
        if not hay_repetidos(permutacion) and cumple_diferencia(permutacion):
            print(permutacion)
    else:
        for i in range(len(numeros)):
            permutacion[e] = numeros[i]
            encontrar_permutaciones_rec(numeros, e + 1, permutacion)

numeros = [1, 2, 3, 4]
encontrar_permutaciones(numeros)

