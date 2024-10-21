# Navegación en el río Ctalamochita, de nuevo. Usted planea navegar en
# canoa aguas abajo por el río Ctalamochita entre las ciudades de Morrison
# y Monte Leña. Hay n puestos de canoas a lo largo de este trayecto. Antes
# de comenzar su excursión, usted consigue para cada 1 ≤ i < j ≤ n, el
# precio fi,j para alquilar una canoa desde el puesto i hasta el puesto j.
# Estos precios son arbitrarios. Por ejemplo, es posible que sea f1,3 = 10 y
# f1,4 = 5. Usted comienza en el puesto 1 y debe terminar en el puesto n
# (usando canoas alquiladas). El objetivo es minimizar el costo.
# Aplique un abordaje de programación dinámica para resolver este
# problema. Considere la posibilidad de construir una tabla en la que la
# posición i contenga el costo mínimo para llegar a este puesto desde el
# puesto 1.

class Puesto:
    def __init__(self, i, j, precio):
        self.i = i
        self.j = j
        self.precio = precio
    
def costo_minimo(puestos):
    M = [float('inf')] * (len(puestos) + 1)
    M[0] = 0

    for i in range(1, len(puestos) + 1):
        for j in range(i):
            M[i] = min(M[i], M[j] + puestos[j].precio)
    
    return M[len(puestos)]

puestos = [Puesto(1, 2, 10), Puesto(1, 3, 5), Puesto(2, 3, 7), Puesto(2, 4, 15), Puesto(3, 4, 20)]
resultado = costo_minimo(puestos)
print(f"El costo mínimo para llegar al puesto n es: {resultado}")
