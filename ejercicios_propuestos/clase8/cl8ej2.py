# Se tiene un grafo dirigido G = (V,E) representado como una matriz de adyacencia. 
# Escriba un programa que enumere todos los caminos de un vértice s ∈ V cualquiera que pasen a lo sumo una vez por cada vértice.

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
    
def EnumerarCaminos(G, s):
    if s not in G.vertices:
        return
    dfs(G, s, set(), [])
    
def dfs(G: Grafo, v: int, visitados: set, camino: list):
    visitados.add(v)
    camino.append(v)

    print(" -> ".join(camino))
    
    for vecino in G.Vecindario(v):
        if vecino not in visitados:
            dfs(G, vecino, visitados, camino)

    camino.pop()
    visitados.remove(v)

g = Grafo()
g.AgregarVertice('A')
g.AgregarVertice('B')
g.AgregarVertice('C')
g.AgregarVertice('D')

g.AgregarArista('A', 'B', 1)
g.AgregarArista('A', 'C', 1)
g.AgregarArista('B', 'C', 1)
g.AgregarArista('C', 'D', 1)

EnumerarCaminos(g, 'A')