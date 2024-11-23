#  Problema de la Mochila: Se tienen n objetos y una mochila.  Para i = 1,2,..n, el 
# objeto i tiene un peso positivo pi y un valor positivo vi. La mochila puede llevar 
# un peso que no sobrepase P. El objetivo es llenar la mochila de tal manera que 
# se maximice el valor de los objetos transportados, respetando la limitación de 
# capacidad impuesta. Los objetos pueden ser fraccionados, si una fracción xi (0 ≤ ≤≤ ≤ 
# xi ≤ ≤≤ ≤ 1) del objeto i es ubicada en la mochila contribuye en xi*pi al peso total de 
# la mochila y en xi*vi al valor de la carga. 

class Obj:
    def __init__(self, value: float, weight: float):
        self.weight = weight
        self.value = value

def knapsack(Objeto: list[Obj], max: int):
    R = [0.0] * len(Objeto)
    n = len(Objeto) - 1
    Objeto.sort(key=lambda x: x.value / x.weight, reverse=True)
    i = 0
    accum = 0
    while accum < max and i < n:
        R[i] = min(1, (max - accum) / Objeto[i].weight)
        accum = accum + R[i] * Objeto[i].weight
        i += 1
    return R


objetos = [
    Obj(4, 3),
    Obj(7, 5),
    Obj(2, 4),
    Obj(5, 4)
]

print(knapsack(objetos, 10))