# Se tiene un conjunto Nk con los números naturales del 1 al k. 
# Escriba un programa que muestre por pantalla todos los posibles subconjuntos U ⊆ Nk.

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
    
k = 4
conjunto = [i + 1 for i in range(k)]
combinaciones(conjunto)
        
