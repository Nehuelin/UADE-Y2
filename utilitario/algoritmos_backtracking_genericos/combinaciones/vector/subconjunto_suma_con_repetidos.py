# Mostrar aquellas combinaciones que sumen M. Se permiten repetir elementos

# backtrack(V: Vector<entero>, S: Vector<entero>, M: entero, suma: entero, E: etapa){ // M valor objetivo 
# 	para i = 0 hasta len(V) - 1{ 
# 		S[E] = V[i]
# 		suma <-- suma + (V[i])
# 		si (suma == M){
# 			mostrarSolucion(V, S) 
# 		} sino {
# 			si (suma <= M){ // Poda: si la suma pasa de M no nos sirve seguir investigando
# 				backtrack(V, S, M, suma, E)
# 			}
# 		}
# 		suma = suma - V[i]
# 	}
# }


def cambio_minimo(C: list, m):
    solucion = [0 for _ in range(100)]
    backtrack(C, m, solucion, 0, 0)


def backtrack(C, m, solucion, suma, e):
    for i in range(len(C)):
        solucion[e] = C[i]
        suma += C[i]
        if suma == m:  
            mostrar(solucion)
        elif suma < m:  
            backtrack(C, m, solucion, suma, e + 1)  
    
        suma -= C[i]

def mostrar(solucion):
    lista = solucion[:]
    for i in range(solucion.count(0)):
        lista.remove(0)
    print(lista)


# Ejemplo: Dado un conjunto C de N tipos de monedas con un número ilimitado de ejemplares de cada tipo, 
# se pide mostrar, si se puede, todas las combinaciones posibles que sumen M

C = [6, 4, 2, 1]
M = 8
cambio_minimo(C, M)

