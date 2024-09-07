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
        cola.insert(nodo) # 1) La construcción del árbol se realiza ordenando en primer lugar los simbolos con menor frecuencia
    
    while len(cola.heap) > 1:
        # 2) Los dos nodos con menor frecuencia se introducen en el arbol y se quitan de la cola
        x = cola.extract_min()
        y = cola.extract_min()
        
        # 3) Se conectan a un nodo cuyo peso es igual a la suma de los pesos de los dos simbolos
        nuevo_nodo = NodoHuffman(frecuencia=x.frecuencia + y.frecuencia, izquierdo=x, derecho=y)
        
        # 4) A cada nodo formado se lo considera como un simbolo nuevo
        cola.insert(nuevo_nodo)
    
    # 5) Los pasos 1 a 4 se repiten hasta que se obtiene un nodo principal llamado raíz
    return cola.extract_min()

 # 6) El código de cada símbolo corresponde a la sucesión de códigos en el camino, comenzando desde la raíz. 
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