import Grafo

def diferencia(A, B):
    C = []
    for i in A:
        if i not in B:
            C.append(i)
    return C

def copiar(A):
    B = []
    for i in A:
        B.append(i)
    return B

def dijkstra(G: Grafo, v: int):
    visitados = {}
    Dijkstra = Grafo()
    Dijkstra.InicializarGrafo()
    for w in G.vertices:
        Dijkstra.AgregarVertice(w)
    for w in G.Vecindario(v):
        Dijkstra.AgregarArista(v, w, G.PesoArista(v, w))
    cantidatos = {}
    cantidatos = diferencia(G.vertices, visitados)
    while not cantidatos.empty():
        min = 999999
        for u in cantidatos:
            if Dijkstra.ExisteArista(v, u) and Dijkstra.PesoArista(v, u) < min:
                min = Dijkstra.PesoArista(v, u)
                w = u
        visitados.append(w)
        cantidatos.remove(w)
        auxCantidatos = copiar(cantidatos)  
        while not auxCantidatos.empty():
            for p in auxCantidatos:
                if G.ExisteArista(w, p):
                    if Dijkstra.ExisteArista(v, p):
                        if (Dijkstra.PesoArista(v, w) + G.PesoArista(w, p)) < Dijkstra.PesoArista(v, p):
                            Dijkstra.AgregarArista(w, p, G.PesoArista(w, p))
                            Dijkstra.EliminarArista(v, p)
                    else:
                        Dijkstra.AgregarArista(w, p, G.PesoArista(w, p))
            auxCantidatos.remove(p)  
    return Dijkstra
        