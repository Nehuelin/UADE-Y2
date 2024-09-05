import heapq
# Numero negativo para que el heap se comporte como un min-heap y no como un max-heap (por defecto)
class ColaPrioridad:
    def __init__(self):
        self.cola = []
    
    def acolar_prioridad(self, x, prioridad):
        heapq.heappush(self.cola, (-prioridad, x))
    
    def desacolar(self):
        if not self.cola_vacia():
            heapq.heappop(self.cola)
    
    def cola_vacia(self):
        return len(self.cola) == 0
    
    def primero(self):
        if not self.cola_vacia():
            return self.cola[0][1]
        else:
            return None  
    
    def prioridad(self):
        if not self.cola_vacia():
            return -self.cola[0][0]
        else:
            return None  

    def imprimir_cola(self):  # Solo para pruebas
        print("Cola con prioridades:")
        for prioridad, elemento in sorted(self.cola, reverse=True):
            print(f"Elemento: {elemento}, Prioridad: {-prioridad}")

