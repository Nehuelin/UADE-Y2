class Grafo:
    def __init__(self):
        self.matriz = []
        self.vertices = []

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            for i in range(len(self.matriz)):
                self.matriz[i].append(0)
            aux = []
            for i in range(len(self.vertices)):
                aux.append(0)
            self.matriz.append(aux)

    def eliminar_vertice(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            self.vertices.remove(v)
            self.matriz.pop(i)
            for i in range(len(self.matriz)):
                self.matriz[i].pop(i)

    def agregar_arista(self, v1, v2, p):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matriz[i][j] = p

    def eliminar_arista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matriz[i][j] = 0

    def peso_arista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            return self.matriz[i][j]
        return 0

    def vertices(self):
        return self.vertices

    def existe_arista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            return self.matriz[i][j] != 0
        return False
    
    def vecindario(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            vecinos = []
            for j in range(len(self.matriz)):
                if self.matriz[i][j] != 0:
                    vecinos.append(self.vertices[j])
            return vecinos
        return []