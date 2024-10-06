# RECORRIDO DE MINIMO COSTO

# ESTRATEGIA: Para calcular el minimo costo se puede utilizar una matriz (llamada acum) donde se almacena el costo acumulado minimo posible para llegar a la celda [i][j]. Para eso se consideran varias situaciones:
# a) El primer elemento de la matriz acum va a ser el mismo que aparece en la matriz L
# b) Si estamos en la primera fila, solo nos podemos mover a la derecha. Por ende la unica operacion a realizar es sumar el valor actual de L con el anterior en la matriz acum.
# c) Si estamos en la primer columna, solo nos podemos mover hacia abajo. Por ende la unica operacion a realizar es sumar el valor actual de L con el de arriba en la matriz acum.
# d) Si no se cumple ninguna de las condiciones previas, el valor de acum[i][j] va a ser el minimo entre el de arriba o el de la izquierda, y a ese valor se le suma el de L[i][j]

# El costo minimo estara en el indice acum[m - 1][n - 1]

# ALGORITMO obtenerRecorrido(int Matrix L){
# 	acum = new int Matrix[len(L), len(L[0])] 
# 	for j in range(len(L[0]) - 1){
# 		for i in range(len(L) - 1){
# 			if (i == 0 && j == 0){
# 				acum[i][j] = L[i][j];
# 			} else if (i == 0){
# 				acum[i][j] = acum[i][j-1] + L[i][j];
# 			} else if (j == 0){
# 				acum[i][j] = acum[i-1] + L[i][j];
# 			} else {
# 				acum[i][j] = min(acum[i-1][j], acum[i][j-1]) + L[i][j];
# 			}
# 		}
# 	}

# 	return acum[len(L) - 1][len(L[0]) - 1]
# }

# COSTO: O(m*n)

def obtener_recorrido(L):
    acum = [[0 for _ in range(len(L[0]))] for _ in range(len(L))]
    for j in range(len(L[0])):
        for i in range(len(L)):
            if i == 0 and j == 0:
                acum[i][j] = L[i][j]
            elif i == 0:
                acum[i][j] = acum[i][j-1] + L[i][j]
            elif j == 0:
                acum[i][j] = acum[i-1][j] + L[i][j]
            else:
                acum[i][j] = min(acum[i-1][j], acum[i][j-1]) + L[i][j]
    return acum[len(L) - 1][len(L[0]) - 1]

L = [[3, 2, 7, 1, 6], 
     [5, 1, 8, 5, 4], 
     [4, 6, 3, 8 ,3],
     [2, 5, 2, 1, 5]]
print(obtener_recorrido(L))
