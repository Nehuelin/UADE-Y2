# ENCONTRAR SUBCONJUNTO DE ELEMENTOS QUE SUMAN K

# ESTRATEGIA: Para encontrar el subconjunto de elementos que suman k, se puede usar una matriz en la cual se almacenan valores booleanos, de acuerdo si se puede obtener la suma del valora columna con el valor de las filas que se usaron hasta ese momento. Como la matriz va a tener tantas filas como elementos tenga el arreglo A (cada fila tendra asignada el valor correspondiente de A) y k + 1 columnas, el elemento T[len(A) - 1][k] va a decir si existe o no ese subconjunto.

# ALGORITMO encontrarSubconjunto(int[] A, int k){
# 	T = new boolean Matrix[len(A), k + 1] // len(A) filas y k + 1 columnas
# 	for i in range(len(T)){
# 		for j in range(len(T[i])){
# 			if (i == 0){
# 				if (j == 0){
# 					T[i][j] = true;
# 				} else if (j > 0){
# 					T[i][j] = A[i] == j;
# 				}
# 			} else if (i > 0){
# 				if (j == 0){
# 					T[i][j] = true;
# 				} else if (j > 0) {
# 					T[i][j] = (A[i] == j) || (T[i - 1][j]) || (A[i] < j && T[i - 1][j - A[i]]);
# 				}
# 			}
# 		}
# 	}
# 	return T[len(A) - 1, k];
# }

# Las formulas planteadas siguen la siguiente logica:
# --> Como el valor de la primera columna es 0, todas las columnas de indice 0 de todas las filas van a tener valor true, ya que para sumar 0 el conjunto puede estar vacio
# --> En la primera fila, el unico instrumento de comparacion que se puede usar es ver si el valor de la fila coincide con el valor de la columna
# --> En las filas subsecuentes, se pueden dar una de tres posibilidades: 
# a) Que el valor de la fila coincida con el de la columna (mismo numero)
# b) Que el valor de la columna ya pueda ser sumado con los valores de otras filas
# c) Que el valor de la fila se sume con el de un valor que ya se logro sumar antes 

# COSTO: O(n*k) ya que se recorren todas las filas y columnas de la matriz

def encontrar_subconjunto(A, k):
    T = [[False for _ in range(k + 1)] for _ in range(len(A))]
    for i in range(len(T)):
        for j in range(len(T[i])):
            if i == 0:
                if j == 0:
                    T[i][j] = True
                elif j > 0:
                    T[i][j] = A[i] == j
            elif i > 0:
                if j == 0:
                    T[i][j] = True
                elif j > 0:
                    T[i][j] = (A[i] == j) or (T[i - 1][j]) or (A[i] < j and T[i - 1][j - A[i]])
    return T[len(A) - 1][k]

A = [3, 34, 4, 12, 5, 2]
k = 100
print(encontrar_subconjunto(A, k))
