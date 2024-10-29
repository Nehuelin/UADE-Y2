class Nodo:
    def __init__(self, valor=None, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

    def es_hoja(self):
        return len(self.hijos) == 0

    def resultado(self):
        return self.valor

    def obtener_hijos(self):
        return self.hijos

def MinMax(nodo: Nodo, es_max):
    if nodo.es_hoja():
        return nodo.resultado()
    else:
        if es_max:
            valor = float('-inf')
            for hijo in nodo.obtener_hijos():
                valor = max(valor, MinMax(hijo, False))
        else:
            valor = float('inf')
            for hijo in nodo.obtener_hijos():
                valor = min(valor, MinMax(hijo, True))
                
    return valor


if __name__ == "__main__":
    H = Nodo(valor=3)
    I = Nodo(valor=5)
    J = Nodo(valor=6)
    K = Nodo(valor=9)
    L = Nodo(valor=1)
    M = Nodo(valor=2)
    N = Nodo(valor=0)
    O = Nodo(valor=-1)
    D = Nodo(hijos=[H, I])
    E = Nodo(hijos=[J, K])
    F = Nodo(hijos=[L, M])
    G = Nodo(hijos=[N, O])
    B = Nodo(hijos=[D, E])
    C = Nodo(hijos=[F, G])
    A = Nodo(hijos=[B, C])

    resultado = MinMax(A, es_max=True)
    print("El valor óptimo para el jugador MAX es:", resultado)

