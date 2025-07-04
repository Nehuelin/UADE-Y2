import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierdo=None, derecho=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __lt__(self, otro): # Asegura que funcione el heapmin
        return self.frecuencia < otro.frecuencia

class ColaPrioridadMinima:
    def __init__(self):
        self.heap = []
    
    def insert(self, x):
        heapq.heappush(self.heap, x) 
    
    def extract_min(self):
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

def imprimir_arbol_huffman(nodo, codigo=""): # preorden
    if nodo is None:
        return
    
    if nodo.simbolo is not None:
        print(f"Símbolo: {nodo.simbolo}, Código: {codigo}") 
    
    imprimir_arbol_huffman(nodo.izquierdo, codigo + "0") 
    imprimir_arbol_huffman(nodo.derecho, codigo + "1") 

def contar_frecuencias(palabra):
    frecuencias = Counter(palabra)
    return [(simbolo, frecuencia) for simbolo, frecuencia in frecuencias.items()]

if __name__ == "__main__":
    palabra = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccccccccddddddddddddddddeeeeeeeeefffff"
    # palabra = "Hipopotamo"
    simbolos = contar_frecuencias(palabra)
    # simbolos = [('a', 45), ('b', 13), ('c', 12), ('d', 16), ('e', 9), ('f', 5)]
    raiz = huffman(simbolos)
    imprimir_arbol_huffman(raiz)
