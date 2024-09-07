import heapq

class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierdo=None, derecho=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierdo = izquierdo
        self.derecho = derecho
    
    # Comparación entre nodos basada en la frecuencia, para que funcione con el heapq (min-heap)
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


class ColaPrioridadMinima:
    def __init__(self):
        self.heap = []
    
    def insert(self, x):
        heapq.heappush(self.heap, x)
    
    def extract_min(self):
        if self.is_empty():
            raise IndexError("extract_min() llamado en una cola vacía")
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0


def huffman(C):
    cola = ColaPrioridadMinima()

    for simbolo, frecuencia in C:
        nodo = NodoHuffman(simbolo, frecuencia)
        cola.insert(nodo)
    
    while len(cola.heap) > 1:
        x = cola.extract_min()
        y = cola.extract_min()
        
        nuevo_nodo = NodoHuffman(frecuencia=x.frecuencia + y.frecuencia, izquierdo=x, derecho=y)
        
        cola.insert(nuevo_nodo)
    
    return cola.extract_min()

def imprimir_arbol_huffman(nodo, codigo=""):
    if nodo is None:
        return
    
    if nodo.simbolo is not None:
        print(f"Símbolo: {nodo.simbolo}, Código: {codigo}")
    
    imprimir_arbol_huffman(nodo.izquierdo, codigo + "0")
    imprimir_arbol_huffman(nodo.derecho, codigo + "1")



if __name__ == "__main__":
    simbolos = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    raiz = huffman(simbolos)
    imprimir_arbol_huffman(raiz)