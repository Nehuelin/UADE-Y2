# Caminos más largos en grafos ordenados: 
# Supongamos que tenemos un grafo dirigido G = (V , E) con V = {v1, . . . , vn}. 
# Decimos que G es ordenado si satisface las siguientes condiciones:
# --> Todas las aristas tienen la forma (vi, vj) con i < j.
# --> Todos los vértices tienen aristas salientes excepto vn.
# El objetivo es encontrar la longitud del camino más largo que va de v1 a vn. 
# Se pide una estrategia de programación dinámica para resolver este problema.
# Por ejemplo, el siguiente grafo es ordenado. El camino más largo de 0 a 5 es (0-1-2-3-4-5), o sea tiene longitud 5.
# ignorar pesos, solo importa la cantidad de aristas

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
    n = len(G.vertices)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if G.ExisteArista(G.vertices[j], G.vertices[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n - 1]

G = Grafo()
G.AgregarVertice('v0')
G.AgregarVertice('v1')
G.AgregarVertice('v2')
G.AgregarVertice('v3')
G.AgregarVertice('v4')
G.AgregarVertice('v5')
G.AgregarVertice('v6')
G.AgregarVertice('v7')
G.AgregarVertice('v8')
G.AgregarArista('v0', 'v1', 1)
G.AgregarArista('v1', 'v2', 3)
G.AgregarArista('v1', 'v3', 4)
G.AgregarArista('v2', 'v3', 5)
G.AgregarArista('v2', 'v4', 6)
G.AgregarArista('v2', 'v5', 2)
G.AgregarArista('v3', 'v4', 6)
G.AgregarArista('v4', 'v5', 7)
G.AgregarArista('v4', 'v6', 8)
G.AgregarArista('v5', 'v7', 9)
G.AgregarArista('v6', 'v7', 10)
G.AgregarArista('v6', 'v8', 11)
G.AgregarArista('v7', 'v8', 11)

print(camino_mas_largo(G))