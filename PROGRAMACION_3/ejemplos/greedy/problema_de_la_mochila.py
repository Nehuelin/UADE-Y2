class Obj:
    def __init__(self, value: float, weight: float):
        self.weight = weight
        self.value = value

def knapsack(O: list[Obj], max: int):
    """
    Algoritmo de la mochila (Knapsack) en Python.
    
    :param objects: Lista de objetos donde cada objeto es un diccionario con 'weight' y 'value'.
    :param max_weight: Peso máximo que la mochila puede llevar.
    :return: Lista con las fracciones de cada objeto a llevar.
    """
    R = [0.0] * len(O)
    n = len(O) - 1
    O.sort(key=lambda x: x.value / x.weight, reverse=True)
    i = 0
    accum = 0
    while accum < max and i < n:
        R[i] = min(1, (max - accum) / O[i].weight)
        accum = accum + R[i] * O[i].weight
        i += 1
    return R


objetos = [
    Obj(4, 3),
    Obj(7, 5),
    Obj(2, 4),
    Obj(5, 4)
]

print(knapsack(objetos, 10))

# Costo O(n log(n))