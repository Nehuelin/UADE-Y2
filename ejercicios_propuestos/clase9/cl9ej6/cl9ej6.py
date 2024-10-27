# Un ciclo Hamiltoniano es un camino cerrado que visita todos los vértices de un grafo exactamente una vez. 
# Aplique backtracking al problema de encontrar un ciclo Hamiltonianiano al siguiente grafo.

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

def ciclo_hamiltoniano(G: GrafoNoDirigido):
    vertices = G.Vertices()
    if not vertices:
        return None
    
    camino = [vertices[0]] 

    if _buscar_ciclo_hamiltoniano(G, camino, len(vertices)):
        return camino + [camino[0]]  
    return None

def _buscar_ciclo_hamiltoniano(G: GrafoNoDirigido, camino: list, n: int):
    if len(camino) == n:
        ultimo_vertice = camino[-1]
        if G.ExisteArista(ultimo_vertice, camino[0]):
            return True
        else:
            return False

    for vecino in G.Vecindario(camino[-1]):
        if vecino not in camino:
            camino.append(vecino)
            if _buscar_ciclo_hamiltoniano(G, camino, n):
                return True
            camino.pop()  
    return False


G = GrafoNoDirigido()
G.AgregarVertice('A')
G.AgregarVertice('B')
G.AgregarVertice('C')
G.AgregarVertice('D')
G.AgregarVertice('E')
G.AgregarVertice('F')
G.AgregarVertice('G')
G.AgregarArista('A', 'B')
G.AgregarArista('A', 'E')
G.AgregarArista('A', 'F')
G.AgregarArista('A', 'G')
G.AgregarArista('B', 'C')
G.AgregarArista('B', 'D')
G.AgregarArista('B', 'G')
G.AgregarArista('C', 'D')
G.AgregarArista('D', 'G')
G.AgregarArista('E', 'F')
G.AgregarArista('E', 'G')

ciclo = ciclo_hamiltoniano(G)
if ciclo:
    print("Ciclo Hamiltoniano encontrado:", ciclo)
else:
    print("No se encontró ciclo Hamiltoniano.")





