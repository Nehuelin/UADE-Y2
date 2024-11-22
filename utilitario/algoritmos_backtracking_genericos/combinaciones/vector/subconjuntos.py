# Mostrar todos los subconjuntos del vector

# ESTRATEGIA: En vez de poner los elementos en el vector S, este vector se convierte en un vector booleano el cual va a indicarnos que elementos de V se usan y cuales no. 

# backtrack(V: Vector<entero>, S: Vector<entero>, E: etapa){ 
# 	para i = 0 hasta 1{ 
# 		S[E] = i
# 		si (E == len(V)){
# 			mostrarSolucion(V, S) // Funcion donde si S[i] = 1 entonces se agrega el elemento V[i] al vector que se va a imprimir por pantalla
# 		} sino {
# 			backtrack(V, S, M, suma, E)
# 		}
# 	}
# }


def combinaciones(V: list):
    solucion = [0 for _ in range(len(V))]
    backtrack(V, solucion, 0)

def backtrack(V, solucion, e):
    for i in range(2):
        solucion[e] = i
        if e == len(V) - 1:
            mostrar(V, solucion)
        else:
            backtrack(V, solucion, e + 1)

def mostrar(conjunto, binario):
    solucion = []
    for i in range(len(conjunto)):
        if binario[i] == 1:
            solucion.append(conjunto[i])
    print(solucion)

# Ejemplo: Dado un conjunto U con numeros naturales del 1 a K, mostrar todos los posibles subconjuntos U ⊆ N.

k = 4
conjunto = [i + 1 for i in range(k)]
combinaciones(conjunto)