# 1) PALABRAS BARAJADAS
# a) ESTRATEGIA: explicada en ayuda

# FORMULA DE RECURRENCIA:
 
# 			{ true si i = 0 y j = 0 (una cadena vacía puede ser el resultado de barajar dos cadenas vacías)
# M[i][j] =	{ true si i = 0 y B[0, j - 1] ∈ C[0, j-1]    
# 			{ true si j = 0 y A[0, i - 1] ∈ C[0, i-1]
# 			{ true si i > 0, j > 0, A[0, i - 1] ∈ C[0, i-1] y B[0, j - 1] ∈ C[0, j-1]  

# b) ALGORITMO esBarajada(String A, String B, String C){ // Los strings 
# 	M = new Boolean Matrix[len(A) + 1, len(B) + 1] # [filas, columnas], llenada con FALSE
# 	for i in range(len(A)){
# 		for j in range(len(B)){
# 			if (i == 0 && j == 0){ // primer elemento de la matriz
# 					M[i][j] = false
# 			} else if (i == 0 && j != 0) { // si en fila 0...
# 				if(B[0, j-1] in C[0, j-1]) { // si la seccion de la palabra B esta en C...
# 					M[i][j] = true
# 				} else {
# 					M[i][j] = false
# 				}
# 			} else if (j == 0){ // si en columna 0...
# 				if(A[0, i-1] in C[0, i-1]) { // si la seccion de la palabra A esta en C...
# 					M[i][j] = true
# 				} else {
# 					M[i][j] = false
# 				}
# 			} else {
# 				if(A[0, i-1] in C[0, i+j-1] && B[0, j-1] in C[0, i+j-1]){
# 					M[i][j] = true
# 				} else {
# 					M[i][j] = false
# 				}
# 			}
# 		}
# 	}
# 	return M[len(A)][len(B)]
# }

# c) COSTO: O(n²) (nested loop)

def es_barajado(A, B, C):
    if len(C) != len(A) + len(B):
        return False
    
    M = [[False for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i == 0 and j == 0:
                M[i][j] = True
            elif i == 0:
                M[i][j] = M[i][j - 1] and B[j - 1] == C[i + j - 1]
            elif j == 0:
                M[i][j] = M[i - 1][j] and A[i - 1] == C[i + j - 1]
            else:
                M[i][j] = (M[i - 1][j] and A[i - 1] == C[i + j - 1]) or (M[i][j - 1] and B[j - 1] == C[i + j - 1])

    return M[len(A)][len(B)]

a = "dado"
b = "cosa"
c = "dacosdoa"
print(es_barajado(a, b, c))