# Mostrar aquellas combinaciones que sumen M

# ESTRATEGIA: En vez de poner los elementos en el vector S, este vector se convierte en un vector booleano el cual va a indicarnos que elementos de V se usan y cuales no. 

# backtrack(V: Vector<entero>, S: Vector<entero>, M: entero, suma: entero, E: etapa){ // M valor objetivo
# 	para i = 0 hasta 1{ 
# 		S[E] = i
# 		suma <-- suma + (V[E] * i)
# 		si (E == len(V)){
# 			si (suma == M){
# 				mostrarSolucion(V, S) // Funcion donde si S[i] = 1 entonces se agrega el elemento V[i] al vector que se va a imprimir por pantalla
# 			}
# 		} sino {
# 			si (suma <= M){ // Poda: si la suma pasa de M no nos sirve seguir investigando
# 				backtrack(V, S, M, suma, E)
# 			}
# 		}
# 	}
# }



def combinaciones(pesos: list, m):
    solucion = [0 for i in range(len(pesos))]
    backtrack(pesos, m, solucion, 0, 0)

def backtrack(pesos, m, solucion, suma, e):
    for i in range(2):
        solucion[e] = i
        suma += pesos[e] * i
        if e == len(pesos) - 1:
            if suma == m:
                mostrar(pesos, solucion)
        else:
            if suma <= m:
                backtrack(pesos, m, solucion, suma, e + 1)

def mostrar(lista, binario):
    resultado = []
    for i in range(len(lista)):
        if binario[i] == 1:
            resultado.append(lista[i])
    print(resultado)

# Ejemplo 1: Dado un objeto con N pesos W, mostrar todas aquellas combinaciones donde la suma sea M 
pesos = [10, 3, 5, 7, 2]
M = 15
combinaciones(pesos, M)

# Ejemplo 2: Dado un vector de N elementos unicos, mostrar todos los subconjuntos del vector cuyos elementos sumen M
V = [3, 5, 8, 2, 7, 3]
M = 11
combinaciones(V, M)