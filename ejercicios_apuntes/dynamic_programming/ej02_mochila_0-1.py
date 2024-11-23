# Se tienen n objetos y una mochila. Para i = 1, 2,..n, el 
# objeto i tiene un peso positivo pi y un valor positivo vi. La mochila puede llevar 
# un peso que no sobrepase P. Los objetos no pueden ser fraccionados. El objetivo 
# es llenar la mochila de manera tal que se maximice el valor de los objetos 
# transportados, respetando la limitación de capacidad impuesta. El algoritmo debe 
# determinar el valor máximo que se podrá cargar. ¿Y si además se quiere saber 
# qué objetos se deberá cargar para alcanzar dicho valor? 

class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

def mochila(O: list[Objeto], P):
    M = [[0] * (P + 1) for _ in range(len(O))]

    for i in range(len(O)):
        for j in range(P + 1):
            if i == 0:
                if O[i].peso > j:
                    M[i][j] = 0
                else:
                    M[i][j] = O[i].valor
            else:
                if O[i].peso > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = max(M[i - 1][j], M[i - 1][j - O[i].peso] + O[i].valor)
    
    i = len(O) - 1
    j = P
    objetos = []
    while j > 0 and i >= 0:
        if i == 0:
            objetos.append(O[i])
            j -= O[i].peso
        elif M[i][j] == M[i - 1][j]:
            i -= 1
        else:
            objetos.append(O[i])
            j -= O[i].peso

    return M[len(O) - 1][P], objetos

objetos = [Objeto(2, 3), Objeto(3, 4), Objeto(4, 5), Objeto(5, 8)]  
capacidad = 15

resultado, objetos_usados = mochila(objetos, capacidad)
print(f"El valor máximo que se puede obtener es: {resultado}")
print(f"Los objetos usados son: {[f'({o.peso}, {o.valor})' for o in objetos_usados]}")