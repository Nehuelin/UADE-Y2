class GrafoNoDirigido:
    def __init__(self):
        self.adyacencias = {}

    def AgregarVertice(self, v):
        if v not in self.adyacencias:
            self.adyacencias[v] = []

    def EliminarVertice(self, v):
        if v in self.adyacencias:
            for vecino in list(self.adyacencias[v]):
                self.adyacencias[vecino].remove(v)
            del self.adyacencias[v]

    def AgregarArista(self, v1, v2, p=1):
        if v1 not in self.adyacencias:
            self.AgregarVertice(v1)
        if v2 not in self.adyacencias:
            self.AgregarVertice(v2)
        
        if v2 not in [v for v, peso in self.adyacencias[v1]]:
            self.adyacencias[v1].append((v2, p))
            self.adyacencias[v2].append((v1, p))  

    def EliminarArista(self, v1, v2):
        if v1 in self.adyacencias and v2 in self.adyacencias:
            self.adyacencias[v1] = [(v, peso) for v, peso in self.adyacencias[v1] if v != v2]
            self.adyacencias[v2] = [(v, peso) for v, peso in self.adyacencias[v2] if v != v1]

    def PesoArista(self, v1, v2):
        if v1 in self.adyacencias:
            for vecino, peso in self.adyacencias[v1]:
                if vecino == v2:
                    return peso
        return 0

    def Vertices(self):
        return list(self.adyacencias.keys())

    def ExisteArista(self, v1, v2):
        if v1 in self.adyacencias:
            return any(vecino == v2 for vecino, _ in self.adyacencias[v1])
        return False

    def Vecindario(self, v):
        if v in self.adyacencias:
            return [vecino for vecino, _ in self.adyacencias[v]]
        return []
