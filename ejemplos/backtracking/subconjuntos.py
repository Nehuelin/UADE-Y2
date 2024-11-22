def mostrar(lista, binario):
    resultado = []
    for i in range(len(lista)):
        if binario[i] == 1:
            resultado.append(lista[i])
    print(resultado)

def suma_sublista(v, m):
    solucion = [0 for _ in range(len(v))]
    suma_sublista_rec(v, m, solucion, 0, 0)

def suma_sublista_rec(v, m, solucion, suma, e):
    for i in range(2):
        solucion[e] = i
        suma += v[e] * i
        if e == len(v) - 1:
            if suma == m:
                mostrar(v, solucion)
        else:
            if suma <= m:
                suma_sublista_rec(v, m, solucion, suma, e + 1)

suma_sublista([3, 5, 8, 2, 7, 3], 11)
