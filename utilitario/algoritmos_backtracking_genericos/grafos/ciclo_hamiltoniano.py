# DFS para ciclos hamiltonianos
# Objetivo: Encontrar un camino que inicie y termine en un vertice V, en donde se pase por todos los vertices exactamente UNA sola vez.



def backtrack(G, camino: list, n: int):
    if len(camino) == n:
        ultimo_vertice = camino[-1]
        if G.ExisteArista(ultimo_vertice, camino[0]):
            return True
        else:
            return False
    
    for vecino in G.Vecindario(camino[-1]):
        if vecino not in camino:
            camino.append(vecino)
            if backtrack(G, camino, n):
                return True
            camino.pop()  
    return False