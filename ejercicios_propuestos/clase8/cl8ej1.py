# Se tiene un conjunto Nk con los números naturales del 1 al k. 
# Escriba un programa que muestre por pantalla todos los posibles subconjuntos U ⊆ Nk.

def generar_conjunto(k):
    return [i+1 for i in range(k)]

def subconjuntos_incluidos(N):
    soluciones = []
    subconjuntos_incluidos_rec(N, soluciones, 1)

def subconjuntos_incluidos_rec(N, subconjunto_actual, e):
    if e == len(N) + 1:
        print(subconjunto_actual)
    else:
        subconjuntos_incluidos_rec(N, subconjunto_actual, e + 1)
        subconjuntos_incluidos_rec(N, subconjunto_actual + [e], e + 1)
        


conjunto = generar_conjunto(5)
subconjuntos_incluidos(conjunto)