# Escriba un algoritmo de backtracking con poda para encontrar todas las permutaciones de los cuatro caracteres (A,B,C,D) de manera que satisfagan las siguientes restricciones:
#  Restricción (1): no debe haber repeticiones.
#  Restricción (2): la diferencia en el valor absoluto del código ASCII entre cada carácter y el previo debe ser siempre mayor o igual a 2.
#  Muestre el árbol de permutaciones para encontrar todas las que satisfagan las restricciones. 
# ¿Cuántas respuestas se obtienen? ¿Cuántas se obtendrían si sólo se tuviera la restricción (1)?

def hay_repetidos(lista: list):
    caracteres = [c for c in lista if c is not None]
    return len(caracteres) != len(set(caracteres))

def cumple_diferencia(lista: int):
    caracteres = [c for c in lista if c is not None]
    for i in range(1, len(caracteres)):
        if abs(ord(caracteres[i]) - ord(caracteres[i - 1])) < 2:
            return False
    return True

def encontrar_permutaciones(caracteres: list[str]):
    permutacion = [None for _ in range(len(caracteres))]
    encontrar_permutaciones_rec(caracteres, 0, permutacion)

def encontrar_permutaciones_rec(caracteres: list[str], e: int, permutacion: list[str]):
    if e == len(caracteres):
        if not hay_repetidos(permutacion) and cumple_diferencia(permutacion):
            print(permutacion)
    else:
        for i in range(len(caracteres)):
            permutacion[e] = caracteres[i]
            encontrar_permutaciones_rec(caracteres, e + 1, permutacion)
                

caracteres = ['A', 'B', 'C', 'D']
encontrar_permutaciones(caracteres)

# RESPUESTAS:
# Se obtienen dos permutaciones: [BDAC] y [CADB]. 
# Si se quitara la restriccion 2, se obtendrian 24 permutaciones posibles

respuestas_sin_restriccion_2 = [['A', 'B', 'C', 'D'],
                                ['A', 'B', 'D', 'C'],
                                ['A', 'C', 'B', 'D'],
                                ['A', 'C', 'D', 'B'],
                                ['A', 'D', 'B', 'C'],
                                ['A', 'D', 'C', 'B'],
                                ['B', 'A', 'C', 'D'],
                                ['B', 'A', 'D', 'C'],
                                ['B', 'C', 'A', 'D'],
                                ['B', 'C', 'D', 'A'],
                                ['B', 'D', 'A', 'C'],
                                ['B', 'D', 'C', 'A'],
                                ['C', 'A', 'B', 'D'],
                                ['C', 'A', 'D', 'B'],
                                ['C', 'B', 'A', 'D'],
                                ['C', 'B', 'D', 'A'],
                                ['C', 'D', 'A', 'B'],
                                ['C', 'D', 'B', 'A'],
                                ['D', 'A', 'B', 'C'],
                                ['D', 'A', 'C', 'B'],
                                ['D', 'B', 'A', 'C'],
                                ['D', 'B', 'C', 'A'],
                                ['D', 'C', 'A', 'B'],
                                ['D', 'C', 'B', 'A']]
print(len(respuestas_sin_restriccion_2))
