# Busqueda en Profundidad (DFS)

# DFS (G: Grafo, V: entero, Visitados: conjunto){ // sea V el vertice donde se investiga los caminos
# 	Visitados.agregar(V)
# 	Vecindario = G.vecindario(V)
# 	mientras (len(Vecindario) > 0){
# 		entero A = vecindario.pop()
# 		si (A no está en Visitados) {
# 			DFS(G, A, Visitados)
# 		}
# 	}	
# }

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

def busqueda_profunda(G, v):
    DFS(G, v, set())

def DFS(G: Grafo, v: int, visitados: set):
    visitados.add(v)
    print(v)
    vecindario = G.Vecindario(v)
    while len(vecindario) > 0:
        a = vecindario.pop()
        if a not in visitados:
            DFS(G, a, visitados)

