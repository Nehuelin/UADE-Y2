# Mostrar las combinaciones con RESTRICCION

# backtrack(S: Vector<entero>, E: etapa){
# 	si (E == len(S)){
# 		si (restriccion){ // sea restriccion una funcion que devuelve TRUE si se cumple la restriccion y FALSE en caso contrario
# 			print(S) 
# 		}
# 	} sino {
# 		para i = 0 hasta N { 
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
        if len(solucion) == len(set(solucion)):  # Si el tamaño de la lista es igual al tamaño del conjunto con los elementos de dicha lista, significa que no hay elementos repetidos
            print(solucion)
    else:
        for i in range(n):
            solucion[e] = i
            backtrack(solucion, n, e + 1)

# Ejemplo 1: mostrar todas las combinaciones de tamaño q posibles para el rango de numeros entre 0 y N, donde cada elemento sea unico
combinaciones(3, 4)

# -----------------------------------------------------------------------------------------------------------

def binarios(n):
    solucion = [0 for _ in range(n)]
    backtrack2(solucion, 0)

def backtrack2(solucion, e):
    if e == len(solucion):
        if cumple_restriccion(solucion):
            print(solucion)
    else:
        for i in range(2):
            solucion[e] = i
            backtrack2(solucion, e + 1)

def cumple_restriccion(solucion: list):
    valido = True
    unos = solucion.count(1)
    if solucion[0] == solucion[1] or unos % 2 == 0:
        valido = False

    return valido

# Ejemplo 2: mostrar los numeros binarios de 4 bits xi donde:
#   a) x1 != x2
#   b) la cantidad de unos (1) sean impares
binarios(4) 
