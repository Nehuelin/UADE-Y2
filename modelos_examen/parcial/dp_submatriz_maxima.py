# MAXIMA SUBMATRIZ CUADRADA DE UNOS EN UNA MATRIZ BINARIA CUADRADA

# ESTRATEGIA: Para encontrar la maxima submatriz cuadrada de unos, se puede utilizar una matriz derivada en la cual se almacenan el tamaño de la maxima submatriz cuadrada de unos que termina en ese punto. Por cada iteracion se guarda el nuevo valor de la maxima submatriz, si corresponde. 

# ALGORITMO encontrarMaximaSubmatriz(int Matrix L[]){
# 	M = new int Matriz[len(L), len(L[0])];
# 	maxima_submatriz = 0;
# 	for i in range(len(L)-1){
# 		for j in range(len(L[0])-1){
# 			if(i == 0 or j == 0){
# 				M[i][j] = L[i][j];
# 			} else {
# 				if(L[i][j] == 0){
# 					M[i][j] = 0;
# 				} else {
# 					M[i][j] = min(M[i][j-1], M[i-1][j-1], M[i-1][j]);
# 				}
# 			}
# 			if (M[i][j] > maxima_submatriz){
# 				maxima_submatriz = M[i][j];
# 			}
# 		}
# 	}

# 	return maxima_submatriz;
# }

# COSTO: O(n^2)

# Para encontrar la posicion de la matriz se puede hacer lo siguiente:
# 1) Guardar los indices de la posicion donde se asigno el valor mas alto de la maxima submatriz
# 2) Parado en ese indice, se le resta 1 a ese valor maximo, y a ese resultado de le resta tanto en i como en j, llegando al punto de inicio de dicha matriz. 

# ALGORITMO posicionMaximaSubmatriz(int Matrix L[]){
# 	M = new int Matriz[len(L), len(L[0])];
# 	maximaSubmatriz = 0;
# 	int inxA = 0;
# 	int inxB = 0;
# 	for i in range(len(L)-1){
# 		for j in range(len(L[0])-1){
# 			if(i == 0 or j == 0){
# 				M[i][j] = L[i][j];
# 			} else {
# 				if(L[i][j] == 0){
# 					M[i][j] = 0;
# 				} else {
# 					M[i][j] = min(M[i][j-1], M[i-1][j-1], M[i-1][j]);
# 				}
# 			}
# 			if (M[i][j] > maximaSubmatriz){
# 				maximaSubmatriz = M[i][j];
# 				inxA = i;
# 				inxB = j;
# 			}
# 		}
# 	}

#  	endPos = [inxA, inxB];
#  	startPos = [inxA-(maximaSubmatriz-1), inxB-(maximaSubmatriz-1)];

# 	return [startPos, endPos];
# }

# La formula dada en la ayuda asegura de que se asigne el numero correcto de maxima submatriz en ese punto. Esto es, el valor solo puede incrementar si los tres vecinos que el elemento tiene (izquierda, izquierda-arriba y arriba) son unos. Si cualquiera de ellos es 0, significa que no se puede formar una matriz cuadrada.

def encontrar_maxima_submatriz(L):
    M = [[0 for _ in range(len(L[0]))] for _ in range(len(L))]
    maxima_submatriz = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == 0 or j == 0:
                M[i][j] = L[i][j]
            else:
                if L[i][j] == 0:
                    M[i][j] = 0
                else:
                    M[i][j] = min(M[i][j-1], M[i-1][j-1], M[i-1][j]) + 1
            if M[i][j] > maxima_submatriz:
                maxima_submatriz = M[i][j]
    return maxima_submatriz

def posicion_maxima_submatriz(L):
    M = [[0 for _ in range(len(L[0]))] for _ in range(len(L))]
    maxima_submatriz = 0
    inxA = 0
    inxB = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == 0 or j == 0:
                M[i][j] = L[i][j]
            else:
                if L[i][j] == 0:
                    M[i][j] = 0
                else:
                    M[i][j] = min(M[i][j-1], M[i-1][j-1], M[i-1][j]) + 1
            if M[i][j] > maxima_submatriz:
                maxima_submatriz = M[i][j]
                inxA = i
                inxB = j
    endPos = [inxA, inxB]
    startPos = [inxA-(maxima_submatriz-1), inxB-(maxima_submatriz-1)]
    return [startPos, endPos]

L = [[1, 0, 1, 1],
     [1, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 0]]

print(encontrar_maxima_submatriz(L))
print(posicion_maxima_submatriz(L))
