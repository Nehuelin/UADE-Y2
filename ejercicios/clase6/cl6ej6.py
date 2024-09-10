import numpy as np

valores = np.array([[2,3,3,8,5],
                    [3,4,1,2,1],
                    [2,5,2,3,4],
                    [1,5,1,2,2]])

acum = np.zeros((4,5),dtype=int)

for j in range(len(valores[0])):
  for i in range(len(valores)):
    if (j == 0):
      acum[i][j] = valores[i][j]
    else:
      if (i == 0):
        acum[i][j] = max(acum[i][j-1], acum[i+1][j-1]) + valores[i][j]
      elif (i == len(valores)-1):
        acum[i][j] = max(acum[i-1][j-1], acum[i][j-1]) + valores[i][j]
      else:
        acum[i][j] = max(acum[i-1][j-1], acum[i][j-1], acum[i+1][j-1]) + valores[i][j]
print(valores)
print(acum)

# FALTA DEVOLVER CAMINO QUE TOMA EL CONEJO

