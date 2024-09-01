# Imagine que se encuentra en Thurgau, donde dispone de las siguientes
# monedas: 5 francos, 2 francos, un franco, 50 centavos (medio franco), 20
# centavos, 10 centavos, 5 centavos, y un centavo.
# Usted debe pagar 8.78 francos por un paquete de frutillas (un producto
# típico local), y quiere usar la menor cantidad posible de monedas.

def cambio(v: int):
    """
    Parameters:
    v: Monto (int)

    Returns:
    Numero de monedas
    """ 
    n = 0 # Numero de monedas usadas
    accum = 0 # Monto pagado
    i = 0
    coins = [500, 200, 100, 50, 20, 10, 5, 1]
    while accum < v and i < len(coins):
        if accum + coins[i] <= v:
            accum += coins[i]
            n += 1 # Mayor moneda que podemos usar
        else:
            i += 1 # Seguimos buscando
    if (i < len(coins)):
        return n # Devolvemos el numero de monedas usadas
    else:
        return -1 # No hay solucion
    
print(cambio(878)) 

# Costo O(v)