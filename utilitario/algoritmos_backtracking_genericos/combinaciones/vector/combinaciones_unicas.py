# Mostrar las permutaciones donde cada elemento se utilize solo UNA vez

# backtrack(V: Vector<entero>, S: Vector<entero>, U: Vetcor<boolean>, E: etapa){ // U vector que nos indica, mediante el valor booleano en U[i], si el elemento V[i] ya fue usado o no
# 	si (E == len(V)){
# 		print(S)
# 	} sino {
# 		para i = 0 hasta len(V) - 1{
# 			si NO U[i]{
# 				U[i] <-- True
# 				S[E] <-- V[i]
# 				backtrack(V, S, U, E + 1)
# 				U[i] = False // retroceder y desmarcar el elemento
# 		    }
# 	   }
#   }
# }

def combinaciones(V):
    solucion = [0 for _ in range(len(V))]
    usados = [False for _ in range(len(V))]
    backtrack(V, solucion, usados, 0)

def backtrack(V, solucion, usados, e):
    if e == len(V):
        print(solucion)
    else:
        for i in range(len(V)):
            if not usados[i]:  
                usados[i] = True  
                solucion[e] = V[i]  
                backtrack(V, solucion, usados, e + 1)  
                usados[i] = False

# Ejemplo: Mostrar todas las combinaciones posibles de un vector de numeros enteros distintos, donde cada elemento se utilize solo una vez
V = [0, 3, 6, 9]
combinaciones(V)