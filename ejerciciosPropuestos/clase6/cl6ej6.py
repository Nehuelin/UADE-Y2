# El campo de zanahorias. Se tiene un campo de zanahorias representado por una matriz M, que es una cuadrícula m × n, 
# en la que cada posición M[i,j] representa la cantidad de zanahorias que se pueden encontrar allí. 
# Un conejo recorre el campo de izquierda a derecha. 
# Comienza en la columna 0 y puede elegir cualquier fila desde 0 hasta m-1. 
# Por supuesto, el conejo devorará todas las zanahorias que encuentre en cada posición por la que pase.
# Si el conejo está en la posición M[i,j], tiene las siguientes posibilidades:
# --> Arriba a la derecha: M[i, j] → M[i − 1,j + 1] (si i > 0 y j < m-1.)
# --> A la derecha: M[i,j] → M[i,j + 1] (si j < m-1.)
# --> Abajo a la derecha: M[i,j] → M[i + 1,j + 1] (si i < n-1 y j < m-1.)
#  Encuentre una estrategia de programación dinámica para que el conejo pueda maximizar la cantidad de zanahorias comidas.

import numpy as np

def analizar_maximo(valor, maximo):
  nuevo_maximo = False
  if (valor > maximo):
    maximo = valor
    nuevo_maximo = True
  return maximo, nuevo_maximo

def asignar_coordenadas_maximo(nuevo_maximo, coordenadas_maximo, i, j):
  if nuevo_maximo:
    coordenadas_maximo[0] = i
    coordenadas_maximo[1] = j

valores = np.array([[2,3,3,8,5],
                    [3,4,1,2,1],
                    [2,5,2,3,4],
                    [1,5,1,2,2]])

acum = np.zeros((4,5), dtype=int)

maximo = 0
coordenadas_maximo = [0, 0]

for j in range(len(valores[0])):
  for i in range(len(valores)):
    if (j == 0):
      acum[i][j] = valores[i][j]
    else:
      if (i == 0):
        acum[i][j] = max(acum[i][j-1], acum[i+1][j-1]) + valores[i][j]
        maximo, nuevo_maximo = analizar_maximo(acum[i][j], maximo)
        asignar_coordenadas_maximo(nuevo_maximo, coordenadas_maximo, i, j)
      elif (i == len(valores)-1):
        acum[i][j] = max(acum[i-1][j-1], acum[i][j-1]) + valores[i][j]
        maximo, nuevo_maximo = analizar_maximo(acum[i][j], maximo)
        asignar_coordenadas_maximo(nuevo_maximo, coordenadas_maximo, i, j)
      else:
        acum[i][j] = max(acum[i-1][j-1], acum[i][j-1], acum[i+1][j-1]) + valores[i][j]
        maximo, nuevo_maximo = analizar_maximo(acum[i][j], maximo)
        asignar_coordenadas_maximo(nuevo_maximo, coordenadas_maximo, i, j)

# IMPRIMIR EL CAMINO QUE TOMA EL CONEJO
camino = []
j = len(valores[0])-1
i = coordenadas_maximo[0]

while (j >= 0):
  camino.append(coordenadas_maximo)
  if i == 0:
    if acum[i][j-1] > acum[i+1][j-1]:
      coordenadas_maximo = [i, j-1] 
    else:
      coordenadas_maximo = [i+1, j-1]
  elif i == len(valores)-1:
    if acum[i-1][j-1] > acum[i][j-1]:
      coordenadas_maximo = [i-1, j-1]
    else:
      coordenadas_maximo = [i, j-1]
  else:
    if acum[i-1][j-1] > acum[i][j-1] and acum[i-1][j-1] > acum[i+1][j-1]:
      coordenadas_maximo = [i-1, j-1]
    elif acum[i][j-1] > acum[i-1][j-1] and acum[i][j-1] > acum[i+1][j-1]:
      coordenadas_maximo = [i, j-1]
    else:
      coordenadas_maximo = [i+1, j-1]
  
  j -= 1

print(valores)
print(acum)
print(maximo)
print(coordenadas_maximo)
print(camino)



