from collections import deque
from Grafo import Grafo

class DFS:
    def camino_corto(self, grafo: Grafo, v1, camino, suma_peso, suma_total_peso):
        if 50 <= v1 <= 57:
            return camino
        
        visitados = grafo.vertices()  

        while visitados:
            x = visitados.pop()
            if grafo.existe_arista(v1, x) and suma_peso < suma_total_peso:
                suma_peso += grafo.peso_arista(v1, x)
                camino.append(x)
                self.camino_corto(grafo, x, camino, suma_peso, suma_total_peso)
        
        return camino