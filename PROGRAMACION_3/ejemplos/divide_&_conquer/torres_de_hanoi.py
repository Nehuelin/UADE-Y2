def hanoi(n, origen, auxiliar, destino):
  """
  Calcula los movimientos necesarios para completar el juego de las torres de hanoi

  El objetivo del juego es mover todos los discos a la clavija C utilizando la clavija B como auxiliar y respetando las siguientes reglas:

  -> Sólo se puede mover un disco por vez de una clavija a otra. 
  
  -> Sólo el tope de cada pila puede desplazarse.
  
  -> Nunca puede haber un disco apilado sobre uno de diámetro menor

  Parameters:
  n (int): Cantidad de discos
  origen (str): Torre de la cual se inicia los movimientos
  auxiliar (str): Torre que se utiliza como auxilio entre movimientos
  destino (str): Torre en donde deben finalizar todos los discos

  Returns:
  Un arreglo que contiene TODOS los movimientos realizados
  """
  if (n == 1):
    return ["Mover " + origen + " a " + destino]
  else:
    x1 = hanoi(n-1, origen, destino, auxiliar)
    x2 = ["Mover " + origen + " a " + destino]
    x3 = hanoi(n-1, auxiliar, origen, destino)
    return x1 + x2 + x3

u = hanoi(3, "A", "B", "C")
for movimiento in u:
  print(movimiento)
print(len(u))