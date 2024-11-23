def particion(v):
    s = [0 for _ in range(len(v))]
    particion_rec(v, s, 0)

def particion_rec(v, s, e):
    for i in range(2):
        s[e] = i
        if e == len(v) - 1:
            coleccion_izquierda = 0
            coleccion_derecha = 0
            for j in range(len(v)):
                if s[j] == 0:
                    coleccion_izquierda += v[j]
                else:
                    coleccion_derecha += v[j]
            if coleccion_izquierda == coleccion_derecha:
                print(coleccion_izquierda, coleccion_derecha)
        else:
            particion_rec(v, s, e + 1)


lista = [2, 5, 8, 3, 2]
particion(lista)