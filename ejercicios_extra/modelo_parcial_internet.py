# 1) 
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

# 2) 
# a) ESTRATEGIA: Se podria dividir el conjunto de numeros en dos subconjuntos en cada recursion, y le preguntamos al brujo si esta en uno de los subconjuntos. Si la respuesta es no, debe estar en el otro. El caso base es cuando queda un solo numero, siendo este el numero ganador.  Si no se cumple el caso base, se agarrar el subconjunto donde podria estar el numero ganador, y continuar la recursion.
# b) Corresponde a la tecnica Divide & Conquer ya que se resuelve un problema mediante la resolucion de subproblemas mas pequeños que llevan a solucionar el problema global
# c) Debido a que el costo del algoritmo es Olog(n), siendo n = 65536 la cantidad de numero, la cantidad de consultas totales es C = log2(n) = 16. Como cada consulta sale $5000, entonces el total es T = C x 5000 = 80000. Como el ultimo ticket no esta incluido en la cuenta, T = 80100. Finalmente podemos concluir que el monto final de ganancia es G = 200000 - T = $119900 

# 3) 
# a) Debido a que la estudiante tiene un numero limitado de capsulas, cada capsula cuenta con una intensidad distinta y el efecto se reduce con cada ingestion, se deberia organizar la secuencia de capsulas de tal forma que la que mayor intensidad tiene se ingiera primero, y el resto se ordene de forma descendiente. Esto se debe a que, al utilizar las mas potentes primero, se garantiza que se utilize su efecto a mayor escala a que si se empezara con las de menos intensidad o intercalados.
# El algoritmo consistiria en ordenar una lista que contiene la intensidad de las capsulas de cafe de forma descendente (mayor a menor)

# b) Corresponde a un algoritmo greedy

# c) El algoritmo propuesto daria como resultado un efecto de 148


# CODIGOS:
import random

# EJERCICIO 1
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

# EJERCICIO 2

def adivinar_numero(L, x, ini, fin):
    if ini == fin:
        return ini
    medio = (ini + fin) // 2
    if x <= L[medio]:
        return adivinar_numero(L, x, ini, medio)
    else:
        return adivinar_numero(L, x, medio + 1, fin)

L = [i for i in range(1, 65537)]
x = random.randint(1, 65536)
print(adivinar_numero(L, x, 0, len(L)))


# EJERCICIO 3
def calcular_intensidad_total(L):
    L.sort(reverse=True)
    efecto = 0
    for i in range(len(L)):
        efecto += L[i] * (1 - i * 0.2) if i < 5 else 0
    return efecto

L = [2, 4, 6, 8, 10, 12]
print(calcular_intensidad_total(L))  

def calcular_intensidad_total2(L):
    L.sort(reverse=True)
    efecto = 0
    for i in range(len(L)):
        efecto += 5 * L[i] * (1 - i * 0.2) if i < 5 else 0
    return efecto

L = [11, 7, 8, 6, 4, 12, 5]
print(calcular_intensidad_total2(L))  

