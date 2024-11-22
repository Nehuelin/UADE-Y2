# Mostrar TODAS las combinaciones

# backtrack(S: Vector<entero>, E: etapa){ // S vector solucion
# 	si (E == len(S)){
# 		print(S)
# 	} sino {
# 		para i = 0 hasta N { // sea N el rango de elementos (I.E si es binario, el bucle sera for i in range(2), ceros y unos)
# 			S[E] <-- i
# 			backtrack(S, E + 1)
# 		}
# 	}
# }

def combinaciones(q, n):
    solucion = [0 for _ in range(q)]
    backtrack(solucion, n + 1, 0)

def backtrack(solucion, n, e):
    if e == len(solucion):
        print(solucion)
    else:
        for i in range(n):
            solucion[e] = i
            backtrack(solucion, n, e + 1)

# Ejemplo 1: mostrar todas las combinaciones de tamaño q posibles para el rango de numeros entre 0 y N
combinaciones(3, 4)

# Ejemplo 2: mostrar todos los numeros binarios de 4 bits
combinaciones(4, 1) # --> directamente se podria establecer el rango del for a 2 por defecto
