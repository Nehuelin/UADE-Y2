# Mostrar TODAS las combinaciones (con REPETICION)

# backtrack(V: Vector<entero>, S: Vector<entero>, E: etapa){ // V vector de numeros, S vector solucion
# 	si (E == len(V)){
# 		print(solucion)
# 	} sino {
# 		para i = 0 hasta len(V) - 1{
# 			solucion[E] <-- V[i]
# 			backtrack(V, S, E + 1)
# 		}
# 	}
# }

def combinaciones(V: list):
    solucion = [0 for _ in range(len(V))]
    backtrack(V, solucion, 0)

def backtrack(V: list, solucion: list, e: list):
    if e == len(V):
        print(solucion)
    else:
        for i in range(len(V)):
            solucion[e] = V[i]
            backtrack(V, solucion, e + 1)

# Ejemplo: Mostrar todas las combinaciones posibles de un vector de numeros enteros distintos
V = [3, 6, 2]
combinaciones(V)