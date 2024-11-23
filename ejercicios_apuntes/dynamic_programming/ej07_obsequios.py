# Ana trabaja en una empresa de comunicaciones y le han encargado la compra del 
# regalo de cumpleaños para Darío, un compañero de trabajo.  Para ello Ana va a 
# un negocio en donde hay diferentes obsequios que le pueden gustar a Darío.  
# Cada obsequio tiene un precio determinado.  Ana conoce el monto mínimo a 
# gastar para la compra del regalo, y su objetivo es encontrar una combinación de 
# objetos a comprar que cubra exactamente el monto a gastar o lo supere en forma 
# mínima, considerando que no puede repetir objetos en su compra. Diseñar un 
# algoritmo que determine cuáles son los objetos que conforman el regalo y el 
# dinero óptimo gastado. 

class Regalo:
    def __init__(self, precio: int, nombre: str):
        self.precio = precio
        self.nombre = nombre

def encontrar_regalos(regalos: list[Regalo], monto_minimo: int):
    n = len(regalos)
    dp = [[float('inf')] * (monto_minimo * 2 + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    seleccion = [[[] for _ in range(monto_minimo * 2 + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        regalo = regalos[i-1]
        for j in range(monto_minimo * 2 + 1):
            dp[i][j] = dp[i-1][j]
            seleccion[i][j] = seleccion[i-1][j].copy()

            if j >= regalo.precio:
                if dp[i-1][j - regalo.precio] != float('inf'):
                    nuevo_valor = dp[i-1][j - regalo.precio] + regalo.precio
                    if nuevo_valor < dp[i][j]:
                        dp[i][j] = nuevo_valor
                        seleccion[i][j] = seleccion[i-1][j - regalo.precio] + [regalo]

    print(dp)

    monto_final = monto_minimo
    while monto_final < len(dp[0]) and dp[n][monto_final] == float('inf'):
        monto_final += 1
        
    if monto_final == len(dp[0]):
        return None, None
        
    return dp[n][monto_final], seleccion[n][monto_final]

def main():
    regalos = [
        Regalo(50, "Libro"),
        Regalo(30, "Taza"),
        Regalo(80, "Reloj"),
        Regalo(40, "Billetera")
    ]
    
    monto_minimo = 100
    monto_total, seleccionados = encontrar_regalos(regalos, monto_minimo)
    
    if monto_total is None:
        print("No se encontró solución")
    else:
        print(f"Monto total gastado: ${monto_total}")
        print("Regalos seleccionados:")
        for regalo in seleccionados:
            print(f"- {regalo.nombre} (${regalo.precio})")

if __name__ == "__main__":
    main()
