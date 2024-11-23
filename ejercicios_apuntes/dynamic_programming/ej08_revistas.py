#  Howard es un fanático de los comics. En la tienda de comics tienen un único 
# ejemplar de cada revista. Cada revista tiene en la tapa el precio y la cantidad de 
# páginas que contiene. Un día particular Howard decide comprar todas las revistas 
# posibles de modo de maximizar la cantidad total de páginas sin superar su 
# presupuesto disponible de $P. La tienda tiene listados con la información de precio 
# y cantidad de páginas de cada revista ordenados por todos los criterios que sean 
# necesarios. ¿Cuántas páginas en total tendrá si compra la mejor combinación 
# posible de revistas?

class Revista:
    def __init__(self, precio: int, paginas: int):
        self.precio = precio
        self.paginas = paginas

def maximizar_paginas(revistas: list[Revista], P: int):
    M = [[0] * (P + 1) for _ in range(len(revistas))]

    for i in range(len(M)):
        for j in range(P + 1):
            if i == 0:
                if revistas[i].precio > j:
                    M[i][j] = 0
                else:
                    M[i][j] = revistas[i].paginas
            else:
                if revistas[i].precio > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = max(M[i - 1][j], M[i - 1][j - revistas[i].precio] + revistas[i].paginas)
    
    return M[len(revistas) - 1][P]

revistas = [
    Revista(precio=1, paginas=50),
    Revista(precio=3, paginas=120),
    Revista(precio=4, paginas=180),
    Revista(precio=5, paginas=200),
    Revista(precio=8, paginas=75)
]

print(maximizar_paginas(revistas, 10))