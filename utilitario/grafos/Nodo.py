class Nodo:
    def __init__(self, valor=None, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

    def es_hoja(self):
        # Un nodo es hoja si no tiene hijos
        return len(self.hijos) == 0

    def resultado(self):
        # Devuelve el valor del nodo si es una hoja
        return self.valor

    def obtener_hijos(self):
        # Devuelve los hijos del nodo
        return self.hijos


