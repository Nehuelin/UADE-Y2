# Se tiene un conjunto de salas numeradas del 0 hasta n. 
# Las salas están comunicadas entre sí a través de puertas que se abren solamente en el sentido de la numeración creciente (si una puerta permite pasar de la sala i a la sala j, entonces i < j.) 
# Todas las salas tienen un puerta saliente, excepto, por supuesto, la sala n. 
# Construya un algoritmo que permita ir desde la sala 0 a la sala n atravesando la máxima cantidad de salas.

class Grafo:
    def __init__(self):
        self.matriz = []
        self.vertices = []

    def AgregarVertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            for i in range(len(self.matriz)):
                self.matriz[i].append(0)
            aux = []
            for i in range(len(self.vertices)):
                aux.append(0)
            self.matriz.append(aux)

    def EliminarVertice(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            self.vertices.remove(v)
            self.matriz.pop(i)
            for i in range(len(self.matriz)):
                self.matriz[i].pop(i)

    def AgregarArista(self, v1, v2, p):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matriz[i][j] = p

    def EliminarArista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matriz[i][j] = 0

    def PesoArista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            return self.matriz[i][j]
        return 0

    def Vertices(self):
        return self.vertices

    def ExisteArista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            return self.matriz[i][j] != 0
        return False
    
    def Vecindario(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            vecinos = []
            for j in range(len(self.matriz)):
                if self.matriz[i][j] != 0:
                    vecinos.append(self.vertices[j])
            return vecinos
        return []
    
def camino_mas_largo(G):
    max_length = [-1]
    max_camino = [None]
    DFS(G, 1, set(), [], max_length, max_camino)
    return max_length, max_camino

def DFS(G: Grafo, sala: int, visitados: set, camino_actual: list, max_length: int, max_camino: list):
    n = max(G.vertices)
    visitados.add(sala)
    camino_actual.append(sala)
    vecindario = G.Vecindario(sala)

    if sala == n and esUltimoElemento(sala, camino_actual) and len(camino_actual) > max_length[0]:
        max_length[0] = len(camino_actual)
        max_camino[0] = camino_actual[:max_length[0]]

    while len(vecindario) > 0:
        a = vecindario.pop()
        if a not in visitados:
            DFS(G, a, visitados, camino_actual, max_length, max_camino)
    
def esUltimoElemento(valor: int, lista: list):
    return valor == lista[len(lista) - 1]


# Test
G = Grafo()
G.AgregarVertice(1)
G.AgregarVertice(2)
G.AgregarVertice(3)
G.AgregarVertice(4)
G.AgregarVertice(5)
G.AgregarVertice(6)
G.AgregarArista(1, 2, 1)
G.AgregarArista(1, 3, 1)
G.AgregarArista(2, 5, 1)
G.AgregarArista(3, 4, 1)
G.AgregarArista(4, 5, 1)
G.AgregarArista(5, 6, 1)

print(camino_mas_largo(G))