# Maximización de programas: 
# Sean n programas P1, ...,Pn que hay que almacenar en un disco. 
# El programa Pi requiere Si GB de espacio y la capacidad del disco es D GB. 
# Realizar un algoritmo que ingrese la mayor cantidad posible de programas en el disco

import numpy as np

def maximizar_programas(S, D):
    M = np.zeros((len(S), D + 1), int)
    for i in range(len(S)):
        for j in range(D + 1):
            if j == 0:
               M[i][j] = 0
            elif i == j:
                M[i][j] = 1
            elif j > i:
                if M[i-1][j-S[i]] + 1 > M[i-1][j]:
                    M[i][j] = M[i-1][j-S[i]] + 1
                else:
                    M[i][j] = M[i-1][j]            
            else:
                M[i][j] = M[i-1][j]
    
    return M[i][j]



D = 10 # 100GB
S = [1, 2, 3, 4, 5] #n*10GB

print(f"La cantidad maxima de programas que se pueden guardar en un disco de {D}GB son {maximizar_programas(S, D)}")
